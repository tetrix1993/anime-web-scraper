from anime.main_download import MainDownload, NewsTemplate, NewsTemplate2, NewsTemplate4
from datetime import datetime, timedelta
from requests.exceptions import HTTPError
from scan import AniverseMagazineScanner
from bs4 import BeautifulSoup
import json
import os


# Winter 2025 Anime
class Winter2025AnimeDownload(MainDownload):
    season = "2025-1"
    season_name = "Winter 2025"
    folder_name = '2025-1'

    def __init__(self):
        super().__init__()


# A-Rank Party wo Ridatsu shita Ore wa, Moto Oshiego-tachi to Meikyuu Shinbu wo Mezasu.
class AparidaDownload(Winter2025AnimeDownload, NewsTemplate):
    title = 'A-Rank Party wo Ridatsu shita Ore wa, Moto Oshiego-tachi to Meikyuu Shinbu wo Mezasu.'
    keywords = [title, "I Left My A-Rank Party to Help My Former Students Reach the Dungeon Depths!", 'aparida']
    website = 'https://arank-party-ridatsu-official.com/'
    twitter = 'Aparidaofficial'
    hashtags = ['エパリダ']
    folder_name = 'aparida'

    PAGE_PREFIX = website
    FINAL_EPISODE = 24
    IMAGES_PER_EPISODE = 5

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_episode_preview_external()
        # self.download_episode_preview_guess()

    def download_episode_preview(self):
        try:
            story_prefix = self.PAGE_PREFIX + 'story/detail/'
            soup = self.get_soup(story_prefix)
            stories = soup.select('.story-detail__item')
            for story in stories:
                try:
                    episode = ''
                    ep_num = story.select('.story-detail__title-num')[0].text
                    for a in ep_num:
                        if a.isnumeric():
                            episode += a
                    if len(episode) == 0:
                        continue
                    episode = str(int(episode)).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                self.image_list = []
                images = story.select('.story-detail__img-item img[src]')
                for i in range(len(images)):
                    image_name = episode + '_' + str(i + 1)
                    image_url = images[i]['src']
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.info__item',
                                    title_select='.info__title', date_select='.info__date', id_select='a',
                                    news_prefix='information/')

    def download_episode_preview_external(self):
        keywords = ['Aランクパーティを離脱した俺は']
        AniverseMagazineScanner(keywords, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20250214', download_id=self.download_id).run()

    def download_episode_preview_guess(self, print_url=False, print_invalid=False):
        if self.is_image_exists(str(self.FINAL_EPISODE).zfill(2) + '_1'):
            return
        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'aWhQreim/wp-content/uploads/%s/%s/【エパリダ】第%s話宣伝用場面写★%s.jpg'
        current_date = datetime.now() + timedelta(hours=1)
        year = current_date.strftime('%Y')
        month = current_date.strftime('%m')
        is_successful = False
        items = ['①', '②', '③', '④', '⑤']
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1') or self.is_image_exists(episode + '_1', folder):
                continue
            is_success = False
            for j in range(self.IMAGES_PER_EPISODE):
                image_name = episode + '_' + str(j + 1)
                image_url = template % (year, month, str(i + 1), items[j])
                if print_url:
                    print(image_url)
                if self.is_valid_url(image_url, is_image=True):
                    print('VALID - ' + image_url)
                    self.download_image(image_url, folder + '/' + image_name, to_jpg=True)
                    is_successful = True
                    is_success = True
                elif print_invalid:
                    print('INVALID - ' + image_url)
                if not is_success:
                    break
            if not is_success:
                break
        if is_successful:
            print(self.__class__.__name__ + ' - Guessed correctly!')
        return is_successful


# Akuyaku Reijou Tensei Ojisan
class TenseiOjisanDownload(Winter2025AnimeDownload, NewsTemplate4):
    title = 'Akuyaku Reijou Tensei Ojisan'
    keywords = [title, "From Bureaucrat to Villainess: Dad's Been Reincarnated!", 'tenseiojisan']
    website = 'https://tensei-ojisan.com/'
    twitter = 'tensei_ojisan'
    hashtags = ['転生おじさん']
    folder_name = 'tenseiojisan'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        json_obj = self.download_episode_preview()
        self.download_news(json_obj)

    def download_episode_preview(self):
        json_obj = None
        try:
            json_obj = self.get_json(self.PAGE_PREFIX + 'api/site-data/init')
            if 'stories' not in json_obj:
                return
            for story in json_obj['stories']:
                episode = story['episode'].zfill(2)
                self.image_list = []
                for i in range(len(story['images'])):
                    image_name = episode + '_' + str(i + 1)
                    image_url = story['images'][i]['image_path']
                    self.add_to_image_list(image_name, image_url, to_jpg=True)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)
        return json_obj

    def download_news(self, json_obj=None):
        self.download_template_news(json_url=self.PAGE_PREFIX + 'api/site-data/init')

    def download_episode_preview_guess(self, print_invalid=False, download_valid=True):
        if self.is_image_exists(str(self.FINAL_EPISODE).zfill(2) + '_' + str(self.IMAGES_PER_EPISODE)):
            return

        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'wp/wp-content/uploads/%s/%s/%s.jpg'
        current_date = datetime.now() + timedelta(hours=1)
        year = current_date.strftime('%Y')
        month = current_date.strftime('%m')
        is_successful = False
        valid_urls = []
        for j in range(self.IMAGES_PER_EPISODE):
            k = 0
            while k < 20:
                if k == 0:
                    append = ''
                else:
                    append = '-' + str(k)
                image_folder = folder + '/' + year + '/' + month
                image_name = str(j + 1).zfill(2) + append
                if not self.is_image_exists(image_name, image_folder):
                    image_url = template % (year, month, image_name)
                    if self.is_valid_url(image_url, is_image=True):
                        print('VALID - ' + image_url)
                        is_successful = True
                        valid_urls.append({'name': image_name, 'url': image_url, 'folder': image_folder})
                    else:
                        if print_invalid:
                            print('INVALID - ' + image_url)
                        break
                k += 1
        if download_valid and len(valid_urls) > 0:
            for valid_url in valid_urls:
                image_name = valid_url['name']
                image_folder = valid_url['folder']
                if not os.path.exists(image_folder):
                    os.makedirs(image_folder)
                self.download_image(valid_url['url'], image_folder + '/' + image_name, to_jpg=True)
        if is_successful:
            print(self.__class__.__name__ + ' - Guessed correctly!')
        return is_successful


