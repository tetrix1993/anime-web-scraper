from anime.main_download import MainDownload, NewsTemplate
import json


# Fall 2024 Anime
class Fall2024AnimeDownload(MainDownload):
    season = "2024-4"
    season_name = "Fall 2024"
    folder_name = '2024-4'

    def __init__(self):
        super().__init__()


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
