from anime.main_download import MainDownload, NewsTemplate


# Eiyuuou, Bu wo Kiwameru Tame Tenseisu: Soshite, Sekai Saikyou no Minarai Kishi https://auo-anime.com/ #英雄王 @auo_anime


# Winter 2023 Anime
class Winter2023AnimeDownload(MainDownload):
    season = "2023-1"
    season_name = "Winter 2023"
    folder_name = '2023-1'

    def __init__(self):
        super().__init__()


# Eiyuuou, Bu wo Kiwameru Tame Tenseisu: Soshite, Sekai Saikyou no Minarai Kishi
class EiyuuouDownload(Winter2023AnimeDownload, NewsTemplate):
    title = 'Eiyuuou, Bu wo Kiwameru Tame Tenseisu: Soshite, Sekai Saikyou no Minarai Kishi'
    keywords = [title]
    website = 'https://auo-anime.com/'
    twitter = 'auo_anime'
    hashtags = '英雄王'
    folder_name = 'eiyuuou'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='li.news-item',
                                    date_select='p.date', title_select='p.title', id_select='a',
                                    next_page_select='div.pagination a.next',
                                    next_page_eval_index_class='off', next_page_eval_index=0)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz', self.PAGE_PREFIX + 'wp/wp-content/themes/euo-teaser-theme/img/kv.jpg')
        # self.add_to_image_list('tz_news', self.PAGE_PREFIX + 'wp/wp-content/uploads/2022/02/英雄王_ティザービジュアル.jpg')
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FNYCWh2VgAM1rSE?format=jpg&name=large')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'wp/wp-content/themes/euo-teaser-theme/img/chara-pic%s.png'
        self.download_by_template(folder, template, 1, 1, prefix='tz_')
