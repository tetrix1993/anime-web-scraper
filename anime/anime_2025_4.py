from anime.main_download import MainDownload, NewsTemplate, NewsTemplate2, NewsTemplate3, NewsTemplate4
from datetime import datetime, timedelta
from requests.exceptions import HTTPError
from scan import AniverseMagazineScanner
from bs4 import BeautifulSoup
import json
import os


# Fall 2025 Anime
class Fall2025AnimeDownload(MainDownload):
    season = "2025-4"
    season_name = "Fall 2025"
    folder_name = '2025-4'

    def __init__(self):
        super().__init__()


# Ansatsusha de Aru Ore no Status ga Yuusha yori mo Akiraka ni Tsuyoi no da ga
class SutetsuyoDownload(Fall2025AnimeDownload, NewsTemplate):
    title = "Ansatsusha de Aru Ore no Status ga Yuusha yori mo Akiraka ni Tsuyoi no da ga"
    keywords = [title, 'sutetsuyo', 'My Status as an Assassin Obviously Exceeds the Hero\'s']
    website = 'https://sutetsuyo-anime.com/'
    twitter = 'sutetsuyo_an'
    hashtags = ['ステつよ', 'sutetsuyo']
    folder_name = 'sutetsuyo'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='article', date_select='time',
                                    title_select='h2', id_select='a', a_tag_prefix=self.PAGE_PREFIX + 'news/')


# Bukiyou na Senpai.
class BukiyouDownload(Fall2025AnimeDownload, NewsTemplate):
    title = "Bukiyou na Senpai."
    keywords = [title, 'My Awkward Senpai']
    website = 'https://bukiyouna-senpai.asmik-ace.co.jp/'
    twitter = 'bukiyou_anime'
    hashtags = '不器用な先輩'
    folder_name = 'bukiyou'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.newsList',
                                    date_select='time', title_select='.newsList__title', id_select='a',
                                    next_page_select='.wp-pagenavi *', next_page_eval_index_class='current',
                                    next_page_eval_index=-1, date_func=lambda x: x[0:4] + '.' + x[5:])


# Chichi wa Eiyuu, Haha wa Seirei, Musume no Watashi wa Tenseisha.
class HahanohaDownload(Fall2025AnimeDownload, NewsTemplate):
    title = "Chichi wa Eiyuu, Haha wa Seirei, Musume no Watashi wa Tenseisha."
    keywords = [title, 'hahanoha', 'Reincarnated as the Daughter of the Legendary Hero and the Queen of Spirits']
    website = 'https://hahanoha-anime.com/'
    twitter = 'hahanoha_anime'
    hashtags = 'ははのは'
    folder_name = 'hahanoha'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.sec-news__list_item',
                                    date_select='.sec-news__list_item_date', title_select='.sec-news__list_item_title',
                                    id_select=None, next_page_select='.pagination .next')


# Chitose-kun wa Ramune Bin no Naka
class ChiramuneDownload(Fall2025AnimeDownload, NewsTemplate2):
    title = "Chitose-kun wa Ramune Bin no Naka"
    keywords = [title, 'chiramune', 'Chitose Is in the Ramune Bottle']
    website = 'https://chiramune.com/'
    twitter = 'anime_chiramune'
    hashtags = 'チラムネ'
    folder_name = 'chiramune'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX)


# Isekai Munchkin
class IsekaiMunchkinDownload(Fall2025AnimeDownload, NewsTemplate):
    title = "Isekai Munchkin"
    keywords = [title, 'Otherworldly Munchkin']
    website = 'https://isekai-munchkin.com/'
    twitter = 'isekai_munchkin'
    hashtags = ['異世界マンチキン', 'munchkin']
    folder_name = 'munchkin'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-item',
                                    date_select='.news-item__date', title_select='.news-item__title', id_select=None,
                                    a_tag_prefix=self.PAGE_PREFIX, a_tag_start_text_to_remove='/',
                                    next_page_select='.pagination .next')


