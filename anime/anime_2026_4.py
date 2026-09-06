from anime.main_download import MainDownload, NewsTemplate


# Fall 2026 Anime
class Fall2026AnimeDownload(MainDownload):
    season = "2026-4"
    season_name = "Fall 2026"
    folder_name = '2026-4'

    def __init__(self):
        super().__init__()


# Seitokai ni mo Ana wa Aru!
class NamaAnaruDownload(Fall2026AnimeDownload, NewsTemplate):
    title = 'Seitokai ni mo Ana wa Aru!'
    keywords = [title, 'Even the Student Council Has Its Holes!', 'nama anaru']
    website = 'https://nama-anaru.com/'
    twitter = 'nama_anaru'
    hashtags = ['アニメ生穴る']
    folder_name = 'namaanaru'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        pass

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news/'
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.p-news__list-item',
                                    date_select='.p-news__list-date', title_select='.p-news__list-ttl',
                                    id_select='a', a_tag_start_text_to_remove='./', a_tag_prefix=news_url,
                                    next_page_select='.-next', paging_type=1)
