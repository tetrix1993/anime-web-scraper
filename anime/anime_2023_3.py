from anime.main_download import MainDownload, NewsTemplate


# Higeki no Genkyou to Naru Saikyou Gedou Last Boss Joou wa Tami no Tame ni Tsukushimasu. https://lastame.com/ #ラス為 @lastame_pr
# Tsuyokute New Saga https://tsuyosaga-pr.com/ #つよサガ @tsuyosaga_pr


# Summer 2023 Anime
class Summer2023AnimeDownload(MainDownload):
    season = "2023-3"
    season_name = "Summer 2023"
    folder_name = '2023-3'

    def __init__(self):
        super().__init__()


# Higeki no Genkyou to Naru Saikyou Gedou Last Boss Joou wa Tami no Tame ni Tsukushimasu.
class LastameDownload(Summer2023AnimeDownload, NewsTemplate):
    title = 'Higeki no Genkyou to Naru Saikyou Gedou Last Boss Joou wa Tami no Tame ni Tsukushimasu.'
    keywords = [title, 'The Most Heretical Last Boss Queen: From Villainess to Savior', 'Lastame']
    website = 'https://lastame.com/'
    twitter = 'lastame_pr'
    hashtags = 'ラス為'
    folder_name = 'lastame'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.newsBox li',
                                    date_select='small', title_select='p', id_select='a',
                                    date_func=lambda x: x.replace('年', '.').replace('月', '.').replace('日', ''))

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FgH9hRHVEAAZFyz?format=jpg&name=large')
        self.add_to_image_list('tz_mv_pc', self.PAGE_PREFIX + 'wp/wp-content/themes/original/assets/img/mv_pc.png')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'wp/wp-content/themes/original/assets/img/character01-main%s.png'
        self.download_by_template(folder, template, 2, start=1, end=3)


# Tsuyokute New Saga
class TsuyosagaDownload(Summer2023AnimeDownload, NewsTemplate):
    title = 'Tsuyokute New Saga'
    keywords = [title, 'New Saga', 'Tsuyosaga']
    website = 'https://tsuyosaga-pr.com/'
    twitter = 'tsuyosaga_pr'
    hashtags = 'つよサガ'
    folder_name = 'tsuyosaga'

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
        pass

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_aniverse', 'https://aniverse-mag.com/wp-content/uploads/2022/10/1628619ceb9f5f0127d70926036c5ffd.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'wp/wp-content/themes/newsaga/static/character/%s/main.png'
        for i in range(10):
            number = str(i + 1).zfill(2)
            image_name = 'tz_char' + number
            if self.is_image_exists(image_name, folder):
                continue
            image_url = template % number
            result = self.download_image(image_url, folder + '/' + image_name)
            if result == -1:
                break