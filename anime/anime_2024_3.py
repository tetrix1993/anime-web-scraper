from anime.main_download import MainDownload, NewsTemplate, NewsTemplate2, NewsTemplate4
from datetime import datetime, timedelta
from requests.exceptions import HTTPError
from scan import AniverseMagazineScanner
import os, math, time

# 2.5-jigen no Ririsa https://ririsa-official.com/ @ririsa_official #にごリリ #nigoriri
# Atri: My Dear Moments https://atri-anime.com/ #ATRI @ATRI_anime
# Boku no Tsuma wa Kanjou ga Nai https://bokutsuma-anime.com/ #僕妻アニメ @bokutsuma_anime
# Dungeon no Naka no Hito https://dungeon-people.com/ #ダンジョンの中のひと @dungeon_people
# Giji Harem https://gijiharem.com/ #疑似ハーレム @GijiHarem
# Gimai Seikatsu https://gimaiseikatsu-anime.com/ #義妹生活 @gimaiseikatsu
# Hazurewaku no "Joutai Ijou Skill" de Saikyou ni Natta Ore ga Subete wo Juurin suru made https://hazurewaku-anime.com/ #ハズレ枠 @hazurewaku_info
# Isekai Shikkaku https://isekaishikkaku.com/ #異世界失格 #isekaishikkaku @isekaishikkaku
# Isekai Yururi Kikou: Kosodateshinagara Boukensha Shimasu https://isekai-yururi-anime.jp/ #異世界ゆるり紀行 @iseyuruanime
# Katsute Mahou Shoujo to Aku wa Tekitai shiteita. https://mahoaku-anime.com/ #まほあく #まほあくアニメ @mahoaku_anime
# Kimi to Boku no Saigo no Senjou, Aruiwa Sekai ga Hajimaru Seisen Season II https://kimisentv.com/ #キミ戦 #kimisen #OurLastCrusade
# Koi wa Futago de Warikirenai https://futakire.com/ #ふたきれ @futakire
# Kono Sekai wa Fukanzen Sugiru https://konofuka.com/ #このふか @konofuka_QA
# Madougushi Dahliya wa Utsumukanai https://dahliya-anime.com/ #魔導具師ダリヤ @dahliya_anime
# Make Heroine ga Oosugiru! https://makeine-anime.com/ #マケイン @makeine_anime
# Maougun Saikyou no Majutsushi wa Ningen datta https://maougun-anime.com/ #魔王軍アニメ @maougun_pr
# Mayonaka Punch https://mayopan.jp/ #マヨぱん @mayopan_anime
# Mob kara Hajimaru Tansaku Eiyuutan https://mobkara.com/ #モブから @mobkara_PR
# Megami no Café Terrace Season 2 https://1st.goddess-cafe.com/ #女神のカフェテラス @goddess_cafe_PR
# Naze Boku no Sekai wo Daremo Oboeteinai no ka? https://www.nazeboku.com/ #なぜ僕 #nazeboku @nazeboku_pr
# Ore wa Subete wo "Parry" suru: Gyaku Kanchigai no Sekai Saikyou wa Boukensha ni Naritai https://parry-anime.com/ #パリイする @parry_anime_pr
# Oshi no Ko Season 2 https://ichigoproduction.com/Season2/ #推しの子 @anime_oshinoko
# Senpai wa Otokonoko https://senpaiha-otokonoko.com/ #ぱいのこアニメ #先輩はおとこのこ @painoko_anime
# Shikanoko Nokonoko Koshitantan https://www.anime-shikanoko.jp/ #しかのこ @shikanoko_PR
# Shinmai Ossan Boukensha, Saikyou Party ni Shinu hodo Kitaerarete Muteki ni Naru. https://shinmaiossan-anime.com/ #新米オッサン @shinmaiossan
# Shoushimin Series https://shoshimin-anime.com/ #小市民 @shoshimin_pr
# Shy Season 2 https://shy-anime.com/ #SHY_hero @SHY_off
# Tokidoki Bosotto Russia-go de Dereru Tonari no Alya-san https://roshidere.com/ #ロシデレ @roshidere
# Tsue to Tsurugi no Wistoria https://wistoria-anime.com/ #ウィストリア #うぃす #Wistoria @Wistoria_PR
# VTuber Nandaga Haishin Kiri Wasuretara Densetsu ni Natteta https://vden.jp/ #ぶいでんアニメ #vden @vden_anime


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
        self.add_to_image_list('kv', self.PAGE_PREFIX + 'assets/img/top/mainvisual/mv.jpg')
        self.download_image_list(folder)

        template = self.PAGE_PREFIX + 'assets/img/top/mainvisual/archive/ph_%s.png'
        self.download_by_template(folder, template, 1, 1, prefix='archive_')

        # self.add_to_image_list('ATRI_visual', 'https://ogre.natalie.mu/media/news/comic/2022/0924/ATRI_visual.jpg')
        # self.add_to_image_list('kv_kv_wide', self.PAGE_PREFIX + 'assets/img/kv/kv_wide.png')
        # self.add_to_image_list('top_mainvisual_mv', self.PAGE_PREFIX + 'assets/img/top/mainvisual/mv.jpg')
        # self.download_image_list(folder)

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


