from anime.main_download import MainDownload, NewsTemplate, NewsTemplate2, NewsTemplate4
from datetime import datetime, timedelta
from requests.exceptions import HTTPError
from scan import AniverseMagazineScanner
from bs4 import BeautifulSoup
import json
import os


# Summer 2025 Anime
class Summer2025AnimeDownload(MainDownload):
    season = "2025-3"
    season_name = "Summer 2025"
    folder_name = '2025-3'

    def __init__(self):
        super().__init__()


# Bad Girl
class BadGirlDownload(Summer2025AnimeDownload, NewsTemplate4):
    title = 'Bad Girl'
    keywords = [title]
    website = 'https://badgirl-anime.com/'
    twitter = 'badgirl_anime'
    hashtags = ['ばっどがーる', 'badgirl']
    folder_name = 'badgirl'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        json_obj = None
        try:
            json_obj = self.get_json(self.PAGE_PREFIX + 'api/site-data/init', verify=False)
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
        self.download_template_news(json_url=self.PAGE_PREFIX + 'api/site-data/init', verify=False)


# Futari Solo Camp
class FutariSoloCampDownload(Summer2025AnimeDownload, NewsTemplate2):
    title = 'Futari Solo Camp'
    keywords = [title, 'Solo Camping for Two']
    website = 'https://2solocamp-anime.com/'
    twitter = '2solocamp_anime'
    hashtags = 'ふたりソロキャンプ'
    folder_name = 'futarisolocamp'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX)


# GaCen Shoujo to Ibunka Kouryuu
class GaCenShoujoDownload(Summer2025AnimeDownload, NewsTemplate2):
    title = 'GaCen Shoujo to Ibunka Kouryuu'
    keywords = [title, 'Cultural Exchange With a Game Centre Girl']
    website = 'https://gacen-girl-anime.com/'
    twitter = 'GaCenGirl_Anime'
    hashtags = 'ゲーセン少女'
    folder_name = 'gacenshoujo'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX)


# Isekai Mokushiroku Mynoghra
class MynoghraDownload(Summer2025AnimeDownload, NewsTemplate):
    title = 'Isekai Mokushiroku Mynoghra'
    keywords = [title, 'Apocalypse Bringer Mynoghra']
    website = 'https://mynoghra-anime.com/'
    twitter = 'myap_GCofficial'
    hashtags = 'マイノグーラ'
    folder_name = 'mynoghra'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.bl_news__article_item',
                                    date_select='time ', title_select='h3', id_select='a', paging_type=3,
                                    paging_suffix='?page=%s', next_page_select='.next.page-numbers')


# Kaoru Hana wa Rin to Saku
class KaoruHanaDownload(Summer2025AnimeDownload, NewsTemplate):
    title = 'Kaoru Hana wa Rin to Saku'
    keywords = [title, 'The Fragrant Flower Blooms with Dignity', 'Kaoruhana']
    website = 'https://kaoruhana-anime.com/'
    twitter = 'kaoruhana_anime'
    hashtags = '薫る花'
    folder_name = 'kaoruhana'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news_list__item',
                                    date_select='.-date', title_select='.-title', id_select='a',
                                    a_tag_start_text_to_remove='./', a_tag_prefix=self.PAGE_PREFIX + 'news/')


# Kizetsu Yuusha to Ansatsu Hime
class KizetsuYushaDownload(Summer2025AnimeDownload, NewsTemplate):
    title = 'Kizetsu Yuusha to Ansatsu Hime'
    keywords = [title, 'The Stunned Hero and the Assassin Princesses']
    website = 'https://kizetsuyusha-anime.com//'
    twitter = 'kzt_toto'
    hashtags = '気絶勇者'
    folder_name = 'kizetsuyusha'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.p-news__item',
                                    date_select='.p-news__date', title_select='.p-news__description', id_select='a',
                                    date_func=lambda x: x[0:4] + '.' + x[5:7] + '.' + x[7:9])


# Koujo Denka no Kateikyoushi
class KoujoDenkaDownload(Summer2025AnimeDownload, NewsTemplate):
    title = 'Koujo Denka no Kateikyoushi'
    keywords = [title, "Private Tutor to the Duke's Daughter", 'Koujodenka']
    website = 'https://koujodenka-anime.com/'
    twitter = 'koujo_anime'
    hashtags = '公女殿下'
    folder_name = 'koujodenka'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.bg-newsItem',
                                    date_select='.text-newsDate', title_select='.text-base.line-clamp-3', id_select='a',
                                    a_tag_start_text_to_remove='/', a_tag_prefix=self.PAGE_PREFIX, paging_type=2,
                                    next_page_select='.h-full.shadow-pagerShadow', next_page_eval_index=-1,
                                    next_page_eval_index_class='pointer-events-none')


# Mattaku Saikin no Tantei to Kitara
class MattanDownload(Summer2025AnimeDownload, NewsTemplate2):
    title = 'Mattaku Saikin no Tantei to Kitara'
    keywords = [title, 'Detectives These Days Are Crazy!']
    website = 'https://mattan-anime.com/'
    twitter = 'mattan_anime'
    hashtags = 'まっ探'
    folder_name = 'mattan'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX)


# Silent Witch: Chinmoku no Majo no Kakushigoto
class SilentWitchDownload(Summer2025AnimeDownload, NewsTemplate):
    title = 'Silent Witch: Chinmoku no Majo no Kakushigoto'
    keywords = [title, 'Secrets of the Silent Witch']
    website = 'https://silentwitch.net/'
    twitter = 'SilentWitch_pr'
    hashtags = 'サイレントウィッチ'
    folder_name = 'silentwitch'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.l-news__list-item',
                                    date_select='.l-news__list-item-date', title_select='.l-news__list-item-title',
                                    id_select='a', a_tag_prefix=self.PAGE_PREFIX + 'news/')


# Tsuyokute New Saga
class TsuyosagaDownload(Summer2025AnimeDownload, NewsTemplate4):
    title = 'Tsuyokute New Saga'
    keywords = [title, 'New Saga', 'Tsuyosaga']
    website = 'https://tsuyosaga-pr.com/'
    twitter = 'tsuyosaga_pr'
    hashtags = 'つよサガ'
    folder_name = 'tsuyosaga'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        # self.download_key_visual()
        # self.download_character()

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

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_aniverse', 'https://aniverse-mag.com/wp-content/uploads/2022/10/1628619ceb9f5f0127d70926036c5ffd.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'wp/wp-content/themes/newsaga/static/character/%s/main.png'
        for i in range(10):
            number = str(i + 1).zfill(2)
            image_name = 'tz_char' + number
            if self.is_image_exists(image_name, folder):
                continue
            image_url = template % number
            result = self.download_image(image_url, folder + '/' + image_name)
            if result == -1:
                break
