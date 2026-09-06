from anime.main_download import MainDownload, NewsTemplate, NewsTemplate2


# Fall 2026 Anime
class Fall2026AnimeDownload(MainDownload):
    season = "2026-4"
    season_name = "Fall 2026"
    folder_name = '2026-4'

    def __init__(self):
        super().__init__()


# Kyouran Reijou Nia Liston
class KyoranReijoDownload(Fall2026AnimeDownload, NewsTemplate):
    title = 'Kyouran Reijou Nia Liston'
    keywords = [title, 'Nia Liston: The Merciless Maiden', 'kyoranreijo']
    website = 'https://kyoranreijo-pr.com/'
    twitter = 'kyoranreijo_pr'
    hashtags = ['凶乱令嬢']
    folder_name = 'kyoranreijo'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-item', date_select='.date',
                                    title_select='.title', id_select='a')


# Mezametara Saikyou Soubi to Uchuusenmochi Datta node, Ikkodate Mezashite Youhei toshite Jiyuu ni Ikitai
class SaikyoSoubiDownload(Fall2026AnimeDownload, NewsTemplate):
    title = 'Mezametara Saikyou Soubi to Uchuusenmochi Datta node, Ikkodate Mezashite Youhei toshite Jiyuu ni Ikitai'
    keywords = [title, 'Reborn as a Space Mercenary: I Woke Up Piloting the Strongest Starship!', 'mezameza']
    website = 'https://saikyosoubi.com/'
    twitter = 'saikyosoubi'
    hashtags = ['めざめざ']
    folder_name = 'saikyosoubi'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.l-news__item',
                                    date_select='.l-news__item-date', title_select='.l-news__item-title',
                                    id_select='.l-news__item-link', a_tag_prefix=news_url, paging_type=1,
                                    next_page_select='.c-pagination__item', next_page_eval_index=-1,
                                    next_page_eval_index_class='is-current')


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


# Toaru Anbu no Item
class ToaruItemDownload(Fall2026AnimeDownload, NewsTemplate2):
    title = 'Toaru Anbu no Item'
    keywords = [title, 'A Certain Dark Side Item']
    website = 'https://toaru-project.com/item/'
    twitter = 'toaru_project'
    hashtags = ['とある暗部の少女共棲']
    folder_name = 'toaruitem'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        pass

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX)