# Boku no Tsuma wa Kanjou ga Nai
class BokutsumaDownload(Summer2024AnimeDownload, NewsTemplate):
    title = "Boku no Tsuma wa Kanjou ga Nai"
    keywords = [title, 'My Wife Has No Emotion']
    website = 'https://bokutsuma-anime.com/'
    twitter = 'bokutsuma_anime'
    hashtags = '僕妻アニメ'
    folder_name = 'bokutsuma'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_episode_preview_external()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        try:
            template = self.PAGE_PREFIX + 'assets/images/story/%s/%s.jpg'
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (str(i + 1), str(j + 1))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_external(self):
        keywords = ['僕の妻は感情がない']
        AniverseMagazineScanner(keywords, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20240627', download_id=self.download_id).run()

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news/'
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.contents article',
                                    title_select='h2', date_select='time', id_select='a', a_tag_prefix=news_url,
                                    date_separator='/')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.main-v img[src*="/top/"]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src']
                image_name = self.generate_image_name_from_url(image_url, 'top')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        prefix = self.PAGE_PREFIX + 'character/'
        try:
            soup = self.get_soup(prefix + 'takuma-kosugi.html')
            pages = soup.select('ul.tabs a[href]')
            for page in pages:
                if not page['href'].endswith('.html'):
                    continue
                page_url = prefix + page['href']
                page_name = page['href'].split('.html')[0]
                if page_name in processed:
                    continue
                if page_name == 'takuma-kosugi':
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(page_url)
                if ep_soup is None:
                    continue
                images = ep_soup.select('img[src*="/character/"].pic')
                self.image_list = []
                for image in images:
                    image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                    image_name = self.generate_image_name_from_url(image_url, 'character')
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(folder)
                processed.append(page_name)
        except Exception as e:
            self.print_exception(e, 'Character')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Dungeon no Naka no Hito
class DungeonPeopleDownload(Summer2024AnimeDownload, NewsTemplate):
    title = 'Dungeon no Naka no Hito'
    keywords = [title, 'Dungeon People']
    website = 'https://dungeon-people.com/'
    twitter = 'dungeon_people'
    hashtags = 'ダンジョンの中のひと'
    folder_name = 'dungeonpeople'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story')
            blocks = soup.select('.story-block')
            for block in blocks:
                try:
                    episode = str(int(block.select('.story-block--tit-id')[0].text.replace('#', ''))).zfill(2)
                except:
                    continue
                images = block.select('.story-block--slide-item img[src]')
                self.image_list = []
                for i in range(len(images)):
                    image_url = images[i]['src']
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-index--list-item',
                                    title_select='.news-index--list-item__detail-text',
                                    date_select='.news-index--list-item__detail-date',
                                    id_select='a', date_separator='/', next_page_select='.next[href*="/page/"]')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.top-mv--slide__item img[src*="/top/"]')
            self.image_list = []
            for image in images:
                image_url = image['src']
                image_name = self.generate_image_name_from_url(image_url, 'top')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/clay')
            pages = soup.select('.chara-subnavi--slide-item a[href]')
            for page in pages:
                page_url = page['href']
                if page_url.endswith('/'):
                    page_name = page_url[:-1].split('/')[-1]
                else:
                    page_name = page_url.split('/')[-1]
                if page_name in processed:
                    continue
                if page_name == 'clay':
                    c_soup = soup
                else:
                    c_soup = self.get_soup(page_url)
                if c_soup is None:
                    continue
                images = c_soup.select('.chara-detail--img img[src*="/character/"],'\
                                       + '.chara-detail--face img[src*="/character/"]')
                self.image_list = []
                for image in images:
                    image_url = image['src']
                    image_name = self.generate_image_name_from_url(image_url, 'character')
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(folder)
                processed.append(page_name)
        except Exception as e:
            self.print_exception(e, 'Character')
        self.create_cache_file(cache_filepath, processed, num_processed)


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
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/01.html')
            stories = soup.select('table[summary="List_Type01"] a[href]')
            for story in stories:
                story_url = self.PAGE_PREFIX + story['href'].replace('../', '')
                try:
                    episode = str(int(story_url.split('/')[-1].split('.html')[0])).zfill(2)
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
                        self.add_to_image_list(image_name, image_url)
                    self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

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
        self.download_media()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/01.html')
            stories = soup.select('table[summary="List_Type01"] a[href]')
            for story in stories:
                story_url = self.PAGE_PREFIX + story['href'].replace('../', '')
                try:
                    episode = str(int(story_url.split('/')[-1].split('.html')[0])).zfill(2)
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
                        self.add_to_image_list(image_name, image_url)
                    self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

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

    def download_media(self):
        folder = self.create_media_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        for page in ['privilege', 'campaign', '01', '02', '03']:
            try:
                if page in processed:
                    continue
                page_url = self.PAGE_PREFIX + 'bd/'
                if page != '01':
                    page_url += page + '.html'
                soup = self.get_soup(page_url)
                images = soup.select('.block_inner img[src]')
                self.image_list = []
                for image in images:
                    image_url = self.PAGE_PREFIX + image['src'].replace('../', '').split('?')[0]
                    if '/bddvd/' in image_url:
                        image_name = self.generate_image_name_from_url(image_url, 'bddvd')
                    else:
                        image_name = self.extract_image_name_from_url(image_url)
                    if not self.is_content_length_in_range(image_url, more_than_amount=25000):
                        continue
                    self.add_to_image_list(image_name, image_url)
                if page.isnumeric() and page != '01':
                    if len(self.image_list) > 0:
                        processed.append(page)
                    else:
                        break
                self.download_image_list(folder)
            except Exception as e:
                self.print_exception(e, f'Blu-ray - {page}')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Hazurewaku no "Joutai Ijou Skill" de Saikyou ni Natta Ore ga Subete wo Juurin suru made https://hazurewaku-anime.com/ #ハズレ枠
