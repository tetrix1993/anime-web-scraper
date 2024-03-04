from anime.main_download import MainDownload, NewsTemplate, NewsTemplate2
from datetime import datetime

# Kami wa Game ni Ueteiru. https://godsgame-anime.com/ #神飢え #神飢えアニメ #kamiue @kami_to_game
# Kono Sekai wa Fukanzen Sugiru https://konofuka.com/ #このふか @konofuka_QA
# Sasayaku You ni Koi wo Utau https://sasakoi-anime.com/ #ささこい @sasakoi_anime
# Tensei shitara Dainana Ouji Datta node, Kimama ni Majutsu wo Kiwamemasu https://dainanaoji.com/ #第七王子 @dainanaoji_pro
# Unnamed Memory https://unnamedmemory.com/ #UnnamedMemory #アンメモ @Project_UM
# Yozakura-san Chi no Daisakusen https://mission-yozakura-family.com/ #夜桜さんちの大作戦 #MissionYozakuraFamily @OfficialHitsuji


# Spring 2024 Anime
class Spring2024AnimeDownload(MainDownload):
    season = "2024-2"
    season_name = "Spring 2024"
    folder_name = '2024-2'

    def __init__(self):
        super().__init__()


# Kami wa Game ni Ueteiru.
class KamiueDownload(Spring2024AnimeDownload, NewsTemplate):
    title = 'Kami wa Game ni Ueteiru.'
    keywords = [title, "Gods' Game We Play"]
    website = 'https://godsgame-anime.com/'
    twitter = 'kami_to_game'
    hashtags = ['神飢え', '神飢えアニメ', 'kamiue']
    folder_name = 'kamiue'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()
        self.download_media()

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
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.visual_wrap .img_100 img[src*="/visual/"]')
            self.image_list = []
            for image in images:
                image_name = self.extract_image_name_from_url(image['src'])
                image_url = self.PAGE_PREFIX + image['src']
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        prefix = self.PAGE_PREFIX + 'images/chara/'
        template = prefix + 'c_%s.png'
        self.download_by_template(folder, template, 3, 1)
        templates = [prefix + 'a%s_left.png', prefix + 'a%s_center.png', prefix + 'a%s_right.png']
        self.download_by_template(folder, templates, 2, 1)

    def download_media(self):
        folder = self.create_media_directory()
        special_folder = self.create_custom_directory(folder.split('/')[-1] + '/special')
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'special.html?cat=visual')
            images = soup.select('article.visual a[href^="images/"]')
            for image in images:
                image_url = self.PAGE_PREFIX + image['href']
                image_name = self.generate_image_name_from_url(image_url, 'images')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(special_folder)
        except Exception as e:
            self.print_exception(e, 'Special')


# Kono Sekai wa Fukanzen Sugiru
class KonofukaDownload(Spring2024AnimeDownload, NewsTemplate):
    title = 'Kono Sekai wa Fukanzen Sugiru'
    keywords = [title, "Quality Assurance in Another World"]
    website = 'https://konofuka.com/'
    twitter = 'konofuka_QA'
    hashtags = ['このふか', 'konofuka']
    folder_name = 'konofuka'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.top-news a',
                                    title_select='.news-ttl', date_select='.news-date', id_select=None,
                                    next_page_select='ul.page-numbers li span', next_page_eval_index=-1,
                                    next_page_eval_index_class='current',
                                    date_func=lambda x: x.replace('(', '').replace(')', ''))

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz', self.PAGE_PREFIX + 'pDK2yjkH/wp-content/themes/konofuka_v0.1/assets/img/top/mv.png')
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/Fr85Cb4aAAAgWlS?format=jpg&name=4096x4096')
        self.download_image_list(folder)


# Sasayaku You ni Koi wo Utau
class SasakoiDownload(Spring2024AnimeDownload, NewsTemplate):
    title = 'Sasayaku You ni Koi wo Utau'
    keywords = [title, "Whisper Me a Love Song"]
    website = 'https://sasakoi-anime.com/'
    twitter = 'sasakoi_anime'
    hashtags = ['ささこい', 'sasakoi']
    folder_name = 'sasakoi'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news__list tr', news_prefix='',
                                    date_select='.day', title_select='.title', id_select='a', date_separator='/',
                                    a_tag_prefix=self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_kv', self.PAGE_PREFIX + 'core_sys/images/main/tz/kv.webp')
        self.add_to_image_list('tz_teaser', self.PAGE_PREFIX + 'core_sys/images/main/tz/teaser.jpg')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.kv__img source[srcset]')
            self.image_list = []
            for image in images:
                if '/main/' not in image['srcset']:
                    continue
                image_name = self.extract_image_name_from_url(image['srcset'])
                if 'kv' not in image_name:
                    continue
                image_name = self.generate_image_name_from_url(image['srcset'], 'main')
                image_url = self.PAGE_PREFIX + image['srcset']
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'core_sys/images/main/tz/chara/c%s_face.jpg'
        self.download_by_template(folder, template, 2, 1, prefix='tz_')


