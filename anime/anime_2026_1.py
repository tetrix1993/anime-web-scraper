from anime.main_download import MainDownload, NewsTemplate, NewsTemplate2, NewsTemplate3, NewsTemplate4
from datetime import datetime, timedelta
from requests.exceptions import HTTPError
from scan import AniverseMagazineScanner
from bs4 import BeautifulSoup
import json
import os


# Winter 2026 Anime
class Winter2026AnimeDownload(MainDownload):
    season = "2026-1"
    season_name = "Winter 2026"
    folder_name = '2026-1'

    def __init__(self):
        super().__init__()


# 29-sai Dokushin Chuuken Boukensha no Nichijou
class Anime29SaiDownload(Winter2026AnimeDownload):
    title = '29-sai Dokushin Chuuken Boukensha no Nichijou'
    keywords = [title, 'The Daily Life of a Single 29-Year-Old Adventurer']
    website = 'https://anime-29sai-dokushin.com/'
    twitter = 'anime29sai'
    hashtags = 'アニメ29歳'
    folder_name = '29sai'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        template = self.PAGE_PREFIX + 'story/img/ep%s/ep%s_%s.jpg'
        try:
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (str(i + 1), episode, str(j + 1))
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
            news_prefix = self.PAGE_PREFIX + 'news/'
            json_obj = self.get_json(news_prefix + 'newslist.json')
            for item in json_obj:
                if 'datetime' in item and 'uniqueId' in item and 'title' in item:
                    try:
                        date = item['datetime'].replace('-', '.')
                    except:
                        continue
                    title = item['title']
                    unique_id = item['uniqueId']
                    if len(unique_id) == 0 and 'directLinkUrl' in item and len(item['directLinkUrl']) > 1:
                        url = self.PAGE_PREFIX + item['directLinkUrl'][1:]
                    else:
                        url = news_prefix + '?id=' + item['uniqueId']
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


# Champignon no Majo
class ChampignonDownload(Winter2026AnimeDownload, NewsTemplate):
    title = 'Champignon no Majo'
    keywords = [title, 'Champignon Witch']
    website = 'https://champignon-pr.com/'
    twitter = 'Champignon_PR'
    hashtags = 'シャンピニオンの魔女'
    folder_name = 'champignon'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        pass

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-list li',
                                    date_select='.date', title_select='.title', id_select='a')


# Eris no Seihai
class ErisSeihaiDownload(Winter2026AnimeDownload, NewsTemplate):
    title = 'Eris no Seihai'
    keywords = [title, 'The Holy Grail of Eris']
    website = 'https://eris-seihai.com/'
    twitter = 'Project_of_Eris'
    hashtags = 'エリスの聖杯'
    folder_name = 'erisseihai'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            stories = soup.select('.story__contents[id]')
            for story in stories:
                try:
                    episode = ''
                    ep_num = story['id']
                    for a in reversed(ep_num):
                        if a.isnumeric():
                            episode = a + episode
                    if len(episode) == 0:
                        continue
                    episode = str(int(episode)).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                images = story.select('.story__contents-sliderItem img[src]')
                self.image_list = []
                for i in range(len(images)):
                    image_url = images[i]['src']
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url, to_jpg=True)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news_item',
                                    date_select='.date', title_select='.desc', id_select=None,
                                    next_page_select='li.item.next a[href]')


# Hell Mode
class HellModeDownload(Winter2026AnimeDownload, NewsTemplate):
    title = 'Hell Mode'
    keywords = [title]
    website = 'https://hellmode-anime.com/'
    twitter = 'hellmode_anime'
    hashtags = ['ヘルモード']
    folder_name = 'hellmode'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        pass

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-list li',
                                    date_select='.date', title_select='.title', id_select='a')


