from anime.main_download import MainDownload, NewsTemplate, NewsTemplate2, NewsTemplate4
from datetime import datetime, timedelta
from requests.exceptions import HTTPError
from scan import AniverseMagazineScanner
from bs4 import BeautifulSoup
import json
import os


# Fall 2024 Anime
class Fall2024AnimeDownload(MainDownload):
    season = "2024-4"
    season_name = "Fall 2024"
    folder_name = '2024-4'

    def __init__(self):
        super().__init__()


# Acro Trip
class AcroTripDownload(Fall2024AnimeDownload, NewsTemplate):
    title = 'Acro Trip'
    keywords = [title]
    website = 'https://acrotrip-anime.com/'
    twitter = 'acrotrip_anime'
    hashtags = ['アクロトリップ']
    folder_name = 'acrotrip'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 5

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        try:
            template = self.PAGE_PREFIX + 'dist/img/story/ep%s/img%s.jpg'
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (str(i + 1), str(j + 1))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name) == -1:
                        stop = True
                        break
                if stop:
                    break
            # soup = self.get_soup(self.PAGE_PREFIX)
            # btns = soup.select('.tp_story__tab_item[data-tab-target]')
            # for btn in btns:
            #     try:
            #         episode = str(int(btn.select('span')[0].text.replace('#', ''))).zfill(2)
            #         target = btn['data-tab-target']
            #     except:
            #         continue
            #     images = soup.select(f'#{target} .tp_story__imgMain_item img[src]')
            #     self.image_list = []
            #     for i in range(len(images)):
            #         image_url = self.PAGE_PREFIX + images[i]['src']
            #         image_name = episode + '_' + str(i + 1)
            #         self.add_to_image_list(image_name, image_url)
            #     self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news_item', title_select='.ttl',
                                    date_select='.p-news__list-date', id_select='a', paging_type=3,
                                    paging_suffix='?page=%s', next_page_select='.page-numbers',
                                    next_page_eval_index_class='current', next_page_eval_index=-1,
                                    date_func=lambda x: x[0:4] + '.' + str(self.convert_month_string_to_number(x[5:8])).zfill(2) + '.' + x[9:])

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.kv_image source[type="image/webp"][srcset]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['srcset']
                if not image_url.endswith('_sp.webp'):
                    continue
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'dist/img/character/character%s/stand.webp'
        try:
            for i in range(20):
                image_name = 'character' + str(i + 1)
                if self.is_image_exists(image_name, folder):
                    continue
                image_url = template % str(i + 1)
                if self.download_image(image_url, folder + '/' + image_name) == -1:
                    break
        except Exception as e:
            self.print_exception(e, 'Character')


# Amagami-san Chi no Enmusubi
class AmagamiDownload(Fall2024AnimeDownload, NewsTemplate):
    title = 'Amagami-san Chi no Enmusubi'
    keywords = [title, 'Tying the Knot with an Amagami Sister']
    website = 'https://amagami-anime.com/'
    twitter = 'amagami_anime'
    hashtags = ['甘神さんちの縁結び']
    folder_name = 'amagami'

    PAGE_PREFIX = website
    FINAL_EPISODE = 24
    IMAGES_PER_EPISODE = 8

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        # self.download_key_visual()
        # self.download_character()
        self.download_media()

    def download_episode_preview(self):
        try:
            template = self.PAGE_PREFIX + 'img/story_%s_%s.jpg'
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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.accordion_one', title_select='p',
                                    date_select='time', id_select=None, id_has_id=True)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.fv__contents .fv__left .swiper-slide img[src]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src']
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'img/character-%s.png'
        self.download_by_template(folder, template, 2, 1)

    def download_media(self):
        folder = self.create_media_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'blu-ray/')
            images = soup.select('.jacket img[src],.image img[src]')
            self.image_list = []
            for image in images:
                if 'nowprinting' in image['src']:
                    continue
                if image['src'].startswith('../'):
                    image_url = self.PAGE_PREFIX + image['src'][3:]
                elif image['src'].startswith('http'):
                    image_url = image['src']
                else:
                    image_url = self.PAGE_PREFIX + image['src']
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')


