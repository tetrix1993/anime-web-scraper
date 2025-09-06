from anime.main_download import MainDownload, NewsTemplate, NewsTemplate2, NewsTemplate3, NewsTemplate4
from datetime import datetime, timedelta
from requests.exceptions import HTTPError
from scan import AniverseMagazineScanner
from bs4 import BeautifulSoup
import json
import os


# Fall 2025 Anime
class Fall2025AnimeDownload(MainDownload):
    season = "2025-4"
    season_name = "Fall 2025"
    folder_name = '2025-4'

    def __init__(self):
        super().__init__()


# Ansatsusha de Aru Ore no Status ga Yuusha yori mo Akiraka ni Tsuyoi no da ga
class SutetsuyoDownload(Fall2025AnimeDownload, NewsTemplate):
    title = "Ansatsusha de Aru Ore no Status ga Yuusha yori mo Akiraka ni Tsuyoi no da ga"
    keywords = [title, 'sutetsuyo', 'My Status as an Assassin Obviously Exceeds the Hero\'s']
    website = 'https://sutetsuyo-anime.com/'
    twitter = 'sutetsuyo_an'
    hashtags = ['ステつよ', 'sutetsuyo']
    folder_name = 'sutetsuyo'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='article', date_select='time',
                                    title_select='h2', id_select='a', a_tag_prefix=self.PAGE_PREFIX + 'news/')


# Bukiyou na Senpai.
class BukiyouDownload(Fall2025AnimeDownload, NewsTemplate):
    title = "Bukiyou na Senpai."
    keywords = [title, 'My Awkward Senpai']
    website = 'https://bukiyouna-senpai.asmik-ace.co.jp/'
    twitter = 'bukiyou_anime'
    hashtags = '不器用な先輩'
    folder_name = 'bukiyou'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.newsList',
                                    date_select='time', title_select='.newsList__title', id_select='a',
                                    next_page_select='.wp-pagenavi *', next_page_eval_index_class='current',
                                    next_page_eval_index=-1, date_func=lambda x: x[0:4] + '.' + x[5:])


# Tomodachi no Imouto ga Ore ni dake Uzai
class ImouzaDownload(Fall2025AnimeDownload, NewsTemplate):
    title = "Tomodachi no Imouto ga Ore ni dake Uzai"
    keywords = [title, 'imouza', 'My Friend\'s Little Sister Has It In for Me!']
    website = 'https://www.imouza-animation.com/'
    twitter = 'imouza_PR'
    hashtags = 'いもウザ'
    folder_name = 'imouza'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.sw-News_Item',
                                    date_select='.sw-News_Date', title_select='.sw-News_Txt', id_select='a',
                                    next_page_select='.nextpostslink')