# Kao ni Denai Kashiwada-san to Kao ni Deru Oota-kun
class KashiwadaOhtaDownload(Fall2025AnimeDownload, NewsTemplate):
    title = "Kao ni Denai Kashiwada-san to Kao ni Deru Oota-kun"
    keywords = [title, 'kashiwada ohta', 'Inexpressive Kashiwada and Expressive Oota']
    website = 'https://kashiwada-ohta.com/'
    twitter = 'kashiwada_ohta'
    hashtags = '#柏田さんと太田君'
    folder_name = 'kashiwadaohta'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news__list li',
                                    date_select='.news__date', title_select='.news__link-title', id_select='a',
                                    next_page_select='.next.page-numbers',
                                    date_func=lambda x: x[0:4] + '.' + x[5:7] + '.' + x[7:])


# Mikata ga Yowasugite Hojo Mahou ni Tesshiteita Kyuutei Mahoushi, Tsuihou sarete Saikyou wo Mezashimasu
class HojomahoDownload(Fall2025AnimeDownload, NewsTemplate):
    title = "Mikata ga Yowasugite Hojo Mahou ni Tesshiteita Kyuutei Mahoushi, Tsuihou sarete Saikyou wo Mezashimasu"
    keywords = [title, 'hojomaho', 'The Banished Court Magician Aims to Become the Strongest']
    website = 'https://hojomaho.com/'
    twitter = 'hojomaho'
    hashtags = '補助魔法'
    folder_name = 'hojomaho'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.newsCol',
                                    date_select='.newsCol__date', title_select='.newsCol__title', id_select=None)


# Mugen Gacha
class MugenGachaDownload(Fall2025AnimeDownload, NewsTemplate):
    title = "Mugen Gacha"
    keywords = [title, 'My Gift Lvl 9999 Unlimited Gacha']
    website = 'https://mugengacha.com/'
    twitter = 'mugengacha9999'
    hashtags = ['無限ガチャ', 'unlimitedgacha']
    folder_name = 'mugengacha'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news_item', date_select='time',
                                    title_select='.news_item_title', id_select='a', next_page_select='.nextpostslink')


# Mushoku no Eiyuu
class MushokuEiyuDownload(Fall2025AnimeDownload, NewsTemplate):
    title = "Mushoku no Eiyuu"
    keywords = [title, 'Hero without a Class']
    website = 'https://mushoku-eiyu-anime.com/'
    twitter = 'mushoku_eiyu'
    hashtags = '無職の英雄'
    folder_name = 'mushokueiyu'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='#news .items-center',
                                    date_select='.inline', title_select='p', id_select='a',
                                    next_page_select='.pagination .next', date_func=lambda x: x[0:4] + '.' + x[4:])


# Tomodachi no Imouto ga Ore ni dake Uzai
class ImouzaDownload(Fall2025AnimeDownload, NewsTemplate):
    title = "Tomodachi no Imouto ga Ore ni dake Uzai"
    keywords = [title, 'imouza', 'My Friend\'s Little Sister Has It In for Me!']
    website = 'https://www.imouza-animation.com/'
    twitter = 'imouza_PR'
    hashtags = 'いもウザ'
    folder_name = 'imouza'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.sw-News_Item',
                                    date_select='.sw-News_Date', title_select='.sw-News_Txt', id_select='a',
                                    next_page_select='.nextpostslink')


# Yasei no Last Boss ga Arawareta!
class YaseinoLastBossDownload(Fall2025AnimeDownload, NewsTemplate2):
    title = "Yasei no Last Boss ga Arawareta!"
    keywords = [title, 'A Wild Last Boss Appeared!']
    website = 'https://www.lastboss-anime.com/'
    twitter = 'lastboss_anime'
    hashtags = ['アニメ野生のラスボスが現れた', 'lastbossanime']
    folder_name = 'lastboss'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX)
