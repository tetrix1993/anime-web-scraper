from anime.main_download import MainDownload, NewsTemplate, NewsTemplate2, NewsTemplate4
from scan import AniverseMagazineScanner
from datetime import datetime, timedelta
from requests.exceptions import HTTPError
import os


# Dark Gathering https://darkgathering.jp/ #ダークギャザリング @DG_anime
# Eiyuu Kyoushitsu https://eiyukyoushitsu-anime.com/ #英雄教室 #eiyu_anime @eiyu_anime
# Helck https://www.helck-anime.com/ #Helck #ヘルク @Helck_anime
# Higeki no Genkyou to Naru Saikyou Gedou Last Boss Joou wa Tami no Tame ni Tsukushimasu. https://lastame.com/ #ラス為 @lastame_pr
# Horimiya: Piece https://horimiya-anime.com/ #ホリミヤ #horimiya @horimiya_anime
# Jidou Hanbaiki ni Umarekawatta Ore wa Meikyuu wo Samayou https://jihanki-anime.com/ #俺自販機 @jihanki_anime
# Jitsu wa Ore, Saikyou deshita? https://jitsuhaoresaikyo-anime.com/ @jitsuoresaikyo
# Kanojo, Okarishimasu 3rd Season https://kanokari-official.com/ #かのかり #kanokari @kanokari_anime
# Level 1 dakedo Unique Skill de Saikyou desu https://level1-anime.com/ #level1_anime @level1_anime
# Lv1 Maou to One Room Yuusha https://lv1room.com/ #lv1room @Lv1room
# Liar Liar https://liar-liar-anime.com/ #ライアー・ライアー #ライアラ @liar2_official
# Masamune-kun no Revenge R https://masamune-tv.com/ #MASA_A @masamune_tv
# Mushoku Tensei II: Isekai Ittara Honki Dasu https://mushokutensei.jp/ #無職転生 #MushokuTensei @mushokutensei_A
# Nanatsu no Maken ga Shihai suru https://nanatsuma-pr.com/ #nanatsuma #ななつま @nanatsuma_pr
# Okashi na Tensei https://okashinatensei-pr.com/ #おかしな転生 @okashinatensei
# Ryza no Atelier: Tokoyami no Joou to Himitsu no Kakurega https://ar-anime.com/ #ライザのアトリエ @Ryza_PR
# Seija Musou: Salaryman, Isekai de Ikinokoru Tame ni Ayumu Michi https://www.tbs.co.jp/anime/seija/ #聖者無双 @seija_anime
# Shinigami Bocchan to Kuro Maid S2 https://bocchan-anime.com/ #死神坊ちゃん @bocchan_anime
# Shiro Seijo to Kuro Bokushi https://shiroseijyo-anime.com/ @shiroseijyo_tv #白聖女と黒牧師
# Suki na Ko ga Megane wo Wasureta https://anime.shochiku.co.jp/sukimega/ #好きめが @Sukimega
# Temple https://temple-anime.com/ #てんぷる #Tenpuru_anime @temple_tvanime
# Uchi no Kaisha no Chiisai Senpai no Hanashi https://chiisaisenpai.com/ #うちの会社の小さい先輩の話 @smallsenpai_pr
# Watashi no Shiawase na Kekkon https://watakon-anime.com/ #watakon #わたしの幸せな結婚
# Yumemiru Danshi wa Genjitsushugisha https://yumemirudanshi.com/ #夢見る男子 @yumemiru_anime
# Zom 100: Zombie ni Naru made ni Shitai 100 no Koto https://zom100.com/ #ゾン100 #Zom100 @Zom100_anime_JP


# Summer 2023 Anime
class Summer2023AnimeDownload(MainDownload):
    season = "2023-3"
    season_name = "Summer 2023"
    folder_name = '2023-3'

    def __init__(self):
        super().__init__()


# Dark Gathering
class DarkGatheringDownload(Summer2023AnimeDownload, NewsTemplate):
    title = 'Dark Gathering'
    keywords = [title]
    website = 'https://darkgathering.jp/'
    twitter = 'DG_anime'
    hashtags = ['ダークギャザリング']
    folder_name = 'darkgathering'

    PAGE_PREFIX = website
    FINAL_EPISODE = 25

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self, print_http_error=False):
        if self.is_image_exists(str(self.FINAL_EPISODE) + '_1') and self.is_image_exists('01_1'):
            return

        try:
            objs = self.get_json(self.PAGE_PREFIX + 'news/wp-json/wp/v2/pages?orderby=date&order=asc&acf_format=standard&per_page=100&parent=73')
            for obj in objs:
                if 'acf' in obj:
                    acf = obj['acf']
                    if 'number' in acf and 'images' in acf and isinstance(acf['images'], list):
                        try:
                            episode = str(int(acf['number'].split('第')[1].split('話')[0])).zfill(2)
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
                                    title_select='.news-item__title', date_select='.news-item__date-text',
                                    id_select='a', a_tag_start_text_to_remove='/', a_tag_prefix=self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        template = self.PAGE_PREFIX + "img/home/visual_%s.webp"
        self.download_by_template(folder, template, 2, 2)

    def download_character(self):
        folder = self.create_character_directory()
        prefix = self.PAGE_PREFIX + 'character/'
        self.image_list = []
        try:
            obj = self.get_json(prefix + 'chara_data.php')
            if 'charas' in obj:
                for chara in obj['charas']:
                    if 'images' in chara:
                        if 'visuals' in chara['images']:
                            for visual in chara['images']['visuals']:
                                if 'image' in visual:
                                    image_url = prefix + visual['image'].replace('./', '').split('?')[0]
                                    image_name = self.extract_image_name_from_url(image_url)
                                    self.add_to_image_list(image_name, image_url)
                        if 'faces' in chara['images']:
                            for face in chara['images']['faces']:
                                image_url = prefix + face.replace('./', '').split('?')[0]
                                image_name = self.extract_image_name_from_url(image_url)
                                self.add_to_image_list(image_name, image_url)
        except Exception as e:
            self.print_exception(e, 'Character')
        self.download_image_list(folder)


# Eiyuu Kyoushitsu
class EiyuKyoushitsuDownload(Summer2023AnimeDownload, NewsTemplate):
    title = 'Eiyuu Kyoushitsu'
    keywords = [title, 'Classroom for Heroes']
    website = 'https://eiyukyoushitsu-anime.com/'
    twitter = 'eiyu_anime'
    hashtags = ['英雄教室', 'eiyu_anime']
    folder_name = 'eiyukyoushitsu'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 8

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
            template = self.PAGE_PREFIX + 'images/story/%s/%s.jpg'
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (episode, str(j + 1).zfill(2))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.newslist li',
                                    date_select='.newstime', title_select='p', id_select='a')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.mobmw img[src]')
            self.image_list = []
            for image in images:
                if 'kv' not in image['src'].lower():
                    continue
                image_url = self.PAGE_PREFIX + image['src'][1:]
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        # template = self.PAGE_PREFIX + 'images/chara_%s.png'
        # self.download_by_template(folder, template, 2, 1, prefix='tz_')
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            images = soup.select('.chara_pre_main img[src]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')

    def download_media(self):
        folder = self.create_media_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        for page in ['tokuten', '01', '02', '03']:
            try:
                if page != 'tokuten' and page in processed:
                    continue
                page_url = self.PAGE_PREFIX + 'bd/'
                if page != '01':
                    if page.isnumeric():
                        page_url += 'bd'
                    page_url += page + '.html'
                soup = self.get_soup(page_url)
                images = soup.select('.longmob div[style*="adding-bottom"] img[src]')
                self.image_list = []
                for image in images:
                    if image['src'].startswith('../'):
                        image_url = self.PAGE_PREFIX + image['src'][3:]
                    else:
                        image_url = image['src']
                    image_url = image_url.split('?')[0]
                    if '/blu-ray/' in image_url:
                        image_name = self.generate_image_name_from_url(image_url, 'blu-ray')
                    else:
                        image_name = self.extract_image_name_from_url(image_url)
                    if 'nowprinting' in image_name:
                        continue
                    if self.is_image_exists(image_name, folder):
                        continue
                    self.add_to_image_list(image_name, image_url)
                if page.isnumeric():
                    if len(self.image_list) > 1:
                        processed.append(page)
                    elif len(self.image_list) == 0:
                        break
                self.download_image_list(folder)
            except Exception as e:
                self.print_exception(e, f'Blu-ray - {page}')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Helck
class HelckDownload(Summer2023AnimeDownload, NewsTemplate):
    title = 'Helck'
    keywords = [title]
    website = 'https://www.helck-anime.com/'
    twitter  = 'Helck_anime'
    hashtags = ['Helck', 'ヘルク']
    folder_name = 'helck'

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
            template = self.PAGE_PREFIX + 'wp/wp-content/themes/helck_v1.0.0/assets/img/story/story%s_%s.jpg'
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (episode, str(j + 1).zfill(2))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='ul.wf li', title_select='.ttl',
                                    date_select='.date', id_select='a', date_func=lambda x: x.strip()[0:10])

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('header img[src]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'][1:]
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'images/character_%s_img_f.png'
        self.download_by_template(folder, template, 2, 1)


