from anime.main_download import MainDownload, NewsTemplate, NewsTemplate2, NewsTemplate3, NewsTemplate4
from datetime import datetime, timedelta
from requests.exceptions import HTTPError
from scan import AniverseMagazineScanner
from bs4 import BeautifulSoup
import json
import os


# Summer 2025 Anime
class Summer2025AnimeDownload(MainDownload):
    season = "2025-3"
    season_name = "Summer 2025"
    folder_name = '2025-3'

    def __init__(self):
        super().__init__()


# 9: Ruler's Crown
class NineDownload(Summer2025AnimeDownload, NewsTemplate):
    title = "9: Ruler's Crown"
    keywords = [title, 'nine']
    website = 'https://nine-anime.marv.jp/'
    twitter = 'info_9_nine_'
    hashtags = ['9ナイン', 'アニメナイン']
    folder_name = 'nine'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.c-news-list__item',
                                    date_select='.date', title_select='.title', id_select='a',
                                    a_tag_prefix=self.PAGE_PREFIX, a_tag_start_text_to_remove='/')


# Bad Girl
class BadGirlDownload(Summer2025AnimeDownload, NewsTemplate4):
    title = 'Bad Girl'
    keywords = [title]
    website = 'https://badgirl-anime.com/'
    twitter = 'badgirl_anime'
    hashtags = ['ばっどがーる', 'badgirl']
    folder_name = 'badgirl'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        json_obj = None
        try:
            json_obj = self.get_json(self.PAGE_PREFIX + 'api/site-data/init', verify=False)
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
        self.download_template_news(json_url=self.PAGE_PREFIX + 'api/site-data/init', verify=False)


# Busamen Gachi Fighter
class BusagachiDownload(Summer2025AnimeDownload, NewsTemplate):
    title = 'Busamen Gachi Fighter'
    keywords = [title, "Uglymug, Epicfighter", "Busagachi"]
    website = 'https://busamen-gachi-fighter.com/'
    twitter = 'busamen_gachi_f'
    hashtags = ['ブサガチ']
    folder_name = 'busagachi'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.archive__list',
                                    date_select='.archive__date p', title_select='.archive__text', id_select='a',
                                    next_page_select='.archive__pagination a', next_page_eval_index=-1,
                                    next_page_eval_index_class='active')


# City The Animation
class CityDownload(Summer2025AnimeDownload, NewsTemplate):
    title = 'City The Animation'
    keywords = [title]
    website = 'https://city-the-animation.com/'
    twitter = 'city_anime_info'
    hashtags = ['アニメCITY', 'animeCITY']
    folder_name = 'city'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        template = self.PAGE_PREFIX + '_assets_kv2/images/story/%s/scene-%s-%s.webp'
        try:
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (episode, episode, str(j + 1).zfill(2))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name, to_jpg=True) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-item', date_select='.news-date',
                                    title_select='.news-title', id_select='a', a_tag_start_text_to_remove='/',
                                    a_tag_prefix=self.PAGE_PREFIX)


# Food Court de, Mata Ashita.
class FoodCourtDownload(Summer2025AnimeDownload, NewsTemplate):
    title = 'Food Court de, Mata Ashita.'
    keywords = [title, 'See You Tomorrow at the Food Court']
    website = 'https://www.foodcourtjk-anime.com/'
    twitter = 'foodcourt_anime'
    hashtags = ['フドあす', 'foodcourtjk']
    folder_name = 'foodcourtjk'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.sw-News_Item', date_select='.date',
                                    title_select='.ttl', id_select='a', next_page_select='.nextpostslink')


# Futari Solo Camp
class FutariSoloCampDownload(Summer2025AnimeDownload, NewsTemplate2):
    title = 'Futari Solo Camp'
    keywords = [title, 'Solo Camping for Two']
    website = 'https://2solocamp-anime.com/'
    twitter = '2solocamp_anime'
    hashtags = 'ふたりソロキャンプ'
    folder_name = 'futarisolocamp'

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


# GaCen Shoujo to Ibunka Kouryuu
class GaCenShoujoDownload(Summer2025AnimeDownload, NewsTemplate2):
    title = 'GaCen Shoujo to Ibunka Kouryuu'
    keywords = [title, 'Cultural Exchange With a Game Centre Girl']
    website = 'https://gacen-girl-anime.com/'
    twitter = 'GaCenGirl_Anime'
    hashtags = 'ゲーセン少女'
    folder_name = 'gacenshoujo'

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