class HazurewakuDownload(Summer2024AnimeDownload, NewsTemplate):
    title = 'Hazurewaku no "Joutai Ijou Skill" de Saikyou ni Natta Ore ga Subete wo Juurin suru made'
    keywords = [title, 'hazurewaku', 'Failure Frame: I Became the Strongest and Annihilated Everything With Low-Level Spells']
    website = 'https://hazurewaku-anime.com/'
    twitter = 'hazurewaku_info'
    hashtags = ['ハズレ枠']
    folder_name = 'hazurewaku'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story')
            blocks = soup.select('.episode-item[id]')
            for block in blocks:
                try:
                    episode = str(int(block['id'].replace('ep', ''))).zfill(2)
                except:
                    continue
                images = block.select('.episode-visual img[src]')
                self.image_list = []
                for i in range(len(images)):
                    image_url = images[i]['src']
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-list__scroll li',
                                    title_select='.title', date_select='.news-date', id_select='a', news_prefix='',
                                    date_func=lambda x: x[0:4] + '.' + x[4:])

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('.hero-image img[src*="/top/"]')
            for image in images:
                image_url = image['src']
                image_name = self.generate_image_name_from_url(image_url, 'top')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            a_tags = soup.select('a[href].btn-character-list')
            for a_tag in a_tags:
                chara_url = a_tag['href']
                if chara_url.endswith('/'):
                    chara_name = chara_url[:-1].split('/')[-1]
                else:
                    chara_name = chara_url.split('/')[-1]
                if chara_name in processed:
                    continue
                chara_soup = self.get_soup(chara_url)
                if chara_soup is not None:
                    images = chara_soup.select('.chara img[src],.face img[src]')
                    for image in images:
                        image_url = image['src'].split('?')[0]
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