# Higeki no Genkyou to Naru Saikyou Gedou Last Boss Joou wa Tami no Tame ni Tsukushimasu.
class LastameDownload(Summer2023AnimeDownload, NewsTemplate):
    title = 'Higeki no Genkyou to Naru Saikyou Gedou Last Boss Joou wa Tami no Tame ni Tsukushimasu.'
    keywords = [title, 'The Most Heretical Last Boss Queen: From Villainess to Savior', 'Lastame']
    website = 'https://lastame.com/'
    twitter = 'lastame_pr'
    hashtags = 'ラス為'
    folder_name = 'lastame'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_episode_preview_guess(download_valid=True)
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            stories = soup.select('.story__cnt--storyArea--linkArea a[href]')
            for i in range(len(stories)):
                try:
                    episode = str(int(stories[i].text.strip())).zfill(2)
                    if self.is_image_exists(episode + '_1'):
                        continue
                except:
                    continue
                if stories[i].has_attr('class') and 'currentLast' in stories[i]['class'] and (i == len(stories) - 1):
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(stories[i]['href'])
                if ep_soup is None:
                    continue
                self.image_list = []
                images = ep_soup.select('.js-storySwiper .swiper-slide img[src]')
                for j in range(len(images)):
                    image_url = images[j]['src']
                    if image_url.endswith('-807.jpg') or image_url.endswith('movie_thumbnail-1.jpg'):
                        break
                    image_name = episode + '_' + str(j + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.newsBox li',
                                    date_select='small', title_select='p', id_select='a',
                                    date_func=lambda x: x.replace('年', '.').replace('月', '.').replace('日', ''))

    def download_episode_preview_guess(self, print_invalid=False, download_valid=False):
        if self.is_image_exists(str(self.FINAL_EPISODE).zfill(2) + '_1'):
            return

        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'wp/wp-content/uploads/%s/%s/MAINlastame_ep%s_%s.jpg'
        current_date = datetime.now() + timedelta(hours=1)
        year = current_date.strftime('%Y')
        month = current_date.strftime('%m')
        is_successful = False
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1') or self.is_image_exists(episode + '_1', folder):
                continue
            episode_success = False
            valid_urls = []
            for j in range(self.IMAGES_PER_EPISODE):
                image_url = template % (year, month, episode, str(j + 1))
                if self.is_valid_url(image_url, is_image=True):
                    print('VALID - ' + image_url)
                    episode_success = True
                    valid_urls.append(image_url)
                elif print_invalid:
                    print('INVALID - ' + image_url)
            if download_valid and len(valid_urls) > 0:
                for valid_url in valid_urls:
                    image_name = self.extract_image_name_from_url(valid_url)
                    self.download_image(valid_url, folder + '/' + image_name)
            if not episode_success:
                break
            is_successful = True
        if is_successful:
            print(self.__class__.__name__ + ' - Guessed correctly!')
        return is_successful

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FgH9hRHVEAAZFyz?format=jpg&name=large')
        self.add_to_image_list('kv', self.PAGE_PREFIX + 'wp/wp-content/uploads/2023/04/ラス為キービジュアル.jpg')
        # self.add_to_image_list('tz_mv_pc', self.PAGE_PREFIX + 'wp/wp-content/themes/original/assets/img/mv_pc.png')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.mv__mainSlider img[src]')
            for image in images:
                image_url = image['src']
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            images = soup.select('.imageArea img[src], .thumbnailArea img[src]')
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'][1:]
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')

    def download_media(self):
        folder = self.create_media_directory()
        for page in ['store', 'bluray']:
            try:
                page_url = self.PAGE_PREFIX + page
                soup = self.get_soup(page_url)
                if page == 'store':
                    images = soup.select('.store__list--img img[src]')
                else:
                    images = soup.select('.bluray__cnt--area img[src]')
                self.image_list = []
                for image in images:
                    if image['src'].startswith('/'):
                        image_url = self.PAGE_PREFIX + image['src'][1:]
                    else:
                        image_url = image['src']
                    image_url = self.clear_resize_in_url(image_url.split('?')[0])
                    if 'bluray' in image_url:
                        image_name = self.generate_image_name_from_url(image_url, 'bluray')
                    else:
                        image_name = self.extract_image_name_from_url(image_url)
                    if 'nowprinting' in image_name:
                        continue
                    if self.is_image_exists(image_name, folder):
                        continue
                    if page == 'bluray':
                        if self.is_not_matching_content_length(image_url, '631227'):
                            self.add_to_image_list(image_name, image_url)
                    else:
                        self.add_to_image_list(image_name, image_url)
                self.download_image_list(folder)
            except Exception as e:
                self.print_exception(e, f'Blu-ray - {page}')


# Horimiya: Piece
class Horimiya2Download(Summer2023AnimeDownload, NewsTemplate):
    title = "Horimiya: Piece"
    keywords = [title]
    website = 'https://horimiya-anime.com/'
    twitter = 'horimiya_anime'
    hashtags = ['ホリミヤ', 'horimiya']
    folder_name = 'horimiya2'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        # self.download_character()
        self.download_media()

    def download_episode_preview(self):
        try:
            story_prefix = self.PAGE_PREFIX + 'story/'
            soup = self.get_soup(story_prefix)
            stories = soup.select('.p-story__tab-item')
            for story in stories:
                try:
                    episode = str(int(story.select('.p-in_num')[0].text)).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                if 'is-current' in story['class']:
                    ep_soup = soup
                else:
                    a_tag = story.select('a[href]')
                    if len(a_tag) == 0:
                        continue
                    story_url = a_tag['href']
                    if story_url.startswith('/'):
                        story_url = self.PAGE_PREFIX + story_url[1:]
                    ep_soup = self.get_soup(story_url)
                if ep_soup is None:
                    continue
                self.image_list = []
                images = ep_soup.select('.p-story__scene-item img[src]')
                for i in range(len(images)):
                    image_name = episode + '_' + str(i + 1)
                    image_url = story_prefix + images[i]['src']
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.p-news__list__item',
                                    date_select='.p-news__list__date', title_select='.p-news__list__title',
                                    id_select='p-news__list__link', a_tag_prefix=self.PAGE_PREFIX,
                                    a_tag_start_text_to_remove='/', stop_date='2021', paging_type=1,
                                    next_page_select='.c-pager__btn--next')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/Fr_j-0eWAAEq9Id?format=jpg&name=4096x4096')
        self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/Fxiu43gakAAzJP6?format=jpg&name=4096x4096')
        self.download_image_list(folder)

    def download_media(self):
        folder = self.create_media_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        for page in ['benefit', '01', '02', '03', '04', '05', '06']:
            try:
                if page != 'benefit' and page in processed:
                    continue
                page_url = self.PAGE_PREFIX + 'bddvd/' + page + '.html'
                soup = self.get_soup(page_url)
                images = soup.select('.p-bddvd img[src]')
                self.image_list = []
                for image in images:
                    if image['src'].startswith('/'):
                        image_url = self.PAGE_PREFIX + image['src'][1:]
                    else:
                        image_url = image['src']
                    image_url = image_url.split('?')[0]
                    if '/bddvd/' in image_url:
                        image_name = self.generate_image_name_from_url(image_url, 'bddvd')
                    else:
                        image_name = self.extract_image_name_from_url(image_url)
                    if image_name in ['np', 'np_mini']:
                        continue
                    if self.is_image_exists(image_name, folder):
                        continue
                    self.add_to_image_list(image_name, image_url)
                if page != 'benefit' and len(self.image_list) > 0:
                    processed.append(page)
                if page.isnumeric() and len(self.image_list) == 0:
                    break
                self.download_image_list(folder)
            except Exception as e:
                self.print_exception(e, f'Blu-ray - {page}')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Jidou Hanbaiki ni Umarekawatta Ore wa Meikyuu wo Samayou