# Grand Blue S2
class GrandBlue2Download(Summer2025AnimeDownload, NewsTemplate2):
    title = 'Grand Blue Season 2'
    keywords = [title, 'Grand Blue Dreaming', '2nd']
    website = 'https://www.grandblue-anime.com/'
    twitter = 'gb_anime'
    hashtags = 'ぐらんぶる'
    folder_name = 'grandblue2'

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


# Isekai Mokushiroku Mynoghra
class MynoghraDownload(Summer2025AnimeDownload, NewsTemplate):
    title = 'Isekai Mokushiroku Mynoghra'
    keywords = [title, 'Apocalypse Bringer Mynoghra']
    website = 'https://mynoghra-anime.com/'
    twitter = 'myap_GCofficial'
    hashtags = 'マイノグーラ'
    folder_name = 'mynoghra'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.bl_news__article_item',
                                    date_select='time', title_select='h3', id_select='a', paging_type=3,
                                    paging_suffix='?page=%s', next_page_select='.next.page-numbers')


# Jidou Hanbaiki ni Umarekawatta Ore wa Meikyuu wo Samayou S2
class Jihanki2Download(Summer2025AnimeDownload, NewsTemplate):
    title = 'Jidou Hanbaiki ni Umarekawatta Ore wa Meikyuu wo Samayou 2nd Season'
    keywords = [title, "jihanki", 'Reborn as a Vending Machine, I Now Wander the Dungeon']
    website = 'https://jihanki-anime.com/'
    twitter = 'jihanki_anime'
    hashtags = ['jihanki', '俺自販機']
    folder_name = 'jihanki2'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 5

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        template = self.PAGE_PREFIX + 'assets/img/story/%s/story_%s_%s.jpg'
        try:
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (episode, episode, str(j + 1).zfill(2))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name, to_jpg=True) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        news_url = 'https://up-info.news/jihanki-anime/2nd/'
        self.download_template_news(page_prefix=news_url, article_select='.modListNews li', title_select='h3',
                                    date_select='time', id_select='a', date_separator='/', news_prefix='')


# Kakkou no Iinazuke S2
class KakkounoIinazuke2Download(Summer2025AnimeDownload, NewsTemplate3):
    title = 'Kakkou no Iinazuke Season 2'
    keywords = [title, 'A Couple of Cuckoos', '2nd']
    website = 'https://cuckoos-anime.com/'
    twitter = 'cuckoo_anime'
    hashtags = 'カッコウの許嫁'
    folder_name = 'cuckoo2'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(self.PAGE_PREFIX)


# Kanojo, Okarishimasu 4th Season
class Kanokari4Download(Summer2025AnimeDownload, NewsTemplate4):
    title = "Kanojo, Okarishimasu 4th Season"
    keywords = [title, "Kanokari", "Rent-a-Girlfriend"]
    website = 'https://kanokari-official.com/'
    twitter = 'kanokari_anime'
    hashtags = ['彼女お借りします', 'かのかり', 'kanokari']
    folder_name = 'kanokari4'

    PAGE_PREFIX = website
    FIRST_EPISODE = 37
    FINAL_EPISODE = 48
    IMAGES_PER_EPISODE = 6

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


# Kaoru Hana wa Rin to Saku
class KaoruHanaDownload(Summer2025AnimeDownload, NewsTemplate):
    title = 'Kaoru Hana wa Rin to Saku'
    keywords = [title, 'The Fragrant Flower Blooms with Dignity', 'Kaoruhana']
    website = 'https://kaoruhana-anime.com/'
    twitter = 'kaoruhana_anime'
    hashtags = '薫る花'
    folder_name = 'kaoruhana'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news_list__item',
                                    date_select='.-date', title_select='.-title', id_select='a',
                                    a_tag_start_text_to_remove='./', a_tag_prefix=self.PAGE_PREFIX + 'news/')


# Kizetsu Yuusha to Ansatsu Hime
class KizetsuYushaDownload(Summer2025AnimeDownload, NewsTemplate):
    title = 'Kizetsu Yuusha to Ansatsu Hime'
    keywords = [title, 'The Shy Hero and the Assassin Princesses']
    website = 'https://kizetsuyusha-anime.com/'
    twitter = 'kzt_toto'
    hashtags = '気絶勇者'
    folder_name = 'kizetsuyusha'

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
                                    date_select='.p-news__date', title_select='.p-news__description', id_select='a',
                                    date_func=lambda x: x[0:4] + '.' + x[5:7] + '.' + x[7:9])