# Isekai Yururi Kikou: Kosodateshinagara Boukensha Shimasu
class IseyuruDownload(Summer2024AnimeDownload, NewsTemplate):
    title = 'Isekai Yururi Kikou: Kosodateshinagara Boukensha Shimasu'
    keywords = [title, 'iseyuru', "A Journey Through Another World: Raising Kids While Adventuring"]
    website = 'https://isekai-yururi-anime.jp/'
    twitter = 'iseyuruanime'
    hashtags = ['異世界ゆるり紀行']
    folder_name = 'iseyuru'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        soup = self.download_key_visual()
        self.download_character(soup)

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.c-Post__link',
                                    title_select='.c-Post__textHover', date_select='.c-Post__dateBox', id_select=None,
                                    date_func=lambda x: x[0:4] + '.' + str(self.convert_month_string_to_number(x.split(' ')[1])) + '.' + x.split(' ')[2])

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        soup = None
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.p-Fv__kv img[src*="/top/"]')
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].split('?')[0]
                image_name = self.generate_image_name_from_url(image_url, 'top')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')
        return soup

    def download_character(self, soup=None):
        folder = self.create_character_directory()
        self.image_list = []
        template = self.PAGE_PREFIX + 'dist/img/top/chara/art/%s.png'
        try:
            if soup is None:
                soup = self.get_soup(self.PAGE_PREFIX)
            lis = soup.select('.p-Chara__listItem[data-modal-path]')
            for li in lis:
                image_name = li['data-modal-path'].split('/')[-1].replace('.html', '')
                image_url = template % image_name
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Katsute Mahou Shoujo to Aku wa Tekitai shiteita.
class MahoakuDownload(Summer2024AnimeDownload, NewsTemplate):
    title = 'Katsute Mahou Shoujo to Aku wa Tekitai shiteita.'
    keywords = [title, "The Magical Girl and the Evil Lieutenant Used to Be Archenemies"]
    website = 'https://mahoaku-anime.com/'
    twitter = 'mahoaku_anime'
    hashtags = ['まほあく', 'まほあくアニメ']
    folder_name = 'mahoaku'

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
        news_url = self.PAGE_PREFIX + 'news/'
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.p-news__list-item',
                                    title_select='.p-news__list-detail', date_select='.p-news__list-date',
                                    id_select='a', a_tag_prefix=news_url, date_separator='/', paging_type=3,
                                    paging_suffix='?page=%s', next_page_select='.c-pagination__list-item',
                                    next_page_eval_index_class='is-current', next_page_eval_index=-1)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('.p-hero__kv-img img[src*="/assets/"]')
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].replace('./', '')
                image_name = self.generate_image_name_from_url(image_url, 'assets')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'assets/img/character/img_chara_stand%s.png'
        self.download_by_template(folder, template, 1, 1)


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


# Madougushi Dahliya wa Utsumukanai
class DahliyaDownload(Summer2024AnimeDownload, NewsTemplate):
    title = 'Madougushi Dahliya wa Utsumukanai'
    keywords = [title, "Dahliya in Bloom"]
    website = 'https://dahliya-anime.com/'
    twitter = 'dahliya_anime'
    hashtags = ['魔導具師ダリヤ']
    folder_name = 'dahliya'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self, print_http_error=False):
        try:
            objs = self.get_json(self.PAGE_PREFIX + 'story_data?_=' + str(math.floor(time.time() * 1000)))
            for obj in objs:
                if 'acf' in obj:
                    acf = obj['acf']
                    if 'number' in acf and 'images' in acf and isinstance(acf['images'], list):
                        try:
                            episode = str(int(acf['number'].replace('第', '').replace('話', ''))).zfill(2)
                        except:
                            continue
                        for i in range(len(acf['images'])):
                            image_url = acf['images'][i]
                            image_name = episode + '_' + str(i + 1)
                            self.add_to_image_list(image_name, image_url)
                        self.download_image_list(self.base_folder)
        except HTTPError:
            if print_http_error:
                print(self.__class__.__name__ + ' - 403 Error when retrieving story API.')
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-item',
                                    title_select='.news-item__title', date_select='.news-item__date',
                                    id_select=None, a_tag_prefix=self.PAGE_PREFIX, a_tag_start_text_to_remove='/')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.home-visual__image img[src*="/img/"]')
            for image in images:
                image_url = image['src'].split('?')[0]
                image_name = self.generate_image_name_from_url(image_url, 'img')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        json_url = self.PAGE_PREFIX + 'chara_data'
        self.image_list = []
        try:
            json_obj = self.get_json(json_url)
            if 'charas' in json_obj and isinstance(json_obj['charas'], list):
                for chara in json_obj['charas']:
                    if 'images' in chara:
                        if 'visuals' in chara['images'] and isinstance(chara['images']['visuals'], list):
                            for visual in chara['images']['visuals']:
                                if 'image' in visual:
                                    image_url = visual['image'].split('?')[0]
                                    image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                                    self.add_to_image_list(image_name, image_url)
        except Exception as e:
            self.print_exception(e, 'Character')
        self.download_image_list(folder)