# Ao no Exorcist: Yuki no Hate-hen
class Aoex4Download(Fall2024AnimeDownload, NewsTemplate):
    title = 'Ao no Exorcist: Yuki no Hate-hen'
    keywords = [title, 'aoex', 'Blue Exorcist: Beyond the Snow Saga', '4th Season']
    website = 'https://ao-ex.com/snow/'
    twitter = 'aoex_anime'
    hashtags = ['青エク', 'aoex']
    folder_name = 'aoex4'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()

    def download_episode_preview(self):
        try:
            story_prefix = self.PAGE_PREFIX + 'story/'
            soup = self.get_soup(story_prefix)
            stories = soup.select('.story_navList a[href]')
            for story in stories:
                try:
                    episode = str(int(story.select('.linkbox_txt')[0].text)).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_5'):
                    continue
                if '--current' in story['class']:
                    ep_soup = soup
                else:
                    story_url = story['href']
                    if story_url.startswith('./'):
                        story_url = story_prefix + story_url[2:]
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


# Arifureta Shokugyou de Sekai Saikyou 3rd Season
class Arifureta3Download(Fall2024AnimeDownload, NewsTemplate):
    title = "Arifureta Shokugyou de Sekai Saikyou 3rd Season"
    keywords = [title, "Arifureta: From Commonplace to World's Strongest 3rd Season"]
    website = 'https://arifureta.com/'
    twitter = 'ARIFURETA_info'
    hashtags = ['ARIFURETA', 'ありふれた']
    folder_name = 'arifureta3'

    PAGE_PREFIX = website
    FINAL_EPISODE = 16
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        # self.download_episode_preview_guess()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')

            # Evaluate current page
            title = soup.select('h1.title')
            try:
                text = title[0].text.split('話')[0].split('第')[1]
                episode = str(int(self.convert_kanji_to_number(text))).zfill(2)
                if not self.is_image_exists(episode + '_1'):
                    self.image_list = []
                    images = soup.select('#story_cont img[src]')
                    for i in range(len(images)):
                        image_url = self.clear_resize_in_url(images[i]['src'])
                        image_name = episode + '_' + str(i + 1)
                        self.add_to_image_list(image_name, image_url, to_jpg=True)
                    self.download_image_list(self.base_folder)
            except:
                pass

            # Evaluate other pages
            stories = soup.select('ol.season03 a[href]')
            for story in stories:
                try:
                    text = story.text.replace('第', '').replace('話', '')
                    episode = str(int(self.convert_kanji_to_number(text))).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                ep_soup = self.get_soup(story['href'])
                if ep_soup is None:
                    continue
                self.image_list = []
                images = ep_soup.select('#story_cont img[src]')
                for i in range(len(images)):
                    image_url = self.clear_resize_in_url(images[i]['src'])
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url, to_jpg=True)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_guess(self, print_url=False, print_invalid=False):
        if self.is_image_exists(str(self.FINAL_EPISODE).zfill(2) + '_1'):
            return
        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'wp3/wp-content/uploads/%s/%s/%s'
        current_date = datetime.now() + timedelta(hours=1)
        year = current_date.strftime('%Y')
        month = current_date.strftime('%m')
        is_successful = False
        image_folder = folder + '/' + year + '/' + month
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1'):
                continue
            image_count = 0
            for j in range(100):
                for k in ['jpg', 'png']:
                    image_name = str(i + 1) + '-' + str(j) + '.' + k
                    image_url = template % (year, month, image_name)
                    if self.is_valid_url(image_url, is_image=True):
                        print('VALID - ' + image_url)
                        if not os.path.exists(image_folder):
                            os.makedirs(image_folder)
                        self.download_image(image_url, image_folder + '/' + image_name, to_jpg=True)
                        is_successful = True
                        image_count += 1
                        break
                    elif print_invalid:
                        print('INVALID - ' + image_url)
                if image_count == self.IMAGES_PER_EPISODE:
                    break
            if image_count == 0:
                break
        if is_successful:
            print(self.__class__.__name__ + ' - Guessed correctly!')
        return is_successful


