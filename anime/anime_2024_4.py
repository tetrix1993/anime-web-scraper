from anime.main_download import MainDownload, NewsTemplate, NewsTemplate2, NewsTemplate4
import json


# Fall 2024 Anime
class Fall2024AnimeDownload(MainDownload):
    season = "2024-4"
    season_name = "Fall 2024"
    folder_name = '2024-4'

    def __init__(self):
        super().__init__()


# Acro Trip
class AcroTripDownload(Fall2024AnimeDownload, NewsTemplate):
    title = 'Acro Trip'
    keywords = [title]
    website = 'https://acrotrip-anime.com/'
    twitter = 'acrotrip_anime'
    hashtags = ['アクロトリップ']
    folder_name = 'acrotrip'

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
                    image_url = template % (str(i + 1), str(j + 1))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name) == -1:
                        stop = True
                        break
                if stop:
                    break
            # soup = self.get_soup(self.PAGE_PREFIX)
            # btns = soup.select('.tp_story__tab_item[data-tab-target]')
            # for btn in btns:
            #     try:
            #         episode = str(int(btn.select('span')[0].text.replace('#', ''))).zfill(2)
            #         target = btn['data-tab-target']
            #     except:
            #         continue
            #     images = soup.select(f'#{target} .tp_story__imgMain_item img[src]')
            #     self.image_list = []
            #     for i in range(len(images)):
            #         image_url = self.PAGE_PREFIX + images[i]['src']
            #         image_name = episode + '_' + str(i + 1)
            #         self.add_to_image_list(image_name, image_url)
            #     self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news_item', title_select='.ttl',
                                    date_select='.p-news__list-date', id_select='a', paging_type=3,
                                    paging_suffix='?page=%s', next_page_select='.page-numbers',
                                    next_page_eval_index_class='current', next_page_eval_index=-1,
                                    date_func=lambda x: x[0:4] + '.' + str(self.convert_month_string_to_number(x[5:8])).zfill(2) + '.' + x[9:])

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.kv_image source[type="image/webp"][srcset]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['srcset']
                if not image_url.endswith('_sp.webp'):
                    continue
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'dist/img/character/character%s/stand.webp'
        try:
            for i in range(20):
                image_name = 'character' + str(i + 1)
                if self.is_image_exists(image_name, folder):
                    continue
                image_url = template % str(i + 1)
                if self.download_image(image_url, folder + '/' + image_name) == -1:
                    break
        except Exception as e:
            self.print_exception(e, 'Character')


# Amagami-san Chi no Enmusubi
class AmagamiDownload(Fall2024AnimeDownload, NewsTemplate):
    title = 'Amagami-san Chi no Enmusubi'
    keywords = [title, 'Tying the Knot with an Amagami Sister']
    website = 'https://amagami-anime.com/'
    twitter = 'amagami_anime'
    hashtags = ['甘神さんちの縁結び']
    folder_name = 'amagami'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.accordion_one', title_select='p',
                                    date_select='time', id_select=None, id_has_id=True)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.fv__contents .fv__left .swiper-slide img[src]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src']
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'img/character-%s.png'
        self.download_by_template(folder, template, 2, 1)


# Hitoribocchi no Isekai Kouryaku
class BocchiKouryakuDownload(Fall2024AnimeDownload, NewsTemplate):
    title = 'Hitoribocchi no Isekai Kouryaku'
    keywords = [title, 'Loner Life in Another World']
    website = 'https://bocchi-kouryaku.com/'
    twitter = 'bocchi_PR'
    hashtags = 'ぼっち攻略'
    folder_name = 'bocchikouryaku'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.c-fGHEql', paging_type=2,
                                    skip_first_page_num=False, title_select='.c-gKRVtX p',
                                    date_select='.c-jrhcXL p', id_select=None,
                                    a_tag_prefix=self.PAGE_PREFIX, a_tag_start_text_to_remove='/',
                                    next_page_select='.c-igANRe button.c-gulvcB', next_page_eval_index=-1,
                                    next_page_eval_index_class='c-gulvcB-kCOsjz-hidden-true')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('kv_pc', self.PAGE_PREFIX + 'assets/image/kv/pc.png')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'assets/character/%s/whole-body_PC.png'
        face_template = self.PAGE_PREFIX + 'assets/character/%s/face%s.png'
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character')
            content = soup.select('#__NEXT_DATA__')
            json_obj = json.loads(content[0].contents[0])
            for chara in json_obj['props']['pageProps']['characterCastList']:
                if chara is None or 'character' not in chara and 'images' not in chara['character']:
                    continue
                image_urls = chara['character']['images']
                self.image_list = []
                if 'main' in image_urls:
                    image_name = self.generate_image_name_from_url(image_urls['main'], 'character')
                    self.add_to_image_list(image_name, self.PAGE_PREFIX + image_urls['main'][1:])
                if 'facies' in image_urls:
                    image_name = self.generate_image_name_from_url(image_urls['facies'], 'character')
                    self.add_to_image_list(image_name, self.PAGE_PREFIX + image_urls['facies'][1:])
                self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Kabushikigaisha Magi-Lumière