# Make Heroine ga Oosugiru!
class MakeineDownload(Summer2024AnimeDownload, NewsTemplate):
    title = 'Make Heroine ga Oosugiru!'
    keywords = [title, "Too Many Losing Heroines!"]
    website = 'https://makeine-anime.com/'
    twitter = 'makeine_anime'
    hashtags = ['マケイン']
    folder_name = 'makeine'

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
        news_url = self.PAGE_PREFIX + 'news/'
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news_list__item',
                                    title_select='.news_list__item-title', date_select='.news_list__item-date',
                                    id_select='a', a_tag_prefix=news_url, a_tag_start_text_to_remove='./',
                                    paging_type=1, next_page_select='.news_pager-next a')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.main_image img[src*="/top/"]')
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].split('?')[0]
                image_name = self.generate_image_name_from_url(image_url, 'top')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        prefix = self.PAGE_PREFIX + 'assets/img/character/img_%s.png'
        templates = [prefix % 'main%s', prefix % 'face%s']
        self.download_by_template(folder, templates, 2, 1)


# Maougun Saikyou no Majutsushi wa Ningen datta
class MaougunDownload(Summer2024AnimeDownload, NewsTemplate):
    title = 'Maougun Saikyou no Majutsushi wa Ningen datta'
    keywords = [title, "The Strongest Magician in the Demon Lord's Army Was a Human"]
    website = 'https://maougun-anime.com/'
    twitter = 'maougun_pr'
    hashtags = ['魔王軍アニメ']
    folder_name = 'maougun'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        soup = self.download_key_visual()
        self.download_character(soup)

    def download_episode_preview(self):
        try:
            template = self.PAGE_PREFIX + 'dist/img/top/story/ep%s/img%s.jpg'
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (str(i + 1), str(j + 1))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.c-Post__link',
                                    title_select='.c-Post__textHover', date_select='.c-Post__date p', id_select=None)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        soup = None
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.p-Fv__kv img[src*="/top/"]')
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].split('?')[0]
                image_name = self.generate_image_name_from_url(image_url, 'top')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')
        return soup

    def download_character(self, soup=None):
        folder = self.create_character_directory()
        self.image_list = []
        try:
            if soup is None:
                soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.p-Chara__imgSlide img[src*="/chara/"],.p-Chara__profFace img[src*="/chara/"]')
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].split('?')[0]
                image_name = self.generate_image_name_from_url(image_url, 'chara')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Mayonaka Punch
class MayopanDownload(Summer2024AnimeDownload, NewsTemplate):
    title = 'Mayonaka Punch'
    keywords = [title, 'mayopan']
    website = 'https://mayopan.jp/'
    twitter = 'mayopan_anime'
    hashtags = ['マヨぱん']
    folder_name = 'mayopan'

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
        news_url = self.PAGE_PREFIX + 'news/'
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.newsList',
                                    title_select='.newsTitle__txt', date_select='.newsTitle__date', id_select='a',
                                    a_tag_prefix=news_url, a_tag_start_text_to_remove='./')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        selector = '.visualImage source[srcset*="/top/"]:not(source[srcset*="_bg"])'\
                   + ':not(source[srcset*="-s"]):not(source[srcset*="_chara"]):not(source[srcset*="_catch"])'
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select(selector)
            for image in images:
                image_url = self.PAGE_PREFIX + image['srcset'].split('?')[0].replace('./', '')
                image_name = self.generate_image_name_from_url(image_url, 'top')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        self.image_list = []
        selector = '.characterMain__image img[src*="/character/"],'\
                   + '.characterMain__faceImageList img[src*="/character/"]'
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            images = soup.select(selector)
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].split('?')[0].replace('../', '')
                image_name = self.generate_image_name_from_url(image_url, 'character')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Mob kara Hajimaru Tansaku Eiyuutan
class MobkaraDownload(Summer2024AnimeDownload, NewsTemplate):
    title = 'Mob kara Hajimaru Tansaku Eiyuutan'
    keywords = [title, "A Nobody's Way Up to an Exploration Hero LV"]
    website = 'https://mobkara.com/'
    twitter = 'mobkara_PR'
    hashtags = ['モブから']
    folder_name = 'mobkara'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story')
            blocks = soup.select('.storyBox[id]')
            for block in blocks:
                try:
                    episode = str(int(block['id'].replace('story', ''))).zfill(2)
                except:
                    continue
                images = block.select('.imgList__item img[src]')
                self.image_list = []
                for i in range(len(images)):
                    image_url = images[i]['src']
                    if image_url.startswith('/'):
                        image_url = self.PAGE_PREFIX + image_url[1:]
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url, to_jpg=True)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.newsList',
                                    title_select='.newsList_ttl', date_select='.news_day', id_select='a',
                                    a_tag_prefix=self.PAGE_PREFIX, a_tag_start_text_to_remove='/',
                                    next_page_select='.wp-pagenavi *', next_page_eval_index_class='current',
                                    next_page_eval_index=-1)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        soup = None
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.mainvisalBox img[src*="/top/"]')
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].split('?')[0][1:]
                image_name = self.generate_image_name_from_url(image_url, 'top')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')
        return soup

    def download_character(self):
        folder = self.create_character_directory()
        prefix = self.PAGE_PREFIX + 'wordpress/wp-content/themes/mobkara/assets/img/character/chara_chara%s.png'
        self.download_by_template(folder, [prefix % '%s_img', prefix % '%s_face'], 1, 1)


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
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 5

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        try:
            template = self.PAGE_PREFIX + 'dist/img/story/ep%s/img%s.jpg'
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (str(i + 1), str(j + 1).zfill(2))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

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