# Hitoribocchi no Isekai Kouryaku
class BocchiKouryakuDownload(Fall2024AnimeDownload, NewsTemplate):
    title = 'Hitoribocchi no Isekai Kouryaku'
    keywords = [title, 'Loner Life in Another World']
    website = 'https://bocchi-kouryaku.com/'
    twitter = 'bocchi_PR'
    hashtags = 'ぼっち攻略'
    folder_name = 'bocchikouryaku'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/latest')
            build_id = soup.select('script[src*="/_buildManifest.js"]')[0]['src'].split('/static/')[1].split('/')[0]
            obj = self.get_json(self.PAGE_PREFIX + f'_next/data/{build_id}/story/latest.json')
            for story in obj['pageProps']['storyList']:
                story_data = story['data'][0]
                episode = str(story_data['episode']).zfill(2)
                image_list = story_data['imageList']
                for i in range(len(image_list)):
                    image_name = episode + '_' + str(i + 1)
                    image_url = self.PAGE_PREFIX + image_list[i]['url'][1:]
                    self.add_to_image_list(image_name, image_url, to_jpg=True)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.c-fGHEql', paging_type=2,
                                    skip_first_page_num=False, title_select='.c-gKRVtX p',
                                    date_select='.c-jrhcXL p', id_select=None,
                                    a_tag_prefix=self.PAGE_PREFIX, a_tag_start_text_to_remove='/',
                                    next_page_select='.c-igANRe button.c-gulvcB', next_page_eval_index=-1,
                                    next_page_eval_index_class='c-gulvcB-kCOsjz-hidden-true')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('kv_20240917_pc', self.PAGE_PREFIX + 'assets/image/kv/20240917/pc.png')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character')
            content = soup.select('#__NEXT_DATA__')
            json_obj = json.loads(content[0].contents[0])
            for chara in json_obj['props']['pageProps']['characterCastList']:
                if chara is None or 'character' not in chara and 'images' not in chara['character']:
                    continue
                image_urls = chara['character']['images']
                self.image_list = []
                if 'main' in image_urls:
                    image_name = self.generate_image_name_from_url(image_urls['main'], 'character')
                    self.add_to_image_list(image_name, self.PAGE_PREFIX + image_urls['main'][1:])
                if 'facies' in image_urls:
                    image_name = self.generate_image_name_from_url(image_urls['facies'], 'character')
                    self.add_to_image_list(image_name, self.PAGE_PREFIX + image_urls['facies'][1:])
                self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Kabushikigaisha Magi-Lumière
class MagilumiereDownload(Fall2024AnimeDownload, NewsTemplate4):
    title = 'Kabushikigaisha Magi-Lumière'
    keywords = [title, 'Magilumiere Magical Girls Inc.']
    website = 'https://magilumiere-pr.com/'
    twitter = 'MagilumiereLtd'
    hashtags = 'マジルミエ'
    folder_name = 'magilumiere'

    PAGE_PREFIX = website
    IMAGES_PER_EPISODE = 6
    FINAL_EPISODE = 12

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
            for story in json_obj['story']:
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

    def download_news(self, json_obj=None):
        self.download_template_news(json_url=self.PAGE_PREFIX + 'api/site-data/init')


# Kekkon suru tte, Hontou desu ka
class KekkonDesukaDownload(Fall2024AnimeDownload, NewsTemplate):
    title = 'Kekkon suru tte, Hontou desu ka'
    keywords = [title, '365 Days to the Wedding']
    website = 'https://365-wedding-anime.com/'
    twitter = 'kekkon_anime'
    hashtags = ['kekkon_anime', '結婚ですか']
    folder_name = 'kekkondesuka'

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
                            episode = str(int(acf['number'].split('#')[1])).zfill(2)
                        except:
                            continue
                        for i in range(len(acf['images'])):
                            image_url = acf['images'][i]
                            image_name = episode + '_' + str(i + 1)
                            self.add_to_image_list(image_name, image_url)
                        self.download_image_list(self.base_folder)
        except HTTPError:
            if print_http_error:
                print(self.__class__.__name__ + ' - 403 Error when retrieving story API.')
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-item',
                                    title_select='.news-item__title', date_select='.news-item__date',
                                    id_select=None, a_tag_prefix=self.PAGE_PREFIX, a_tag_start_text_to_remove='/')


