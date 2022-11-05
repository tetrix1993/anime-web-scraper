from anime.main_download import MainDownload, NewsTemplate, NewsTemplate2


# Isekai wa Smartphone to Tomo ni. 2 http://isesuma-anime.jp/ #イセスマ @isesumaofficial
# Kuma Kuma Kuma Bear Punch! https://kumakumakumabear.com/ #くまクマ熊ベアー #kumabear @kumabear_anime
# Shiro Seijo to Kuro Bokushi https://shiroseijyo-anime.com/ @shiroseijyo_tv #白聖女と黒牧師
# Tensei Kizoku no Isekai Boukenroku https://www.tensei-kizoku.jp/ #転生貴族 @tenseikizoku


# Spring 2023 Anime
class Spring2023AnimeDownload(MainDownload):
    season = "2023-2"
    season_name = "Spring 2023"
    folder_name = '2023-2'

    def __init__(self):
        super().__init__()


# Isekai wa Smartphone to Tomo ni. 2
class Isesuma2Download(Spring2023AnimeDownload, NewsTemplate):
    title = 'Isekai wa Smartphone to Tomo ni. 2'
    keywords = [title, "In Another World With My Smartphone 2"]
    website = 'http://isesuma-anime.jp/'
    twitter = 'isesumaofficial'
    hashtags = 'イセスマ'
    folder_name = 'isesuma2'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.entryArea',
                                    date_select='.date', title_select='.subj', id_select='.notexist')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_main', self.PAGE_PREFIX + 'img/main.jpg')
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FYQeHycaMAIdyyN?format=jpg&name=medium')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.charaArea img[src]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src']
                image_name = self.generate_image_name_from_url(image_url, 'chara')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Kuma Kuma Kuma Bear Punch!
class KumaBear2Download(Spring2023AnimeDownload, NewsTemplate2):
    title = 'Kuma Kuma Kuma Bear Punch!'
    keywords = [title, "2nd"]
    website = 'https://kumakumakumabear.com/'
    twitter = 'kumabear_anime'
    hashtags = ['くまクマ熊ベアー', 'kumabear']
    folder_name = 'kumabear2'

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
        self.image_list = []
        self.add_to_image_list('kv_aniverse', 'https://aniverse-mag.com/wp-content/uploads/2022/11/96785c9962f5ef9863dc77113ebdf26f.jpg')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.loading__kv-img img[src]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src']
                if '/main/' in image_url:
                    image_name = self.generate_image_name_from_url(image_url, 'main')
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        self.image_list = []
        self.add_to_image_list('tz_yuna', 'https://aniverse-mag.com/wp-content/uploads/2022/11/aade6f0c762346c7e43719675da36208.png')
        self.add_to_image_list('tz_fina', 'https://aniverse-mag.com/wp-content/uploads/2022/11/de14b80b290bdc786e18e6150c323d0e.png')
        self.download_image_list(folder)

        template = self.PAGE_PREFIX + 'core_sys/images/main/tz/chara_%s.png'
        self.download_by_template(folder, template, 2, 1, prefix='tz_')


# Shiro Seijo to Kuro Bokushi
class ShiroSeijoDownload(Spring2023AnimeDownload, NewsTemplate):
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
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.movieCharaImg img[src]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'][2:]
                image_name = self.generate_image_name_from_url(image_url, 'img')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Tensei Kizoku no Isekai Boukenroku
class TenseiKizokuDownload(Spring2023AnimeDownload, NewsTemplate):
    title = 'Tensei Kizoku no Isekai Boukenroku'
    keywords = [title, "Chronicles of an Aristocrat Reborn in Another World"]
    website = 'https://www.tensei-kizoku.jp/'
    twitter = 'tenseikizoku'
    hashtags = '転生貴族'
    folder_name = 'tenseikizoku'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news li',
                                    date_select='.news_date', title_select='.news_title', id_select='a',
                                    news_prefix='')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('kv', self.PAGE_PREFIX + 'img/kv.png')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('.character img[src]')
            for image in images:
                if '/chara/' in image['src']:
                    image_url = self.PAGE_PREFIX + image['src']
                    image_name = self.generate_image_name_from_url(image_url, 'chara')
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')