# Ore wa Subete wo "Parry" suru: Gyaku Kanchigai no Sekai Saikyou wa Boukensha ni Naritai
class ParrySuruDownload(Summer2024AnimeDownload, NewsTemplate4):
    title = 'Ore wa Subete wo "Parry" suru: Gyaku Kanchigai no Sekai Saikyou wa Boukensha ni Naritai'
    keywords = [title, 'parrysuru', 'I Parry Everything']
    website = 'https://parry-anime.com/'
    twitter = 'parry_anime_pr'
    hashtags = 'パリイする'
    folder_name = 'parrysuru'

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
        self.download_template_news(json_url=self.PAGE_PREFIX + 'api/site-data/init')

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
                if 'icon' in image_name or 'logo' in image_name:
                    continue
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'wp/wp-content/themes/b5ffe5fce0e1/static/character/%s/main.webp'
        try:
            for i in range(20):
                num = str(i + 1).zfill(2)
                image_url = template % num
                image_name = num + '_main'
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

    def download_episode_preview(self, print_http_error=False):
        prefix = 'https://www.news.anime-shikanoko.jp/'
        try:
            objs = self.get_json(prefix + 'wp-json/wp/v2/story?acf_format=standard&per_page=100&page=1&_='
                                 + str(math.floor(time.time() * 1000)))
            for obj in objs:
                if 'acf' in obj:
                    acf = obj['acf']
                    if 'story_num' in acf and 'story_imgs' in acf and isinstance(acf['story_imgs'], list):
                        try:
                            episode = str(int(acf['story_num'].replace('#', ''))).zfill(2)
                        except:
                            continue
                        for i in range(len(acf['story_imgs'])):
                            story_img = acf['story_imgs'][i]
                            if 'story_img' in story_img and 'url' in story_img['story_img']:
                                image_url = story_img['story_img']['url']
                                image_name = episode + '_' + str(i + 1)
                                self.add_to_image_list(image_name, image_url)
                            else:
                                continue
                        self.download_image_list(self.base_folder)
        except HTTPError:
            if print_http_error:
                print(self.__class__.__name__ + ' - 403 Error when retrieving story API.')
        except Exception as e:
            self.print_exception(e)

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