class JihankiDownload(Summer2023AnimeDownload, NewsTemplate):
    title = 'Jidou Hanbaiki ni Umarekawatta Ore wa Meikyuu wo Samayou'
    keywords = [title, "jihanki", 'Reborn as a Vending Machine, I Now Wander the Dungeon']
    website = 'https://jihanki-anime.com/'
    twitter = 'jihanki_anime'
    hashtags = ['jihanki', '俺自販機']
    folder_name = 'jihanki'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 5

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        soup = self.download_key_visual()
        self.download_character()
        self.download_media(soup)

    def download_episode_preview(self):
        try:
            template = self.PAGE_PREFIX + 'assets/img/story/story%s_%s.jpg'
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (episode, str(j + 1).zfill(2))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        news_url = 'https://up-info.news/jihanki-anime/'
        self.download_template_news(page_prefix=news_url, article_select='.modListNews li', title_select='h3',
                                    date_select='time', id_select='a', date_separator='/', news_prefix='')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FqhSbfPaYAIYg4i?format=jpg&name=4096x4096')
        self.download_image_list(folder)

        soup = None
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            divs = soup.select('.l-jihanki-kv__inner>div[class]')
            for div in divs:
                has_visual_class = False
                for _class in div['class']:
                    if 'visual' in _class:
                        has_visual_class = True
                        break
                if not has_visual_class:
                    continue
                images = div.select('img[src]')
                for image in images:
                    image_url = self.PAGE_PREFIX + image['src'].replace('./', '')
                    if '/img/' not in image_url:
                        continue
                    image_name = self.generate_image_name_from_url(image_url, 'img')
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')
        return soup

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'assets/img/chara/img_chara%s.png'
        self.download_by_template(folder, template, 1, 1)

    def download_media(self, soup=None):
        folder = self.create_media_directory()
        try:
            if soup is None:
                soup = self.get_soup(self.PAGE_PREFIX)
        except:
            return

        try:
            images = soup.select('.p-jihanki-bd-visual__inner img[src]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'][2:]
                if '/bd/' not in image_url:
                    continue
                image_name = self.generate_image_name_from_url(image_url, 'bd')
                if self.is_image_exists(image_name, folder):
                    continue
                if self.is_not_matching_content_length(image_url, 341121):
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')

        try:
            images = soup.select('.p-jihanki-bd-media__inner img[src]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'][2:]
                image_name = self.generate_image_name_from_url(image_url, 'bd')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray Bonus')


# Jitsu wa Ore, Saikyou deshita?
class JitsuoresaikyouDownload(Summer2023AnimeDownload, NewsTemplate):
    title = 'Jitsu wa Ore, Saikyou deshita?'
    keywords = [title, 'Am I Actually the Strongest?']
    website = 'https://jitsuhaoresaikyo-anime.com/'
    twitter = 'jitsuoresaikyo'
    hashtags = '実は俺最強でした '
    folder_name = 'jitsuoresaikyo'

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
        story_url = self.PAGE_PREFIX + 'story/'
        try:
            soup = self.get_soup(story_url)
            stories = soup.select('.p-story__list-item')
            for story in stories:
                title = story.select('.p-story_card__title')
                try:
                    episode = str(int(title[0].text.split('第')[1].split('話')[0])).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                a_tag = story.select('a.p-story_card[href]')
                if len(a_tag) == 0:
                    continue
                ep_soup = self.get_soup(story_url + a_tag[0]['href'])
                if ep_soup is None:
                    continue
                self.image_list = []
                images = ep_soup.select('.p-story_in__text img[src]')
                for i in range(len(images)):
                    image_url = images[i]['src']
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.c-in-news__item',
                                    date_select='.c-in-news__item-date', title_select='.c-in-news__item-ttl',
                                    id_select='a', a_tag_prefix=self.PAGE_PREFIX, a_tag_start_text_to_remove='../')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FcBIWLTaMAA2GK6?format=jpg&name=large')
        self.add_to_image_list('top_img_main', self.PAGE_PREFIX + 'assets/img/top/img_main.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        prefix = self.PAGE_PREFIX + 'assets/img/character/img_chara-'
        templates = [prefix + 'main_%s.png', prefix + 'face_%s.png']
        self.download_by_template(folder, templates, 2, 1)

    def download_media(self):
        folder = self.create_media_directory()
        try:
            prefix = self.PAGE_PREFIX + 'bd-cd/detail/?id='
            for page_id in ['1019830', '1019833']:
                soup = self.get_soup(prefix + page_id)
                if soup is None:
                    continue
                images = soup.select('.p-disco_content img[data-src]')
                self.image_list = []
                for image in images:
                    image_url = self.PAGE_PREFIX + image['data-src'][1:]
                    if 'nowprinting' in image_url:
                        continue
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
                if len(self.image_list) == 0:
                    break
                self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e)


# Kanojo, Okarishimasu 3rd Season
class Kanokari3Download(Summer2023AnimeDownload, NewsTemplate):
    title = "Kanojo, Okarishimasu 3rd Season"
    keywords = [title, "Kanokari", "Rent-a-Girlfriend"]
    website = 'https://kanokari-official.com/'
    twitter = 'kanokari_anime'
    hashtags = ['彼女お借りします', 'かのかり', 'kanokari']
    folder_name = 'kanokari3'

    PAGE_PREFIX = website
    FIRST_EPISODE = 25
    FINAL_EPISODE = 36
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        template = self.PAGE_PREFIX + '3rd/wp-content/uploads/%s/%s/かのかり3_%s-%s.%s'
        current_date = datetime.now() + timedelta(hours=1)
        year = current_date.strftime('%Y')
        month = current_date.strftime('%m')
        for i in range(self.FIRST_EPISODE, self.FINAL_EPISODE + 1, 1):
            episode = str(i).zfill(2)
            if self.is_image_exists(episode + '_1'):
                continue
            is_success = False
            for j in range(self.IMAGES_PER_EPISODE):
                image_name = episode + '_' + str(j + 1)
                for k in ['jpg', 'png']:
                    image_url = template % (year, month, episode, str(j + 1).zfill(2), k)
                    result = self.download_image(image_url, self.base_folder + '/' + image_name)
                    if result != -1:
                        is_success = True
                        break
                if not is_success:
                    break
            if not is_success:
                break

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-item',
                                    title_select='.news-title', date_select='.news-date', id_select='a',
                                    paging_type=0, next_page_select='ul.pagenation-list li', next_page_eval_index=-1,
                                    next_page_eval_index_class='is__current')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            divs = soup.select('.firstview>div[class]')
            self.image_list = []
            for div in divs:
                has_visual_class = False
                for _class in div['class']:
                    if 'visual' in _class:
                        has_visual_class = True
                        break
                if not has_visual_class:
                    continue
                images = div.select('img[src]')
                for image in images:
                    image_url = image['src']
                    if '/images/' not in image_url:
                        continue
                    image_name = self.generate_image_name_from_url(image_url, 'images')
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

        template = self.PAGE_PREFIX + '3rd/wp-content/themes/kanokari_3rd_honban/images/kv-3rd%s.jpg'
        self.download_by_template(folder, template, 1, 4)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'chara/')
            images = soup.select('.chara-stand img[src]')
            self.image_list = []
            for image in images:
                image_url = image['src']
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')

    def download_media(self):
        folder = self.create_media_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        for page in ['store', 'vol1', 'vol2']:
            try:
                if page.startswith('vol') and page in processed:
                    continue
                page_url = self.PAGE_PREFIX + 'bd/' + page
                soup = self.get_soup(page_url)
                if page.startswith('vol'):
                    images = soup.select('.bd-container img[src]')
                else:
                    images = soup.select('.store-item img[src]')
                for image in images:
                    image_url = image['src']
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
                if page.startswith('vol'):
                    if len(self.image_list) == 0:
                        break
                    else:
                        processed.append(page)
                self.download_image_list(folder)
            except Exception as e:
                self.print_exception(e, f'Blu-ray - {page}')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Level 1 dakedo Unique Skill de Saikyou desu
