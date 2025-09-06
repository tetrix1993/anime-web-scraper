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