# Jingai Kyoushitsu no Ningengirai Kyoushi
class JingaiKyoshitsuDownload(Winter2026AnimeDownload, NewsTemplate2):
    title = 'Jingai Kyoushitsu no Ningengirai Kyoushi'
    keywords = [title, 'A Misanthrope Teaches a Class for Demi-Humans']
    website = 'https://jingai-kyoshitsu-anime.com/'
    twitter = 'jingaikyoshitsu'
    hashtags = ['人外教室']
    folder_name = 'jingaikyoshitsu'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        pass

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX)


# Kirei ni Shitemoraemasu ka.
class KinishiteDownload(Winter2026AnimeDownload, NewsTemplate):
    title = 'Kirei ni Shitemoraemasu ka.'
    keywords = [title, 'Wash It All Away', 'kinishite']
    website = 'https://kinishite.com/'
    twitter = 'kinishite_anime'
    hashtags = ['きにして']
    folder_name = 'kinishite'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        template = self.PAGE_PREFIX + 'assets/img/story/ep%s/img%s.jpg'
        try:
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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.bl_posts_item', date_select='time',
                                    title_select='.bl_posts_txt', id_select='a', next_page_select='a.next.page-numbers',
                                    paging_type=3, paging_suffix='?page=%s')


# Kizoku Tensei: Megumareta Umare kara Saikyou no Chikara wo Eru
class KizokuTenseiDownload(Winter2026AnimeDownload, NewsTemplate):
    title = 'Kizoku Tensei: Megumareta Umare kara Saikyou no Chikara wo Eru'
    keywords = [title, "Noble Reincarnation: Born Blessed, So I'll Obtain Ultimate Power"]
    website = 'https://kizoku-tensei.com/'
    twitter = 'kizokutensei_PR'
    hashtags = ['貴族転生']
    folder_name = 'kizokutensei'

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
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            stories = soup.select('.idx-Story_Article')
            for story in stories:
                try:
                    episode = ''
                    ep_num = story.select('.idx-Story_Article-Numbering span')[0].text
                    for a in reversed(ep_num):
                        if a.isnumeric():
                            episode = a + episode
                    if len(episode) == 0:
                        continue
                    episode = str(int(episode)).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                images = story.select('.story-Slider_Slide img[src]')
                self.image_list = []
                for i in range(len(images)):
                    image_url = images[i]['src']
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url, to_jpg=True)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-archive-Item',
                                    date_select='.date', title_select='.title', id_select='a',
                                    next_page_select='.wp-pagenavi *', next_page_eval_index_class='current',
                                    next_page_eval_index=-1)

    def download_episode_preview_guess(self, print_invalid=False, download_valid=True):
        if self.is_image_exists(str(self.FINAL_EPISODE).zfill(2) + '_' + str(self.IMAGES_PER_EPISODE)):
            return

        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'wp/wp-content/uploads/%s/%s/KizokuTensei_%s.jpg'
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


# Majutsushi Kunon wa Mieteiru
class KunonDownload(Winter2026AnimeDownload, NewsTemplate):
    title = 'Majutsushi Kunon wa Mieteiru'
    keywords = [title, 'Kunon the Sorcerer Can See']
    website = 'https://kunonanime.jp/'
    twitter = 'animekunon'
    hashtags = ['アニメクノン']
    folder_name = 'kunon'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 5

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        template = self.PAGE_PREFIX + 'assets/img/story/ep%s/img%s.webp'
        try:
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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.c-post__list-item',
                                    date_select='.c-post__date', title_select='.c-post__title',
                                    id_select='.c-post__link--sub', a_tag_start_text_to_remove='../',
                                    a_tag_prefix=self.PAGE_PREFIX, next_page_select='.c-btn-pager__txt-wrap--next',
                                    paging_type=3, paging_suffix='?page=%s', date_func=lambda x: x[0:4] + '.' + x[5:])


