from anime.main_download import MainDownload, NewsTemplate, NewsTemplate2, NewsTemplate4
from datetime import datetime, timedelta
from requests.exceptions import HTTPError
from scan import AniverseMagazineScanner
from bs4 import BeautifulSoup
import json
import os


# Spring 2025 Anime
class Spring2025AnimeDownload(MainDownload):
    season = "2025-2"
    season_name = "Spring 2025"
    folder_name = '2025-2'

    def __init__(self):
        super().__init__()


# Slime Taoshite 300-nen, Shiranai Uchi ni Level Max ni Nattemashita: Sono Ni
class Slime3002Download(Spring2025AnimeDownload, NewsTemplate):
    title = "Slime Taoshite 300-nen, Shiranai Uchi ni Level Max ni Nattemashita: Sono Ni"
    keywords = [title, "I've Been Killing Slimes for 300 Years and Maxed Out My Level", "Slime 300", "slime300", '2nd']
    website = 'https://slime300-anime.com/'
    twitter = 'slime300_PR'
    hashtags = 'スライム倒して300年'
    folder_name = 'slime300-2'

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
                                    date_select='.date', title_select='p:nth-child(2)', id_select='a')