# Ameku Takao no Suiri Karte
class AmekuTakaoDownload(Winter2025AnimeDownload, NewsTemplate):
    title = 'Ameku Takao no Suiri Karte'
    keywords = [title, "Ameku M.D.: Doctor Detective"]
    website = 'https://atdk-a.com/'
    twitter = 'Ameku_off'
    hashtags = ['あめく', '天久鷹央の推理カルテ', 'アニメあめく']
    folder_name = 'amekutakao'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        prefix = self.PAGE_PREFIX + 'story/'
        try:
            soup = self.get_soup(prefix)
            stories = soup.select('.p-story_tab-item')
            for story in stories:
                try:
                    episode = str(int(story.select('p')[0].text)).zfill(2)
                except:
                    continue
                if 'is-current' in story['class']:
                    ep_soup = soup
                else:
                    a_tag = story.select('a[href]')
                    if len(a_tag) == 0:
                        continue
                    ep_soup = self.get_soup(prefix + a_tag[0]['href'].replace('./', ''))
                if ep_soup is None:
                    continue
                self.image_list = []
                images = ep_soup.select('.swiper-slide img[src]')
                for i in range(len(images)):
                    image_url = prefix + images[i]['src']
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url, to_jpg=True)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.p-news__list-item',
                                    title_select='.p-news_data__ttl', date_select='.p-news_data__date',
                                    id_select='a', a_tag_prefix=self.PAGE_PREFIX + 'news/', paging_type=1,
                                    next_page_select='.c-pagination__list-item',
                                    next_page_eval_index_class='is-current', next_page_eval_index=-1)


# Ao no Exorcist: Yosuga-hen
class Aoex5Download(Winter2025AnimeDownload, NewsTemplate):
    title = 'Ao no Exorcist: Yosuga-hen'
    keywords = [title, 'aoex', 'Blue Exorcist: The Blue Night Saga', '5th Season']
    website = 'https://ao-ex.com/bluenight/'
    twitter = 'aoex_anime'
    hashtags = ['青エク', 'aoex']
    folder_name = 'aoex5'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()

    def download_episode_preview(self):
        try:
            story_prefix = self.PAGE_PREFIX + 'story/'
            soup = self.get_soup(story_prefix)
            stories = soup.select('li.storyNavList')
            for story in stories:
                try:
                    episode = str(int(story.select('a[href] span')[0].text)).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_5'):
                    continue
                if '--is-current' in story['class']:
                    ep_soup = soup
                else:
                    a_tag = story.select('a[href]')
                    if len(a_tag) == 0:
                        continue
                    story_url = story_prefix + a_tag[0]['href']
                    ep_soup = self.get_soup(story_url)
                if ep_soup is None:
                    continue
                self.image_list = []
                images = ep_soup.select('.storyImageList img[src]')
                for i in range(len(images)):
                    image_name = episode + '_' + str(i + 1)
                    image_url = story_prefix + images[i]['src']
                    self.add_to_image_list(image_name, image_url, to_jpg=True)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)


# Arafoo Otoko no Isekai Tsuuhan
class ArafoTsuhanDownload(Winter2025AnimeDownload):
    title = 'Arafoo Otoko no Isekai Tsuuhan'
    keywords = [title, "The Daily Life of a Middle-Aged Online Shopper in Another World", 'arafotsuhan']
    website = 'https://arafo-tsuhan.com/'
    twitter = 'arafotsuhan'
    hashtags = ['アラフォー通販']
    folder_name = 'arafotsuhan'

    PAGE_PREFIX = website
    FINAL_EPISODE = 13
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        try:
            template = self.PAGE_PREFIX + 'images/story/%s/p_%s.jpg'
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (str(i + 1).zfill(3), str(j + 1).zfill(3))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name, to_jpg=True) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        try:
            results = []
            news_obj = self.get_last_news_log_object()
            json_obj = self.get_json(self.PAGE_PREFIX + 'news.json')
            for item in json_obj:
                if 'day' in item and 'url' in item and 'title' in item:
                    try:
                        date = item['day']
                    except:
                        continue
                    title = item['title']
                    url = self.PAGE_PREFIX + item['url']
                    if news_obj is not None and (news_obj['id'] == url or news_obj['title'] == title
                                                 or date < news_obj['date']):
                        break
                    results.append(self.create_news_log_object(date, title, url))
            success_count = 0
            for result in reversed(results):
                process_result = self.create_news_log_from_news_log_object(result)
                if process_result == 0:
                    success_count += 1
            if len(results) > 0:
                self.create_news_log_cache(success_count, results[0])
        except Exception as e:
            self.print_exception(e, 'News')


# Botsuraku Yotei no Kizoku dakedo, Hima Datta kara Mahou wo Kiwametemita
class BotsurakuKizokuDownload(Winter2025AnimeDownload, NewsTemplate):
    title = 'Botsuraku Yotei no Kizoku dakedo, Hima Datta kara Mahou wo Kiwametemita'
    keywords = [title, "I'm a Noble on the Brink of Ruin, So I Might as Well Try Mastering Magic"]
    website = 'https://botsurakukizoku-anime.com/'
    twitter = 'botsuraku_pr'
    hashtags = ['没落貴族']
    folder_name = 'botsurakukizoku'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 5

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        try:
            template = self.PAGE_PREFIX + 'assets/img/story/ep%s/img%s.jpg'
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (str(i + 1), str(j + 1).zfill(2))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name, to_jpg=True) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.bl_posts_item',
                                    title_select='.bl_posts_txt', date_select='.bl_posts_date', id_select='a')


# Class no Daikirai na Joshi to Kekkon suru Koto ni Natta.
class KurakonDownload(Winter2025AnimeDownload, NewsTemplate):
    title = 'Class no Daikirai na Joshi to Kekkon suru Koto ni Natta.'
    keywords = [title, "I'm Getting Married to a Girl I Hate in My Class", 'kurakon']
    website = 'https://kura-kon.com/'
    twitter = 'kurakon'
    hashtags = ['クラ婚']
    folder_name = 'kurakon'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        story_url = self.PAGE_PREFIX + 'story/'
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            stories = soup.select('.tab_list li')
            for story in stories:
                try:
                    p_tag = story.select('p')[0]
                    a_tag = story.select('a[href]')[0]
                    episode = ''
                    for s in p_tag.text:
                        if s.isnumeric():
                            episode += s
                        elif s == ' ' and len(episode) > 0:
                            break
                    episode = episode.zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                if 'is-current' in story['class']:
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(story_url + a_tag['href'].replace('./', ''))
                images = ep_soup.select('.p-story__img-swiper img[src]')
                self.image_list = []
                for i in range(len(images)):
                    image_url = story_url + images[i]['src']
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url, to_jpg=True)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.p-news__list-item',
                                    title_select='.p-news__list-text', date_select='.p-news__list-date',
                                    id_select='a', a_tag_start_text_to_remove='./',
                                    a_tag_prefix=self.PAGE_PREFIX + 'news/', paging_type=1,
                                    next_page_select='.c-pagination__list-item',
                                    next_page_eval_index_class='is-current', next_page_eval_index=-1)