# Maou no Musume wa Yasashisugiru!!
class MaomusuDownload(Winter2026AnimeDownload, NewsTemplate):
    title = 'Maou no Musume wa Yasashisugiru!!'
    keywords = [title, "The Demon King's Daughter is too Kind!!", 'maomusu']
    website = 'https://maomusu.com/'
    twitter = 'maomusu_info'
    hashtags = ['まおむす']
    folder_name = 'maomusu'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 5

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        template = self.PAGE_PREFIX + 'assets/img/story/ep%s/img%s.jpg'
        try:
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
                                    date_select='time', title_select='.bl_posts_txt', id_select='a',
                                    date_separator='/', next_page_select='a.next.page-numbers', paging_type=3,
                                    paging_suffix='?page=%s')


# Mayonaka Heart Tune
class MayochuDownload(Winter2026AnimeDownload, NewsTemplate2):
    title = 'Mayonaka Heart Tune'
    keywords = [title, 'Tune in to the Midnight Heart', 'mayochu']
    website = 'https://mayochu-anime.com/'
    twitter = 'anime_mayochu'
    hashtags = ['真夜中ハートチューン']
    folder_name = 'mayochu'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_external()
        self.download_news()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/01.html')
            stories = soup.select('table[summary="List_Type01"] a[href]')
            for story in stories:
                story_url = self.PAGE_PREFIX + story['href'].replace('../', '')
                try:
                    episode = ''
                    ep_num = story.text
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
        keywords = ['真夜中ハートチューン']
        AniverseMagazineScanner(keywords, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20251225', download_id=self.download_id).run()

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX)


# Okiraku Ryoushu no Tanoshii Ryouchi Bouei
class OkirakuRyoushuDownload(Winter2026AnimeDownload, NewsTemplate):
    title = 'Okiraku Ryoushu no Tanoshii Ryouchi Bouei'
    keywords = [title, 'Easygoing Territory Defense by the Optimistic Lord']
    website = 'https://okiraku-ryousyu-anime.jp/'
    twitter = 'okiraku_anime'
    hashtags = ['お気楽領主アニメ']
    folder_name = 'okirakuryoushu'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        pass

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.bl_news__article_item',
                                    date_select='time', title_select='.bl_news__article_body', id_select='a',
                                    next_page_select='a.next.page-numbers', paging_type=3, paging_suffix='?page=%s')


# Omae Gotoki ga Maou ni Kateru to Omouna
class OmagotoDownload(Winter2026AnimeDownload, NewsTemplate):
    title = 'Omae Gotoki ga Maou ni Kateru to Omouna'
    keywords = [title, 'Roll Over and Die', 'omagoto']
    website = 'https://omagoto.com/'
    twitter = 'omagoto_anime'
    hashtags = ['おまごと']
    folder_name = 'omagoto'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        pass

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-item', date_select='.date',
                                    title_select='.title', id_select='a', next_page_select='a.next.page-numbers')


# Osananajimi to wa Love Comedy ni Naranai
class OsaloveDownload(Winter2026AnimeDownload, NewsTemplate):
    title = 'Osananajimi to wa Love Comedy ni Naranai'
    keywords = [title, "You Can't Be In a Rom-Com with Your Childhood Friends!", 'osalove']
    website = 'https://anime-osalove.com/'
    twitter = 'love_Osnnjm_wm'
    hashtags = ['幼ラブ', '幼ラブアニメ']
    folder_name = 'osalove'

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
            soup = self.get_soup(self.PAGE_PREFIX + 'episode/')
            stories = soup.select('.newsCategory__anc[href]')
            for story in stories:
                try:
                    episode = ''
                    ep_num = story.text
                    for a in reversed(ep_num):
                        if a.isnumeric():
                            episode = a + episode
                    if len(episode) == 0:
                        continue
                    episode = str(int(episode)).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                ep_soup = self.get_soup(story['href'])
                if ep_soup is None:
                    continue
                images = ep_soup.select('img.mvSlider__main__item__img[src]')
                self.image_list = []
                for i in range(len(images)):
                    image_url = images[i]['src']
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url, to_jpg=True)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.newsCol',
                                    date_select='.newsCol__date', title_select='.newsCol__title', id_select=None,
                                    next_page_select='#load-more')

    def download_episode_preview_guess(self, print_url=False, print_invalid=False):
        if self.is_image_exists(str(self.FINAL_EPISODE).zfill(2) + '_1'):
            return
        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'websys/wp-content/uploads/%s/%s/%s_%s.'
        extensions = ['jpg']
        current_date = datetime.now() + timedelta(hours=1)
        year = current_date.strftime('%Y')
        month = current_date.strftime('%m')
        is_successful = False
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1') or self.is_image_exists(episode + '_1', folder):
                continue
            is_success = False
            for ext in extensions:
                for j in range(self.IMAGES_PER_EPISODE):
                    image_name = episode + '_' + str(j + 1)
                    f = '01★メインカット★' if j == 0 else str(j + 1).zfill(2)
                    image_url = (template % (year, month, episode, f) + ext)
                    if print_url:
                        print(image_url)
                    if self.is_valid_url(image_url, is_image=True):
                        print('VALID - ' + image_url)
                        self.download_image(image_url, folder + '/' + image_name, to_jpg=True)
                        is_successful = True
                        is_success = True
                    elif print_invalid:
                        print('INVALID - ' + image_url)
                    # if not is_success:
                    #     break
                if is_success:
                    break
            if not is_success:
                break
        if is_successful:
            print(self.__class__.__name__ + ' - Guessed correctly!')
        return is_successful