class Level1Download(Summer2023AnimeDownload, NewsTemplate):
    title = 'Level 1 dakedo Unique Skill de Saikyou desu'
    keywords = [title, 'My Unique Skill Makes Me OP Even at Level 1']
    website = 'https://level1-anime.com/'
    twitter = 'level1_anime'
    hashtags = 'level1_anime'
    folder_name = 'level1'

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

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            stories = soup.select('.story-item')
            for story in stories:
                try:
                    episode = str(int(story.select('.story-num')[0].text)).zfill(2)
                except:
                    continue
                self.image_list = []
                images = story.select('.story-ss-item img[src]')
                for i in range(len(images)):
                    image_url = images[i]['src'].split('?')[0]
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-item',
                                    date_select='.date', title_select='.title', id_select='a',
                                    next_page_select='div.pagination .page-numbers',
                                    next_page_eval_index_class='current', next_page_eval_index=-1)

    def download_episode_preview_external(self):
        keywords = ['レベル１だけどユニークスキルで最強です']
        AniverseMagazineScanner(keywords, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20230706', download_id=self.download_id).run()

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FeSNHVXaYAEXR1w?format=jpg&name=medium')
        self.add_to_image_list('tz_kv-pc', self.PAGE_PREFIX + 'wp/wp-content/themes/level1_teaser/images/kv-pc.jpg')
        self.add_to_image_list('tz_kv-sp', self.PAGE_PREFIX + 'wp/wp-content/themes/level1_teaser/images/kv-sp.jpg')
        self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/FqmF5NgaIAE4lDX?format=jpg&name=4096x4096')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('.fv-slider img[src]')
            for image in images:
                image_url = image['src']
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'wp/wp-content/themes/level1_honban/images/chara-pic%s.png'
        self.download_by_template(folder, template, 1, 1)


# Lv1 Maou to One Room Yuusha
class Lv1RoomDownload(Summer2023AnimeDownload, NewsTemplate2):
    title = 'Lv1 Maou to One Room Yuusha'
    keywords = [title, 'Level 1 Demon Lord and One Room Hero']
    website = 'https://lv1room.com/'
    twitter = 'Lv1room'
    hashtags = 'lv1room'
    folder_name = 'lv1room'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_external()
        self.download_news()
        self.download_episode_preview_guess()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/01.html')
            trs = soup.select('#ContentsListUnit02 tr[class]')
            for tr in trs:
                a_tags = tr.select('a[href]')
                if len(a_tags) == 0:
                    continue
                try:
                    episode = str(int(a_tags[0].text.replace('#', ''))).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                if episode == '01':
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(self.PAGE_PREFIX + a_tags[0]['href'].replace('../', ''))
                if ep_soup is None:
                    continue
                self.image_list = []
                images = ep_soup.select('.block.line_01 img[src]')
                for i in range(len(images)):
                    image_url = self.PAGE_PREFIX + images[i]['src'].split('?')[0].replace('../', '').replace('sn_', '')
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_external(self):
        keywords = ['Lv1魔王とワンルーム勇者']
        AniverseMagazineScanner(keywords, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20230602', download_id=self.download_id).run()

    def download_episode_preview_guess(self):
        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'core_sys/images/contents/%s/block/%s/%s.jpg'
        is_successful = False
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1'):
                continue
            is_success = False
            first = 13 + i
            second = 16 + 3 * i
            third = 29 + 6 * i
            for j in range(self.IMAGES_PER_EPISODE):
                image_url = template % (str(first).zfill(8), str(second).zfill(8), str(third + j).zfill(8))
                # if not self.is_content_length_in_range(image_url, more_than_amount=7000):
                #     break
                image_name = episode + '_' + str(j + 1)
                result = self.download_image(image_url, folder + '/' + image_name)
                if result == 0:
                    is_success = True
                    is_successful = True
                elif result == -1:
                    break
            if is_success:
                print(self.__class__.__name__ + ' - Guessed successfully!')
            else:
                if len(os.listdir(folder)) == 0:
                    os.rmdir(folder)
                return
        if len(os.listdir(folder)) == 0:
            os.rmdir(folder)
        return is_successful

    def download_news(self):
        self.download_template_news(self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_kv', self.PAGE_PREFIX + 'core_sys/images/main/tz/kv.webp')
        self.add_to_image_list('tz_kv2', self.PAGE_PREFIX + 'core_sys/images/main/tz/kv2.webp')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.kv__img source[srcset]')
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
                    images = chara_soup.select('.chara img[src]')
                    for image in images:
                        image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
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
                page_url = self.PAGE_PREFIX + 'bddvd/'
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
                    if page.isnumeric() and not self.is_content_length_in_range(image_url, more_than_amount=10000):
                        continue
                    self.add_to_image_list(image_name, image_url)
                if not page.isnumeric() or len(self.image_list) > 2:
                    processed.append(page)
                self.download_image_list(folder)
            except Exception as e:
                self.print_exception(e, f'Blu-ray - {page}')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Liar Liar
class LiarLiarDownload(Summer2023AnimeDownload, NewsTemplate):
    title = 'Liar Liar'
    keywords = [title]
    website = 'https://liar-liar-anime.com/'
    twitter = 'liar2_official'
    hashtags = ['ライアー・ライアー', 'ライアラ']
    folder_name = 'liarliar'

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
            a_tags = soup.select('.music_links_story a[href][class]')
            for a_tag in a_tags:
                try:
                    episode = str(int(a_tag.text)).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                if 'current' in a_tag['class']:
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(a_tag['href'])
                if ep_soup is None:
                    continue
                self.image_list = []
                images = ep_soup.select('.story_thumbs img[src]')
                for i in range(len(images)):
                    image_url = self.PAGE_PREFIX + images[i]['src'][1:]
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        # Paging logic may need update
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.archives_ul_li',
                                    date_select='.archives_ul_li_date', title_select='.archives_ul_li_text',
                                    id_select='a', date_separator='/')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/Fhu9_4VUYAAz0MW?format=jpg&name=4096x4096')
        self.add_to_image_list('kv', self.PAGE_PREFIX + 'common/media/24d9f99eea98f74d6add5b03db11dcd9.jpg')
        self.download_image_list(folder)

        prefix = self.PAGE_PREFIX + 'common/images/contents_top_fv_stand%s'
        templates = [prefix + '.jpg', prefix + 'b.jpg']
        self.download_by_template(folder, templates, 2, 1, prefix='tz_')

    def download_character(self):
        folder = self.create_character_directory()
        prefix = self.PAGE_PREFIX + 'common/images/contents_character_'
        prefix2 = self.PAGE_PREFIX + 'common/images/contents_character02_'
        prefix3 = self.PAGE_PREFIX + 'common/images/contents_character03_'
        templates = [prefix + 'stand%s.png', prefix + 'face%s.png']
        templates2 = [prefix2 + 'stand%s.png', prefix2 + 'face%s.png']
        templates3 = [prefix3 + 'stand%s.png', prefix3 + 'face%s.png']
        self.download_by_template(folder, templates, 2, 1)
        self.download_by_template(folder, templates2, 2, 1)
        self.download_by_template(folder, templates3, 2, 1)


# Masamune-kun no Revenge R
class Masamunekun2Download(Summer2023AnimeDownload, NewsTemplate):
    title = 'Masamune-kun no Revenge R'
    keywords = [title, "Masamune's Revenge", "2nd"]
    website = 'https://masamune-tv.com/'
    twitter = 'masamune_tv'
    hashtags = ['MASA_A']
    folder_name = 'masamune2'

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
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            stories = soup.select('.story nav a[href]')
            for story in stories:
                try:
                    episode = str(int(story.text)).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                ep_soup = self.get_soup(story['href'])
                if ep_soup is None:
                    continue
                self.image_list = []
                images = ep_soup.select('.story img[src]')
                for i in range(len(images)):
                    image_url = images[i]['src']
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.md-news__archive article',
                                    date_select='.date', title_select='.ttl', id_select='a',
                                    next_page_select='.item-next__link')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        # self.image_list = []
        # self.add_to_image_list('tz_kv', self.PAGE_PREFIX + '_assets/images/fv/fv@2x.png')
        # self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.fv--img__slider source[srcset]')
            for image in images:
                image_url = image['srcset']
                if '_sp' in image_url:
                    continue
                if image_url.startswith('/'):
                    image_url = self.PAGE_PREFIX + image_url[1:]
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('.chardata img[src]')
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'][1:]
                image_name = 'tz_' + self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')

    def download_media(self):
        folder = self.create_media_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        for page in ['vol1', 'vol2']:
            try:
                if page in processed:
                    continue
                page_url = self.PAGE_PREFIX + 'bd/'
                if page != 'vol1':
                    page_url += page + '/'
                soup = self.get_soup(page_url)
                images = soup.select('#Bd img[src]')
                for image in images:
                    image_url = self.clear_resize_in_url(image['src'].replace('-scaled-1', '').replace('-scaled', ''))
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
                if len(self.image_list) == 0:
                    break
                else:
                    processed.append(page)
                self.download_image_list(folder)
            except Exception as e:
                self.print_exception(e, f'Blu-ray - {page}')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Mushoku Tensei II: Isekai Ittara Honki Dasu
class MushokuTensei2Download(Summer2023AnimeDownload, NewsTemplate):
    title = "Mushoku Tensei: Isekai Ittara Honki Dasu II"
    keywords = [title, 'Jobless Reincarnation']
    website = 'https://mushokutensei.jp/'
    twitter = 'mushokutensei_A'
    hashtags = ['無職転生', 'MushokuTensei']
    folder_name = 'mushoku-tensei2'

    PAGE_PREFIX = website
    FINAL_EPISODE = 24
    IMAGES_PER_EPISODE = 5

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
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            stories = soup.select('#js_2nd a.storyarea[href]')
            for story in stories:
                try:
                    episode = str(int(story.select('.storyarea_ttl span')[0].text.replace('#', ''))).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                ep_soup = self.get_soup(story['href'])
                if ep_soup is None:
                    continue
                self.image_list = []
                images = ep_soup.select('.storycontents_subimg_img[data-imgload]')
                for i in range(len(images)):
                    image_url = images[i]['data-imgload']
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_guess(self, print_invalid=False, download_valid=False):
        if self.is_image_exists(str(self.FINAL_EPISODE).zfill(2) + '_1'):
            return

        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'wp-content/uploads/%s/%s/ep%s_%s.jpg'
        current_date = datetime.now() + timedelta(hours=1)
        year = current_date.strftime('%Y')
        month = current_date.strftime('%m')
        is_successful = False
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1') or self.is_image_exists('ep' + episode + '_1', folder):
                continue
            episode_success = False
            valid_urls = []
            for j in range(self.IMAGES_PER_EPISODE):
                image_url = template % (year, month, episode, str(j + 1))
                if self.is_valid_url(image_url, is_image=True):
                    print('VALID - ' + image_url)
                    episode_success = True
                    valid_urls.append(image_url)
                elif print_invalid:
                    print('INVALID - ' + image_url)
            if download_valid and len(valid_urls) > 0:
                for valid_url in valid_urls:
                    image_name = self.extract_image_name_from_url(valid_url)
                    self.download_image(valid_url, folder + '/' + image_name)
            if not episode_success:
                break
            is_successful = True
        if is_successful:
            print(self.__class__.__name__ + ' - Guessed correctly!')
        return is_successful

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.l_news li',
                                    date_select='.news_date', title_select='.news_ttl',
                                    id_select='a', stop_date='2022.03.02')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        template = self.PAGE_PREFIX + 'wp-content/themes/mushoku_re/img/index/img_hero%s.jpg'
        self.download_by_template(folder, template, 2, 10)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            self.image_list = []
            images = soup.select('#js_charaslide_2nd .charaslide_img[data-imgload], '
                                 + '#js_charaslide_2nd .charaslide_data_img[data-imgload]')
            for image in images:
                image_url = image['data-imgload']
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Nanatsu no Maken ga Shihai suru
class NanatsumaDownload(Summer2023AnimeDownload, NewsTemplate4):
    title = 'Nanatsu no Maken ga Shihai suru'
    keywords = [title, 'Reign of the Seven Spellblades']
    website = 'https://nanatsuma-pr.com/'
    twitter = 'nanatsuma_pr'
    hashtags = ['nanatsuma', 'ななつま']
    folder_name = 'nanatsuma'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        init_json = self.download_episode_preview()
        self.download_news(init_json)
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self, print_http_error=False):
        try:
            init_json = self.get_json(self.PAGE_PREFIX + 'wp-json/ssd/init')
            for story in init_json['stories']:
                episode = story['episode']
                if self.is_image_exists(episode + '_1'):
                    continue
                self.image_list = []
                for i in range(len(story['images'])):
                    image = story['images'][i]
                    image_url = image['image_path']
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
            return init_json
        except HTTPError:
            if print_http_error:
                print(self.__class__.__name__ + ' - 403 Error when retrieving story API.')
        except Exception as e:
            self.print_exception(e)
        return None

    def download_news(self, json_obj=None):
        self.download_template_news('ssd', json_obj=json_obj)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/FqyTIkYaAAUAKWT?format=jpg&name=large')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            divs = soup.select('main div[class]')
            for div in divs:
                has_visual_class = False
                for _class in div['class']:
                    if 'visual' in _class.lower():
                        has_visual_class = True
                        break
                if not has_visual_class:
                    continue
                images = div.select('picture *[srcset]')
                for image in images:
                    image_url = self.PAGE_PREFIX + image['srcset'][1:]
                    if '/static/' not in image_url:
                        continue
                    image_name = self.generate_image_name_from_url(image_url, 'static')
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        prefix = self.PAGE_PREFIX + 'wp/wp-content/themes/ssd/static/character/'
        for i in range(30):
            num = str(i + 1).zfill(2)
            if self.is_image_exists(num + '_full', folder) and self.is_image_exists(num + '_close_01', folder):
                continue
            chara_prefix = prefix + num + '/'
            full_name = num + '_full'
            result = self.download_image(chara_prefix + 'full.png', folder + '/' + full_name)
            if result == -1:
                break
            template = chara_prefix + 'close/%s.png'
            for j in range(3):
                close_url = template % str(j + 1).zfill(2)
                close_name = num + '_close_' + str(j + 1).zfill(2)
                result2 = self.download_image(close_url, folder + '/' + close_name)
                if result2 == -1:
                    break


