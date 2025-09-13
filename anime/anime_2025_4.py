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


# Alma-chan wa Kazoku ni Naritai
class AlmachanDownload(Fall2025AnimeDownload):
    title = "Alma-chan wa Kazoku ni Naritai"
    keywords = [title, 'almachan' 'Alma-chan Wants to Have a Family!']
    website = 'https://alma-chan.com/'
    twitter = 'alma_chan_pr'
    hashtags = 'アルマちゃん'
    folder_name = 'almachan'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_news(self, print_http_error=False):
        try:
            json_obj = self.get_json(self.PAGE_PREFIX + 'news.json')
            news_obj = self.get_last_news_log_object()
            results = []
            for item in json_obj:
                article_id = self.PAGE_PREFIX + item['url']
                date = item['day']
                title = item['title']
                if news_obj and (news_obj['id'] == article_id or date < news_obj['date']):
                    break
                results.append(self.create_news_log_object(date, title, article_id))
            success_count = 0
            for result in reversed(results):
                process_result = self.create_news_log_from_news_log_object(result)
                if process_result == 0:
                    success_count += 1
            if len(results) > 0:
                self.create_news_log_cache(success_count, results[0])
        except HTTPError as e:
            if print_http_error:
                print(self.__class__.__name__ + ' - 403 Error when retrieving news API.')
        except Exception as e:
            self.print_exception(e, 'News')


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


# Ao no Orchestra Season 2
class Aooke2Download(Fall2025AnimeDownload, NewsTemplate):
    title = 'Ao no Orchestra Season 2'
    keywords = [title, 'Blue Orchestra']
    website = 'https://aooke-anime.com/'
    twitter = 'aooke_anime'
    hashtags = '青のオーケストラ'
    folder_name = 'aooke2'

    PAGE_PREFIX = website
    FINAL_EPISODE = 21
    IMAGES_PER_EPISODE = 4

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news/'
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news_item',
                                    date_select='time', title_select='.ttl',
                                    id_select=None, a_tag_start_text_to_remove='./', a_tag_prefix=news_url,
                                    stop_date='2023.09')


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


# Chanto Suenai Kyuuketsuki-chan
class KyuketsukichanDownload(Fall2025AnimeDownload, NewsTemplate):
    title = "Chanto Suenai Kyuuketsuki-chan"
    keywords = [title, 'kyuketsukichan', "Li'l Miss Vampire Can't Suck Right"]
    website = 'https://kyuketsuki-chan.com/'
    twitter = 'kyuketsukichan_'
    hashtags = ['アニメ吸血鬼ちゃん', 'ちゃんと吸えない吸血鬼ちゃん']
    folder_name = 'kyuketsukichan'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.bl_posts_item',
                                    date_select='.bl_posts_date', title_select='.bl_posts_txt', id_select='a',
                                    next_page_select='.next.page-numbers', paging_type=3, paging_suffix='?page=%s')


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


# Egao no Taenai Shokuba desu.
class EgataeDownload(Fall2025AnimeDownload, NewsTemplate):
    title = "Egao no Taenai Shokuba desu."
    keywords = [title, "egatae", "A Mangaka's Weirdly Wonderful Workplace"]
    website = 'https://www.egatae.com/'
    twitter = 'egatae'
    hashtags = 'えがたえ'
    folder_name = 'egatae'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news_item',
                                    date_select='.year', title_select='.ttl p', id_select='a',
                                    next_page_select='.next.page-numbers', paging_type=3, paging_suffix='?page=%s')


# Fumetsu no Anata e Season 3
class FumetsuNoAnatae3Download(Fall2025AnimeDownload, NewsTemplate):
    title = 'Fumetsu no Anata e Season 3'
    keywords = [title, 'To Your Eternity', '3rd']
    website = 'https://www.nhk-character.com/chara/fumetsu/'
    twitter = 'nep_fumetsu'
    hashtags = '不滅のあなたへ'
    folder_name = 'fumetsunoanatae3'

    PAGE_PREFIX = website
    FINAL_EPISODE = 22

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.c-post__list-item',
                                    date_select='.c-post__year', title_select='.c-post__text-hover', id_select='a',
                                    date_func=lambda x: x.replace('年', '.').replace('月', '.').replace('日', ''),
                                    news_prefix='topics/', next_page_select='.next.page-numbers', paging_type=3,
                                    paging_suffix='?page=%s')


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


# Sawaranaide Kotesashi-kun
class KotesashikunDownload(Fall2025AnimeDownload, NewsTemplate):
    title = "Sawaranaide Kotesashi-kun"
    keywords = [title, 'sozaisaishu', "Don't Touch Kotesashi"]
    website = 'https://kotesashikun.deregula.com/'
    twitter = 'kotesashi_anime'
    hashtags = 'アニメ小手指くん'
    folder_name = 'kotesashikun'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-item', id_select='a',
                                    date_select='.news_inner_date', title_select='.newslist_ttl',
                                    next_page_select='.pagination', next_page_eval_index=-1,
                                    next_page_eval_index_compare_page=True)


# Shuumatsu Touring
class ShumatsuTouringDownload(Fall2025AnimeDownload, NewsTemplate):
    title = "Shuumatsu Touring"
    keywords = [title, 'Touring After the Apocalypse']
    website = 'https://shumatsu-touring.jp/'
    twitter = 'shmts_touring'
    hashtags = '終末ツーリング'
    folder_name = 'shumatsutouring'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.p-news__list-item', id_select='a',
                                    date_select='.p-news_article__date', title_select='.p-news_article__title',
                                    a_tag_prefix=self.PAGE_PREFIX, a_tag_start_text_to_remove='/',
                                    next_page_select='.c-pagination__nav.--next', paging_type=1)


# Souzai Saishuka no Isekai Ryokouki
class SozaiSaishuDownload(Fall2025AnimeDownload, NewsTemplate):
    title = "Souzai Saishuka no Isekai Ryokouki"
    keywords = [title, 'sozaisaishu', 'A Gatherer\'s Adventure in Isekai']
    website = 'https://www.sozaisaishu-pr.com/'
    twitter = 'sozaisaishu'
    hashtags = '素材採取家の異世界旅行記'
    folder_name = 'sozaisaishu'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-list', id_select='a',
                                    date_select='.news-list-link__date', title_select='.news-list-link__ttl',
                                    next_page_select='.next.page-numbers', paging_type=3, paging_suffix='?page=%s')


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


# Tondemo Skill de Isekai Hourou Meshi 2
class TondemoSkill2Download(Fall2025AnimeDownload, NewsTemplate):
    title = 'Tondemo Skill de Isekai Hourou Meshi 2'
    keywords = [title, 'Campfire Cooking in Another World with My Absurd Skill Season 2', 'Tonsuki', '2nd']
    website = 'https://tondemoskill-anime.com/'
    twitter = 'tonsuki_anime'
    hashtags = ['とんでもスキル', 'tondemo_skill']
    folder_name = 'tondemoskill2'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news__item',
                                    date_select='.news__item-time', title_select='.news__item-tit',
                                    id_select='a', next_page_select='.wp-pagenavi *',
                                    next_page_eval_index_class='current', next_page_eval_index=-1)


# Towa no Yuugure
class TowanoYuugureDownload(Fall2025AnimeDownload, NewsTemplate):
    title = "Towa no Yuugure"
    keywords = [title, 'Dusk Beyond the End of the World']
    website = 'https://towanoyuugure.com/'
    twitter = 'towanoyuugure'
    hashtags = '永久のユウグレ'
    folder_name = 'towanoyuugure'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news a', date_select='time',
                                    title_select='.ttl', id_select=None)


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