# Shibou Yuugi de Meshi wo Kuu.
class ShiboyugiDownload(Winter2026AnimeDownload, NewsTemplate2):
    title = "Shibou Yuugi de Meshi wo Kuu."
    keywords = [title, 'Playing Death Games to Put Food on the Table']
    website = 'https://shiboyugi-anime.com/'
    twitter = 'shibouyugi_'
    hashtags = ['死亡遊戯']
    folder_name = 'shiboyugi'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/01.html')
            stories = soup.select('table[summary="List_Type01"] a[href]')
            for story in stories:
                story_url = self.PAGE_PREFIX + story['href'].replace('../', '')
                try:
                    episode = ''
                    ep_num = story.text
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


# Yuusha no Kuzu
class YushanoKuzuDownload(Winter2026AnimeDownload, NewsTemplate):
    title = 'Yuusha no Kuzu'
    keywords = [title, 'Scum of the Brave']
    website = 'https://yushanokuzu.com/'
    twitter = 'yushanokuzu'
    hashtags = ['勇者のクズ']
    folder_name = 'yushanokuzu'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        pass

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.bl_news__article_item',
                                    date_select='time', title_select='.bl_news__article__ttl', id_select='a',
                                    next_page_select='a.next.page-numbers', paging_type=3, paging_suffix='?page=%s')


# Yuusha Party ni Kawaii Ko ga Ita node, Kokuhaku shitemita.
class YuukawaDownload(Winter2026AnimeDownload, NewsTemplate):
    title = 'Yuusha Party ni Kawaii Ko ga Ita node, Kokuhaku shitemita.'
    keywords = [title, "There was a Cute Girl in the Hero's Party, so I Tried Confessing to Her", 'yuukawa']
    website = 'https://yuukawa-anime.com/'
    twitter = 'yuukawa_anime'
    hashtags = ['ゆうかわ']
    folder_name = 'yuukawa'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            stories = soup.select('.story__contents[id]')
            for story in stories:
                try:
                    episode = ''
                    ep_num = story['id']
                    for a in reversed(ep_num):
                        if a.isnumeric():
                            episode = a + episode
                    if len(episode) == 0:
                        continue
                    episode = str(int(episode)).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                images = story.select('.story__contents-sliderItem img[src]')
                self.image_list = []
                for i in range(len(images)):
                    image_url = images[i]['src']
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url, to_jpg=True)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news__list li',
                                    date_select='.news__date', title_select='.news__link-title', id_select='a',
                                    next_page_select='ul.page-numbers li *.page-numbers',
                                    next_page_eval_index_class='current', next_page_eval_index=-1,
                                    date_func=lambda x: x[0:4] + '.' + x[5:7] + '.' + x[7:])


