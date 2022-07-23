from anime.main_download import MainDownload, NewsTemplate


# Isekai wa Smartphone to Tomo ni. 2 http://isesuma-anime.jp/ #イセスマ @isesumaofficial


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