# Koujo Denka no Kateikyoushi
class KoujoDenkaDownload(Summer2025AnimeDownload, NewsTemplate):
    title = 'Koujo Denka no Kateikyoushi'
    keywords = [title, "Private Tutor to the Duke's Daughter", 'Koujodenka']
    website = 'https://koujodenka-anime.com/'
    twitter = 'koujo_anime'
    hashtags = '公女殿下'
    folder_name = 'koujodenka'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.bg-newsItem',
                                    date_select='.text-newsDate', title_select='.text-base.line-clamp-3', id_select='a',
                                    a_tag_start_text_to_remove='/', a_tag_prefix=self.PAGE_PREFIX, paging_type=2,
                                    next_page_select='.h-full.shadow-pagerShadow', next_page_eval_index=-1,
                                    next_page_eval_index_class='pointer-events-none')


# Mattaku Saikin no Tantei to Kitara
class MattanDownload(Summer2025AnimeDownload, NewsTemplate2):
    title = 'Mattaku Saikin no Tantei to Kitara'
    keywords = [title, 'Detectives These Days Are Crazy!']
    website = 'https://mattan-anime.com/'
    twitter = 'mattan_anime'
    hashtags = 'まっ探'
    folder_name = 'mattan'

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


# Mikadono Sanshimai wa Angai, Choroi.
class MikadonoDownload(Summer2025AnimeDownload, NewsTemplate):
    title = 'Mikadono Sanshimai wa Angai, Choroi.'
    keywords = [title, 'Dealing with Mikadono Sisters Is a Breeze']
    website = 'https://mikadono.family/'
    twitter = 'mikadono_anime'
    hashtags = '帝乃三姉妹'
    folder_name = 'mikadono'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.p-news__contents-list-item',
                                    date_select='.p-in-date', title_select='.p-in-title', id_select='a',
                                    a_tag_prefix=self.PAGE_PREFIX + 'news/', paging_type=1,
                                    next_page_select='.p-pagination__list li', next_page_eval_index=-1,
                                    next_page_eval_index_class='is-current')


# Mizu Zokusei no Mahoutsukai
class MizuZokuseiDownload(Summer2025AnimeDownload, NewsTemplate):
    title = 'Mizu Zokusei no Mahoutsukai'
    keywords = [title, 'The Water Magician']
    website = 'https://mizuzokusei-anime.com/'
    twitter = 'anime_mizuzoku'
    hashtags = '水属性'
    folder_name = 'mizuzokusei'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-list .item',
                                    date_select='.date', title_select='.text', id_select='a',
                                    date_func=lambda x: x[0:10])


# Nukitashi the Animation
class NukitashiDownload(Summer2025AnimeDownload, NewsTemplate):
    title = 'Nukitashi the Animation'
    keywords = [title]
    website = 'https://nukiani.com/'
    twitter = 'nukitashi_anime'
    hashtags = ['ぬきたし', 'ぬきアニ']
    folder_name = 'nukitashi'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        # self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.content-entry',
                                    title_select='.entry-title', date_select='.entry-date', id_select=None,
                                    id_has_id=True, news_prefix='news.html',
                                    date_func=lambda x: x[0:4] + '.' + x[4:6] + '.' + x[6:8])


# Onmyou Kaiten Re:Birth
class OnmyoKaitenDownload(Summer2025AnimeDownload, NewsTemplate):
    title = 'Onmyou Kaiten Re:Birth'
    keywords = [title, 'Onmyo Kaiten Re:Birth Verse']
    website = 'https://onmyo-kaiten.com/'
    twitter = 'OnmyoKaiten_PR'
    hashtags = '陰陽廻天'
    folder_name = 'onmyokaiten'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 5

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        # self.download_news()

    def download_episode_preview(self):
        template = self.PAGE_PREFIX + 'assets/img/story/ep%s/img%s.jpg'
        try:
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (str(i + 1), str(j + 1).zfill(2))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name, to_jpg=True) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.bl_posts_item', date_select='time',
                                    title_select='.bl_posts_txt', id_select='a', date_attr='datetime',
                                    date_separator='-')


