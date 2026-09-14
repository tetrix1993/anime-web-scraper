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


# Sekai Saikyou no Majo, Hajimemashita
class SekamajoDownload(Fall2026AnimeDownload, NewsTemplate):
    title = 'Sekai Saikyou no Majo, Hajimemashita'
    keywords = [title, "The World's Strongest Witch"]
    website = 'https://sekamajo-anime.com/'
    twitter = 'sekamajo_anime'
    hashtags = ['せかまじょ', '世界最強魔女']
    folder_name = 'sekamajo'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        pass

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.article',
                                    date_select='.article__date', title_select='.article__ttl', id_select='a')


# Shinja Zero no Megami-sama to Hajimeru Isekai Kouryaku
class ShinjaZeroDownload(Fall2026AnimeDownload, NewsTemplate):
    title = 'Shinja Zero no Megami-sama to Hajimeru Isekai Kouryaku'
    keywords = [title, 'Full Clearing Another World under a Goddess with Zero Believers']
    website = 'https://zero-believers-anime.com/'
    twitter = 'zero_believers'
    hashtags = ['信者ゼロ']
    folder_name = 'shinjazero'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        pass

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.p-news__item',
                                    date_select='time', title_select='.c-card-news__title', id_select='a',
                                    next_page_select='.next.page-numbers', paging_type=3, paging_suffix='?page=%s')


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


# Tensei shitara Ken deshita II
class Tenken2Download(Fall2026AnimeDownload, NewsTemplate):
    title = 'Tensei shitara Ken deshita II'
    keywords = [title, 'Reincarnated as a Sword Season 2', 'tenken', '2nd']
    website = 'https://tenken-anime.com/'
    twitter = 'tenken_official'
    hashtags = ['転生したら剣でした', '転剣']
    folder_name = 'tenken2'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        template = self.PAGE_PREFIX + 'assets/story/%s/%s.webp'
        try:
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_1'):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (str(i + 1), str(j + 1))
                    image_name = episode + '_' + str(j + 1)
                    result = self.download_image(image_url, self.base_folder + '/' + image_name)
                    if result == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='article.content-entry',
                                    title_select='h2.entry-title span', date_select='div.entry-date',
                                    id_select=None, id_has_id=True, news_prefix='news.html',
                                    date_func=lambda x: x[0:4] + '.' + x[4:],
                                    a_tag_prefix=self.PAGE_PREFIX + 'news.html#')


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


# Tsuihou sareta Cheat Fuyo Majutsushi wa Kimama na Second Life wo Ouka suru.
class ChiifuyoDownload(Fall2026AnimeDownload, NewsTemplate):
    title = 'Tsuihou sareta Cheat Fuyo Majutsushi wa Kimama na Second Life wo Ouka suru.'
    keywords = [title, 'The Laid-Off Cheat-Granting Mage Enjoys a Second Lease on Life', 'chiifuyo']
    website = 'https://sh-anime.shochiku.co.jp/chiifuyo-anime/'
    twitter = 'chi_fuyo'
    hashtags = ['チー付与']
    folder_name = 'chiifuyo'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        pass

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news_list_item',
                                    title_select='.title', date_select='.date', id_select='a')