# Fuguushoku "Kanteishi" ga Jitsu wa Saikyou Datta
class FugukanDownload(Winter2025AnimeDownload, NewsTemplate):
    title = 'Fuguushoku "Kanteishi" ga Jitsu wa Saikyou Datta'
    keywords = [title, 'Even Given the Worthless "Appraiser" Class, I\'m Actually the Strongest', 'fugukan']
    website = 'https://fugukan.com/'
    twitter = 'fugu_kan'
    hashtags = ['ふぐ鑑', '不遇職', '鑑定士']
    folder_name = 'fugukan'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            stories = soup.select('#story_link_list li')
            for story in stories:
                a_tag = story.select('a')
                if len(a_tag) == 0 or 'introduction' in a_tag[0]['href']:
                    continue
                episode = ''
                ep_num = a_tag[0].text
                for a in ep_num:
                    if a.isnumeric():
                        episode += a
                if len(episode) == 0:
                    continue
                episode = str(int(episode)).zfill(2)
                if self.is_image_exists(episode + '_01'):
                    continue
                if 'current' in story['class']:
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(a_tag[0]['href'])
                if ep_soup is None:
                    continue
                self.image_list = []
                images = ep_soup.select('p.story_thumbs img[src]')
                for i in range(len(images)):
                    image_url = self.PAGE_PREFIX + images[i]['src'][1:]
                    image_name = episode + '_' + str(i + 1).zfill(2)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news_list a',
                                    title_select='.news_title', date_select='time', id_select=None)


# Grisaia: Phantom Trigger
class GrisaiaPTDownload(Winter2025AnimeDownload, NewsTemplate):
    title = 'Grisaia: Phantom Trigger'
    keywords = [title]
    website = 'https://grisaia-pt.com/gptanime/'
    twitter = 'grisaia_fw'
    hashtags = ['グリザイア', 'グリザイアPT']
    folder_name = 'grisaiapt'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            stories = soup.select('.page_list li')
            for story in stories:
                a_tag = story.select('a[href]')
                if len(a_tag) == 0:
                    continue
                if a_tag[0].text.startswith('OVA'):
                    continue
                try:
                    episode = ''
                    for s in a_tag[0].text:
                        if s.isnumeric():
                            episode += s
                    if len(episode) == 0:
                        continue
                    episode = str(int(episode)).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_01'):
                    continue
                if story.has_attr('class') and 'active' in story['class']:
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(a_tag[0]['href'])
                if ep_soup is None:
                    continue
                images = ep_soup.select('.slide img[src]')
                for i in range(len(images)):
                    image_url = images[i]['src']
                    image_name = episode + '_' + str(i + 1).zfill(2)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news_area ul.list>li',
                                    title_select='.title', date_select='.date', id_select='a', stop_date='2021',
                                    next_page_select='li.next a')


# Guild no Uketsukejou desu ga, Zangyou wa Iya nanode Boss wo Solo Toubatsu Shiyou to Omoimasu
class GirumasuDownload(Winter2025AnimeDownload, NewsTemplate):
    title = 'Guild no Uketsukejou desu ga, Zangyou wa Iya nanode Boss wo Solo Toubatsu Shiyou to Omoimasu'
    keywords = [title, "I May Be a Guild Receptionist, but I'll Solo Any Boss to Clock Out on Time", 'girumasu']
    website = 'https://girumasu.com/'
    twitter = 'girumasu001'
    hashtags = ['ギルます']
    folder_name = 'girumasu'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        try:
            story_prefix = self.PAGE_PREFIX + 'story/'
            soup = self.get_soup(story_prefix)
            stories = soup.select('li.p-story__nav-item')
            for story in stories:
                try:
                    episode = str(int(story.select('a[href] span')[0].text.replace('#', ''))).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_5'):
                    continue
                if 'is-active' in story['class']:
                    ep_soup = soup
                else:
                    a_tag = story.select('a[href]')
                    if len(a_tag) == 0:
                        continue
                    story_url = story_prefix + a_tag[0]['href'].replace('./', '')
                    ep_soup = self.get_soup(story_url)
                if ep_soup is None:
                    continue
                self.image_list = []
                images = ep_soup.select('.p-story__cut-imglist img[src]')
                for i in range(len(images)):
                    image_name = episode + '_' + str(i + 1)
                    image_url = story_prefix + images[i]['src']
                    self.add_to_image_list(image_name, image_url, to_jpg=True)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.p-news__list-item',
                                    title_select='.p-news_article__title', date_select='.p-news_article__date',
                                    id_select='a', a_tag_start_text_to_remove='/', a_tag_prefix=self.PAGE_PREFIX,
                                    paging_type=1, next_page_select='.c-pagination__list-item',
                                    next_page_eval_index_class='is-current', next_page_eval_index=-1,
                                    date_func=lambda x: x[0:4] + '.' + x[4:])


# Hana wa Saku, Shura no Gotoku
class HanashuraDownload(Winter2025AnimeDownload, NewsTemplate):
    title = 'Hana wa Saku, Shura no Gotoku'
    keywords = [title, "Flower and Asura", 'hanashura']
    website = 'https://hanashura-anime.com/'
    twitter = 'hanashura_PR'
    hashtags = ['花修羅']
    folder_name = 'hanashura'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        try:
            template = self.PAGE_PREFIX + 'assets/images/story/%s_%s.jpg'
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (episode, str(j + 1).zfill(2))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name, to_jpg=True) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='article', title_select='.title h3',
                                    date_select='time', id_select=None, id_has_id=True,
                                    a_tag_prefix=self.PAGE_PREFIX + 'news/#')