# Ruri no Houseki
class RurinoHousekiDownload(Summer2025AnimeDownload, NewsTemplate):
    title = 'Ruri no Houseki'
    keywords = [title, 'Ruri Rocks']
    website = 'https://rurinohouseki.com/'
    twitter = 'rurinohouseki'
    hashtags = '瑠璃の宝石'
    folder_name = 'rurinohouseki'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        # self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.p-news__list-item',
                                    date_select='.p-news_article__date', title_select='.p-news_article__title',
                                    id_select='a', a_tag_prefix=self.PAGE_PREFIX, a_tag_start_text_to_remove='/')


# Seishun Buta Yarou wa Santa Claus no Yume wo Minai
class AobutaSantaDownload(Summer2025AnimeDownload, NewsTemplate):
    title = 'Seishun Buta Yarou wa Santa Claus no Yume wo Minai'
    keywords = [title, 'Rascal Does Not Dream of Santa Claus']
    website = 'https://ao-buta.com/santa/'
    twitter = 'aobuta_anime'
    hashtags = '青ブタ'
    folder_name = 'aobutasanta'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.l-list__item',
                                    date_select='.l-list__item-date', title_select='.l-list__item-title',
                                    id_select='a', a_tag_prefix=self.PAGE_PREFIX + 'news/', paging_type=1,
                                    next_page_select='.c-pagination__list li', next_page_eval_index=-1,
                                    next_page_eval_index_class='is-current')


# Silent Witch: Chinmoku no Majo no Kakushigoto
class SilentWitchDownload(Summer2025AnimeDownload, NewsTemplate):
    title = 'Silent Witch: Chinmoku no Majo no Kakushigoto'
    keywords = [title, 'Secrets of the Silent Witch']
    website = 'https://silentwitch.net/'
    twitter = 'SilentWitch_pr'
    hashtags = 'サイレントウィッチ'
    folder_name = 'silentwitch'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        prefix = self.PAGE_PREFIX + 'story/'
        try:
            soup = self.get_soup(prefix)
            stories = soup.select('.p-story_tab li')
            for story in stories:
                try:
                    episode = ''
                    ep_num = story.select('p')[0].text
                    for a in ep_num:
                        if a.isnumeric():
                            episode += a
                    if len(episode) == 0:
                        continue
                    episode = str(int(episode)).zfill(2)
                except:
                    continue
                if 'is-current' in story['class']:
                    ep_soup = soup
                else:
                    try:
                        ep_soup = self.get_soup(prefix + story.select('a[href]')[0]['href'].replace('./', ''))
                    except:
                        continue
                if ep_soup is None:
                    continue
                self.image_list = []
                images = ep_soup.select('ul.swiper-wrapper img[src]')
                for i in range(len(images)):
                    image_url = prefix + images[i]['src']
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url, to_jpg=True)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.l-news__list-item',
                                    date_select='.l-news__list-item-date', title_select='.l-news__list-item-title',
                                    id_select='a', a_tag_prefix=self.PAGE_PREFIX + 'news/')


# Sono Bisque Doll wa Koi wo Suru S2
class Kisekoi2Download(Summer2025AnimeDownload, NewsTemplate):
    title = 'Sono Bisque Doll wa Koi wo Suru Season 2'
    keywords = [title, 'kisekoi', 'My Dress-Up Darling', '2nd']
    website = 'https://bisquedoll-anime.com/'
    twitter = 'kisekoi_anime'
    hashtags = '着せ恋'
    folder_name = 'kisekoi2'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.l-news__list-item',
                                    date_select='.l-news__date', title_select='.l-news__title',
                                    id_select='a', paging_type=1, a_tag_prefix=self.PAGE_PREFIX + 'news/',
                                    stop_date='2024.06', next_page_select='.c-nav__item.--next a',
                                    next_page_eval_index_class='is-disable', next_page_eval_index=-1)


# Tate no Yuusha no Nariagari Season 4
class TateNoYuusha4Download(Summer2025AnimeDownload):
    title = "Tate no Yuusha no Nariagari Season 4"
    keywords = [title, "The Rising of the Shield Hero", "4th"]
    website = "http://shieldhero-anime.jp/"
    twitter = 'shieldheroanime'
    hashtags = ['shieldhero', '盾の勇者の成り上がり']
    folder_name = 'tatenoyuusha4'

    PAGE_PREFIX = website
    FINAL_EPISODE = 13
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        news_url = self.website + 'news/'
        try:
            soup = self.get_soup(news_url, decode=True)
            articles = soup.select('article.p-newspage_item')
            news_obj = self.get_last_news_log_object()
            results = []
            for article in articles:
                tag_date = article.find('span', class_='a')
                tag_title = article.find('h2', class_='txt')
                if tag_date and tag_title and tag_title.has_attr('id'):
                    article_id = tag_title['id'].strip()
                    date = self.format_news_date(tag_date.text.strip())
                    if len(date) == 0:
                        continue
                    title = tag_title.text.strip()
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
        except Exception as e:
            self.print_exception(e, 'News')