# Tensei shitara Dainana Ouji Datta node, Kimama ni Majutsu wo Kiwamemasu
class DainanaojiDownload(Spring2024AnimeDownload, NewsTemplate):
    title = 'Tensei shitara Dainana Ouji Datta node, Kimama ni Majutsu wo Kiwamemasu'
    keywords = [title, 'I Was Reincarnated as the 7th Prince so I Can Take My Time Perfecting My Magical Ability']
    website = 'https://dainanaoji.com/'
    twitter = 'dainanaoji_pro'
    hashtags = '第七王子'
    folder_name = 'dainanaoji'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        # self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='#news-container article',
                                    date_select='.news-box-date', title_select='.news-txt-box', id_select='a',
                                    next_page_select='.pagination .page-numbers',
                                    next_page_eval_index_class='current', next_page_eval_index=-1)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/Fgo-UydUAAAq3qH?format=jpg&name=medium')
        self.add_to_image_list('tz_visual_img', self.PAGE_PREFIX + 'd81Ft6ye/wp-content/themes/v0/assets/img/top/visual/img.webp')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        # template = self.PAGE_PREFIX + 'd81Ft6ye/wp-content/themes/v0/assets/img/character/%s.webp'
        # self.download_by_template(folder, template, 1, 0, prefix='tz_')
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('.character-img-box>img[src]')
            for image in images:
                if '/img/' not in image['src']:
                    continue
                image_url = image['src']
                image_name = self.generate_image_name_from_url(image_url, 'img')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Unnamed Memory
class UnnamedMemoryDownload(Spring2024AnimeDownload, NewsTemplate):
    title = 'Unnamed Memory'
    keywords = [title]
    website = 'https://unnamedmemory.com/'
    twitter = 'Project_UM'
    hashtags = ['UnnamedMemory', 'アンメモ']
    folder_name = 'unnamedmemory'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.content-entry',
                                    title_select='.entry-title span', date_select='.entry-date span',
                                    id_select=None, id_has_id=True, news_prefix='news.html')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/Fj2aPSZVIAEC9LY?format=jpg&name=4096x4096')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.vis source[srcset], .vis img[src]')
            self.image_list = []
            for image in images:
                if image.has_attr('srcset'):
                    image_url = image['srcset']
                else:
                    image_url = image['src']
                if image_url.startswith('./'):
                    image_url = self.PAGE_PREFIX + image_url[2:]
                if '/assets/' not in image_url:
                    continue
                image_name = self.generate_image_name_from_url(image_url, 'assets')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

        sub_folder = self.create_custom_directory(folder.split('/')[-1] + '/news')
        cache_filepath = sub_folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        temp_processed = set()  # Some of the id is not unique
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'news.html')
            items = soup.select('article article')
            for item in items:
                page_name = item['id']
                if page_name in processed:
                    break
                title = item.select('.entry-title span')[0].text.strip()
                if 'ビジュアル' in title or 'イラスト' in title:
                    images = item.select('img[data-src]')
                    self.image_list = []
                    for image in images:
                        image_url = self.PAGE_PREFIX + image['data-src'].replace('./', '').split('?')[0]
                        if '/news/' not in image_url:
                            continue
                        image_name = self.generate_image_name_from_url(image_url, 'news')
                        self.add_to_image_list(image_name, image_url)
                    self.download_image_list(sub_folder)
                temp_processed.add(page_name)
        except Exception as e:
            self.print_exception(e, 'Key Visual News')
        for page_name in temp_processed:
            processed.append(page_name)
        self.create_cache_file(cache_filepath, processed, num_processed)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'assets/character/%s.webp'
        self.download_by_template(folder, template, 1, 1)


# Yozakura-san Chi no Daisakusen
class YozakurasanDownload(Spring2024AnimeDownload, NewsTemplate2):
    title = 'Yozakura-san Chi no Daisakusen'
    keywords = [title, 'Mission: Yozakura Family']
    website = 'https://mission-yozakura-family.com/'
    twitter = 'OfficialHitsuji'
    hashtags = ['夜桜さんちの大作戦', 'MissionYozakuraFamily']
    folder_name = 'yozakurasan'

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
        self.download_template_news(self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FkJB8aSVEAA5Xd1?format=jpg&name=medium')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.kv__img img[src]')
            self.image_list = []
            for image in images:
                if '/images/' in image['src']:
                    image_url = self.PAGE_PREFIX + image['src']
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
            soup = self.get_soup(self.PAGE_PREFIX + 'character/taiyo.html')
            pages = soup.select('#ContentsListUnit01 a[href]')
            for page in pages:
                if not page['href'].endswith('.html') or not page['href'].startswith('../'):
                    continue
                page_url = self.PAGE_PREFIX + page['href'].replace('../', '')
                page_name = page_url.split('/')[-1].split('.html')[0]
                if page_name in processed:
                    continue
                if page_name == 'taiyo':
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(page_url)
                if ep_soup is None:
                    continue
                images = ep_soup.select('.charaVisual__img source[srcset]')
                self.image_list = []
                for image in images:
                    image_url = self.PAGE_PREFIX + image['srcset'].replace('../', '')
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(folder)
                processed.append(page_name)
        except Exception as e:
            self.print_exception(e, 'Character')
        self.create_cache_file(cache_filepath, processed, num_processed)
