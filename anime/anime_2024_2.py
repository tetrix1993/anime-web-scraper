from anime.main_download import MainDownload, NewsTemplate

# Kono Sekai wa Fukanzen Sugiru https://konofuka.com/ #このふか @konofuka_QA


# Spring 2024 Anime
class Spring2024AnimeDownload(MainDownload):
    season = "2024-2"
    season_name = "Spring 2024"
    folder_name = '2024-2'

    def __init__(self):
        super().__init__()


# Kono Sekai wa Fukanzen Sugiru
class KonofukaDownload(Spring2024AnimeDownload, NewsTemplate):
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

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.top-news a',
                                    title_select='.news-ttl', date_select='.news-date', id_select=None,
                                    next_page_select='ul.page-numbers li span', next_page_eval_index=-1,
                                    next_page_eval_index_class='current',
                                    date_func=lambda x: x.replace('(', '').replace(')', ''))

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz', self.PAGE_PREFIX + 'pDK2yjkH/wp-content/themes/konofuka_v0.1/assets/img/top/mv.png')
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/Fr85Cb4aAAAgWlS?format=jpg&name=4096x4096')
        self.download_image_list(folder)
