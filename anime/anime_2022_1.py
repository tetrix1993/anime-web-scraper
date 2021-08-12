import os
import anime.constants as constants
from anime.main_download import MainDownload, NewsTemplate, NewsTemplate2, NewsTemplate3
from datetime import datetime
from scan import AniverseMagazineScanner, MocaNewsScanner, WebNewtypeScanner


# Arifureta Shokugyou de Sekai Saikyou 2nd Season https://arifureta.com/ #ありふれた #ARIFURETA @ARIFURETA_info
# Leadale no Daichi nite https://leadale.net/ #leadale #リアデイル @leadale_anime
# Slow Loop https://slowlooptv.com/ #slowloop @slowloop_tv
# Tensai Ouji no Akaji Kokka Saisei Jutsu: Souda, Baikoku shiyou https://tensaiouji-anime.com/ #天才王子 #天才王子の赤字国家再生術 @tensaiouji_PR


# Winter 2022 Anime
class Winter2022AnimeDownload(MainDownload):
    season = "2022-1"
    season_name = "Winter 2022"
    folder_name = '2022-1'

    def __init__(self):
        super().__init__()


# Arifureta Shokugyou de Sekai Saikyou 2nd Season
class Arifureta2Download(Winter2022AnimeDownload):
    title = "Arifureta Shokugyou de Sekai Saikyou 2nd Season"
    keywords = [title, "Arifureta: From Commonplace to World's Strongest 2nd Season"]
    website = 'https://arifureta.com/'
    twitter = 'ARIFURETA_info'
    hashtags = ['ARIFURETA', 'ありふれた']
    folder_name = 'arifureta2'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, diff=67)

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news/'
        stop = False
        try:
            results = []
            news_obj = self.get_last_news_log_object()
            for page in range(1, 100, 1):
                page_url = news_url
                if page > 1:
                    page_url = news_url + 'page/' + str(page) + '/'
                soup = self.get_soup(page_url, decode=True)
                articles = soup.select('ul.news_list li')
                for article in articles:
                    tag_date = article.find('h5', class_='date')
                    tag_title = article.find('h1')
                    a_tag = article.find('a')
                    if tag_date and tag_title and a_tag and a_tag.has_attr('href'):
                        article_id = a_tag['href']
                        date = self.format_news_date(tag_date.text.strip())
                        if len(date) == 0:
                            continue
                        title = tag_title.text.strip()
                        if date.startswith('2021.03') or \
                                news_obj and (news_obj['id'] == article_id or date < news_obj['date']):
                            stop = True
                            break
                        results.append(self.create_news_log_object(date, title, article_id))
                if stop:
                    break
                pagination = soup.select('ul.pagenation-list li')
                if len(pagination) == 0:
                    break
                if pagination[-1].has_attr('class') and 'is__current' in pagination[-1]['class']:
                    break
            success_count = 0
            for result in reversed(results):
                process_result = self.create_news_log_from_news_log_object(result)
                if process_result == 0:
                    success_count += 1
            if len(results) > 0:
                self.create_news_log_cache(success_count, results[0])
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - News')
            print(e)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('mainvisual08', self.PAGE_PREFIX + 'wp-content/themes/arifureta-v3.2/library/img/main_visual/mainvisual08.png')
        self.add_to_image_list('kv1', self.PAGE_PREFIX + 'wp-content/uploads/2021/04/02.jpg')
        self.add_to_image_list('kv1_art', self.PAGE_PREFIX + 'wp-content/uploads/2021/04/03.jpg')
        self.download_image_list(folder)


# Leadale no Daichi nite
class LeadaleDownload(Winter2022AnimeDownload, NewsTemplate3):
    title = 'Leadale no Daichi nite'
    keywords = [title, 'World of Leadale']
    website = 'https://leadale.net/'
    twitter = 'leadale_anime'
    hashtags = ['leadale', 'リアデイル']
    folder_name = 'leadale'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_character()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_news(self):
        self.download_template_news(self.PAGE_PREFIX)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'assets/character/c/%s.png'
        self.download_by_template(folder, template, 1, 1, prefix='c', save_zfill=2)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('kv1', self.PAGE_PREFIX + 'assets/top/main-t1/vis.jpg')
        self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/Ezi8NqIVkAMv0Yv?format=jpg&name=medium')
        self.add_to_image_list('kv2_tw', 'https://pbs.twimg.com/media/E8Ouua3UUAIFSvH?format=jpg&name=medium')
        self.download_image_list(folder)

        template = self.PAGE_PREFIX + 'assets/news/kv-t%s.jpg'
        template2 = self.PAGE_PREFIX + 'assets/special/vis/%s.jpg'
        self.download_by_template(folder, template, 1, 1)
        self.download_by_template(folder, template2, 1, 1, prefix='kv_s')


# Slow Loop
class SlowLoopDownload(Winter2022AnimeDownload):
    title = 'Slow Loop'
    keywords = [title]
    website = 'https://slowlooptv.com/'
    twitter = 'slowloop_tv'
    hashtags = 'slowloop'
    folder_name = 'slow-loop'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news.html'
        try:
            soup = self.get_soup(news_url, decode=True)
            articles = soup.select('article')
            news_obj = self.get_last_news_log_object()
            results = []
            for article in articles:
                tag_title = article.find('div', class_='news_list_title')
                tag_date = article.find('div', class_='news_list_day')
                a_tag = article.find('a')
                if tag_title and tag_date and a_tag and a_tag.has_attr('href'):
                    article_id = self.PAGE_PREFIX + a_tag['href']
                    title = self.format_news_title(tag_title.text)
                    date = self.format_news_date(tag_date.text.strip().replace('/', '.'))
                    if len(date) == 0:
                        continue
                    if news_obj and (news_obj['id'] == article_id or date < news_obj['date']):
                        break
                    results.append(self.create_news_log_object(date, title, article_id))
            success_count = 0
            for result in reversed(results):
                process_result = self.create_news_log_from_news_log_object(result)
                if process_result == 0:
                    success_count += 1
            if len(results) > 0:
                self.create_news_log_cache(success_count, results[0])
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - News')
            print(e)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('announce', 'https://pbs.twimg.com/media/Ep5-SoLUUAAHq36?format=jpg&name=4096x4096')
        self.add_to_image_list('announce_2', self.PAGE_PREFIX + 'images/top/v_001.jpg')
        self.add_to_image_list('teaser', self.PAGE_PREFIX + 'images/top/v_002_02.jpg')
        self.add_to_image_list('teaser_tw', 'https://pbs.twimg.com/media/E15YSghVgAIdgJf?format=jpg&name=medium')
        self.download_image_list(folder)


# Tensai Ouji no Akaji Kokka Saisei Jutsu: Souda, Baikoku shiyou
class TensaiOujiDownload(Winter2022AnimeDownload, NewsTemplate2):
    title = 'Tensai Ouji no Akaji Kokka Saisei Jutsu: Souda, Baikoku shiyou'
    keywords = [title, 'tensaiouji']
    website = 'https://tensaiouji-anime.com/'
    twitter = 'tensaiouji_PR'
    hashtags = ['天才王子', '天才王子の赤字国家再生術']
    folder_name = 'tensaiouji'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(self.PAGE_PREFIX, 'news/list00010000.html')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('kv', self.PAGE_PREFIX + 'core_sys/images/main/home/kv.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'core_sys/images/main/cont/char/c%s_%s.png'
        templates = [template % ('%s', '01'), template % ('%s', '02')]
        self.download_by_template(folder, templates, 2, 1)
