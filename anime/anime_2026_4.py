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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-item', date_select='.date',
                                    title_select='.title', id_select='a')


# Magical Explorer
class MajiekuDownload(Fall2026AnimeDownload, NewsTemplate):
    title = 'Magical Explorer'
    keywords = [title, 'majieku']
    website = 'https://majieku.com/'
    twitter = 'Majieku_anime'
    hashtags = ['マジエク']
    folder_name = 'majieku'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.newsList',
                                    date_select='.newsList__date', title_select='.newsList__title', id_select='a',
                                    date_func=lambda x: x[0:4] + '.' + x[5:], a_tag_prefix=news_url, paging_type=1,
                                    next_page_select='.-next')


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


# Shiotaiou no Satou-san ga Ore ni dake Amai
class ShioamaDownload(Fall2026AnimeDownload):
    title = 'Shiotaiou no Satou-san ga Ore ni dake Amai'
    keywords = [title, 'The Salty Koharu Has a Soft Spot for Me', 'shioama']
    website = 'https://shioama-anime.com/'
    twitter = 'shioamaofficial'
    hashtags = ['しおあま']
    folder_name = 'shioama'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        pass

    def download_news(self):
        try:
            results = []
            news_obj = self.get_last_news_log_object()
            json_obj = self.get_json(self.PAGE_PREFIX + 'news.json')
            for item in json_obj:
                if 'date' in item and 'id' in item and 'title' in item:
                    date = item['date'].replace('/', '.')
                    title = item['title']
                    id_ = item['id']
                    url = self.PAGE_PREFIX + 'news.html?id=' + id_
                    if news_obj is not None and (news_obj['id'] == url or news_obj['title'] == title
                                                 or date < news_obj['date']):
                        break
                    results.append(self.create_news_log_object(date, title, url))
            success_count = 0
            for result in reversed(results):
                process_result = self.create_news_log_from_news_log_object(result)
                if process_result == 0:
                    success_count += 1
            if len(results) > 0:
                self.create_news_log_cache(success_count, results[0])
        except Exception as e:
            self.print_exception(e, 'News')


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
