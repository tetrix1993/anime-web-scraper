from anime.main_download import MainDownload, NewsTemplate, NewsTemplate2, NewsTemplate4
from datetime import datetime
from requests.exceptions import HTTPError

# 2.5-jigen no Ririsa https://ririsa-official.com/ @ririsa_official #にごリリ #nigoriri
# Atri: My Dear Moments https://atri-anime.com/ #ATRI @ATRI_anime
# Giji Harem https://gijiharem.com/ #疑似ハーレム @GijiHarem
# Gimai Seikatsu https://gimaiseikatsu-anime.com/ #義妹生活 @gimaiseikatsu
# Isekai Shikkaku https://isekaishikkaku.com/ #異世界失格 #isekaishikkaku @isekaishikkaku
# Kimi to Boku no Saigo no Senjou, Aruiwa Sekai ga Hajimaru Seisen Season II https://kimisentv.com/ #キミ戦 #kimisen #OurLastCrusade
# Koi wa Futago de Warikirenai https://futakire.com/ #ふたきれ @futakire
# Kono Sekai wa Fukanzen Sugiru https://konofuka.com/ #このふか @konofuka_QA
# Megami no Café Terrace Season 2 https://1st.goddess-cafe.com/ #女神のカフェテラス @goddess_cafe_PR
# Naze Boku no Sekai wo Daremo Oboeteinai no ka? https://www.nazeboku.com/ #なぜ僕 #nazeboku @nazeboku_pr
# Oshi no Ko Season 2 https://ichigoproduction.com/Season2/ #推しの子 @anime_oshinoko
# Senpai wa Otokonoko https://senpaiha-otokonoko.com/ #ぱいのこアニメ #先輩はおとこのこ @painoko_anime
# Shikanoko Nokonoko Koshitantan https://www.anime-shikanoko.jp/ #しかのこ @shikanoko_PR
# Shoushimin Series https://shoshimin-anime.com/ #小市民 @shoshimin_pr
# Tokidoki Bosotto Russia-go de Dereru Tonari no Alya-san https://roshidere.com/ #ロシデレ @roshidere


# Summer 2024 Anime
class Summer2024AnimeDownload(MainDownload):
    season = "2024-3"
    season_name = "Summer 2024"
    folder_name = '2024-3'

    def __init__(self):
        super().__init__()


# 2.5-jigen no Ririsa
class NigoririDownload(Summer2024AnimeDownload, NewsTemplate):
    title = '2.5-jigen no Ririsa'
    keywords = [title, '2.5 Dimensional Seduction']
    website = 'https://ririsa-official.com/'
    twitter = 'ririsa_official'
    hashtags = ['にごリリ', 'nigoriri']
    folder_name = 'nigoriri'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='article',
                                    title_select='.ttl', date_select='.date', id_select='a',
                                    next_page_select='.item-next__link')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('.fvslide source[srcset*="_pc"][srcset*="/webp/"]')
            for image in images:
                image_url = self.PAGE_PREFIX + image['srcset'][1:].split('?')[0]
                image_name = self.generate_image_name_from_url(image_url, 'webp')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            self.image_list = []
            images = soup.select('.visual source[srcset*="_pc"][srcset*="/webp/"]')
            for image in images:
                image_url = self.PAGE_PREFIX + image['srcset'][1:].split('?')[0]
                image_name = self.generate_image_name_from_url(image_url, 'webp')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Atri: My Dear Moments
class AtriDownload(Summer2024AnimeDownload, NewsTemplate):
    title = 'Atri: My Dear Moments'
    keywords = [title]
    website = 'https://atri-anime.com/'
    twitter = 'ATRI_anime'
    hashtags = 'ATRI'
    folder_name = 'atri'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news_cont__item',
                                    title_select='.title', date_select='.date', id_select='a', paging_type=1,
                                    a_tag_start_text_to_remove='./', a_tag_prefix=self.PAGE_PREFIX + 'news/',
                                    next_page_select='.news_cont__paging__item.-next',
                                    next_page_eval_index_class='-disable', next_page_eval_index=-1)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('ATRI_visual', 'https://ogre.natalie.mu/media/news/comic/2022/0924/ATRI_visual.jpg')
        self.add_to_image_list('kv_kv_wide', self.PAGE_PREFIX + 'assets/img/kv/kv_wide.png')
        self.add_to_image_list('top_mainvisual_mv', self.PAGE_PREFIX + 'assets/img/top/mainvisual/mv.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        self.image_list = []
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.character__ph__main img[src*="/character/"]')
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].replace('./', '')
                image_name = self.generate_image_name_from_url(image_url, 'character')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Giji Harem
