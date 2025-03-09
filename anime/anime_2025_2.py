from anime.main_download import MainDownload, NewsTemplate, NewsTemplate2, NewsTemplate4
from datetime import datetime, timedelta
from requests.exceptions import HTTPError
from scan import AniverseMagazineScanner
from bs4 import BeautifulSoup
import json
import os


# Spring 2025 Anime
class Spring2025AnimeDownload(MainDownload):
    season = "2025-2"
    season_name = "Spring 2025"
    folder_name = '2025-2'

    def __init__(self):
        super().__init__()


# Aharen-san wa Hakarenai Season 2
class Aharensan2Download(Spring2025AnimeDownload, NewsTemplate):
    title = 'Aharen-san wa Hakarenai Season 2'
    keywords = [title]
    website = 'https://aharen-pr.com/'
    twitter = 'aharen_pr'
    hashtags = '阿波連さん'
    folder_name = 'aharensan2'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.md-li__news',
                                    date_select='time', title_select='.ttl', id_select='a',
                                    next_page_select='.pagination li', next_page_eval_index_class='is__current',
                                    next_page_eval_index=-1)


# Aru Majo ga Shinu Made
class ArumajoDownload(Spring2025AnimeDownload, NewsTemplate2):
    title = 'Aru Majo ga Shinu Made'
    keywords = [title]
    website = 'https://arumajo-anime.com/'
    twitter = 'arumajo_anime'
    hashtags = 'ある魔女が死ぬまで'
    folder_name = 'arumajo'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX)


# Chotto dake Ai ga Omoi Dark Elf ga Isekai kara Oikaketekita
class AiomoDarkElfDownload(Spring2025AnimeDownload, NewsTemplate):
    title = 'Chotto dake Ai ga Omoi Dark Elf ga Isekai kara Oikaketekita'
    keywords = [title, 'Yandere Dark Elf: She Chased Me All the Way From Another World!']
    website = 'https://aiomodarkelf.deregula.com/'
    twitter = 'aiomodarkelf'
    hashtags = '愛重ダークエルフ'
    folder_name = 'aiomodarkelf'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.l_newslist a',
                                    date_select='.newslist_date', title_select='.newslist_ttl', id_select=None,
                                    next_page_select='.pagination', next_page_eval_index_compare_page=True,
                                    next_page_eval_index=-1)


# Danjo no Yuujou wa Seiritsu suru? (Iya, Shinai!!)
class DanjoruDownload(Spring2025AnimeDownload, NewsTemplate):
    title = 'Danjo no Yuujou wa Seiritsu suru? (Iya, Shinai!!)'
    keywords = [title, 'danjoru']
    website = 'https://www.danjoru.com/'
    twitter = 'danjoru_'
    hashtags = 'だんじょる'
    folder_name = 'danjoru'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news_item', date_select='.year',
                                    title_select='.ttl', id_select='a')


# Gorilla no Kami kara Kago sareta Reijou wa Ouritsu Kishidan de Kawaigarareru
class GorillaLadyDownload(Spring2025AnimeDownload, NewsTemplate2):
    title = 'Gorilla no Kami kara Kago sareta Reijou wa Ouritsu Kishidan de Kawaigarareru'
    keywords = [title]
    website = 'https://gorillalady-anime.com/'
    twitter = 'gorilla_bless'
    hashtags = 'ゴリラの加護令嬢'
    folder_name = 'gorillalady'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX)


# Haite Kudasai, Takamine-san
class TakaminesanDownload(Spring2025AnimeDownload, NewsTemplate2):
    title = 'Haite Kudasai, Takamine-san'
    keywords = [title, 'Please Put Them On, Takamine-san']
    website = 'https://takaminesan.com/'
    twitter = 'takamine_anime'
    hashtags = '鷹峰さん'
    folder_name = 'takaminesan'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX)