# Okashi na Tensei
class OkashinaTenseiDownload(Summer2023AnimeDownload, NewsTemplate4):
    title = 'Okashi na Tensei'
    keywords = [title, 'Sweet Reincarnation']
    website = 'https://okashinatensei-pr.com/'
    twitter = 'okashinatensei'
    hashtags = 'おかしな転生'
    folder_name = 'okashinatensei'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        json_obj = self.download_episode_preview()
        self.download_news(json_obj=json_obj)
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self, print_http_error=False):
        try:
            init_json = self.get_json(self.PAGE_PREFIX + 'wp-json/okashinatensei/init')
            for story in init_json['stories']:
                episode = story['episode']
                if self.is_image_exists(episode + '_1'):
                    continue
                self.image_list = []
                for i in range(len(story['images'])):
                    image = story['images'][i]
                    image_url = image['image_path']
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
            return init_json
        except HTTPError:
            if print_http_error:
                print(self.__class__.__name__ + ' - 403 Error when retrieving story API.')
        except Exception as e:
            self.print_exception(e)
        return None

    def download_news(self, json_obj=None):
        self.download_template_news('okashinatensei', json_obj=json_obj)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        # self.image_list = []
        # self.add_to_image_list('tz_natalie', 'https://ogre.natalie.mu/media/news/comic/2022/1215/okashinatensei_teaser.jpg')
        # self.download_image_list(folder)

        static_url = self.PAGE_PREFIX + 'wp/wp-content/themes/okashinatensei/static/'
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            scripts = soup.select('script[src*="pages/index-"]')
            if len(scripts) > 0:
                js_url = scripts[0]['src']
                if js_url.startswith('/'):
                    js_url = self.PAGE_PREFIX + js_url[1:]
                js_page = self.get_response(js_url)
                split1 = js_page.split('"mainvisual/')
                self.image_list = []
                for i in range(1, len(split1), 1):
                    s = split1[i].split('"')[0]
                    if len(s) == 0 or not s.endswith('.webp') or s == 'copy.webp' or 'switch_icon' in s:
                        continue
                    image_url = static_url + 'mainvisual/' + s
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'wp/wp-content/themes/okashinatensei/static/character/%s/main.png'
        for i in range(10):
            number = str(i + 1).zfill(2)
            image_name = 'tz_char' + number
            if self.is_image_exists(image_name, folder):
                continue
            image_url = template % number
            result = self.download_image(image_url, folder + '/' + image_name)
            if result == -1:
                break


