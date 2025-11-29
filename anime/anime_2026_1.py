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
        pass

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

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        pass

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-archive-Item',
                                    date_select='.date', title_select='.title', id_select='a',
                                    next_page_select='.wp-pagenavi *', next_page_eval_index_class='current',
                                    next_page_eval_index=-1)


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