# Isshun de Chiryou shiteita noni Yakutatazu to Tsuihou sareta Tensai Chiyushi, Yami Healer toshite Tanoshiku Ikiru
class YamiHealerDownload(Spring2025AnimeDownload, NewsTemplate):
    title = 'Isshun de Chiryou shiteita noni Yakutatazu to Tsuihou sareta Tensai Chiyushi, Yami Healer toshite Tanoshiku Ikiru'
    keywords = [title, "The Brilliant Healer's New Life in the Shadows", 'yamihealer']
    website = 'https://sh-anime.shochiku.co.jp/yamihealer/'
    twitter = 'yamihealer'
    hashtags = '闇ヒーラー'
    folder_name = 'yamihealer'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.p-news__item',
                                    date_select='.p-news__item__date', title_select='.p-news__item__ttl',
                                    id_select=None, next_page_select='.c-pager__number', next_page_eval_index=-1,
                                    next_page_eval_index_class='is-active')


# Kakushite! Makina-san!!
class MakinasanDownload(Spring2025AnimeDownload, NewsTemplate):
    title = 'Kakushite! Makina-san!!'
    keywords = [title]
    website = 'https://makinasan-anime.com/'
    twitter = 'makinasan_anime'
    hashtags = 'マキナさん'
    folder_name = 'makinasan'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-list__item', title_select='a',
                                    date_select='.news-list__item-data', id_select='a', news_prefix='news.html',
                                    a_tag_prefix=self.PAGE_PREFIX, date_separator='/')


# Kanchigai no Atelier Meister
class KanchigaiAtelierDownload(Spring2025AnimeDownload, NewsTemplate4):
    title = 'Kanchigai no Atelier Meister'
    keywords = [title, 'The Unaware Atelier Master']
    website = 'https://kanchigai-pr.com/'
    twitter = 'kanchigai_pr'
    hashtags = '勘違いの工房主'
    folder_name = 'kanchigaiatelier'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        json_obj = None
        try:
            json_obj = self.get_json(self.PAGE_PREFIX + 'api/site-data/init')
            if 'stories' not in json_obj:
                return
            for story in json_obj['stories']:
                episode = story['episode'].zfill(2)
                self.image_list = []
                for i in range(len(story['images'])):
                    image_name = episode + '_' + str(i + 1)
                    image_url = story['images'][i]['image_path']
                    self.add_to_image_list(image_name, image_url, to_jpg=True)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)
        return json_obj

    def download_news(self, json_obj=None):
        self.download_template_news(json_url=self.PAGE_PREFIX + 'api/site-data/init')


# Kanpeki Sugite Kawaige ga Nai to Konyaku Haki sareta Seijo wa Ringoku ni Urareru
class KanpekiSeijoDownload(Spring2025AnimeDownload, NewsTemplate):
    title = 'Kanpeki Sugite Kawaige ga Nai to Konyaku Haki sareta Seijo wa Ringoku ni Urareru'
    keywords = [title, 'The Too-Perfect Saint: Tossed Aside by My Fiancé and Sold to Another Kingdom']
    website = 'https://kanpekiseijo-anime.com/'
    twitter = 'kanpekiseijo_pr'
    hashtags = '完璧聖女'
    folder_name = 'kanpekiseijo'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news_item',
                                    date_select='.date_inner', title_select='.ttl', id_select='a',
                                    next_page_select='.next.page-numbers',
                                    date_func=lambda x: x[0:4] + '.' + x[4:9])


# Katainaka no Ossan, Kensei ni Naru
class OssanKenseiDownload(Spring2025AnimeDownload, NewsTemplate2):
    title = 'Katainaka no Ossan, Kensei ni Naru'
    keywords = [title, 'From Old Country Bumpkin to Master Swordsman']
    website = 'https://ossan-kensei.com/'
    twitter = 'ossan_kensei'
    hashtags = 'おっさん剣聖'
    folder_name = 'ossankensei'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX)


# Ninja to Koroshiya no Futarigurashi
class NinkoroDownload(Spring2025AnimeDownload, NewsTemplate2):
    title = 'Ninja to Koroshiya no Futarigurashi'
    keywords = [title]
    website = 'https://ninkoro.jp/'
    twitter = 'ninkoro_anime'
    hashtags = ['にんころ', 'ninkoro']
    folder_name = 'ninkoro'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX)