class GijiHaremDownload(Summer2024AnimeDownload, NewsTemplate2):
    title = "Giji Harem"
    keywords = [title]
    website = 'https://gijiharem.com/'
    twitter = 'GijiHarem'
    hashtags = '疑似ハーレム'
    folder_name = 'gijiharem'

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
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.kvSlide__img source[srcset]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['srcset']
                if '/main/' not in image_url:
                    continue
                image_name = self.generate_image_name_from_url(image_url, 'main')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/eiji.html')
            pages = soup.select('#ContentsListUnit01 a[href]')
            for page in pages:
                if not page['href'].endswith('.html') or not page['href'].startswith('../'):
                    continue
                page_url = self.PAGE_PREFIX + page['href'].replace('../', '')
                page_name = page_url.split('/')[-1].split('.html')[0]
                if page_name in processed:
                    continue
                if page_name == 'eiji':
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(page_url)
                if ep_soup is None:
                    continue
                images = ep_soup.select('.chara__body img[src]')
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


# Gimai Seikatsu
class GimaiSeikatsuDownload(Summer2024AnimeDownload, NewsTemplate2):
    title = 'Gimai Seikatsu'
    keywords = [title, "Days with My Step Sister"]
    website = 'https://gimaiseikatsu-anime.com/'
    twitter = 'gimaiseikatsu'
    hashtags = ['義妹生活']
    folder_name = 'gimaiseikatsu'

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
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('.mainImg__img source[srcset*="/main/"]')
            for image in images:
                image_url = self.PAGE_PREFIX + image['srcset']
                image_name = self.generate_image_name_from_url(image_url, 'main')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'chara/')
            a_tags = soup.select('#ContentsListUnit01 a[href]')
            for a_tag in a_tags:
                chara_url = self.PAGE_PREFIX + a_tag['href'].replace('../', '')
                chara_name = chara_url.split('/')[-1].replace('.html', '')
                if chara_name in processed:
                    continue
                if chara_name == 'index':
                    chara_soup = soup
                else:
                    chara_soup = self.get_soup(chara_url)
                if chara_soup is not None:
                    images = chara_soup.select('.chara__img img[src],.charaface img[src]')
                    for image in images:
                        image_url = self.PAGE_PREFIX + image['src'].replace('../', '').split('?')[0]
                        image_name = self.extract_image_name_from_url(image_url)
                        self.add_to_image_list(image_name, image_url)
                    if len(self.image_list) > 0:
                        processed.append(chara_name)
                    self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Isekai Shikkaku
class IsekaiShikkakuDownload(Summer2024AnimeDownload, NewsTemplate):
    title = 'Isekai Shikkaku'
    keywords = [title, 'No Longer Allowed in Another World']
    website = 'https://isekaishikkaku.com/'
    twitter = 'isekaishikkaku'
    hashtags = ['異世界失格', 'isekaishikkaku']
    folder_name = 'isekaishikkaku'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.content-entry-wrap',
                                    title_select='.entry-title span', date_select='.entry-date',
                                    id_select=None, id_has_id=True, news_prefix='news.html',
                                    date_func=lambda x: x.replace('年', '.').replace('月', '.').replace('日', ''))

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('.vis source[srcset*="/top/"]')
            for image in images:
                image_url = self.PAGE_PREFIX + image['srcset'].replace('./', '')
                image_name = self.generate_image_name_from_url(image_url, 'top')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'assets/character/%s.webp'
        self.download_by_template(folder, [template % '%sc', template % '%sf'], 1, 1)


# Kimi to Boku no Saigo no Senjou, Aruiwa Sekai ga Hajimaru Seisen Season II
class Kimisen2Download(Summer2024AnimeDownload, NewsTemplate):
    title = 'Kimi to Boku no Saigo no Senjou, Aruiwa Sekai ga Hajimaru Seisen Season II'
    keywords = [title, "Our Last Crusade or the Rise of a New World Season 2"]
    website = 'https://kimisentv.com/'
    twitter = 'kimisen_project'
    hashtags = ['キミ戦', 'kimisen', 'OurLastCrusade']
    folder_name = 'kimisen2'

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
                                    title_select='.entry-title span', date_select='.entry-date',
                                    id_select=None, id_has_id=True, stop_date='2021.03')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('.vis source[srcset*="/top/"]')
            for image in images:
                image_url = self.PAGE_PREFIX + image['srcset'].replace('./', '')
                image_name = self.generate_image_name_from_url(image_url, 'top')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'assets/character/s2/c%s.webp'
        self.download_by_template(folder, template, 1, 1)


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