# Ryza no Atelier: Tokoyami no Joou to Himitsu no Kakurega
class AtelierRyzaDownload(Summer2023AnimeDownload, NewsTemplate):
    title = 'Ryza no Atelier: Tokoyami no Joou to Himitsu no Kakurega'
    keywords = [title, 'Atelier Ryza: Ever Darkness & the Secret Hideout']
    website = 'https://ar-anime.com/'
    twitter = 'Ryza_PR'
    hashtags = 'ライザのアトリエ'
    folder_name = 'atelier-ryza'

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
        self.download_media()

    def download_episode_preview(self):
        story_url = self.PAGE_PREFIX + 'story/'
        try:
            soup = self.get_soup(story_url)
            story_list = soup.select('.tab_list')
            if len(story_list) > 0:
                lis = story_list[0].select('li')
                for li in lis:
                    p_tag = li.select('p')
                    try:
                        ep_num = int(p_tag[0].text)
                        if ep_num is None or ep_num < 1:
                            continue
                        episode = str(ep_num).zfill(2)
                    except:
                        continue
                    if self.is_image_exists(episode + '_1'):
                        continue
                    if li.has_attr('class') and 'is-current' in li['class']:
                        ep_soup = soup
                    else:
                        a_tag = li.select('a[href]')
                        if len(a_tag) == 0:
                            continue
                        ep_soup = self.get_soup(story_url + a_tag[0]['href'].replace('./', ''))
                    if ep_soup is not None:
                        images = ep_soup.select('.swiper-wrapper img[src]')
                        self.image_list = []
                        for i in range(len(images)):
                            image_url = story_url + images[i]['src']
                            image_name = episode + '_' + str(i + 1)
                            self.add_to_image_list(image_name, image_url)
                        self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.p-news_in__content-list-item',
                                    date_select='.p-in-data', title_select='.p-in-title',
                                    id_select='a', a_tag_start_text_to_remove='/', a_tag_prefix=self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz', self.PAGE_PREFIX + 'news/SYS/CONTENTS/afaf78fb-2da9-4a38-85e8-36282052d381')
        self.add_to_image_list('kv', self.PAGE_PREFIX + 'assets/img/top/kv.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        self.download_by_template(folder, self.PAGE_PREFIX + 'assets/img/character/chara_%s.png', 2, 1)

    def download_media(self):
        folder = self.create_media_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        for page in ['special', '01', '02', '03', '04', '05', '06']:
            try:
                if page != 'special' and page in processed:
                    continue
                page_url = self.PAGE_PREFIX + 'bddvd/' + page + '.html'
                soup = self.get_soup(page_url)
                images = soup.select('.p-bddvd__content>section img[src]')
                for image in images:
                    image_url = self.PAGE_PREFIX + image['src'].replace('../', '').split('?')[0]
                    if 'np.jpg' in image_url:
                        continue
                    if '/bddvd/' in image_url:
                        image_name = self.generate_image_name_from_url(image_url, 'bddvd')
                    else:
                        continue
                    if self.is_image_exists(image_name, folder):
                        continue
                    self.add_to_image_list(image_name, image_url)
                if page.isnumeric():
                    if len(self.image_list) == 0:
                        break
                    else:
                        processed.append(page)
                self.download_image_list(folder)
            except Exception as e:
                self.print_exception(e, f'Blu-ray - {page}')
        self.create_cache_file(cache_filepath, processed, num_processed)

        special_folder = folder + '/special'
        if not os.path.exists(special_folder):
            os.makedirs(special_folder)
        template = self.PAGE_PREFIX + 'assets/img/special/illust/illust_%s.jpg'
        self.download_by_template(special_folder, template, 2, 1)


# Seija Musou: Salaryman, Isekai de Ikinokoru Tame ni Ayumu Michi
class SeijaMusouDownload(Summer2023AnimeDownload, NewsTemplate):
    title = 'Seija Musou: Salaryman, Isekai de Ikinokoru Tame ni Ayumu Michi'
    keywords = [title, 'The Great Cleric']
    website = 'https://www.tbs.co.jp/anime/seija/'
    twitter = 'seija_anime'
    hashtags = '聖者無双'
    folder_name = 'seijamusou'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        try:
            template = self.PAGE_PREFIX + 'story/img/story%s/%s.jpg'
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (episode, str(j + 1).zfill(2))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news/'
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.newsall-box',
                                    date_select='.newsall-date', title_select='.newsall-text',
                                    id_select='a', a_tag_prefix=news_url)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FpJpjE6acAEXVFF?format=jpg&name=large')
        self.add_to_image_list('kv_tw', 'https://pbs.twimg.com/media/FwUYw_PaMAA8jF0?format=jpg&name=4096x4096')
        self.add_to_image_list('topimg_key@2x', self.PAGE_PREFIX + 'img/topimg_key@2x.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'img/chara_img_%s@2x.png'
        self.download_by_template(folder, template, 2, 1)


# Shinigami Bocchan to Kuro Maid S2
class ShinigamiBocchan2Download(Summer2023AnimeDownload, NewsTemplate2):
    title = 'Shinigami Bocchan to Kuro Maid 2nd Season'
    keywords = [title, 'The Duke of Death and His Maid']
    website = 'https://bocchan-anime.com/'
    twitter = 'bocchan_anime'
    hashtags = '死神坊ちゃん'
    folder_name = 'shinigami-bocchan2'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_news(self):
        self.download_template_news(self.PAGE_PREFIX, stop_date='2022.05.13')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        sub_folder = self.create_custom_directory(folder.split('/')[-1] + '/news')
        cache_filepath = sub_folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'news/', decode=True)
            while True:
                stop = False
                items = soup.select('#list_01 .bg_a, #list_01 .bg_b')
                for item in items:
                    date = item.select('.day')
                    if len(date) == 0 or date[0].text.startswith('2022'):
                        stop = True
                        break
                    a_tag = item.select('a[href]')
                    if len(a_tag) == 0:
                        continue
                    if not a_tag[0]['href'].startswith('../') or '/news/' not in a_tag[0]['href'] \
                            or not a_tag[0]['href'].endswith('.html'):
                        continue
                    page_name = a_tag[0]['href'].split('/')[-1].split('.html')[0]
                    if page_name in processed:
                        stop = True
                        break
                    title = a_tag[0].text.strip()
                    if 'ビジュアル' in title:
                        news_soup = self.get_soup(self.PAGE_PREFIX + a_tag[0]['href'].replace('../', ''))
                        if news_soup is not None:
                            images = news_soup.select('#news_block img[src]')
                            self.image_list = []
                            for image in images:
                                image_url = self.PAGE_PREFIX + image['src'].replace('../', '').split('?')[0]
                                if '/news/' not in image_url:
                                    continue
                                image_name = self.generate_image_name_from_url(image_url, 'news') \
                                    .replace('_block_', '_')
                                self.add_to_image_list(image_name, image_url)
                            self.download_image_list(sub_folder)
                    processed.append(page_name)
                if stop:
                    break
                next_page = soup.select('.nb_nex a[href]')
                if len(next_page) == 0:
                    break
                soup = self.get_soup(self.PAGE_PREFIX + next_page[0]['href'].replace('../', ''))
        except Exception as e:
            self.print_exception(e, 'Key Visual News')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Shiro Seijo to Kuro Bokushi
class ShiroSeijoDownload(Summer2023AnimeDownload, NewsTemplate):
    title = 'Shiro Seijo to Kuro Bokushi'
    keywords = [title, "Saint Cecilia and Pastor Lawrence", 'shiroseijyo']
    website = 'https://shiroseijyo-anime.com/'
    twitter = 'shiroseijyo_tv'
    hashtags = '白聖女と黒牧師'
    folder_name = 'shiroseijyo'

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
        self.has_website_updated(self.PAGE_PREFIX)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='li.newsList',
                                    date_select='.newsList__date', title_select='.newsList__title span', id_select='a',
                                    a_tag_prefix=self.PAGE_PREFIX + 'news/')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FdZsEiyWYAA1hfB?format=jpg&name=4096x4096')
        self.add_to_image_list('top_mv_character', self.PAGE_PREFIX + 'assets/img/top/mv_character.png')
        self.add_to_image_list('kv_tw', 'https://pbs.twimg.com/media/Fj7f8HNUUAASOrr?format=jpg&name=4096x4096')
        self.add_to_image_list('top_mv2_character', self.PAGE_PREFIX + 'assets/img/top/mv2_character.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.characterList img[src]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'][2:]
                image_name = self.generate_image_name_from_url(image_url, 'img')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')

    def download_media(self):
        folder = self.create_media_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        bd_prefix = self.PAGE_PREFIX + 'bddvd/'
        for page in ['tokuten', 'vol1', 'vol2', 'vol3']:
            try:
                if page != 'tokuten' and page in processed:
                    continue
                bd_url = bd_prefix
                if page != 'vol1':
                    bd_url += page + '.html'
                soup = self.get_soup(bd_url)
                images = soup.select('.bddvdArtile img[src]')
                self.image_list = []
                for image in images:
                    image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                    if '/bddvd/' in image_url:
                        image_name = self.generate_image_name_from_url(image_url, 'bddvd')
                    else:
                        image_name = self.extract_image_name_from_url(image_url)
                    if 'nowpri' in image_name:
                        continue
                    if self.is_image_exists(image_name, folder):
                        continue
                    self.add_to_image_list(image_name, image_url)
                if page.startswith('vol'):
                    if len(self.image_list) == 0:
                        break
                    else:
                        processed.append(page)
                self.download_image_list(folder)
            except Exception as e:
                self.print_exception(e, f'Blu-ray - {page}')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Suki na Ko ga Megane wo Wasureta
class SukimegaDownload(Summer2023AnimeDownload, NewsTemplate):
    title = 'Suki na Ko ga Megane wo Wasureta'
    keywrods = [title, 'The Girl I Like Forgot Her Glasses']
    website = 'https://anime.shochiku.co.jp/sukimega/'
    twitter = 'Sukimega'
    hashtags = '好きめが'
    folder_name = 'sukimega'

    PAGE_PREFIX = website
    FINAL_EPISODE = 13

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
            soup = self.get_soup(self.PAGE_PREFIX + 'story')
            a_tags = soup.select('a.skmg_page_story_tabs_item[href]')
            for a_tag in a_tags:
                try:
                    episode = str(int(a_tag.text)).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                if 'current' in a_tag['class']:
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(a_tag['href'])
                if ep_soup is None:
                    continue
                self.image_list = []
                images = ep_soup.select('.story_thumbs img[src]')
                for i in range(len(images)):
                    image_url = images[i]['src']
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_external(self):
        keywords = ['好きな子がめがねを忘れた']
        AniverseMagazineScanner(keywords, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20230627', download_id=self.download_id).run()

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='section .list_item',
                                    date_select='.date', title_select='.title', id_select='a')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('kv_tw', 'https://pbs.twimg.com/media/FrLPIEiakAA_j0O?format=jpg&name=4096x4096')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.skmg_top_fv_kv_box_item_image img[src]')
            self.image_list = []
            for image in images:
                image_url = image['src']
                if '/images/' not in image_url:
                    continue
                image_name = self.generate_image_name_from_url(image_url, 'images')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e)

    def download_media(self):
        folder = self.create_media_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        for page in ['store_benefits', '1', '2', '3']:
            try:
                if page.isnumeric() and page in processed:
                    continue
                page_url = self.PAGE_PREFIX + 'blu-ray/'
                if page.isnumeric():
                    page_url += 'volume'
                page_url += page
                soup = self.get_soup(page_url)
                if page.isnumeric():
                    images = soup.select('.skmg_page_bluray_body_rl1_left img[src]')
                else:
                    images = soup.select('.skmg_page_bluray_body_rl2_left img[src],.bluray_multi_images_body img[src]')
                self.image_list = []
                for image in images:
                    image_url = image['src'].split('?')[0]
                    if image_url.endswith('sample02.png'):
                        continue
                    if '/images/' not in image_url:
                        continue
                    image_name = self.generate_image_name_from_url(image_url, 'images')
                    self.add_to_image_list(image_name, image_url)
                if page.isnumeric() and len(self.image_list) > 0:
                    processed.append(page)
                self.download_image_list(folder)
            except Exception as e:
                self.print_exception(e, f'Blu-ray - {page}')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Temple