# Hazure Skill "Kinomi Master": Skill no Mi (Tabetara Shinu) wo Mugen ni Taberareru You ni Natta Ken ni Tsuite
class KinomiMasterDownload(Winter2025AnimeDownload, NewsTemplate4):
    title = 'Hazure Skill "Kinomi Master": Skill no Mi (Tabetara Shinu) wo Mugen ni Taberareru You ni Natta Ken ni Tsuite'
    keywords = [title, 'kinomimaster']
    website = 'https://kinomimaster.com/'
    twitter = 'kinomimaster_PR'
    hashtags = ['木の実マスター']
    folder_name = 'kinomimaster'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        json_obj = self.download_episode_preview()
        self.download_news(json_obj)
        self.download_episode_preview_guess()

    def download_episode_preview(self):
        json_obj = None
        try:
            json_obj = self.get_json(self.PAGE_PREFIX + 'api/site-data/init')
            if 'stories' not in json_obj:
                return
            for story in json_obj['stories']:
                episode = story['episode'].zfill(2)
                self.image_list = []
                for i in range(len(story['images'])):
                    image_name = episode + '_' + str(i + 1)
                    image_url = story['images'][i]['image_path']
                    self.add_to_image_list(image_name, image_url, to_jpg=True)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)
        return json_obj

    def download_news(self, json_obj=None):
        self.download_template_news(json_url=self.PAGE_PREFIX + 'api/site-data/init')

    def download_episode_preview_guess(self, print_url=False, print_invalid=False):
        if self.is_image_exists(str(self.FINAL_EPISODE).zfill(2) + '_1'):
            return
        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'wp/wp-content/uploads/%s/%s/kinomimaster_ep%s-%s.jpg'
        current_date = datetime.now() + timedelta(hours=1)
        year = current_date.strftime('%Y')
        month = current_date.strftime('%m')
        is_successful = False
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1') or self.is_image_exists(episode + '_1', folder):
                continue
            is_success = False
            for j in range(self.IMAGES_PER_EPISODE):
                image_name = episode + '_' + str(j + 1)
                image_url = template % (year, month, episode, str(j + 1).zfill(2))
                if print_url:
                    print(image_url)
                if self.is_valid_url(image_url, is_image=True):
                    print('VALID - ' + image_url)
                    self.download_image(image_url, folder + '/' + image_name, to_jpg=True)
                    is_successful = True
                    is_success = True
                elif print_invalid:
                    print('INVALID - ' + image_url)
                if not is_success:
                    break
            if not is_success:
                break
        if is_successful:
            print(self.__class__.__name__ + ' - Guessed correctly!')
        return is_successful


# Izure Saikyou no Renkinjutsushi?
class IzureSaikyoDownload(Winter2025AnimeDownload, NewsTemplate4):
    title = 'Izure Saikyou no Renkinjutsushi?'
    keywords = [title, "Someday Will I Be the Greatest Alchemist?", 'izuresaikyo']
    website = 'https://izuresaikyo-pr.com/'
    twitter = 'izuresaikyo_pr'
    hashtags = ['いずれ最強の錬金術師']
    folder_name = 'izuresaikyo'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        json_obj = self.download_episode_preview()
        self.download_news(json_obj)
        self.download_episode_preview_guess()

    def download_episode_preview(self):
        json_obj = None
        try:
            json_obj = self.get_json(self.PAGE_PREFIX + 'api/site-data/init')
            if 'stories' not in json_obj:
                return
            for story in json_obj['stories']:
                episode = story['episode'].zfill(2)
                self.image_list = []
                for i in range(len(story['images'])):
                    image_name = episode + '_' + str(i + 1)
                    image_url = story['images'][i]['image_path']
                    self.add_to_image_list(image_name, image_url, to_jpg=True)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)
        return json_obj

    def download_news(self, json_obj=None):
        self.download_template_news(json_url=self.PAGE_PREFIX + 'api/site-data/init')

    def download_episode_preview_guess(self, print_url=False, print_invalid=False):
        if self.is_image_exists(str(self.FINAL_EPISODE).zfill(2) + '_1'):
            return
        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'wp/wp-content/uploads/%s/%s/izuren_ep%s-%s.jpg'
        current_date = datetime.now() + timedelta(hours=1)
        year = current_date.strftime('%Y')
        month = current_date.strftime('%m')
        is_successful = False
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1') or self.is_image_exists(episode + '_1', folder):
                continue
            is_success = False
            for j in range(self.IMAGES_PER_EPISODE):
                image_name = episode + '_' + str(j + 1)
                image_url = template % (year, month, episode, str(j + 1).zfill(2))
                if print_url:
                    print(image_url)
                if self.is_valid_url(image_url, is_image=True):
                    print('VALID - ' + image_url)
                    self.download_image(image_url, folder + '/' + image_name, to_jpg=True)
                    is_successful = True
                    is_success = True
                elif print_invalid:
                    print('INVALID - ' + image_url)
                if not is_success:
                    break
            if not is_success:
                break
        if is_successful:
            print(self.__class__.__name__ + ' - Guessed correctly!')
        return is_successful


# Kimi no Koto ga Daidaidaidaidaisuki na 100-nin no Kanojo 2nd Season
class Hyakkano2Download(Winter2025AnimeDownload, NewsTemplate):
    title = 'Kimi no Koto ga Daidaidaidaidaisuki na 100-nin no Kanojo 2nd Season'
    keywords = [title, 'The 100 Girlfriends Who Really, Really, Really, Really, Really Love You', '2nd']
    website = 'https://hyakkano.com/'
    twitter = 'hyakkano_anime'
    hashtags = '100カノ'
    folder_name = 'hyakkano2'

    PAGE_PREFIX = website
    FIRST_EPISODE = 13
    FINAL_EPISODE = 24
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        # self.download_episode_preview_guess(download_valid=True)

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/season2/')
            stories = soup.select('.story-Wrapper[id]')
            for story in stories:
                try:
                    episode = str(int(story['id'].replace('ep', '')) + self.FIRST_EPISODE - 1).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                self.image_list = []
                images = story.select('.swiper-slide img[src]')
                for i in range(len(images)):
                    image_url = self.clear_resize_in_url(images[i]['src'])
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url, to_jpg=True)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-List li',
                                    date_select='.date', title_select='.title', id_select='a',
                                    next_page_select='.nextpostslink', stop_date='2024.08')

    '''
    def download_episode_preview_guess(self, print_invalid=False, download_valid=False):
        if self.is_image_exists(str(self.FINAL_EPISODE).zfill(2) + '_' + str(self.IMAGES_PER_EPISODE)):
            return

        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'xUtUy1FY/wp-content/uploads/%s/%s/img_story%s_%s.jpg'
        current_date = datetime.now() + timedelta(hours=1)
        year = current_date.strftime('%Y')
        month = current_date.strftime('%m')
        is_successful = False
        for ep_num in range(self.FIRST_EPISODE, self.FINAL_EPISODE + 1, 1):
            episode = str(ep_num).zfill(2)
            if self.is_image_exists(episode + '_1'):
                continue
            for j in range(self.IMAGES_PER_EPISODE):
                image_name = episode + '_' + str(j + 1)
                if not self.is_image_exists(image_name, folder):
                    image_url = template % (year, month, episode, str(j + 1).zfill(2))
                    if self.is_valid_url(image_url, is_image=True):
                        print('VALID - ' + image_url)
                        is_successful = True
                        if download_valid:
                            self.download_image(image_url, folder + '/' + image_name)
                    else:
                        if print_invalid:
                            print('INVALID - ' + image_url)
                        break
            if not is_successful:
                break
        if is_successful:
            print(self.__class__.__name__ + ' - Guessed correctly!')
        return is_successful
    '''

    def download_episode_preview_guess(self, print_invalid=False, download_valid=True):
        if self.is_image_exists(str(self.FINAL_EPISODE).zfill(2) + '_' + str(self.IMAGES_PER_EPISODE)):
            return

        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'xUtUy1FY/wp-content/uploads/%s/%s/%s.jpg'
        current_date = datetime.now() + timedelta(hours=1)
        year = current_date.strftime('%Y')
        month = current_date.strftime('%m')
        is_successful = False
        valid_urls = []
        for j in range(self.IMAGES_PER_EPISODE):
            k = 0
            while k < 20:
                if k == 0:
                    append = ''
                else:
                    append = '-' + str(k)
                image_folder = folder + '/' + year + '/' + month
                if j == 0:
                    image_name = '01_main' + append
                else:
                    image_name = str(j + 1).zfill(2) + '_sub' + str(j) + append
                if not self.is_image_exists(image_name, image_folder):
                    image_url = template % (year, month, image_name)
                    if self.is_valid_url(image_url, is_image=True):
                        print('VALID - ' + image_url)
                        is_successful = True
                        valid_urls.append({'name': image_name, 'url': image_url, 'folder': image_folder})
                    else:
                        if print_invalid:
                            print('INVALID - ' + image_url)
                        break
                k += 1
        if download_valid and len(valid_urls) > 0:
            for valid_url in valid_urls:
                image_name = valid_url['name']
                image_folder = valid_url['folder']
                if not os.path.exists(image_folder):
                    os.makedirs(image_folder)
                self.download_image(valid_url['url'], image_folder + '/' + image_name, to_jpg=True)
        if is_successful:
            print(self.__class__.__name__ + ' - Guessed correctly!')
        return is_successful