# Kono Sekai wa Fukanzen Sugiru
class KonofukaDownload(Summer2024AnimeDownload, NewsTemplate):
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
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-box',
                                    title_select='.news-txt-box', date_select='.news-box-date', id_select='.news-link',
                                    next_page_select='.next', unescape_title=True)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('#kv>img[src*="/themes/"]')
            for image in images:
                image_url = image['src']
                image_name = self.generate_image_name_from_url(image_url, 'themes')
                if 'assets_img_top_' in image_name:
                    image_name = image_name.replace('assets_img_top_', '')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

        self.image_list = []
        self.add_to_image_list('tz', self.PAGE_PREFIX + 'pDK2yjkH/wp-content/themes/konofuka_v0.1/assets/img/top/mv.png')
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/Fr85Cb4aAAAgWlS?format=jpg&name=4096x4096')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        prefix = self.PAGE_PREFIX + 'pDK2yjkH/wp-content/uploads/2024/05/%s.png'
        self.image_list = []
        self.add_to_image_list('img', prefix % 'img')
        self.add_to_image_list('face', prefix % 'face')
        self.download_image_list(folder)
        templates = [prefix % 'img-%s', prefix % 'face-%s']
        self.download_by_template(folder, templates, 1, 1)


# Megami no Café Terrace Season 2
class MegamiCafe2Download(Summer2024AnimeDownload, NewsTemplate4):
    title = 'Megami no Café Terrace Season 2'
    keywords = [title, 'Cafe', 'The Cafe Terrace and its Goddesses Season 2']
    website = 'https://goddess-cafe.com/'
    twitter = 'goddess_cafe_PR'
    hashtags = '女神のカフェテラス'
    folder_name = 'megamicafe2'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        init_json = self.download_episode_preview()
        self.download_news(init_json)
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self, print_http_error=False):
        self.has_website_updated(self.PAGE_PREFIX, 'index')
        return None

        # try:
        #     init_json = self.get_json(self.PAGE_PREFIX + 'wp-json/site-data/init')
        #     for story in init_json['story']:
        #         episode = story['episode']
        #         if self.is_image_exists(episode + '_1'):
        #             continue
        #         self.image_list = []
        #         for i in range(len(story['images'])):
        #             image = story['images'][i]
        #             image_url = image['image_path']
        #             image_name = episode + '_' + str(i + 1)
        #             self.add_to_image_list(image_name, image_url)
        #         self.download_image_list(self.base_folder)
        #     return init_json
        # except HTTPError:
        #     if print_http_error:
        #         print(self.__class__.__name__ + ' - 403 Error when retrieving story API.')
        # except Exception as e:
        #     self.print_exception(e)
        # return None

    def download_news(self, json_obj=None):
        self.download_template_news('site-data', json_obj=json_obj)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('div[class*="Visual"] img[src*="kv"][src*="/static/"]')
            for image in images:
                image_url = image['src']
                if image_url.startswith('/'):
                    image_url = self.PAGE_PREFIX + image_url[1:]
                image_name = self.generate_image_name_from_url(image_url, 'static')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character')
            self.image_list = []
            images = soup.select('img[src*="/character/"][class*="Character__CharaImage"]')
            for image in images:
                image_url = image['src']
                if '/character/' not in image_url:
                    continue
                if image_url.startswith('/'):
                    image_url = self.PAGE_PREFIX + image_url[1:]
                image_name = self.generate_image_name_from_url(image_url, 'character')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Naze Boku no Sekai wo Daremo Oboeteinai no ka?
class NazebokuDownload(Summer2024AnimeDownload, NewsTemplate):
    title = 'Naze Boku no Sekai wo Daremo Oboeteinai no ka?'
    keywords = [title, 'nazeboku', 'Why Nobody Remembers My World?']
    website = 'https://www.nazeboku.com/'
    twitter = 'nazeboku_pr'
    hashtags = ['なぜ僕', 'nazeboku']
    folder_name = 'nazeboku'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news_item',
                                    title_select='.ttl', date_select='.day', id_select='a',
                                    paging_type=3, paging_suffix='?page=%s', next_page_select='.next.page-numbers')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.p-kv__img source[srcset*="/img/"]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['srcset'].split('?')[0].replace('./', '')
                image_name = self.generate_image_name_from_url(image_url, 'img')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'dist/img/character/chara%s/stand.webp'
        try:
            for i in range(20):
                image_name = f'chara{i + 1}_stand'
                if self.is_image_exists(image_name, folder):
                    continue
                image_url = template % str(i + 1)
                result = self.download_image(image_url, folder + '/' + image_name)
                if result == -1:
                    break
        except Exception as e:
            self.print_exception(e, 'Character')