class TempleDownload(Summer2023AnimeDownload, NewsTemplate):
    title = 'Temple'
    keywords = [title, 'TenPuru: No One Can Live on Loneliness']
    website = 'https://temple-anime.com/'
    twitter = 'temple_tvanime'
    hashtags = ['てんぷる', 'Tenpuru_anime']
    folder_name = 'temple'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

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
            template = self.PAGE_PREFIX + 'assets/images/story/%s_%s.jpg'
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (episode, str(j + 1).zfill(2))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='#news article',
                                    date_select='time', title_select='h3', id_select=None, id_has_id=True)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/FmrextbacAMbNvi?format=jpg&name=large')
        self.add_to_image_list('mainimg', self.PAGE_PREFIX + 'images/mainimg.jpg')
        self.add_to_image_list('img_story', self.PAGE_PREFIX + 'images/img_story.jpg')
        self.download_image_list(folder)

        image_prefix = self.PAGE_PREFIX + 'assets/'
        css_url = image_prefix + 'css/style.min.css'
        try:
            self.image_list = []
            css_page = self.get_response(css_url)
            search_text = '.mainimg{background:url('
            split1 = css_page.split(search_text)
            for i in range(1, len(split1), 1):
                right_idx = split1[i].find(')')
                if right_idx > 0:
                    image_url = split1[i][0:right_idx]
                    if image_url.startswith('../'):
                        image_url = image_prefix + image_url[3:]
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        prefix = self.PAGE_PREFIX + 'assets/images/character/'
        templates = [
            prefix + 'img_%s.png',
            prefix + 'face_%s.png'
        ]
        self.download_by_template(folder, templates, 2, 1)

    def download_media(self):
        folder = self.create_media_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'blu-ray/')
            self.image_list = []
            images = soup.select('.image img[src]')
            for image in images:
                image_url = image['src']
                if 'nowprinting' in image_url:
                    continue
                if image_url.startswith('../'):
                    image_url = self.PAGE_PREFIX + image_url[3:]
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


# Uchi no Kaisha no Chiisai Senpai no Hanashi
class ChiisaiSenpaiDownload(Summer2023AnimeDownload, NewsTemplate):
    title = 'Uchi no Kaisha no Chiisai Senpai no Hanashi'
    keywords = [title]
    website = 'https://chiisaisenpai.com/'
    twitter = 'smallsenpai_pr'
    hashtags = 'うちの会社の小さい先輩の話'
    folder_name = 'chiisaisenpai'

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
        self.download_media()

    def download_episode_preview(self):
        story_url = self.PAGE_PREFIX + 'story/ep01'
        try:
            soup = self.get_soup(story_url)
            a_tags = soup.select('.elementor-button-wrapper a[href]')
            for a_tag in a_tags:
                span_tag = a_tag.select('.elementor-button-text')
                try:
                    ep_num = int(span_tag[0].text)
                    if ep_num is None or ep_num < 1:
                        continue
                    episode = str(ep_num).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                if episode == '01':
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(a_tag['href'])
                if ep_soup is not None:
                    images = ep_soup.select('img[src].swiper-slide-image')
                    self.image_list = []
                    for i in range(len(images)):
                        image_url = self.clear_resize_in_url(images[i]['src'])
                        image_name = episode + '_' + str(i + 1)
                        self.add_to_image_list(image_name, image_url)
                    self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_guess(self, print_invalid=False, download_valid=False):
        if self.is_image_exists(str(self.FINAL_EPISODE).zfill(2) + '_1'):
            return

        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'wp-content/uploads/%s/%s/ep%s-%s-1.jpg'
        current_date = datetime.now() + timedelta(hours=1)
        year = current_date.strftime('%Y')
        month = current_date.strftime('%m')
        is_successful = False
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1') or self.is_image_exists(episode + '_1', folder):
                continue
            episode_success = False
            valid_urls = []
            for j in range(self.IMAGES_PER_EPISODE):
                image_url = template % (year, month, episode, str(j + 1))
                if self.is_valid_url(image_url, is_image=True):
                    print('VALID - ' + image_url)
                    episode_success = True
                    valid_urls.append(image_url)
                elif print_invalid:
                    print('INVALID - ' + image_url)
            if download_valid and len(valid_urls) > 0:
                for valid_url in valid_urls:
                    image_name = self.extract_image_name_from_url(valid_url)
                    self.download_image(valid_url, folder + '/' + image_name)
            if not episode_success:
                break
            is_successful = True
        if is_successful:
            print(self.__class__.__name__ + ' - Guessed correctly!')
        return is_successful

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, date_separator='-',
                                    article_select='.jet-listing-grid__item[data-post-id]',
                                    date_select='.elementor-heading-title', title_select='a', id_select='a')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        css_prefix = self.PAGE_PREFIX + 'wp-content/uploads/elementor/css/post-'
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            elements = soup.select('#tpca_front_page .plus-slide-content .elementor[data-elementor-id]')
            for element in elements:
                element_id = element['data-elementor-id']
                css_response = self.get_response(css_prefix + element_id + '.css', decode=True)
                split1 = css_response.split('background-image:url("')
                image_urls = []
                for i in range(1, len(split1), 1):
                    image_urls.append(split1[i].split('"')[0].replace('-scaled', ''))
                for image_url in image_urls:
                    if not image_url.startswith(self.PAGE_PREFIX):
                        continue
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

        # self.image_list = []
        # self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FrY-UPcaAAAxGJO?format=jpg&name=medium')
        # self.add_to_image_list('PC-フロントビュー-1', self.PAGE_PREFIX + 'wp-content/uploads/2023/03/PC-フロントビュー-1.jpg')
        # self.add_to_image_list('SP-フロントビュー-1', self.PAGE_PREFIX + 'wp-content/uploads/2023/03/SP-フロントビュー-1.jpg')
        # self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('#character img[src]')
            for image in images:
                image_url = self.clear_resize_in_url(image['src'])
                image_name = self.extract_image_name_from_url(image_url)
                if image_name.startswith('cv'):
                    continue
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')

    def download_media(self):
        folder = self.create_media_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        for page in ['store', 'vol1', 'vol2', 'vol3', 'vol4']:
            try:
                if page.startswith('vol') and page in processed:
                    continue
                page_url = self.PAGE_PREFIX + 'blu-ray/' + page + '/'
                soup = self.get_soup(page_url)
                if page.startswith('vol'):
                    images = soup.select('.elementor-container img[src].attachment-large, img[src].swiper-slide-image')
                else:
                    images = soup.select('.jet-listing-grid figure img[src]')
                self.image_list = []
                for image in images:
                    image_url = self.clear_resize_in_url(image['src'].split('?')[0])
                    image_name = self.extract_image_name_from_url(image_url)
                    if image_name.startswith('Frame-') or '/2023/03/' in image_url:
                        continue
                    if self.is_image_exists(image_name, folder):
                        continue
                    self.add_to_image_list(image_name, image_url)
                if page.startswith('vol') and len(self.image_list) > 0:
                    processed.append(page)
                if page.startswith('vol') and len(self.image_list) == 0:
                    break
                self.download_image_list(folder)
            except Exception as e:
                self.print_exception(e, f'Blu-ray - {page}')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Watashi no Shiawase na Kekkon