# Kisaki Kyouiku kara Nigetai Watashi
class KisakiKyouikuDownload(Winter2025AnimeDownload, NewsTemplate):
    title = 'Kisaki Kyouiku kara Nigetai Watashi'
    keywords = [title, "I Want to Escape from Princess Lessons", 'kisakikyouiku']
    website = 'https://kisakikyouiku.com/'
    twitter = 'kisakikyouiku'
    hashtags = ['妃教育']
    folder_name = 'kisakikyouiku'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        try:
            template = self.PAGE_PREFIX + 'assets/story/%s/%s.webp'
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (str(i + 1), str(j + 1))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name, to_jpg=True) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='article', title_select='.entry-title',
                                    date_select='.entry-date', id_select=None, id_has_id=True, news_prefix='news.html',
                                    a_tag_prefix=self.PAGE_PREFIX + 'news.html#')


# Kono Kaisha ni Suki na Hito ga Imasu
class KonosukiDownload(Winter2025AnimeDownload, NewsTemplate):
    title = 'Kono Kaisha ni Suki na Hito ga Imasu'
    keywords = [title, "I Have a Crush at Work", "Can You Keep a Secret?", 'kononsuki']
    website = 'https://kaishani-sukinahito.com/'
    twitter = 'kaishani_suki'
    hashtags = ['この好き']
    folder_name = 'konosuki'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        try:
            story_url = self.PAGE_PREFIX + 'story/'
            soup = self.get_soup(story_url)
            if soup is None:
                return
            stories = soup.select('.story-list li')
            for story in stories:
                a_tag = story.select('a[href]')
                if len(a_tag) == 0:
                    continue
                episode = ''
                ep_num = a_tag[0].text
                for a in ep_num:
                    if a.isnumeric():
                        episode += a
                if len(episode) == 0:
                    continue
                episode = str(int(episode)).zfill(2)
                if self.is_image_exists(episode + '_1'):
                    continue
                if story.has_attr('class') and 'current' in story['class']:
                    ep_soup = soup
                else:
                    if len(a_tag[0]['href'].strip()) == 0:
                        continue
                    ep_soup = self.get_soup(story_url + a_tag[0]['href'])
                if ep_soup is None:
                    continue
                self.image_list = []
                images = ep_soup.select('.swiper-slide img[src]')
                for i in range(len(images)):
                    image_name = episode + '_' + str(i + 1)
                    image_url = self.PAGE_PREFIX + images[i]['src'].replace('../', '')
                    self.add_to_image_list(image_name, image_url, to_jpg=True)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        news_prefix = self.PAGE_PREFIX + 'news/'
        try:
            results = []
            news_obj = self.get_last_news_log_object()
            json_obj = self.get_json(news_prefix + 'news.json')
            for item in json_obj:
                if 'date' in item and 'url' in item and 'title' in item:
                    try:
                        date = item['date']
                    except:
                        continue
                    title = item['title']
                    url = news_prefix + item['url']
                    if news_obj is not None and (news_obj['id'] == url or news_obj['title'] == title
                                                 or date < news_obj['date']):
                        break
                    results.append(self.create_news_log_object(date, title, url))
            success_count = 0
            for result in reversed(results):
                process_result = self.create_news_log_from_news_log_object(result)
                if process_result == 0:
                    success_count += 1
            if len(results) > 0:
                self.create_news_log_cache(success_count, results[0])
        except Exception as e:
            self.print_exception(e, 'News')


# Kuroiwa Medaka ni Watashi no Kawaii ga Tsuujinai
class MedakawaDownload(Winter2025AnimeDownload, NewsTemplate):
    title = 'Kuroiwa Medaka ni Watashi no Kawaii ga Tsuujinai'
    keywords = [title, "Medaka Kuroiwa Is Impervious to My Charms", 'medakawa']
    website = 'https://monaxmedaka.com/'
    twitter = 'monaxmedaka'
    hashtags = ['メダかわ']
    folder_name = 'medakawa'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_episode_preview_external()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            articles = soup.select('.articleContentWrap')
            for article in articles:
                try:
                    episode = str(int(article.select('h3 span')[0].text.replace('#', ''))).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_01'):
                    continue
                images = article.select('.story__contentImg-swiper-slide img[src]')
                for i in range(len(images)):
                    image_name = episode + '_' + str(i + 1).zfill(2)
                    image_url = images[i]['src']
                    self.add_to_image_list(image_name, image_url, to_jpg=True)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.newsList',
                                    title_select='.newsList__title_txt>span', date_select='.newsList__date',
                                    id_select='a')

    def download_episode_preview_external(self):
        keywords = ['黒岩メダカに私の可愛いが通じない']
        AniverseMagazineScanner(keywords, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20241216', download_id=self.download_id).run()


# Kusuriya no Hitorigoto 2nd Season
class Kusuriya2Download(Winter2025AnimeDownload, NewsTemplate):
    title = 'Kusuriya no Hitorigoto 2nd Season'
    keywords = [title, 'The Apothecary Diaries']
    website = 'https://kusuriyanohitorigoto.jp/season2/'
    twitter = 'kusuriya_PR'
    hashtags = ['薬屋のひとりごと']
    folder_name = 'kusuriya2'

    PAGE_PREFIX = website
    FIRST_EPISODE = 25
    FINAL_EPISODE = 50
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()

    def download_episode_preview(self):
        try:
            template = self.PAGE_PREFIX + 'episodes/img/%s/%s.jpg'
            stop = False
            for i in range(self.FIRST_EPISODE, self.FINAL_EPISODE + 1, 1):
                episode = str(i).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (str(i), str(j + 1))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)


