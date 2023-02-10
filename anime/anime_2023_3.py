from anime.main_download import MainDownload, NewsTemplate


# Higeki no Genkyou to Naru Saikyou Gedou Last Boss Joou wa Tami no Tame ni Tsukushimasu. https://lastame.com/ #ラス為 @lastame_pr
# Level 1 dakedo Unique Skill de Saikyou desu https://level1-anime.com/ #レベル1だけどアニメ化です @level1_anime
# Okashi na Tensei https://okashinatensei-pr.com/ #おかしな転生 @okashinatensei
# Shiro Seijo to Kuro Bokushi https://shiroseijyo-anime.com/ @shiroseijyo_tv #白聖女と黒牧師
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


# Level 1 dakedo Unique Skill de Saikyou desu
class Level1Download(Summer2023AnimeDownload, NewsTemplate):
    title = 'Level 1 dakedo Unique Skill de Saikyou desu'
    keywords = [title, 'My Unique Skill Makes Me OP Even at Level 1']
    website = 'https://level1-anime.com/'
    twitter = 'level1_anime'
    hashtags = 'レベル1だけどアニメ化です'
    folder_name = 'level1'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-item',
                                    date_select='.date', title_select='.title', id_select='a',
                                    next_page_select='div.pagination .page-numbers',
                                    next_page_eval_index_class='current', next_page_eval_index=-1)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FeSNHVXaYAEXR1w?format=jpg&name=medium')
        self.add_to_image_list('tz_kv-pc', self.PAGE_PREFIX + 'wp/wp-content/themes/level1_teaser/images/kv-pc.jpg')
        self.add_to_image_list('tz_kv-sp', self.PAGE_PREFIX + 'wp/wp-content/themes/level1_teaser/images/kv-sp.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'wp/wp-content/themes/level1_teaser/images/chara-pic%s.png'
        self.download_by_template(folder, template, 1, 1, prefix='tz_')


# Okashi na Tensei
class OkashinaTenseiDownload(Summer2023AnimeDownload, NewsTemplate):
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
        self.add_to_image_list('tz_natalie', 'https://ogre.natalie.mu/media/news/comic/2022/1215/okashinatensei_teaser.jpg')
        self.download_image_list(folder)

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