# Tsuihousha Shokudou e Youkoso!
class TsuishokuDownload(Summer2025AnimeDownload, NewsTemplate):
    title = 'Tsuihousha Shokudou e Youkoso!'
    keywords = [title, "Welcome to the Outcast's Restaurant!", 'tsuishoku']
    website = 'https://tsuihosha-shokudo.com/'
    twitter = 'tsuishoku_PR'
    hashtags = ['追放者食堂', 'WelcomeToTheOutcastsRestaurant']
    folder_name = 'tsuishoku'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.p-news__list-item',
                                    date_select='.p-news_data__date', title_select='.p-news_data__ttl',
                                    id_select='a', a_tag_prefix=self.PAGE_PREFIX + 'news/',
                                    a_tag_start_text_to_remove='./', paging_type=3, paging_suffix='?page=%s',
                                    next_page_select='.c-pagination__list-item', next_page_eval_index=-1,
                                    next_page_eval_index_class='is-current')


# Tsuyokute New Saga
class TsuyosagaDownload(Summer2025AnimeDownload, NewsTemplate4):
    title = 'Tsuyokute New Saga'
    keywords = [title, 'New Saga', 'Tsuyosaga']
    website = 'https://tsuyosaga-pr.com/'
    twitter = 'tsuyosaga_pr'
    hashtags = 'つよサガ'
    folder_name = 'tsuyosaga'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        # self.download_key_visual()
        # self.download_character()

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

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_aniverse', 'https://aniverse-mag.com/wp-content/uploads/2022/10/1628619ceb9f5f0127d70926036c5ffd.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'wp/wp-content/themes/newsaga/static/character/%s/main.png'
        for i in range(10):
            number = str(i + 1).zfill(2)
            image_name = 'tz_char' + number
            if self.is_image_exists(image_name, folder):
                continue
            image_url = template % number
            result = self.download_image(image_url, folder + '/' + image_name)
            if result == -1:
                break


# Watari-kun no xx ga Houkai Sunzen
class WatarikunDownload(Summer2025AnimeDownload, NewsTemplate2):
    title = 'Watari-kun no xx ga Houkai Sunzen'
    keywords = [title, "Watari-kun's ****** Is about to Collapse"]
    website = 'https://watarikunxx-anime.com/'
    twitter = 'watarikun_anime'
    hashtags = '渡くん'
    folder_name = 'watarikun'

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


# Watashi ga Koibito ni Nareru Wake Nai jan, Muri Muri! (※Muri ja Nakatta!?)
class WatanareDownload(Summer2025AnimeDownload, NewsTemplate):
    title = 'Watashi ga Koibito ni Nareru Wake Nai jan, Muri Muri! (※Muri ja Nakatta!?)'
    keywords = [title, "There's No Freaking Way I'll be Your Lover! Unless...", 'Watanare']
    website = 'https://www.watanare-anime.com/'
    twitter = 'watanare_anime'
    hashtags = 'わたなれ'
    folder_name = 'watanare'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-item',
                                    date_select='.c-card-article__date', title_select='.c-card-article__title',
                                    id_select='a', next_page_select='.c-arrow-btn--next')


# Yuusha Party wo Tsuihou sareta Shiromadoushi, S-Rank Boukensha ni Hirowareru
class TsuihoShiromadoshiDownload(Summer2025AnimeDownload, NewsTemplate):
    title = 'Yuusha Party wo Tsuihou sareta Shiromadoushi, S-Rank Boukensha ni Hirowareru'
    keywords = [title, "Scooped Up by an S-Rank Adventurer!"]
    website = 'https://tsuiho-shiromadoshi.com/'
    twitter = 'tsuiho_anime'
    hashtags = '追放白魔導師'
    folder_name = 'tsuihoshiromadoshi'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.bl_posts_item',
                                    date_select='.bl_posts_date', title_select='.bl_posts_txt', id_select='a',
                                    paging_type=3, paging_suffix='?page=%s', next_page_select='.next.page-numbers')