# Shinmai Ossan Boukensha, Saikyou Party ni Shinu hodo Kitaerarete Muteki ni Naru.
class ShinmaiOssanDownload(Summer2024AnimeDownload, NewsTemplate):
    title = 'Shinmai Ossan Boukensha, Saikyou Party ni Shinu hodo Kitaerarete Muteki ni Naru.'
    keywords = [title, 'shinmaiossan']
    website = 'https://shinmaiossan-anime.com/'
    twitter = 'shinmaiossan'
    hashtags = ['新米オッサン']
    folder_name = 'shinmaiossan'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_episode_preview_guess(print_invalid=False, download_valid=True)
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            blocks = soup.select('.story-box')
            for block in blocks:
                try:
                    episode = str(int(block.select('.num')[0].text)).zfill(2)
                except:
                    continue
                images = block.select('.ss-item.swiper-slide img[src]')
                self.image_list = []
                for i in range(len(images)):
                    image_url = images[i]['src']
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_guess(self, print_invalid=False, download_valid=False):
        if self.is_image_exists(str(self.FINAL_EPISODE).zfill(2) + '_' + str(self.IMAGES_PER_EPISODE)):
            return

        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'wp/wp-content/uploads/%s/%s/%s.jpg'
        current_date = datetime.now() + timedelta(hours=1)
        year = current_date.strftime('%Y')
        month = current_date.strftime('%m')
        is_successful = False
        valid_urls = []
        for j in range(self.IMAGES_PER_EPISODE):
            k = 0
            while k < 20:
                if k == 0:
                    append = ''
                else:
                    append = '-' + str(k)
                image_folder = folder + '/' + year + '/' + month
                image_name = str(j + 1).zfill(2) + append
                if not self.is_image_exists(image_name, image_folder):
                    image_url = template % (year, month, image_name)
                    if self.is_valid_url(image_url, is_image=True):
                        print('VALID - ' + image_url)
                        is_successful = True
                        valid_urls.append({'name': image_name, 'url': image_url, 'folder': image_folder})
                    else:
                        if print_invalid:
                            print('INVALID - ' + image_url)
                        break
                k += 1
        if download_valid and len(valid_urls) > 0:
            for valid_url in valid_urls:
                image_name = valid_url['name']
                image_folder = valid_url['folder']
                if not os.path.exists(image_folder):
                    os.makedirs(image_folder)
                self.download_image(valid_url['url'], image_folder + '/' + image_name)
        if is_successful:
            print(self.__class__.__name__ + ' - Guessed correctly!')
        return is_successful

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-item', title_select='.title',
                                    date_select='.date', id_select='a', a_tag_prefix=self.PAGE_PREFIX,
                                    next_page_select='.next-button', next_page_eval_index_class='off',
                                    next_page_eval_index=-1)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.kv img[src*="/themes/"]')
            self.image_list = []
            for image in images:
                image_url = image['src'].split('?')[0]
                image_name = self.generate_image_name_from_url(image_url, 'themes').replace('_images_', '_')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        t = self.PAGE_PREFIX + 'wp/wp-content/themes/sinmaiossan_teaser/images/chara-%s.png'
        self.download_by_template(folder, [t % 'pic%s', t % 'face%s'], 1, 1)


# Shoushimin Series
class ShoshiminDownload(Summer2024AnimeDownload, NewsTemplate2):
    title = 'Shoushimin Series'
    keywords = [title, 'Shoshimin', 'How to Become Ordinary']
    website = 'https://shoshimin-anime.com/'
    twitter = 'shoshimin_pr'
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
                if not image_url.endswith('.webp'):
                    continue
                image_name = self.generate_image_name_from_url(image_url, 'main')
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


# Shy Season 2
class ShyDownload(Summer2024AnimeDownload, NewsTemplate):
    title = 'Shy Season 2'
    keywords = [title]
    website = 'https://shy-anime.com/'
    twitter = 'SHY_off'
    hashtags = 'SHY_hero'
    folder_name = 'shy2'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/2nd')
            stories = soup.select('.story-episode-item a[href]')
            for story in stories:
                story_url = story['href']
                if story_url.endswith('/'):
                    story_url = story_url[:-1]
                try:
                    episode = str(int(story_url.split('/')[-1])).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                ep_soup = self.get_soup(story['href'])
                if ep_soup is None:
                    continue
                self.image_list = []
                images = ep_soup.select('.story-thumb-item img[src]')
                for i in range(len(images)):
                    image_url = images[i]['src'].split('?')[0]
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url, to_jpg=True)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-box',
                                    title_select='.news-txt-box', date_select='.news-box-date', id_select='a',
                                    paging_type=0, next_page_select='span.page-numbers', next_page_eval_index=-1,
                                    next_page_eval_index_class='current', stop_date='2023.12.04')


