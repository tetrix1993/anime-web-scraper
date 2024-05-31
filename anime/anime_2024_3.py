from anime.main_download import MainDownload, NewsTemplate, NewsTemplate2
from datetime import datetime

# Koi wa Futago de Warikirenai https://futakire.com/ #ふたきれ @futakire
# Tokidoki Bosotto Russia-go de Dereru Tonari no Alya-san https://roshidere.com/ #ロシデレ @roshidere


# Summer 2024 Anime
class Summer2024AnimeDownload(MainDownload):
    season = "2024-3"
    season_name = "Summer 2024"
    folder_name = '2024-3'

    def __init__(self):
        super().__init__()


# Koi wa Futago de Warikirenai
class FutakireDownload(Summer2024AnimeDownload, NewsTemplate):
    title = 'Koi wa Futago de Warikirenai'
    keywords = [title, "Futakire"]
    website = 'https://futakire.com/'
    twitter = 'futakire'
    hashtags = ['ふたきれ', 'futakire']
    folder_name = 'futakire'

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
        try:
            results = []
            news_obj = self.get_last_news_log_object()
            json_obj = self.get_json(self.PAGE_PREFIX + 'news.json')
            for item in json_obj:
                if 'day' in item and 'url' in item and 'title' in item:
                    try:
                        date = datetime.strptime(item['day'], "%Y/%m/%d").strftime("%Y.%m.%d")
                    except:
                        continue
                    title = item['title']
                    url = self.PAGE_PREFIX + item['url']
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

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.visual_wrap img[src*="/visual/"]')
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].split('?')[0]
                image_name = self.generate_image_name_from_url(image_url, 'visual')
                self.add_to_image_list(image_name, image_url)
        except Exception as e:
            self.print_exception(e, 'Key Visual')
        self.download_image_list(folder)

        sub_folder = self.create_custom_directory(folder.split('/')[-1] + '/news')
        cache_filepath = sub_folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        try:
            json_obj = self.get_json(self.PAGE_PREFIX + 'news.json')
            for item in json_obj:
                date = item['day']
                if len(date) == 0:
                    break
                if not item['url'].startswith('news') or not item['url'].endswith('.html'):
                    continue
                page_name = item['url'].split('/')[-1].split('.html')[0]
                if page_name in processed:
                    break
                title = item['title'].strip()
                if 'ビジュアル' in title:
                    news_soup = self.get_soup(self.PAGE_PREFIX + item['url'])
                    if news_soup is not None:
                        images = news_soup.select('.news_container img[src*="/news/"]')
                        self.image_list = []
                        for image in images:
                            image_url = self.PAGE_PREFIX + image['src'].replace('../', '').split('?')[0]
                            image_name = self.generate_image_name_from_url(image_url, 'news')
                            self.add_to_image_list(image_name, image_url)
                        self.download_image_list(sub_folder)
                processed.append(page_name)
        except Exception as e:
            self.print_exception(e, 'Key Visual News')
        self.create_cache_file(cache_filepath, processed, num_processed)

    def download_character(self):
        folder = self.create_character_directory()
        prefix = self.PAGE_PREFIX + 'images/chara/p_%s.png'
        templates = [prefix % '%s_01', prefix % '%s_02_001', prefix % '%s_02_002', prefix % '%s_02_003']
        self.download_by_template(folder, templates, 3, 1)


# Tokidoki Bosotto Russia-go de Dereru Tonari no Alya-san
class RoshidereDownload(Summer2024AnimeDownload, NewsTemplate2):
    title = 'Tokidoki Bosotto Russia-go de Dereru Tonari no Alya-san'
    keywords = [title, 'Alya Sometimes Hides Her Feelings in Russian', 'Aalya', 'roshidere']
    website = 'https://roshidere.com/'
    twitter = 'roshidere'
    hashtags = ['ロシデレ', 'roshidere']
    folder_name = 'roshidere'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_news(self):
        self.download_template_news(self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.kv__img source[srcset]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['srcset'].split('?')[0]
                if '/images/' not in image_url or not image_url.endswith('.webp'):
                    continue
                image_name = self.generate_image_name_from_url(image_url, 'images')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'chara/index.html')
            pages = soup.select('#ContentsListUnit01 a[href]')
            for page in pages:
                if not page['href'].endswith('.html') or not page['href'].startswith('../'):
                    continue
                page_url = self.PAGE_PREFIX + page['href'].replace('../', '')
                page_name = page_url.split('/')[-1].split('.html')[0]
                if page_name in processed:
                    continue
                if page_name == 'index':
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(page_url)
                if ep_soup is None:
                    continue
                images = ep_soup.select('.charaMain__stand img[src]')
                self.image_list = []
                for image in images:
                    image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(folder)
                processed.append(page_name)
        except Exception as e:
            self.print_exception(e, 'Character')
        self.create_cache_file(cache_filepath, processed, num_processed)

        template = self.PAGE_PREFIX + 'core_sys/images/main/home/chara%s.png'
        self.download_by_template(folder, template, 2, 1, prefix='tz_')
