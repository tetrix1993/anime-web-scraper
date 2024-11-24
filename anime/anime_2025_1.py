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

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.info__item',
                                    title_select='.info__title', date_select='.info__date', id_select='a',
                                    news_prefix='information/')


# Akuyaku Reijou Tensei Ojisan
class TenseiOjisanDownload(Winter2025AnimeDownload, NewsTemplate4):
    title = 'Akuyaku Reijou Tensei Ojisan'
    keywords = [title, "From Bureaucrat to Villainess: Dad's Been Reincarnated!", 'tenseiojisan']
    website = 'https://tensei-ojisan.com/'
    twitter = 'tensei_ojisan'
    hashtags = ['転生おじさん']
    folder_name = 'tenseiojisan'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self, json_obj=None):
        self.download_template_news(json_url=self.PAGE_PREFIX + 'api/site-data/init')


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
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.p-news__list-item',
                                    title_select='.p-news_data__ttl', date_select='.p-news_data__date',
                                    id_select='a', a_tag_prefix=self.PAGE_PREFIX + 'news/', paging_type=1,
                                    next_page_select='.c-pagination__list-item',
                                    next_page_eval_index_class='is-current', next_page_eval_index=-1)


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
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.p-news__list-item',
                                    title_select='.p-news__list-text', date_select='.p-news__list-date',
                                    id_select='a', a_tag_start_text_to_remove='./',
                                    a_tag_prefix=self.PAGE_PREFIX + 'news/', paging_type=1,
                                    next_page_select='.c-pagination__list-item',
                                    next_page_eval_index_class='is-current', next_page_eval_index=-1)


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
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.p-news__list-item',
                                    title_select='.p-news_article__title', date_select='.p-news_article__date',
                                    id_select='a', a_tag_start_text_to_remove='/', a_tag_prefix=self.PAGE_PREFIX,
                                    paging_type=1, next_page_select='.c-pagination__list-item',
                                    next_page_eval_index_class='is-current', next_page_eval_index=-1,
                                    date_func=lambda x: x[0:4] + '.' + x[4:])


# Hazure Skill "Kinomi Master": Skill no Mi (Tabetara Shinu) wo Mugen ni Taberareru You ni Natta Ken ni Tsuite
class KinomiMasterDownload(Winter2025AnimeDownload, NewsTemplate4):
    title = 'Hazure Skill "Kinomi Master": Skill no Mi (Tabetara Shinu) wo Mugen ni Taberareru You ni Natta Ken ni Tsuite'
    keywords = [title, 'kinomimaster']
    website = 'https://kinomimaster.com/'
    twitter = 'kinomimaster_PR'
    hashtags = ['木の実マスター']
    folder_name = 'kinomimaster'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self, json_obj=None):
        self.download_template_news(json_url=self.PAGE_PREFIX + 'api/site-data/init')


# Kisaki Kyouiku kara Nigetai Watashi
class KisakiKyouikuDownload(Winter2025AnimeDownload, NewsTemplate):
    title = 'Kisaki Kyouiku kara Nigetai Watashi'
    keywords = [title, "I Want to Escape from Princess Lessons", 'kisakikyouiku']
    website = 'https://kisakikyouiku.com/'
    twitter = 'kisakikyouiku'
    hashtags = ['妃教育']
    folder_name = 'kisakikyouiku'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='article', title_select='.entry-title',
                                    date_select='.entry-date', id_select=None, id_has_id=True, news_prefix='news.html',
                                    a_tag_prefix=self.PAGE_PREFIX + 'news.html#')


# Kuroiwa Medaka ni Watashi no Kawaii ga Tsuujinai
class MedakawaDownload(Winter2025AnimeDownload, NewsTemplate):
    title = 'Kuroiwa Medaka ni Watashi no Kawaii ga Tsuujinai'
    keywords = [title, "Medaka Kuroiwa Is Impervious to My Charms", 'medakawa']
    website = 'https://monaxmedaka.com/'
    twitter = 'monaxmedaka'
    hashtags = ['メダかわ']
    folder_name = 'medakawa'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.newsList',
                                    title_select='.newsList__title_txt>span', date_select='.newsList__date',
                                    id_select='a')


# NEET Kunoichi to Nazeka Dousei Hajimemashita
class NeetKunoichiDownload(Winter2025AnimeDownload, NewsTemplate):
    title = 'NEET Kunoichi to Nazeka Dousei Hajimemashita'
    keywords = [title, "I'm Living with an Otaku NEET Kunoichi!?"]
    website = 'https://neet-kunoichi.com/'
    twitter = 'neet_kunoichi'
    hashtags = ['ニートくノ一 ']
    folder_name = 'neetkunoichi'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

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
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-item', title_select='.title',
                                    date_select='.date', id_select='a')


# S-Rank Monster no "Behemoth" dakedo, Neko to Machigawarete Elf Musume no Pet toshite Kurashitemasu
class BehenekoDownload(Winter2025AnimeDownload, NewsTemplate2):
    title = 'S-Rank Monster no "Behemoth" dakedo, Neko to Machigawarete Elf Musume no Pet toshite Kurashitemasua'
    keywords = [title, "Beheneko: The Elf-Girl's Cat is Secretly an S-Ranked Monster!"]
    website = 'https://behemoth-anime.com/'
    twitter = 'beheneko_anime'
    hashtags = ['べヒ猫', 'beheneko']
    folder_name = 'beheneko'

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