class MagilumiereDownload(Fall2024AnimeDownload, NewsTemplate4):
    title = 'Kabushikigaisha Magi-Lumière'
    keywords = [title, 'Magilumiere Magical Girls Inc.']
    website = 'https://magilumiere-pr.com/'
    twitter = 'MagilumiereLtd'
    hashtags = 'マジルミエ'
    folder_name = 'magilumiere'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self, json_obj=None):
        self.download_template_news(json_url=self.PAGE_PREFIX + 'api/site-data/init')


# Kekkon suru tte, Hontou desu ka
class KekkonDesukaDownload(Fall2024AnimeDownload, NewsTemplate):
    title = 'Kekkon suru tte, Hontou desu ka'
    keywords = [title, '365 Days to the Wedding']
    website = 'https://365-wedding-anime.com/'
    twitter = 'kekkon_anime'
    hashtags = ['kekkon_anime', '結婚ですか']
    folder_name = 'kekkondesuka'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-item',
                                    title_select='.news-item__title', date_select='.news-item__date',
                                    id_select=None, a_tag_prefix=self.PAGE_PREFIX, a_tag_start_text_to_remove='/')


# Nageki no Bourei wa Intai shitai
class NagekiDownload(Fall2024AnimeDownload, NewsTemplate):
    title = 'Nageki no Bourei wa Intai shitai'
    keywords = [title, 'Let This Grieving Soul Retire']
    website = 'https://nageki-anime.com/'
    twitter = 'nageki_official'
    hashtags = ['嘆きの亡霊']
    folder_name = 'nageki'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.c-hnachi', paging_type=2,
                                    skip_first_page_num=False, title_select='.c-hnachi .c-dbxBTl p',
                                    date_select='.c-hnachi .c-dhzjXW p', id_select=None,
                                    a_tag_prefix=self.PAGE_PREFIX, a_tag_start_text_to_remove='/',
                                    next_page_select='.c-iEPVyt button', next_page_eval_index=-1,
                                    next_page_eval_index_class='c-PJLV-cqNpHX-disabled-true')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        template = self.PAGE_PREFIX + 'assets/keyvisual/%s/pc.png'
        try:
            for i in range(10):
                image_url = template % str(i + 1)
                image_name = 'kv' + str(i + 1)
                if self.download_image(image_url, folder + '/' + image_name) == -1:
                    break
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'assets/character/%s/whole-body_PC.png'
        face_template = self.PAGE_PREFIX + 'assets/character/%s/face%s.png'
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character')
            content = soup.select('#__NEXT_DATA__')
            json_obj = json.loads(content[0].contents[0])
            for character in json_obj['props']['pageProps']['characterData']:
                if character is None or 'id' not in character:
                    continue
                name = character['id']
                image_name = name + '_whole-body_PC'
                if self.is_image_exists(image_name, folder):
                    continue
                self.image_list = []
                image_url = template % name
                self.add_to_image_list(image_name, image_url)
                for i in range(3):
                    face_url = face_template % (name, str(i + 1))
                    face_name = name + '_face' + str(i + 1)
                    self.add_to_image_list(face_name, face_url)
                self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Party kara Tsuihou sareta Sono Chiyushi, Jitsu wa Saikyou ni Tsuki
class SonoChiyushiDownload(Fall2024AnimeDownload, NewsTemplate2):
    title = 'Party kara Tsuihou sareta Sono Chiyushi, Jitsu wa Saikyou ni Tsuki'
    keywords = [title, 'The Healer Who Was Banished From His Party, Is, in Fact, the Strongest']
    website = 'https://sonochiyushi.com/'
    twitter = 'sonochiyushi'
    hashtags = ['その治癒師']
    folder_name = 'sonochiyushi'

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
            images = soup.select('.hero__img source[srcset]')
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
        prefix = self.PAGE_PREFIX + 'core_sys/images/main/chara/chara'
        templates = [prefix + '%s.webp', prefix + '%s_face.webp',
                     prefix + '%s.png', prefix + '%s_face.png']
        self.download_by_template(folder, templates, 2, 1, max_skip=1)


# Rekishi ni Nokoru Akujo ni Naru zo
class ReikiakuDownload(Fall2024AnimeDownload, NewsTemplate):
    title = 'Rekishi ni Nokoru Akujo ni Naru zo'
    keywords = [title, 'I\'ll Become a Villainess Who Goes Down in History', 'rekiaku']
    website = 'https://rekiaku-anime.com/'
    twitter = 'rekiaku'
    hashtags = ['rekiaku', '歴史に残る悪女になるぞ', '歴悪']
    folder_name = 'rekiaku'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.newsList li',
                                    title_select='.text', date_select='.days', id_select='a',
                                    a_tag_prefix=self.PAGE_PREFIX, a_tag_start_text_to_remove='/')