# Kimi wa Meido-sama.
class MeidosamaDownload(Fall2024AnimeDownload, NewsTemplate):
    title = 'Kimi wa Meido-sama.'
    keywords = [title, 'You Are Ms. Servant.']
    website = 'https://kimihameidosama-anime.com/'
    twitter = 'meidosama_anime'
    hashtags = ['君は冥土様']
    folder_name = 'meidosama'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        prefix = self.PAGE_PREFIX + 'story/'
        try:
            soup = self.get_soup(prefix)
            wrap = soup.select('.epNumWrap')
            episode = ''
            for s in wrap[0].text:
                if s.isnumeric():
                    episode += s
                elif s == ' ' and len(episode) > 0:
                    break
            episode = episode.zfill(2)
            self.image_list = []
            images = soup.select('.storyBox_txt img[src]')
            for i in range(len(images)):
                image_url = images[i]['src']
                image_name = episode + '_' + str(i + 1)
                self.add_to_image_list(image_name, image_url, to_jpg=True)
            self.download_image_list(self.base_folder)
            # stories = soup.select('.storyNav a[href]')
            # for story in stories:
            #     try:
            #         episode = str(int(story.text.replace('EP', ''))).zfill(2)
            #     except:
            #         continue
            #     if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
            #         continue
            #     story_soup = soup
            #     # story_soup = self.get_soup(prefix + story['href'])
            #     # if story_soup is None:
            #     #     continue
            #     self.image_list = []
            #     images = story_soup.select('.storyBox_txt img[src]')
            #     for i in range(len(images)):
            #         image_url = images[i]['src']
            #         image_name = episode + '_' + str(i + 1)
            #         self.add_to_image_list(image_name, image_url, to_jpg=True)
            #     self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news/'
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news_item', title_select='.news_ttl',
                                    date_select='.news_date', id_select='a', a_tag_prefix=news_url, paging_type=1,
                                    next_page_select='.pagerList .linkBox', next_page_eval_index=-1,
                                    next_page_eval_index_class='is-active')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('#js-imgModal img[src*="/img/"]')
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].split('?')[0][1:]
                image_name = self.generate_image_name_from_url(image_url, 'img')
                self.add_to_image_list(image_name, image_url)
        except Exception as e:
            self.print_exception(e, 'Key Visual')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'assets/img/character/chara%s_full.png'
        self.download_by_template(folder, template, 1, 1)


# Maou 2099
class Maou2099Download(Fall2024AnimeDownload, NewsTemplate):
    title = 'Maou 2099'
    keywords = [title, 'Demon Lord 2099']
    website = 'https://2099.world/'
    twitter = '2099_anime'
    hashtags = ['魔王2099']
    folder_name = 'maou2099'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        story_url = self.PAGE_PREFIX + 'story/'
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            stories = soup.select('.p-story_nav__list-item')
            for story in stories:
                try:
                    a_tag = story.select('a[href]')[0]
                    episode = ''
                    for s in a_tag.text:
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
                    ep_soup = self.get_soup(self.PAGE_PREFIX + a_tag['href'][1:])
                images = ep_soup.select('.p-story_visual__list-item img[src]')
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
                                    title_select='.p-news_data__title', date_select='.p-news_data__date',
                                    id_select='a', a_tag_prefix=self.PAGE_PREFIX, a_tag_start_text_to_remove='/',
                                    date_func=lambda x: x[0:4] + '.' + x[5:7] + '.' + x[7:9], paging_type=1,
                                    next_page_select='.c-pagination__list-item', next_page_eval_index=-1,
                                    next_page_eval_index_class='is-current')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.p-hero_kv__main-img img[src*="/main/"]')
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].split('?')[0][1:]
                image_name = self.generate_image_name_from_url(image_url, 'main')
                self.add_to_image_list(image_name, image_url)
        except Exception as e:
            self.print_exception(e, 'Key Visual')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'teaser/img/character/img_chara%s.png'
        self.download_by_template(folder, template, 2, 1)