# Oshi no Ko Season 2
class Oshinoko2Download(Summer2024AnimeDownload, NewsTemplate2):
    title = 'Oshi no Ko Season 2'
    keywords = [title, 'oshinoko']
    website = 'https://ichigoproduction.com/Season2/'
    twitter = 'anime_oshinoko'
    hashtags = '推しの子'
    folder_name = 'oshinoko2'

    PAGE_PREFIX = website
    IMAGES_PER_EPISODE = 6

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
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('.kv__img source[srcset*="/main/"]')
            for image in images:
                image_url = self.PAGE_PREFIX + image['srcset']
                image_name = self.generate_image_name_from_url(image_url, 'main')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'chara/')
            a_tags = soup.select('#ContentsListUnit01 a[href]')
            for a_tag in a_tags:
                chara_url = self.PAGE_PREFIX + a_tag['href'].replace('../', '')
                chara_name = chara_url.split('/')[-1].replace('.html', '')
                if chara_name in processed:
                    continue
                if chara_name == 'index':
                    chara_soup = soup
                else:
                    chara_soup = self.get_soup(chara_url)
                if chara_soup is not None:
                    images = chara_soup.select('.ph img[src]')
                    for image in images:
                        image_url = self.PAGE_PREFIX + image['src'].replace('../', '').split('?')[0]
                        image_name = self.extract_image_name_from_url(image_url)
                        self.add_to_image_list(image_name, image_url)
                    if len(self.image_list) > 0:
                        processed.append(chara_name)
                    self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Senpai wa Otokonoko
class PainokoDownload(Summer2024AnimeDownload, NewsTemplate):
    title = 'Senpai wa Otokonoko'
    keywords = [title, 'Senpai Is an Otokonoko']
    website = 'https://senpaiha-otokonoko.com/'
    twitter = 'painoko_anime'
    hashtags = ['ぱいのこアニメ', '先輩はおとこのこ']
    folder_name = 'painoko'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.p-news__list-item',
                                    title_select='.p-news_data__title', date_select='.p-news_data__date',
                                    id_select='a', a_tag_prefix=self.PAGE_PREFIX, a_tag_start_text_to_remove='/',
                                    next_page_select='.-next', paging_type=1, date_separator=' ')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz1', self.PAGE_PREFIX + 'teaser/img/top/main.jpg')
        self.add_to_image_list('tz2', self.PAGE_PREFIX + 'teaser/img/top/main2.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'teaser/img/top/chara_%s.png'
        self.download_by_template(folder, template, 2, 1, prefix='tz_')


# Shikanoko Nokonoko Koshitantan
class ShikanokoDownload(Summer2024AnimeDownload):
    title = 'Shikanoko Nokonoko Koshitantan'
    keywords = [title, 'My Deer Friend Nokotan', 'shikanoko']
    website = 'https://www.anime-shikanoko.jp/'
    twitter = 'shikanoko_PR'
    hashtags = ['しかのこ', 'shikanoko']
    folder_name = 'shikanoko'

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

    def download_news(self, print_http_error=False):
        news_url = self.PAGE_PREFIX + 'news/detail.html?id='
        api_url = 'https://www.news.anime-shikanoko.jp/wp-json/wp/v2/posts?acf_format=standard&per_page=20&page='
        try:
            page = 1
            page_url = api_url + str(page)
            json_obj = self.get_json(page_url)
            news_obj = self.get_last_news_log_object()
            results = []
            for item in json_obj:
                article_id = news_url + str(item['id'])
                date = item['date'][0:10].replace('-', '.')
                title = item['title']['rendered']
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
        except HTTPError as e:
            if print_http_error:
                print(self.__class__.__name__ + ' - 403 Error when retrieving news API.')
        except Exception as e:
            self.print_exception(e, 'News')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.kv__rightSwiperNav img[src*="/top/"]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].split('?')[0].replace('./', '')
                image_name = self.generate_image_name_from_url(image_url, 'top')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        prefix = self.PAGE_PREFIX + 'assets/img/character/%s'
        self.download_by_template(folder, [prefix % '%smain.png', prefix % '%sface1.jpg', prefix % '%sface2.jpg'], 1, 0)


# Shoushimin Series
class ShoshiminDownload(Summer2024AnimeDownload, NewsTemplate2):
    title = 'Shoushimin Series'
    keywords = [title, 'Shoshimin', 'How to Become Ordinary']
    website = 'https://shoshimin-anime.com/'
    twitter = 'shoshimin'
    hashtags = ['小市民']
    folder_name = 'shoshimin'

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
            images = soup.select('.hero__img source[srcset*="/main/"],.hero__img img[src*="/main/"]')
            self.image_list = []
            for image in images:
                if image.has_attr('srcset'):
                    image_url = self.PAGE_PREFIX + image['srcset'].split('?')[0]
                else:
                    image_url = self.PAGE_PREFIX + image['src'].split('?')[0]
                image_name = self.generate_image_name_from_url(image_url, 'main')
                if image_url.endswith('.webp'):
                    image_name += '_'
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('#character .chara__img img[src*="/main/"],#character .chInfo__img img[src*="/main/"]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].split('?')[0]
                image_name = self.generate_image_name_from_url(image_url, 'main')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


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