# Ore wa Seikan Kokka no Akutoku Ryoushu!
class SeikanKokkaDownload(Spring2025AnimeDownload, NewsTemplate):
    title = 'Ore wa Seikan Kokka no Akutoku Ryoushu!'
    keywords = [title, "I'm the Evil Lord of an Intergalactic Empire!"]
    website = 'https://seikankokka-anime.com/'
    twitter = 'akutoku_ryoushu'
    hashtags = '星間国家'
    folder_name = 'seikankokka'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.border-newsBorder',
                                    date_select='a .absolute', title_select='.line-clamp-2',
                                    id_select='a', a_tag_start_text_to_remove='/', a_tag_prefix=self.PAGE_PREFIX,
                                    paging_type=2, next_page_select='a[href] .rotate-180')


# Shiunji-ke no Kodomotachi
class ShinunjiDownload(Spring2025AnimeDownload):
    title = 'Shiunji-ke no Kodomotachi'
    keywords = [title, 'The Shiunji Family Children']
    website = 'https://shiunjifamily.com/'
    twitter = 'shiunji_anime'
    hashtags = ['紫雲寺家の子供たち', 'shiunjifamily']
    folder_name = 'shiunji'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        try:
            results = []
            news_obj = self.get_last_news_log_object()
            news_prefix = self.PAGE_PREFIX + 'news/'
            json_obj = self.get_json(news_prefix + 'newslist.json')
            for item in json_obj:
                if 'date' in item and 'uniqueId' in item and 'title' in item:
                    try:
                        date = item['date']
                    except:
                        continue
                    title = item['title']
                    unique_id = item['uniqueId']
                    if len(unique_id) == 0 and 'directLinkUrl' in item and len(item['directLinkUrl']) > 1:
                        url = self.PAGE_PREFIX + item['directLinkUrl'][1:]
                    else:
                        url = news_prefix + '?id=' + item['uniqueId']
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


# Slime Taoshite 300-nen, Shiranai Uchi ni Level Max ni Nattemashita: Sono Ni
class Slime3002Download(Spring2025AnimeDownload, NewsTemplate):
    title = "Slime Taoshite 300-nen, Shiranai Uchi ni Level Max ni Nattemashita: Sono Ni"
    keywords = [title, "I've Been Killing Slimes for 300 Years and Maxed Out My Level", "Slime 300", "slime300", '2nd']
    website = 'https://slime300-anime.com/'
    twitter = 'slime300_PR'
    hashtags = 'スライム倒して300年'
    folder_name = 'slime300-2'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        pass

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-list li',
                                    date_select='.date', title_select='p:nth-child(2)', id_select='a')


# Summer Pockets
class SamapokeDownload(Spring2025AnimeDownload, NewsTemplate):
    title = 'Summer Pockets'
    keywords = [title, 'samapoke']
    website = 'https://summerpockets-anime.jp/'
    twitter = 'samapoke_anime'
    hashtags = 'サマポケアニメ'
    folder_name = 'samapoke'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.News-cont2',
                                    date_select='.News-cont-date2', title_select='.News-cont-txt2', id_select='a')


# Witch Watch
class WitchWatchDownload(Spring2025AnimeDownload, NewsTemplate):
    title = "Witch Watch"
    keywords = [title]
    website = 'https://witchwatch-anime.com/'
    twitter = 'WITCHWATCHanime'
    hashtags = 'ウィッチウォッチ'
    folder_name = 'witchwatch'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.md-li__topics', title_select='.ttl',
                                    date_select='time', id_select='a', news_prefix='topics')


# Zatsu Tabi: That's Journey
class ZatsuTabiDownload(Spring2025AnimeDownload, NewsTemplate):
    title = "Zatsu Tabi: That's Journey"
    keywords = [title]
    website = 'https://zatsutabi.com/'
    twitter = 'zatsutabi_anime'
    hashtags = 'ざつ旅'
    folder_name = 'zatsutabi'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='article', title_select='.entry-title',
                                    date_select='.entry-date', id_select=None, id_has_id=True, news_prefix='news.html',
                                    a_tag_prefix=self.PAGE_PREFIX + 'news.html#',
                                    date_func=lambda x: x.replace('年', '.').replace('月', '.').replace('日', ''))