# Maou-sama, Retry! R
class MaousamaRetry2Download(Fall2024AnimeDownload, NewsTemplate):
    title = 'Maou-sama, Retry! R'
    keywords = [title, 'Demon Lord, Retry! R', '2nd']
    website = 'https://maousama-anime.com/2024/'
    twitter = 'maousama_anime'
    hashtags = ['魔王様リトライ']
    folder_name = 'maousamaretry2'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/01/')
            a_tags = soup.select('.story__list a[href]')
            for a_tag in a_tags:
                try:
                    episode = str(int(a_tag.select('.story__link-text')[0].text)).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                if episode == '01':
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(a_tag['href'])
                if ep_soup is None:
                    continue
                self.image_list = []
                images = ep_soup.select('.story__contents-slider-item img[src]')
                for i in range(len(images)):
                    image_url = images[i]['src']
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url, to_jpg=True)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news__link',
                                    title_select='.news__txt', date_select='.news__dateWrap',
                                    id_select=None, date_func=lambda x: x[0:4] + '.' + x[4:])

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.kv__container img[src*="/kv/"]')
            for image in images:
                image_url = image['src'].split('?')[0]
                image_name = self.generate_image_name_from_url(image_url, 'kv')
                self.add_to_image_list(image_name, image_url)
        except Exception as e:
            self.print_exception(e, 'Key Visual')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        self.image_list = []
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            images = soup.select('.character__img[src*="/character/"]')
            for image in images:
                image_url = image['src'].split('?')[0]
                image_name = self.generate_image_name_from_url(image_url, 'character')
                self.add_to_image_list(image_name, image_url)
        except Exception as e:
            self.print_exception(e, 'Character')
        self.download_image_list(folder)


# Nageki no Bourei wa Intai shitai
class NagekiDownload(Fall2024AnimeDownload, NewsTemplate):
    title = 'Nageki no Bourei wa Intai shitai'
    keywords = [title, 'Let This Grieving Soul Retire']
    website = 'https://nageki-anime.com/'
    twitter = 'nageki_official'
    hashtags = ['嘆きの亡霊']
    folder_name = 'nageki'

    PAGE_PREFIX = website
    FINAL_EPISODE = 13

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_external()
        self.download_news()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/latest')
            content = soup.select('#__NEXT_DATA__')
            obj = json.loads(content[0].contents[0])
            for story in obj['props']['pageProps']['contentList']:
                story_data = story['data'][0]
                episode = str(story_data['episode']).zfill(2)
                image_list = story_data['imageList']
                for i in range(len(image_list)):
                    image_name = episode + '_' + str(i + 1)
                    image_url = self.PAGE_PREFIX + image_list[i]['url'][1:]
                    self.add_to_image_list(image_name, image_url, to_jpg=True)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_external(self):
        keywords = ['嘆きの亡霊は引退したい']
        AniverseMagazineScanner(keywords, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20240927', download_id=self.download_id).run()

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.c-hnachi', paging_type=2,
                                    skip_first_page_num=False, title_select='.c-hnachi .c-dbxBTl p',
                                    date_select='.c-hnachi .c-dhzjXW p', id_select=None,
                                    a_tag_prefix=self.PAGE_PREFIX, a_tag_start_text_to_remove='/',
                                    next_page_select='.c-iEPVyt button', next_page_eval_index=-1,
                                    next_page_eval_index_class='c-PJLV-cqNpHX-disabled-true')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        template = self.PAGE_PREFIX + 'assets/keyvisual/%s/pc.png'
        try:
            for i in range(10):
                image_url = template % str(i + 1)
                image_name = 'kv' + str(i + 1)
                if self.download_image(image_url, folder + '/' + image_name) == -1:
                    break
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'assets/character/%s/whole-body_PC.png'
        face_template = self.PAGE_PREFIX + 'assets/character/%s/face%s.png'
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character')
            content = soup.select('#__NEXT_DATA__')
            json_obj = json.loads(content[0].contents[0])
            for character in json_obj['props']['pageProps']['characterData']:
                if character is None or 'id' not in character:
                    continue
                name = character['id']
                image_name = name + '_whole-body_PC'
                if self.is_image_exists(image_name, folder):
                    continue
                self.image_list = []
                image_url = template % name
                self.add_to_image_list(image_name, image_url)
                for i in range(3):
                    face_url = face_template % (name, str(i + 1))
                    face_name = name + '_face' + str(i + 1)
                    self.add_to_image_list(face_name, face_url)
                self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')

    def download_media(self):
        folder = self.create_media_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'products')
            content = soup.select('#__NEXT_DATA__')
            obj = json.loads(content[0].contents[0])
            for product in obj['props']['pageProps']['productsList']:
                product_data = product['data']
                for data in product_data:
                    content = data['content']
                    content_soup = BeautifulSoup(content, 'html.parser')
                    images = content_soup.select('img[src]')
                    for image in images:
                        if 'nowprinting' in image['src']:
                            continue
                        image_url = self.PAGE_PREFIX + image['src'][1:].split('?')[0]
                        image_name = self.extract_image_name_from_url(image_url)
                        self.add_to_image_list(image_name, image_url, to_jpg=True)
                    self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