# Tokidoki Bosotto Russia-go de Dereru Tonari no Alya-san
class RoshidereDownload(Summer2024AnimeDownload, NewsTemplate2):
    title = 'Tokidoki Bosotto Russia-go de Dereru Tonari no Alya-san'
    keywords = [title, 'Alya Sometimes Hides Her Feelings in Russian', 'Aalya', 'roshidere']
    website = 'https://roshidere.com/'
    twitter = 'roshidere'
    hashtags = ['ロシデレ', 'roshidere']
    folder_name = 'roshidere'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_external()
        self.download_news()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/01.html')
            stories = soup.select('table[summary="List_Type01"] a[href]')
            for story in stories:
                story_url = self.PAGE_PREFIX + story['href'].replace('../', '')
                try:
                    episode = str(int(story_url.split('/')[-1].split('.html')[0])).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                if episode == '01':
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(story_url)
                if ep_soup is not None:
                    images = ep_soup.select('ul.tp5 img[src]')
                    self.image_list = []
                    for i in range(len(images)):
                        image_url = self.PAGE_PREFIX + images[i]['src'].split('?')[0]
                        image_url = self.remove_string(image_url, ['../', 'sn_'])
                        image_name = episode + '_' + str(i + 1)
                        self.add_to_image_list(image_name, image_url)
                    self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_external(self):
        keywords = ['時々ボソッとロシア語でデレる隣のアーリャさん']
        AniverseMagazineScanner(keywords, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20240628', download_id=self.download_id).run()

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

    def download_media(self):
        folder = self.create_media_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        for page in ['privilege', 'campaign', '01', '02', '03']:
            try:
                if page in processed:
                    continue
                page_url = self.PAGE_PREFIX + 'bd/'
                if page != '01':
                    page_url += page + '.html'
                soup = self.get_soup(page_url)
                images = soup.select('.block_inner img[src]')
                self.image_list = []
                for image in images:
                    image_url = self.PAGE_PREFIX + image['src'].replace('../', '').split('?')[0]
                    if '/bddvd/' in image_url:
                        image_name = self.generate_image_name_from_url(image_url, 'bddvd')
                    else:
                        image_name = self.extract_image_name_from_url(image_url)
                    if not self.is_content_length_in_range(image_url, more_than_amount=32000):
                        continue
                    self.add_to_image_list(image_name, image_url)
                if page.isnumeric() and len(self.image_list) > 0:
                    processed.append(page)
                elif page.isnumeric():
                    break
                self.download_image_list(folder)
            except Exception as e:
                self.print_exception(e, f'Blu-ray - {page}')
        self.create_cache_file(cache_filepath, processed, num_processed)

        prefix = self.PAGE_PREFIX + 'core_sys/images/contents/%s/block/%s/%s.jpg'
        self.image_list = []
        imgs = [(19, 30, 51), (22, 44, 59), (20, 35, 54), (23, 48, 60), (21, 40, 57), (24, 52, 61)]
        try:
            for img in imgs:
                image_name = str(img[2]).zfill(8)
                if self.is_image_exists(folder, image_name):
                    continue
                image_url = prefix % (str(img[0]).zfill(8), str(img[1]).zfill(8), str(img[2]).zfill(8))
                if not self.is_content_length_in_range(image_url, more_than_amount=32000):
                    continue
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


# Tsue to Tsurugi no Wistoria
class WistoriaDownload(Summer2024AnimeDownload, NewsTemplate):
    title = 'Tsue to Tsurugi no Wistoria'
    keywords = [title, "Wistoria's Wand and Sword"]
    website = 'https://wistoria-anime.com/'
    twitter = 'Wistoria_PR'
    hashtags = ['ウィストリア', 'うぃす', 'Wistoria']
    folder_name = 'wistoria'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.newsList',
                                    title_select='.newsTitle__txt', date_select='.newsTitle__date', id_select='a',
                                    next_page_select='.nextpostslink')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.visualIn source[srcset*="/img/"],.visualIn img[src*="/img/"]')
            self.image_list = []
            for image in images:
                if image.has_attr('srcset'):
                    image_url = image['srcset'].split('?')[0]
                else:
                    image_url = image['src'].split('?')[0]
                if not image_url.endswith('.webp'):
                    continue
                image_name = self.generate_image_name_from_url(image_url, 'img')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        t = self.PAGE_PREFIX + 'jrepgmrf/wp-content/themes/wistoria-anime/assets/img/character/character_%s_main.png'
        self.download_by_template(folder, t, 1, 1)


# VTuber Nandaga Haishin Kiri Wasuretara Densetsu ni Natteta
class VdenDownload(Summer2024AnimeDownload, NewsTemplate2):
    title = 'VTuber Nandaga Haishin Kiri Wasuretara Densetsu ni Natteta'
    keywords = [title, "VTuber Legend: How I Went Viral after Forgetting to Turn Off My Stream", 'vden']
    website = 'https://vden.jp/'
    twitter = 'vden_anime'
    hashtags = ['ぶいでんアニメ', 'vden']
    folder_name = 'vden'

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
            images = soup.select('.kvImg__slide source[srcset*="/main/"],.kvImg__slide img[src*="/main/"]')
            self.image_list = []
            names = set()
            for image in images:
                if image.has_attr('srcset'):
                    image_url = self.PAGE_PREFIX + image['srcset'].split('?')[0]
                else:
                    image_url = self.PAGE_PREFIX + image['src'].split('?')[0]
                image_name = self.generate_image_name_from_url(image_url, 'main')
                if image_name in names:
                    continue
                else:
                    names.add(image_name)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        t = self.PAGE_PREFIX + 'core_sys/images/main/tz/cahara/chara%s_full.png'
        self.download_by_template(folder, t, 2, 1, prefix='tz_')
