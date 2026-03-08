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


# Class de 2-banme ni Kawaii Onnanoko to Tomodachi ni Natta
class KuranikaDownload(Spring2026AnimeDownload, NewsTemplate):
    title = 'Class de 2-banme ni Kawaii Onnanoko to Tomodachi ni Natta'
    keywords = [title, 'I Made Friends with the Second Prettiest Girl in My Class', 'kuranika']
    website = 'https://kuranika.asmik-ace.co.jp/'
    twitter = 'kuranika'
    hashtags = 'クラにか'
    folder_name = 'kuranika'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        pass

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.bl_posts_item', date_select='time',
                                    title_select='.bl_posts_txt', id_select='a', next_page_select='a.next.page-numbers',
                                    paging_type=3, paging_suffix='?page=%s', date_separator='/')


# Haibara-kun no Tsuyokute Seishun New Game
class HaibarakunDownload(Spring2026AnimeDownload, NewsTemplate):
    title = 'Haibara-kun no Tsuyokute Seishun New Game'
    keywords = [title, "Haibara's Teenage New Game+"]
    website = 'https://haibarakun-anime.com/'
    twitter = 'haibara_anime'
    hashtags = '灰原くんの強くて青春ニューゲーム'
    folder_name = 'haibarakun'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        pass

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.md-li__topics li',
                                    date_select='time', title_select='.info--postttl', id_select='a',
                                    news_prefix='topics/', date_separator='-')


# Kuroneko to Majo no Kyoushitsu
class NekomajoDownload(Spring2026AnimeDownload, NewsTemplate):
    title = 'Kuroneko to Majo no Kyoushitsu'
    keywords = [title, "The Classroom of a Black Cat and a Witch"]
    website = 'https://witch-classroom.com/'
    twitter = 'witch_classroom'
    hashtags = ['猫魔女', '黒猫と魔女の教室']
    folder_name = 'nekomajo'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        pass

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.entry-title',
                                    date_select='.news__date', title_select='.news__text', id_select='a',
                                    next_page_select='.pagination .next')


# Replica datte, Koi wo Suru.
class ReplicoDownload(Spring2026AnimeDownload):
    title = 'Replica datte, Koi wo Suru.'
    keywords = [title, "Even a Replica Can Fall in Love", 'replico']
    website = 'https://replico.jp/'
    twitter = 'REPLICO_dengeki'
    hashtags = 'レプリコ'
    folder_name = 'replico'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        pass

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


# Yowayowa Sensei
class YowayowaSenseiDownload(Spring2026AnimeDownload, NewsTemplate):
    title = 'Yowayowa Sensei'
    keywords = [title, "Yowayowa Teacher"]
    website = 'https://www.yowayowasensei-anime.com/'
    twitter = 'yowayowa_anime'
    hashtags = ['よわよわ先生']
    folder_name = 'yowayowasensei'

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