# NegiPosi Angler
class NegaguraDownload(Fall2024AnimeDownload):
    title = 'NegaPosi Angler'
    keywords = [title, 'Negative Positive Angler']
    website = 'https://np-angler.com/'
    twitter = 'np_angler'
    hashtags = ['ネガグラ']
    folder_name = 'negagura'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()

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
                    if self.download_image(image_url, self.base_folder + '/' + image_name) == -1:
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
                        date = datetime.strptime(item['day'], "%Y.%m.%d").strftime("%Y.%m.%d")
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

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.visual_wrap img[src*="/top/"]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src']
                if '/visual/' in image_url:
                    image_name = self.generate_image_name_from_url(image_url, 'top')
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')


# Party kara Tsuihou sareta Sono Chiyushi, Jitsu wa Saikyou ni Tsuki
class SonoChiyushiDownload(Fall2024AnimeDownload, NewsTemplate2):
    title = 'Party kara Tsuihou sareta Sono Chiyushi, Jitsu wa Saikyou ni Tsuki'
    keywords = [title, 'The Healer Who Was Banished From His Party, Is, in Fact, the Strongest']
    website = 'https://sonochiyushi.com/'
    twitter = 'sonochiyushi'
    hashtags = ['その治癒師']
    folder_name = 'sonochiyushi'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_episode_preview_guess()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/01.html')
            stories = soup.select('table[summary="List_Type01"] a[href]')
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
                        self.add_to_image_list(image_name, image_url)
                    self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_guess(self, print_url=False):
        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'core_sys/images/contents/%s/block/%s/%s.jpg'
        is_successful = False
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1'):
                continue
            is_success = False
            first = 42 + i
            second = 80 + 4 * i
            third = 98 + 6 * i
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

    def download_news(self):
        self.download_template_news(self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.hero__img source[srcset]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['srcset']
                if '/main/' not in image_url:
                    continue
                image_name = self.generate_image_name_from_url(image_url, 'main')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        prefix = self.PAGE_PREFIX + 'core_sys/images/main/chara/chara'
        templates = [prefix + '%s.webp', prefix + '%s_face.webp',
                     prefix + '%s.png', prefix + '%s_face.png']
        self.download_by_template(folder, templates, 2, 1, max_skip=1)


# Re:Zero kara Hajimeru Isekai Seikatsu 3rd Season
class ReZero3Download(Fall2024AnimeDownload):
    title = "Re:Zero kara Hajimeru Isekai Seikatsu 3rd Season"
    keywords = [title, "rezero", "Re:Zero - Starting Life in Another World"]
    folder_name = 'rezero3'
    website = 'http://re-zero-anime.jp/tv/'
    twitter = 'Rezero_official'

    PAGE_PREFIX = website
    FIRST_EPISODE = 51
    FINAL_EPISODE = 66
    IMAGES_PER_EPISODE = 10

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()

    def download_episode_preview(self):
        try:
            template = self.PAGE_PREFIX + 'assets/episode/%s/%s.webp'
            stop = False
            for i in range(self.FIRST_EPISODE, self.FINAL_EPISODE + 1, 1):
                episode = str(i).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE).zfill(2)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (episode, str(j + 1))
                    image_name = episode + '_' + str(j + 1).zfill(2)
                    if self.download_image(image_url, self.base_folder + '/' + image_name, to_jpg=True) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)


# Rekishi ni Nokoru Akujo ni Naru zo
class ReikiakuDownload(Fall2024AnimeDownload, NewsTemplate):
    title = 'Rekishi ni Nokoru Akujo ni Naru zo'
    keywords = [title, 'I\'ll Become a Villainess Who Goes Down in History', 'rekiaku']
    website = 'https://rekiaku-anime.com/'
    twitter = 'rekiaku'
    hashtags = ['rekiaku', '歴史に残る悪女になるぞ', '歴悪']
    folder_name = 'rekiaku'

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
            template = self.PAGE_PREFIX + 'story/_image/story%s_%s@2x.png'
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (episode, str(j + 1))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name, to_jpg=True) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.newsList li',
                                    title_select='.text', date_select='.days', id_select='a',
                                    a_tag_prefix=self.PAGE_PREFIX, a_tag_start_text_to_remove='/')


