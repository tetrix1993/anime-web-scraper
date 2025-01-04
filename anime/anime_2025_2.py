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


# Danjo no Yuujou wa Seiritsu suru? (Iya, Shinai!!)
class DanjoruDownload(Spring2025AnimeDownload, NewsTemplate):
    title = 'Danjo no Yuujou wa Seiritsu suru? (Iya, Shinai!!)'
    keywords = [title, 'danjoru']
    website = 'https://www.danjoru.com/'
    twitter = 'danjoru_'
    hashtags = 'だんじょる'
    folder_name = 'danjoru'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news_item', date_select='.year',
                                    title_select='.ttl', id_select='a')


# Haite Kudasai, Takamine-san
class TakaminesanDownload(Spring2025AnimeDownload, NewsTemplate2):
    title = 'Haite Kudasai, Takamine-san'
    keywords = [title, 'Please Put Them On, Takamine-san']
    website = 'https://takaminesan.com/'
    twitter = 'takamine_anime'
    hashtags = '鷹峰さん'
    folder_name = 'takaminesan'

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


# Isshun de Chiryou shiteita noni Yakutatazu to Tsuihou sareta Tensai Chiyushi, Yami Healer toshite Tanoshiku Ikiru
class YamiHealerDownload(Spring2025AnimeDownload, NewsTemplate):
    title = 'Isshun de Chiryou shiteita noni Yakutatazu to Tsuihou sareta Tensai Chiyushi, Yami Healer toshite Tanoshiku Ikiru'
    keywords = [title, "The Brilliant Healer's New Life in the Shadows", 'yamihealer']
    website = 'https://sh-anime.shochiku.co.jp/yamihealer/'
    twitter = 'yamihealer'
    hashtags = '闇ヒーラー'
    folder_name = 'yamihealer'

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
                                    date_select='.p-news__item__date', title_select='.p-news__item__ttl',
                                    id_select=None, next_page_select='.c-pager__number', next_page_eval_index=-1,
                                    next_page_eval_index_class='is-active')


# Katainaka no Ossan, Kensei ni Naru
class OssanKenseiDownload(Spring2025AnimeDownload, NewsTemplate2):
    title = 'Katainaka no Ossan, Kensei ni Naru'
    keywords = [title, 'From Old Country Bumpkin to Master Swordsman']
    website = 'https://ossan-kensei.com/'
    twitter = 'ossan_kensei'
    hashtags = 'おっさん剣聖'
    folder_name = 'ossankensei'

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


# Shiunji-ke no Kodomotachi
class ShinunjiDownload(Spring2025AnimeDownload):
    title = 'Shiunji-ke no Kodomotachi'
    keywords = [title, 'The Shiunji Family Children']
    website = 'https://shiunjifamily.com/'
    twitter = 'shiunji_anime'
    hashtags = ['紫雲寺家の子供たち', 'shiunjifamily']
    folder_name = 'shiunji'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

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