# Magic Maker: Isekai Mahou no Tsukurikata
class MagicMakerDownload(Winter2025AnimeDownload, NewsTemplate2):
    title = 'Magic Maker: Isekai Mahou no Tsukurikata'
    keywords = [title, "How to Create Magic in Another World"]
    website = 'https://magicmaker-anime.com/'
    twitter = 'magicmakeranime'
    hashtags = ['マジックメイカー']
    folder_name = 'magicmaker'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_external()
        self.download_news()
        self.download_episode_preview_guess()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/01.html')
            stories = soup.select('table[summary="List_Type01"] a[href]')
            for story in stories:
                story_url = self.PAGE_PREFIX + story['href'].replace('../', '')
                try:
                    episode = str(int(story.text)).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                if episode == '01':
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(story_url)
                if ep_soup is not None:
                    images = ep_soup.select('.ph img[src]')
                    self.image_list = []
                    for i in range(len(images)):
                        image_url = self.PAGE_PREFIX + images[i]['src'].split('?')[0]
                        image_url = self.remove_string(image_url, ['../', 'sn_'])
                        image_name = episode + '_' + str(i + 1)
                        self.add_to_image_list(image_name, image_url, to_jpg=True)
                    self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_external(self):
        keywords = ['マジック・メイカー']
        AniverseMagazineScanner(keywords, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20250103', download_id=self.download_id).run()

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX)

    def download_episode_preview_guess(self, print_url=False):
        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'core_sys/images/contents/%s/block/%s/%s.jpg'
        is_successful = False
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1') or self.is_image_exists(episode + '_1', folder):
                continue
            is_success = False
            first = 16 + i
            second = 34 + 4 * i
            third = 32 + 6 * i
            for j in range(self.IMAGES_PER_EPISODE):
                image_url = template % (str(first).zfill(8), str(second).zfill(8), str(third + j).zfill(8))
                if print_url:
                    print(image_url)
                if not self.is_content_length_in_range(image_url, more_than_amount=2500):
                    break
                image_name = episode + '_' + str(j + 1)
                result = self.download_image(image_url, folder + '/' + image_name)
                if result == 0:
                    is_success = True
                    is_successful = True
                elif result == -1:
                    break
            if is_success:
                print(self.__class__.__name__ + ' - Guessed successfully!')
            else:
                if len(os.listdir(folder)) == 0:
                    os.rmdir(folder)
                return
        if len(os.listdir(folder)) == 0:
            os.rmdir(folder)
        return is_successful


# Medalist
class MedalistDownload(Winter2025AnimeDownload, NewsTemplate):
    title = 'Medalist'
    keywords = [title]
    website = 'https://medalist-pr.com/'
    twitter = 'medalist_PR'
    hashtags = ['メダリスト', 'medalist']
    folder_name = 'medalist'

    PAGE_PREFIX = website
    FINAL_EPISODE = 13
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        template = self.PAGE_PREFIX + 'assets/story/%s/%s.webp'
        try:
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (str(i + 1), str(j + 1))
                    image_name = episode + '_' + str(j + 1)
                    result = self.download_image(image_url, self.base_folder + '/' + image_name, to_jpg=True)
                    if result == -1:
                        return
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='article',
                                    title_select='.entry-title .text span', date_select='.entry-date', id_select=None,
                                    id_has_id=True, news_prefix='news.html',
                                    a_tag_prefix=self.PAGE_PREFIX + 'news.html#')


# NEET Kunoichi to Nazeka Dousei Hajimemashita
class NeetKunoichiDownload(Winter2025AnimeDownload, NewsTemplate):
    title = 'NEET Kunoichi to Nazeka Dousei Hajimemashita'
    keywords = [title, "I'm Living with an Otaku NEET Kunoichi!?"]
    website = 'https://neet-kunoichi.com/'
    twitter = 'neet_kunoichi'
    hashtags = ['ニートくノ一']
    folder_name = 'neetkunoichi'

    PAGE_PREFIX = website
    FINAL_EPISODE = 24
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        # self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        try:
            template = self.PAGE_PREFIX + 'assets/images/story/%s_%s.jpg'
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE).zfill(2)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (episode, str(j + 1).zfill(2))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name, to_jpg=True) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='article', title_select='.title h3',
                                    date_select='time', id_select=None, id_has_id=True,
                                    a_tag_prefix=self.PAGE_PREFIX + 'news/#')


# Nihon e Youkoso Elf-san.
class NihonElfsanDownload(Winter2025AnimeDownload, NewsTemplate):
    title = 'Nihon e Youkoso Elf-san.'
    keywords = [title, "Welcome to Japan, Ms. Elf!"]
    website = 'https://welcome-elfsan.com/'
    twitter = 'welcome_elfsan'
    hashtags = ['日本へようこそエルフさん']
    folder_name = 'nihonelfsan'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            stories = soup.select('.story-box')
            for story in stories:
                try:
                    episode = ''
                    for a in story.select('.num')[0].text:
                        if a.isnumeric():
                            episode += a
                    if len(episode) == 0:
                        continue
                    episode = str(int(episode)).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                images = story.select('.ss-item img[src]')
                self.image_list = []
                for i in range(len(images)):
                    image_url = images[i]['src']
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url, to_jpg=True)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-item', title_select='.title',
                                    date_select='.date', id_select='a')


# Okinawa de Suki ni Natta Ko ga Hougen Sugite Tsurasugiru
class OkitsuraDownload(Winter2025AnimeDownload, NewsTemplate):
    title = 'Okinawa de Suki ni Natta Ko ga Hougen Sugite Tsurasugiru'
    keywords = [title, "Okitsura"]
    website = 'https://okitsura.com/'
    twitter = 'okitsura'
    hashtags = ['沖ツラ']
    folder_name = 'okitsura'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 5

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        try:
            template = self.PAGE_PREFIX + 'assets/img/story/ep%s/img%s.jpg'
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE).zfill(2)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (episode, str(j + 1).zfill(2))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name, to_jpg=True) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.bl_vertPosts_item',
                                    title_select='.bl_vertPosts_txt', date_select='.bl_vertPosts_date',
                                    id_select='a', paging_type=3, paging_suffix='?page=%s',
                                    next_page_select='.page-numbers', next_page_eval_index_class='current',
                                    next_page_eval_index=-1,
                                    date_func=lambda x: x[0:4] + '.' + str(self.convert_month_string_to_number(x[4:7])).zfill(2) + '.' + x[8:])