# Saikyou no Shienshoku "Wajutsushi" de Aru Ore wa Sekai Saikyou Clan wo Shitagaeru
class WajutsushiDownload(Fall2024AnimeDownload, NewsTemplate):
    title = 'Saikyou no Shienshoku "Wajutsushi" de Aru Ore wa Sekai Saikyou Clan wo Shitagaeru'
    keywords = [title, 'The Most Notorious "Talker" Runs the World\'s Greatest Clan']
    website = 'https://wajutsushi-anime.com/'
    twitter = 'wajutsushi_PR'
    hashtags = ['話術士', 'wajutsushi']
    folder_name = 'wajutsushi'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/latest')
            build_id = soup.select('script[src*="/_buildManifest.js"]')[0]['src'].split('/static/')[1].split('/')[0]
            obj = self.get_json(self.PAGE_PREFIX + f'_next/data/{build_id}/story/latest.json')
            for story in obj['pageProps']['storyList']:
                story_data = story['data'][0]
                episode = str(story_data['episode']).zfill(2)
                image_list = story_data['imageList']
                for i in range(len(image_list)):
                    image_name = episode + '_' + str(i + 1)
                    image_url = self.PAGE_PREFIX + image_list[i]['url'][1:]
                    self.add_to_image_list(image_name, image_url, to_jpg=True)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.c-jhOyWv',
                                    skip_first_page_num=False, title_select='.c-canASN',
                                    date_select='.c-cmzDjZ p', id_select=None, paging_type=2,
                                    a_tag_prefix=self.PAGE_PREFIX, a_tag_start_text_to_remove='/',
                                    next_page_select='.c-guJmrn-enMdry-variant-next')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('kv_pc', self.PAGE_PREFIX + 'assets/kv/pc.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'assets/character/%s/main.png'
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character')
            content = soup.select('#__NEXT_DATA__')
            json_obj = json.loads(content[0].contents[0])
            self.image_list = []
            for character in json_obj['props']['pageProps']['characterList']:
                if character is None or 'id' not in character:
                    continue
                name = character['id']
                image_name = name + '_main'
                if self.is_image_exists(image_name, folder):
                    continue
                self.add_to_image_list(image_name, template % name)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Sayounara Ryuusei, Konnichiwa Jinsei
class SayounaraRyuuseiDownload(Fall2024AnimeDownload, NewsTemplate):
    title = "Sayounara Ryuusei, Konnichiwa Jinsei"
    keywords = [title, 'Good Bye, Dragon Life.']
    website = "https://dragonlife-anime.com/"
    twitter = 'dragonlife_PR'
    hashtags = '竜生'
    folder_name = 'sayounararyuusei'

    PAGE_PREFIX = website
    IMAGES_PER_EPISODE = 8
    FINAL_EPISODE = 12

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        try:
            template = self.PAGE_PREFIX + 'images/episodes/%s/img_%s.jpg'
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (episode, str(j + 1).zfill(2))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news/'
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.icihran dl',
                                    title_select='a', date_select='dt', id_select='a', a_tag_prefix=news_url,
                                    news_prefix='news/index.html')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.main_ph img[src*="/images/"],.main_ph source[srcset*="/images/"]')
            self.image_list = []
            for image in images:
                if image.has_attr('src'):
                    image_url = image['src'].split('?')[0]
                else:
                    image_url = image['srcset'].split('?')[0]
                if image_url.startswith('./'):
                    image_url = self.PAGE_PREFIX + image_url[2:]
                image_name = self.generate_image_name_from_url(image_url, 'images')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.chara02 img[src*="/images/"]')
            self.image_list = []
            for image in images:
                image_url = image['src'].split('?')[0]
                if image_url.startswith('./'):
                    image_url = self.PAGE_PREFIX + image_url[2:]
                image_name = self.generate_image_name_from_url(image_url, 'images')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Seirei Gensouki 2
