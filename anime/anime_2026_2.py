from anime.main_download import MainDownload, NewsTemplate, NewsTemplate2, NewsTemplate3, NewsTemplate4
from datetime import datetime, timedelta
from requests.exceptions import HTTPError
from scan import AniverseMagazineScanner
import os


# Spring 2026 Anime
class Spring2026AnimeDownload(MainDownload):
    season = "2026-2"
    season_name = "Spring 2026"
    folder_name = '2026-2'

    def __init__(self):
        super().__init__()


# Aishiteru Game wo Owarasetai
class AishiteruGameDownload(Spring2026AnimeDownload, NewsTemplate):
    title = 'Aishiteru Game wo Owarasetai'
    keywords = [title, 'I Want to End This Love Game']
    website = 'https://www.aishiteru-game.com/'
    twitter = 'aishiterugame'
    hashtags = '愛してるゲームを終わらせたい'
    folder_name = 'aishiterugame'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        pass

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='article.content-entry',
                                    title_select='.entry-title span', date_select='.entry-date span',
                                    id_select=None, id_has_id=True, news_prefix='news.html',
                                    a_tag_prefix=self.PAGE_PREFIX + 'news.html#')
