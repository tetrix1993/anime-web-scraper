import requests
from anime.main_download import MainDownload, NewsTemplate


# Soredemo Ayumu wa Yosetekuru https://soreayu.com/ #それあゆ @soreayu_staff
# Utawarerumono: Futari no Hakuoro https://utawarerumono.jp/ #うたわれ @UtawareAnime


# Summer 2022 Anime
class Summer2022AnimeDownload(MainDownload):
    season = "2022-3"
    season_name = "Summer 2022"
    folder_name = '2022-3'

    def __init__(self):
        super().__init__()


# Soredemo Ayumu wa Yosetekuru
class SoreayuDownload(Summer2022AnimeDownload, NewsTemplate):
    title = "Soredemo Ayumu wa Yosetekuru"
    keywords = [title, "Soreayu"]
    website = 'https://soreayu.com/'
    twitter = 'soreayu_staff'
    hashtags = 'それあゆ'
    folder_name = 'soreayu'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='div.news-page-news',
                                    date_select='div.date-label span', title_select='div.page-link h2',
                                    id_select='div.nullclass')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('teaser', self.PAGE_PREFIX + '_nuxt/img/key_visual.7d7640c.jpg')
        self.add_to_image_list('teaser_big', 'https://firebasestorage.googleapis.com/v0/b/pj-ayumu.appspot.com/o/articles%2F1625582107153?alt=media&token=2561cd21-5081-471b-9019-11f379fff1f7')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character')
            links = soup.select('link')
            if len(links) == 0:
                return
            js_file = self.PAGE_PREFIX + links[-1]['href'][1:]
            r = requests.get(js_file)
            r.raise_for_status()
            results = r.content.decode().split('"img/')
            self.image_list = []
            for i in range(len(results)):
                if i == 0:
                    continue
                image_name_with_extension = results[i].split('"')[0]
                if '_full' in image_name_with_extension or '_expression' in image_name_with_extension:
                    image_url = self.PAGE_PREFIX + '_nuxt/img/' + image_name_with_extension
                    image_name = self.extract_image_name_from_url(image_name_with_extension)
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Character')
            print(e)


# Utawarerumono: Futari no Hakuoro
class Utawarerumono3Download(Summer2022AnimeDownload, NewsTemplate):
    title = 'Utawarerumono: Futari no Hakuoro'
    keywords = [title, 'Utawarerumono: Mask of Truth', '3rd']
    website = 'https://utawarerumono.jp/'
    twitter = 'UtawareAnime'
    hashtags = 'うたわれ'
    folder_name = 'utawarerumono3'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='li.md-list__article--li',
                                    title_select='h4', date_select='dt', id_select='a', news_prefix='topics/',)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FE9Ma5NaAAABavo?format=jpg&name=4096x4096')
        self.add_to_image_list('fv@2x', self.PAGE_PREFIX + 'manage/wp-content/themes/hakuoro/_assets/images/fv/fv@2x.png')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'manage/wp-content/themes/hakuoro/_assets/images/char/detail/char%s_pc.png'
        self.download_by_template(folder, template, 2, 1)