class WatakonDownload(Summer2023AnimeDownload, NewsTemplate):
    title = 'Watashi no Shiawase na Kekkon'
    keywords = [title, 'My Happy Marriage', 'watakon']
    website = 'https://watakon-anime.com/'
    twitter = 'watashino_info'
    hashtags = ['watakon', 'わたしの幸せな結婚']
    folder_name = 'watakon'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_episode_preview_guess(download_valid=True)
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            stories = soup.select('.index-Story_Content')
            for story in stories:
                try:
                    episode = str(int(self.convert_kanji_to_number(
                        story.select('span.num')[0].text.replace('第', '').replace('話', '')))).zfill(2)
                except:
                    continue
                self.image_list = []
                images = story.select('.swiper-slide img[src]')
                for i in range(len(images)):
                    image_url = self.PAGE_PREFIX + images[i]['src'][1:]
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news_List li.item',
                                    date_select='span.time', title_select='.ttl', id_select='a',
                                    date_func=lambda x: x[0:4] + '.' + x[4:6] + '.' + x[6:8],
                                    next_page_select='.nextpostslink')

    def download_episode_preview_guess(self, print_invalid=False, download_valid=False):
        if self.is_image_exists(str(self.FINAL_EPISODE).zfill(2) + '_1'):
            return

        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'wp-content/uploads/%s/%s/img_story_%s_%s.jpg'
        current_date = datetime.now() + timedelta(hours=1)
        year = current_date.strftime('%Y')
        month = current_date.strftime('%m')
        is_successful = False
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1') or self.is_image_exists(episode + '_1', folder):
                continue
            episode_success = False
            valid_urls = []
            for j in range(self.IMAGES_PER_EPISODE):
                image_url = template % (year, month, episode, str(j + 1).zfill(2))
                if self.is_valid_url(image_url, is_image=True):
                    print('VALID - ' + image_url)
                    episode_success = True
                    valid_urls.append(image_url)
                elif print_invalid:
                    print('INVALID - ' + image_url)
            if download_valid and len(valid_urls) > 0:
                for valid_url in valid_urls:
                    image_name = self.extract_image_name_from_url(valid_url)
                    self.download_image(valid_url, folder + '/' + image_name)
            if not episode_success:
                break
            is_successful = True
        if is_successful:
            print(self.__class__.__name__ + ' - Guessed correctly!')
        return is_successful

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('.modal-KV_Img img[src]')
            for image in images:
                if '/index/' in image['src']:
                    image_url = image['src'].split('?')[0]
                    image_name = self.generate_image_name_from_url(image_url, 'index')
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
            a_tags = soup.select('.character-List li>a[href]')
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
                    images = chara_soup.select('.character_Content .visual img[src]')
                    for image in images:
                        image_url = image['src']
                        image_name = self.extract_image_name_from_url(image_url)
                        self.add_to_image_list(image_name, image_url)
                    if len(self.image_list) > 0:
                        processed.append(chara_name)
                    self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Yumemiru Danshi wa Genjitsushugisha
class YumemiruDanshiDownload(Summer2023AnimeDownload, NewsTemplate):
    title = 'Yumemiru Danshi wa Genjitsushugisha'
    keywords = [title]
    website = 'https://yumemirudanshi.com/'
    twitter = 'yumemiru_anime'
    hashtags = '夢見る男子'
    folder_name = 'yumemirudanshi'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 5

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_external()
        self.download_news()
        self.download_episode_preview_guess(download_valid=True)
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self, print_http_error=False):
        if self.is_image_exists(str(self.FINAL_EPISODE) + '_1') and self.is_image_exists('01_1'):
            return

        try:
            objs = self.get_json(
                self.PAGE_PREFIX + 'news/wp-json/wp/v2/pages?orderby=date&order=asc&acf_format=standard&per_page=100&parent=85')
            for obj in objs:
                if 'acf' in obj:
                    acf = obj['acf']
                    if 'number' in acf and 'images' in acf and isinstance(acf['images'], list):
                        try:
                            episode = str(int(acf['number'].split('#')[1])).zfill(2)
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

    def download_episode_preview_external(self):
        keywords = ['夢見る男子は現実主義者']
        AniverseMagazineScanner(keywords, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20230629', download_id=self.download_id).run()

    def download_episode_preview_guess(self, print_invalid=False, download_valid=False):
        if self.is_image_exists(str(self.FINAL_EPISODE).zfill(2) + '_1'):
            return

        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'news/wp/wp-content/uploads/%s/%s/%s_%s.jpg'
        current_date = datetime.now() + timedelta(hours=1)
        year = current_date.strftime('%Y')
        month = current_date.strftime('%m')
        is_successful = False
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1') or self.is_image_exists(episode + '_01', folder):
                continue
            episode_success = False
            valid_urls = []
            for j in range(self.IMAGES_PER_EPISODE):
                image_url = template % (year, month, episode, str(j + 1).zfill(2))
                if self.is_valid_url(image_url, is_image=True):
                    print('VALID - ' + image_url)
                    episode_success = True
                    valid_urls.append(image_url)
                elif print_invalid:
                    print('INVALID - ' + image_url)
            if download_valid and len(valid_urls) > 0:
                for valid_url in valid_urls:
                    image_name = self.extract_image_name_from_url(valid_url)
                    self.download_image(valid_url, folder + '/' + image_name)
            if not episode_success:
                break
            is_successful = True
        if is_successful:
            print(self.__class__.__name__ + ' - Guessed correctly!')
        return is_successful

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-list a',
                                    date_select='.news-list-item__date', title_select='.news-list-item__title',
                                    id_select=None, a_tag_start_text_to_remove='/', a_tag_prefix=self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('.home-visual__visual img[src]')
            for image in images:
                if '/img/' in image['src']:
                    image_url = self.PAGE_PREFIX + image['src'].split('?')[0].replace('./', '')
                    image_name = self.generate_image_name_from_url(image_url, 'img')
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        prefix = self.PAGE_PREFIX + 'character/'
        self.image_list = []
        try:
            obj = self.get_json(prefix + 'chara_data.php')
            if 'charas' in obj:
                for chara in obj['charas']:
                    if 'images' in chara:
                        if 'visuals' in chara['images']:
                            for visual in chara['images']['visuals']:
                                if 'image' in visual:
                                    image_url = prefix + visual['image'].replace('./', '').split('?')[0]
                                    image_name = self.extract_image_name_from_url(image_url)
                                    self.add_to_image_list(image_name, image_url)
                        if 'faces' in chara['images']:
                            for face in chara['images']['faces']:
                                image_url = prefix + face.replace('./', '').split('?')[0]
                                image_name = self.extract_image_name_from_url(image_url)
                                self.add_to_image_list(image_name, image_url)
        except Exception as e:
            self.print_exception(e, 'Character')
        self.download_image_list(folder)

    def download_media(self):
        folder = self.create_media_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        for page in ['1', '2', '3']:
            try:
                if page != '1' and page in processed:
                    continue
                page_url = self.PAGE_PREFIX + 'product/bd/bd_' + page + '/'
                soup = self.get_soup(page_url)
                selector = 'img.c-article-visual__image[src]'
                if page != '1':
                    selector += ',.c-card__thumb[data-bg]'
                images = soup.select(selector)
                self.image_list = []
                for image in images:
                    if image.has_attr('src'):
                        image_url = image['src']
                    else:
                        image_url = image['data-bg']
                    image_url = self.PAGE_PREFIX + image_url.replace('../', '').split('?')[0]
                    if image_url.endswith('/np.png'):
                        continue
                    if '/img/' in image_url:
                        image_name = self.generate_image_name_from_url(image_url, 'img')
                    else:
                        image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
                if page != '1':
                    if len(self.image_list) > 1:
                        processed.append(page)
                    elif len(self.image_list) == 0:
                        break
                self.download_image_list(folder)
            except Exception as e:
                self.print_exception(e, f'Blu-ray - {page}')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Zom 100: Zombie ni Naru made ni Shitai 100 no Koto https://zom100.com/ #ゾン100 #Zom100
class Zom100Download(Summer2023AnimeDownload, NewsTemplate):
    title = 'Zom 100: Zombie ni Naru made ni Shitai 100 no Koto'
    keywords = [title, 'Bucket List of the Dead', 'zom100']
    website = 'https://zom100.com/'
    twitter = 'Zom100_anime_JP'
    hashtags = ['ゾン100', 'Zom100']
    folder_name = 'zom100'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 4

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        try:
            template = self.PAGE_PREFIX + 'assets/story/%s/%s.jpg'
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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.content-entry',
                                    title_select='.entry-title span', date_select='.entry-date span',
                                    id_select=None, id_has_id=True, news_prefix='news.html',
                                    date_func=lambda x: x.replace('年', '.').replace('月', '.').replace('日', ''))

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.vis source[srcset]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['srcset'].replace('./', '')
                if '/assets/' not in image_url:
                    continue
                image_name = self.generate_image_name_from_url(image_url, 'assets')
                if image_name.endswith('-sp'):
                    continue
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'assets/character/c%s.webp'
        self.download_by_template(folder, template, 1, 1)