class SeireiGensouki2Download(Fall2024AnimeDownload, NewsTemplate):
    title = "Seirei Gensouki 2"
    keywords = [title, "Spirit Chronicles", '2nd']
    website = "https://seireigensouki.com/"
    twitter = 'seireigensouki'
    hashtags = '精霊幻想記'
    folder_name = 'seireigensouki2'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def run(self):
        soup = self.download_episode_preview()
        self.download_news()
        self.download_episode_preview_guess()
        self.download_key_visual(soup)
        self.download_character()

    def download_episode_preview(self):
        soup = None
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            stories = soup.select('.story-box')
            for story in stories:
                try:
                    episode = str(int(story.select('.num')[0].text)).zfill(2)
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
        return soup

    def download_episode_preview_guess(self, print_invalid=False, download_valid=True):
        if self.is_image_exists(str(self.FINAL_EPISODE).zfill(2) + '_' + str(self.IMAGES_PER_EPISODE)):
            return

        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + '2ndwp/wp-content/uploads/%s/%s/%s.png'
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

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-item',
                                    title_select='.title', date_select='.date', id_select='a')

    def download_key_visual(self, soup=None):
        folder = self.create_key_visual_directory()
        try:
            if soup is None:
                soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.kv-container img[src]')
            self.image_list = []
            for image in images:
                image_url = image['src'].split('?')[0]
                if '/images/' not in image_url:
                    continue
                image_name = self.generate_image_name_from_url(image_url, 'images')
                if image_name.endswith('-sp'):
                    continue
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        template = 'https://seireigensouki.com/2ndwp/wp-content/themes/seirei2-teaser/images/chara-pic%s.png'
        self.download_by_template(folder, template, 2, 1)


# Sword Art Online Alternative: Gun Gale Online II
class GunGaleOnline2Download(Fall2024AnimeDownload):
    title = "Sword Art Online Alternative: Gun Gale Online II"
    keywords = [title, 'ggo', '2nd']
    website = 'https://gungale-online.net/'
    twitter = 'ggo_anime'
    hashtags = ['ggo_anime']
    folder_name = 'ggo2'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()

    def download_episode_preview(self):
        story_url = self.PAGE_PREFIX + 'story/'
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            stories = soup.select('.p-in_story__contents-nav-list-item')
            for story in stories:
                try:
                    a_tag = story.select('a[href]')[0]
                    episode = ''
                    for s in a_tag.text:
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
                images = ep_soup.select('.p-in-list-item img[src]')
                self.image_list = []
                for i in range(len(images)):
                    image_url = story_url + images[i]['src']
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url, to_jpg=True)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)


# Yarinaoshi Reijou wa Ryuutei Heika wo Kouryakuchuu
class YariryuDownload(Fall2024AnimeDownload):
    title = 'Yarinaoshi Reijou wa Ryuutei Heika wo Kouryakuchuu'
    keywords = [title, 'The Do-Over Damsel Conquers The Dragon Emperor', 'yariryu']
    website = 'https://yarinaoshi-reijyou.com/'
    twitter = 'yarinaoshi_pr'
    hashtags = ['やり竜']
    folder_name = 'yariryu'

    PAGE_PREFIX = website
    IMAGES_PER_EPISODE = 6
    FINAL_EPISODE = 12

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_external()
        self.download_news()
        self.download_key_visual()
        self.download_character()

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
                    if self.download_image(image_url, self.base_folder + '/' + image_name) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_external(self):
        keywords = ['やり直し令嬢は竜帝陛下を攻略中']
        AniverseMagazineScanner(keywords, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20240927', download_id=self.download_id).run()

    def download_news(self):
        try:
            results = []
            news_obj = self.get_last_news_log_object()
            json_obj = self.get_json(self.PAGE_PREFIX + 'news.json')
            for item in json_obj:
                if 'day' in item and 'url' in item and 'title' in item:
                    try:
                        date = datetime.strptime(item['day'], "%Y/%m/%d").strftime("%Y.%m.%d")
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

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.visual_wrap img[src*="/visual/"]')
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].split('?')[0]
                image_name = self.generate_image_name_from_url(image_url, 'visual')
                self.add_to_image_list(image_name, image_url)
        except Exception as e:
            self.print_exception(e, 'Key Visual')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'images/chara/p_01_%s.png'
        self.download_by_template(folder, template, 2, 1)
