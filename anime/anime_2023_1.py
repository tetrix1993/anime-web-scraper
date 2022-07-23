from anime.main_download import MainDownload, NewsTemplate, NewsTemplate2


# Benriya Saitou-san, Isekai ni Iku https://saitou-anime.com/ #便利屋斎藤さん @saitou_anime
# Eiyuuou, Bu wo Kiwameru Tame Tenseisu: Soshite, Sekai Saikyou no Minarai Kishi https://auo-anime.com/ #英雄王 @auo_anime
# Ijiranaide, Nagatoro-san 2nd Attack https://www.nagatorosan.jp/ #長瀞さん @nagatoro_tv
# Kyokou Suiri S2 https://kyokousuiri.jp/ #虚構推理 @kyokou_suiri
# Tomo-chan wa Onnanoko! https://tomo-chan.jp/ #tomochan @tomo_chan_ani
# Tsundere Akuyaku Reijou Liselotte to Jikkyou no Endou-kun to Kaisetsu no Kobayashi-san http://tsunlise-pr.com/ #ツンリゼ @tsunlise_pr


# Winter 2023 Anime
class Winter2023AnimeDownload(MainDownload):
    season = "2023-1"
    season_name = "Winter 2023"
    folder_name = '2023-1'

    def __init__(self):
        super().__init__()


# Benriya Saitou-san, Isekai ni Iku
class BenriyaSaitouDownload(Winter2023AnimeDownload, NewsTemplate2):
    title = 'Benriya Saitou-san, Isekai ni Iku'
    keywords = [title, 'Handyman Saitou in Another World']
    website = 'https://saitou-anime.com/'
    twitter = 'saitou_anime'
    hashtags = '便利屋斎藤さん'
    folder_name = 'benriya-saitou'

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
        self.add_to_image_list('tz', self.PAGE_PREFIX + 'core_sys/images/news/00000003/block/00000008/00000001.jpg')
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FYMHT1jVUAAUtmQ?format=jpg&name=medium')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        prefix = self.PAGE_PREFIX + 'core_sys/images/main/tz/chara/chara_%s'
        templates = [prefix + '.png', prefix + '_face.png']
        self.download_by_template(folder, templates, 2, 1, prefix='tz_')


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


# Ijiranaide, Nagatoro-san 2nd Attack
class Nagatorosan2Download(Winter2023AnimeDownload, NewsTemplate):
    title = 'Ijiranaide, Nagatoro-san 2nd Attack'
    keywords = [title, 'Nagatorosan', "Don't Toy with Me, Miss Nagatoro"]
    website = 'https://www.nagatorosan.jp/'
    twitter = 'nagatoro_tv'
    hashtags = '長瀞さん'
    folder_name = 'nagatorosan2'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        # self.download_news()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('teaser_img_mainimg', self.PAGE_PREFIX + 'teaser/img/mainimg.jpg')
        self.add_to_image_list('tz', 'https://pbs.twimg.com/media/FWeINYraUAEG6y9?format=jpg&name=medium')
        self.download_image_list(folder)


# Kyokou Suiri S2
class KyokouSuiri2Download(Winter2023AnimeDownload, NewsTemplate):
    title = 'Kyokou Suiri Season 2'
    keywords = ['Kyokou Suiri', 'In/Spectre', '2nd']
    website = 'https://kyokousuiri.jp/'
    twitter = 'kyokou_suiri'
    hashtags = '虚構推理'
    folder_name = 'kyokou-suiri2'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='ul.p-news__list li.p-news__list-item',
                                    date_select='div.p-article__header', title_select='div.p-article__text',
                                    id_select='a', date_separator=' ', stop_date='2021.03.17',
                                    next_page_select='div.c-pagination__nav.-next', next_page_eval_index=-1,
                                    next_page_eval_index_class='is-disable')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        image_prefix = self.PAGE_PREFIX + 'wp/wp-content/uploads/'
        self.add_to_image_list('tz', image_prefix + '2021/11/6271138d893814b7a21c84b078fca0b9.jpg')
        self.add_to_image_list('kv1', image_prefix + '2022/03/cefd7ddc49fafe239a53b1721361c61e.jpg')
        self.add_to_image_list('img_main_kv2', self.PAGE_PREFIX + 'assets_2t/img/top/main/img_main_kv2.png')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('.p-chara_data__visual-img img.is-pc')
            for image in images:
                if image.has_attr('src') and image['src'].startswith('/'):
                    image_url = self.PAGE_PREFIX + image['src'][1:]
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Tomo-chan wa Onnanoko!
class TomochanDownload(Winter2023AnimeDownload, NewsTemplate):
    title = 'Tomo-chan wa Onnanoko!'
    keywords = [title, 'tomochan', 'Tomo Is a Girl!']
    website = 'https://tomo-chan.jp/'
    twitter = 'tomo_chan_ani'
    hashtags = 'tomochan'
    folder_name = 'tomochan'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='li.p-news__list-item',
                                    date_select='.p-news__list-date', title_select='.p-news__list-ttl',
                                    id_select='a', a_tag_start_text_to_remove='./', paging_type=1,
                                    a_tag_prefix=self.PAGE_PREFIX + 'news/',
                                    next_page_select='.c-pagination__nav-button.-next')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FWw4blxagAEvI9K?format=jpg&name=medium')
        self.add_to_image_list('main_img_main-illust', self.PAGE_PREFIX + 'assets/t/img/main/img_main-illust.png')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'assets/t/img/chara/img_chara%s.png'
        self.download_by_template(folder, template, 2, 1, prefix='tz_')


# Tsundere Akuyaku Reijou Liselotte to Jikkyou no Endou-kun to Kaisetsu no Kobayashi-san
class TsunliseDownload(Winter2023AnimeDownload, NewsTemplate):
    title = 'Tsundere Akuyaku Reijou Liselotte to Jikkyou no Endou-kun to Kaisetsu no Kobayashi-san'
    keywords = [title, 'tsunlise', 'Endo and Kobayashi Live! The Latest on Tsundere Villainess Lieselotte']
    website = 'https://tsunlise-pr.com/'
    twitter = 'tsunlise_pr'
    hashtags = 'ツンリゼ'
    folder_name = 'tsunlise'

    PAGE_PREFIX = website

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_news(self):
        # Paging logic need update
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-item',
                                    date_select='.date', title_select='.title', id_select='a')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('kv1_1', self.PAGE_PREFIX + 'wp/wp-content/uploads/2022/07/01_ツンリゼ_第1弾KV_ツンver..jpg')
        self.add_to_image_list('kv1_2', self.PAGE_PREFIX + 'wp/wp-content/uploads/2022/07/02_ツンリゼ_第1弾KV_デレver..jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'wp/wp-content/themes/tunlise-teaser-theme/img/chara-pic%s.png'
        self.download_by_template(folder, template, 1, 1, prefix='tz_')