# Yuusha Party wo Oidasareta Kiyoubinbou
class KiyouBimbouDownload(Winter2026AnimeDownload, NewsTemplate):
    title = 'Yuusha Party wo Oidasareta Kiyoubinbou'
    keywords = [title, "Jack-of-All-Trades, Party of None", 'kiyou bimbou']
    website = 'https://kiyou-bimbou.com/'
    twitter = 'kiyou_bimbou'
    hashtags = ['器用貧乏']
    folder_name = 'kiyoubimbou'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 7

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            stories = soup.select('.story-container')
            for story in stories:
                try:
                    episode = ''
                    ep_num = story.select('.story-detail-ttl')[0].text.split('話')[0]
                    for a in reversed(ep_num):
                        if a.isnumeric():
                            episode = a + episode
                    if len(episode) == 0:
                        continue
                    episode = str(int(episode)).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                images = story.select('.story-thumb-item img[src]')
                self.image_list = []
                for i in range(len(images)):
                    image_url = images[i]['src']
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url, to_jpg=True)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-box',
                                    date_select='.news-box-date', title_select='.news-txt-box', id_select='a',
                                    next_page_select='ul.page-numbers li *.page-numbers',
                                    next_page_eval_index_class='current', next_page_eval_index=-1)

    def download_episode_preview_guess(self, print_url=False, print_invalid=False):
        if self.is_image_exists(str(self.FINAL_EPISODE).zfill(2) + '_1'):
            return
        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'aRbOqWxL/wp-content/uploads/%s/%s/batch_kyou_%s_%s.'
        extensions = ['jpg']
        current_date = datetime.now() + timedelta(hours=1)
        year = current_date.strftime('%Y')
        month = current_date.strftime('%m')
        is_successful = False
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1') or self.is_image_exists(episode + '_1', folder):
                continue
            is_success = False
            for ext in extensions:
                for j in range(self.IMAGES_PER_EPISODE):
                    image_name = episode + '_' + str(j + 1)
                    image_url = (template % (year, month, episode, 'main' if j == 0 else 'sub' + str(j))) + ext
                    if print_url:
                        print(image_url)
                    if self.is_valid_url(image_url, is_image=True):
                        print('VALID - ' + image_url)
                        self.download_image(image_url, folder + '/' + image_name, to_jpg=True)
                        is_successful = True
                        is_success = True
                    elif print_invalid:
                        print('INVALID - ' + image_url)
                    # if not is_success:
                    #     break
                if is_success:
                    break
            if not is_success:
                break
        if is_successful:
            print(self.__class__.__name__ + ' - Guessed correctly!')
        return is_successful


# Yuusha-kei ni Shosu: Choubatsu Yuusha 9004-tai Keimu Kiroku
class YushakeiDownload(Winter2026AnimeDownload):
    title = 'Yuusha-kei ni Shosu: Choubatsu Yuusha 9004-tai Keimu Kiroku'
    keywords = [title, "Sentenced to Be a Hero", 'yushakei']
    website = 'https://yushakei-pj.com/'
    twitter = 'yushakei_PJ'
    hashtags = ['勇者刑に処す', 'yushakei']
    folder_name = 'yushakei'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 8

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        template = self.PAGE_PREFIX + 'episodes/img/%s/%s.jpg'
        try:
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
        try:
            results = []
            news_obj = self.get_last_news_log_object()
            news_prefix = self.PAGE_PREFIX + 'news/'
            json_obj = self.get_json(news_prefix + 'newslist.json')
            for item in json_obj:
                if 'date' in item and 'uniqueId' in item and 'title' in item:
                    try:
                        date = item['date']
                    except:
                        continue
                    title = item['title']
                    unique_id = item['uniqueId']
                    if len(unique_id) == 0 and 'directLinkUrl' in item and len(item['directLinkUrl']) > 1:
                        url = self.PAGE_PREFIX + item['directLinkUrl'][1:]
                    else:
                        url = news_prefix + '?id=' + item['uniqueId']
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