# Ore dake Level Up na Ken Season 2: Arise from the Shadow
class SoloLeveling2Download(Winter2025AnimeDownload, NewsTemplate):
    title = 'Ore dake Level Up na Ken Season 2: Arise from the Shadow'
    keywords = [title, 'Solo Leveling']
    website = 'https://sololeveling-anime.net/'
    twitter = 'sololeveling_pr'
    hashtags = ['俺レベ', 'SoloLeveling']
    folder_name = 'sololeveling2'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        try:
            story_prefix = self.PAGE_PREFIX + 'story/'
            soup = self.get_soup(story_prefix)
            stories = soup.select('.storyNavList')
            for story in stories:
                try:
                    episode = str(int(story.select('.storyNavList__linktxt')[0].text)).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_5'):
                    continue
                if '--is-current' in story['class']:
                    ep_soup = soup
                else:
                    a_tag = story.select('a[href]')
                    if len(a_tag) == 0:
                        continue
                    story_url = story_prefix + a_tag[0]['href']
                    ep_soup = self.get_soup(story_url)
                if ep_soup is None:
                    continue
                self.image_list = []
                images = ep_soup.select('.storyImageList img[src]')
                for i in range(len(images)):
                    image_name = episode + '_' + str(i + 1)
                    image_url = story_prefix + images[i]['src']
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news/'
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news__lists li',
                                    title_select='p', date_select='time', id_select='a', stop_date='2024.03.24',
                                    a_tag_prefix=news_url, paging_type=1, next_page_select='.linkBtn._pager',
                                    next_page_eval_index=-1, next_page_eval_index_class='is-active')


# S-Rank Monster no "Behemoth" dakedo, Neko to Machigawarete Elf Musume no Pet toshite Kurashitemasu
class BehenekoDownload(Winter2025AnimeDownload, NewsTemplate2):
    title = 'S-Rank Monster no "Behemoth" dakedo, Neko to Machigawarete Elf Musume no Pet toshite Kurashitemasua'
    keywords = [title, "Beheneko: The Elf-Girl's Cat is Secretly an S-Ranked Monster!"]
    website = 'https://behemoth-anime.com/'
    twitter = 'beheneko_anime'
    hashtags = ['べヒ猫', 'beheneko']
    folder_name = 'beheneko'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_episode_preview_guess()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/01.html')
            stories = soup.select('#ContentsListUnit02 a[href]')
            for story in stories:
                story_url = self.PAGE_PREFIX + story['href'].replace('../', '')
                try:
                    episode = str(int(story_url.split('/')[-1].split('.html')[0])).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                if episode == '01':
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(story_url)
                if ep_soup is not None:
                    images = ep_soup.select('.ph img[src]')
                    self.image_list = []
                    for i in range(len(images)):
                        image_url = self.PAGE_PREFIX + images[i]['src'].split('?')[0]
                        image_url = self.remove_string(image_url, ['../', 'sn_'])
                        image_name = episode + '_' + str(i + 1)
                        self.add_to_image_list(image_name, image_url, to_jpg=True)
                    self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX)

    def download_episode_preview_guess(self, print_url=False):
        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'core_sys/images/contents/%s/block/%s/%s.jpg'
        is_successful = False
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1') or self.is_image_exists(episode + '_1', folder):
                continue
            is_success = False
            first = 19 + i
            second = 54 + 4 * i
            third = 43 + 6 * i
            for j in range(self.IMAGES_PER_EPISODE):
                image_url = template % (str(first).zfill(8), str(second).zfill(8), str(third + j).zfill(8))
                if print_url:
                    print(image_url)
                image_name = episode + '_' + str(j + 1)
                result = self.download_image(image_url, folder + '/' + image_name)
                if result == 0:
                    is_success = True
                    is_successful = True
                elif result == -1:
                    break
            if is_success:
                print(self.__class__.__name__ + ' - Guessed successfully!')
            else:
                if len(os.listdir(folder)) == 0:
                    os.rmdir(folder)
                return
        if len(os.listdir(folder)) == 0:
            os.rmdir(folder)
        return is_successful


# Salaryman ga Isekai ni Ittara Shitennou ni Natta Hanashi
class SalarymanShitennouDownload(Winter2025AnimeDownload, NewsTemplate):
    title = 'Salaryman ga Isekai ni Ittara Shitennou ni Natta Hanashi'
    keywords = [title, 'Headhunted to Another World: From Salaryman to Big Four!']
    website = 'https://salaryman-big4.com/'
    twitter = 'salaryman_big4'
    hashtags = 'サラリーマン四天王'
    folder_name = 'salarymanshitennou'

    PAGE_PREFIX = 'https://salaryman-big4.com/'
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        # self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            stories = soup.select('.sub-introduction__list.pc a[href]')
            curr_title = soup.select('.sub-introduction__title')
            curr_episode = None
            if len(curr_title) > 0:
                try:
                    curr_episode = int(curr_title[0].text.split('話')[0].split('第')[1])
                except:
                    pass
            for story in stories:
                try:
                    ep_num = int(story.text)
                except:
                    continue
                episode = str(ep_num).zfill(2)
                if self.is_image_exists(episode + '_1'):
                    continue
                if curr_episode is not None and curr_episode == ep_num:
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(story['href'])
                if ep_soup is None:
                    continue
                self.image_list = []
                images = ep_soup.select('.intro__slider img[src]')
                for i in range(len(images)):
                    image_url = images[i]['src']
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='li.js-animation-news',
                                    title_select='.news__ttl', date_select='.news__date', id_select='a',
                                    next_page_select='.next.page-numbers')

    def download_episode_preview_guess(self, print_url=False, print_invalid=False, max_count=100):
        if self.is_image_exists(str(self.FINAL_EPISODE).zfill(2) + '_1'):
            return
        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'wp/wp-content/uploads/%s/%s/サラリーマン四天王_%s-%s.jpg'
        current_date = datetime.now() + timedelta(hours=1)
        year = current_date.strftime('%Y')
        month = current_date.strftime('%m')
        is_successful = False
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1'):
                continue
            image_count = 0
            for j in range(max_count + 1):
                image_url = template % (year, month, str(i + 1), str(j))
                if print_url:
                    print(image_url)
                if self.is_valid_url(image_url, is_image=True):
                    print('VALID - ' + image_url)
                    image_count += 1
                    image_name = episode + '_' + str(image_count)
                    self.download_image(image_url, folder + '/' + image_name, to_jpg=True)
                    is_successful = True
                elif print_invalid:
                    print('INVALID - ' + image_url)
            if image_count != self.IMAGES_PER_EPISODE:
                break
        if is_successful:
            print(self.__class__.__name__ + ' - Guessed correctly!')
        return is_successful


# Sentai Red Isekai de Boukensha ni Naru
class IsekaiRedDownload(Winter2025AnimeDownload, NewsTemplate):
    title = 'Sentai Red Isekai de Boukensha ni Naru'
    keywords = [title, "The Red Ranger Becomes an Adventurer in Another World"]
    website = 'https://isekai-red-anime.com/'
    twitter = 'KizunaFive'
    hashtags = ['異世界レッド', 'isekai_red']
    folder_name = 'isekaired'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 8

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        try:
            template = self.PAGE_PREFIX + 'assets/story/%s/%s.webp'
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (str(i + 1), str(j + 1))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name, to_jpg=True) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='article', title_select='.entry-title',
                                    date_select='.entry-date', id_select=None, id_has_id=True, news_prefix='news.html',
                                    a_tag_prefix=self.PAGE_PREFIX + 'news.html#')


# Ubel Blatt
class UbelBlattDownload(Winter2025AnimeDownload, NewsTemplate):
    title = 'Ubel Blatt'
    keywords = [title, "Übel Blatt"]
    website = 'https://ubel-blatt-anime.com/'
    twitter = 'ubelblatt_info'
    hashtags = ['ユーベルブラット']
    folder_name = 'ubelblatt'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self, print_http_error=False):
        try:
            objs = self.get_json(self.PAGE_PREFIX + 'news/story_data')
            for obj in objs:
                if 'acf' in obj:
                    acf = obj['acf']
                    if 'number' in acf and 'images' in acf and isinstance(acf['images'], list):
                        try:
                            episode = ''
                            ep_num = acf['number']
                            for a in ep_num:
                                if a.isnumeric():
                                    episode += a
                            if len(episode) == 0:
                                continue
                            episode = str(int(episode)).zfill(2)
                        except:
                            continue
                        for i in range(len(acf['images'])):
                            image_url = acf['images'][i]
                            image_name = episode + '_' + str(i + 1)
                            self.add_to_image_list(image_name, image_url, to_jpg=True)
                        self.download_image_list(self.base_folder)
        except HTTPError:
            if print_http_error:
                print(self.__class__.__name__ + ' - 403 Error when retrieving story API.')
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-item',
                                    title_select='.news-item__title', date_select='.news-item__date', id_select=None,
                                    a_tag_start_text_to_remove='/', a_tag_prefix=self.PAGE_PREFIX,
                                    date_func=lambda x: x[0:4] + '.' + x[4:6] + '.' + x[6:8])


# Unnamed Memory Act.2
class UnnamedMemory2Download(Winter2025AnimeDownload, NewsTemplate):
    title = 'Unnamed Memory Act.2'
    keywords = [title]
    website = 'https://unnamedmemory.com/'
    twitter = 'Project_UM'
    hashtags = ['UnnamedMemory', 'アンメモ']
    folder_name = 'unnamedmemory2'

    PAGE_PREFIX = website
    FIRST_EPISODE = 13
    FINAL_EPISODE = 24
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        try:
            template = self.PAGE_PREFIX + 'assets/story/%s/%s.webp'
            stop = False
            for i in range(self.FIRST_EPISODE, self.FINAL_EPISODE + 1, 1):
                episode = str(i).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (str(i), str(j + 1))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name, to_jpg=True) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.content-entry',
                                    title_select='.entry-title span', date_select='.entry-date span',
                                    id_select=None, id_has_id=True, news_prefix='news.html', stop_date='2024.06')


# Watashi no Shiawase na Kekkon 2nd Season
class Watakon2Download(Winter2025AnimeDownload, NewsTemplate):
    title = 'Watashi no Shiawase na Kekkon 2nd Season'
    keywords = [title, 'My Happy Marriage', 'watakon']
    website = 'https://watakon-anime.com/'
    twitter = 'watashino_info'
    hashtags = ['watakon', 'わたしの幸せな結婚']
    folder_name = 'watakon2'

    PAGE_PREFIX = website
    FIRST_EPISODE = 14
    FINAL_EPISODE = 26
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        # self.download_episode_preview_guess()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            stories = soup.select('.index-Story_Content')
            for story in stories:
                try:
                    ep_num = int(self.convert_kanji_to_number(
                        story.select('span.num')[0].text.replace('第', '').replace('話', '')))
                    if ep_num < self.FIRST_EPISODE:
                        continue
                    episode = str(ep_num).zfill(2)
                except:
                    continue
                self.image_list = []
                images = story.select('.swiper-slide img[src]')
                for i in range(len(images)):
                    image_url = images[i]['src']
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url, to_jpg=True)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news_List li.item',
                                    date_select='span.time', title_select='.ttl', id_select='a',
                                    date_func=lambda x: x[0:4] + '.' + x[4:6] + '.' + x[6:8],
                                    next_page_select='.nextpostslink', stop_date='2024.09.18')

    def download_episode_preview_guess(self, print_url=False, print_invalid=False):
        if self.is_image_exists(str(self.FINAL_EPISODE).zfill(2) + '_1'):
            return
        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'wordpress/wp-content/uploads/%s/%s/img_story-%s_%s.jpg'
        current_date = datetime.now() + timedelta(hours=1)
        year = current_date.strftime('%Y')
        month = current_date.strftime('%m')
        is_successful = False
        for i in range(self.FIRST_EPISODE, self.FINAL_EPISODE + 1, 1):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1') or self.is_image_exists(episode + '_1', folder):
                continue
            is_success = False
            for j in range(self.IMAGES_PER_EPISODE):
                image_name = episode + '_' + str(j + 1)
                image_url = template % (year, month, episode, str(j + 1).zfill(2))
                if print_url:
                    print(image_url)
                if self.is_valid_url(image_url, is_image=True):
                    print('VALID - ' + image_url)
                    self.download_image(image_url, folder + '/' + image_name, to_jpg=True)
                    is_successful = True
                    is_success = True
                elif print_invalid:
                    print('INVALID - ' + image_url)
                if not is_success:
                    break
            if not is_success:
                break
        if is_successful:
            print(self.__class__.__name__ + ' - Guessed correctly!')
        return is_successful
