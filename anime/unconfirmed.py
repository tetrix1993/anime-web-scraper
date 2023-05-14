import os
import requests
import anime.constants as constants
from anime.main_download import MainDownload, NewsTemplate, NewsTemplate2, NewsTemplate3

# Akuyaku Reijou Level 99 https://akuyakulv99-anime.com/ #akuyakuLV99 @akuyakuLV99
# Anohana S2 https://10th.anohana.jp/ #あの花 #anohana @anohana_project
# ATRI -My Dear Moments- https://atri-anime.com/ #ATRI @ATRI_anime
# Buta no Liver wa Kanetsu Shiro https://butaliver-anime.com/ #豚レバ @butaliver_anime
# Dekoboko Majo no Oyako Jijou https://dekoboko-majo-anime.jp/ @DEKOBOKO_anime #でこぼこ魔女の親子事情
# Dosanko Gal wa Namara Menkoi https://dosankogal-pr.com/ #道産子ギャル #どさこい @dosankogal_pr
# Dungeon Meshi https://delicious-in-dungeon.com/ #ダンジョン飯 #deliciousindungeon @dun_meshi_anime
# Giji Harem https://gijiharem.com/ #疑似ハーレム @GijiHarem
# Goblin Slayer S2 http://www.goblinslayer.jp/ #ゴブスレ #いせれべ @GoblinSlayer_GA
# Hoshikuzu Telepath https://hoshitele-anime.com/ #星テレ #hoshitele @hoshitele_anime
# Highspeed Etoile https://highspeed-etoile.com/ #ハイスピ @HSE_Project_PR
# Isekai de Mofumofu Nadenade suru Tame ni Ganbattemasu. https://mohunadeanime.com/ #もふなで @mohunade_anime
# Jitsu wa Ore, Saikyou deshita? https://jitsuhaoresaikyo-anime.com/ @jitsuoresaikyo
# Keikenzumi na Kimi to, Keiken Zero na Ore ga, Otsukiai suru Hanashi. https://kimizero.com/ #キミゼロ @kimizero_anime
# Kekkon Yubiwa Monogatari https://talesofweddingrings-anime.jp/ #結婚指輪物語 @weddingringsPR
# Kimi no Koto ga Daidaidaidaidaisuki na 100-nin no Kanojo https://hyakkano.com/ @hyakkano_anime #100カノ
# Kusuriya no Hitorigoto https://kusuriyanohitorigoto.jp/ #薬屋のひとりごと @kusuriya_PR
# Lv1 Maou to One Room Yuusha https://lv1room.com/ #lv1room @Lv1room
# Seijo no Maryoku wa Bannou Desu S2 https://seijyonomaryoku.jp/ #seijyonoanime @seijyonoanime
# Seiken Gakuin no Makentsukai https://seikengakuin.com/ #聖剣学院の魔剣使い #せまつか @SEIKEN_MAKEN
# Shy https://shy-anime.com/ #SHY_hero @SHY_off
# Slime Taoshite 300-nen, Shiranai Uchi ni Level Max ni Nattemashita 2nd Season https://slime300-anime.com/ #スライム倒して300年 @slime300_PR
# Tensei shitara Dainana Ouji Datta node, Kimama ni Majutsu wo Kiwamemasu https://dainanaoji.com/ #第七王子 @dainanaoji_pro
# Unnamed Memory https://unnamedmemory.com/ #UnnamedMemory #アンメモ @Project_UM
# Vlad Love https://www.vladlove.com/index.html #ぶらどらぶ #vladlove @VLADLOVE_ANIME
# Yoru no Kurage wa Oyogenai https://yorukura-anime.com/ #ヨルクラ #yorukura_anime @yorukura_anime
# Yozakura-san Chi no Daisakusen https://mission-yozakura-family.com/ #夜桜さんちの大作戦 #MissionYozakuraFamily @OfficialHitsuji


# Unconfirmed Season Anime
class UnconfirmedDownload(MainDownload):
    season = "9999-9"
    season_name = "Unconfirmed"
    folder_name = 'unconfirmed'

    def __init__(self):
        super().__init__()


# Akuyaku Reijou Level 99
class AkuyakuLv99Download(UnconfirmedDownload):
    title = 'Akuyaku Reijou Level 99'
    keywords = [title, 'Villainess Level 99']
    website = 'https://akuyakulv99-anime.com/'
    twitter = 'akuyakuLV99'
    hashtags = 'akuyakuLV99'
    folder_name = 'akuyakulv99'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/Fr-S3r0aQAAH2xA?format=jpg&name=medium')
        self.add_to_image_list('tzkv', self.PAGE_PREFIX + 'core_sys/images/main/home/tzkv.png')
        self.download_image_list(folder)


# Ano Hi Mita Hana no Namae wo Bokutachi wa Mada Shiranai. 10th Anniversary Project
class Anohana2Download(UnconfirmedDownload):
    title = 'Ano Hi Mita Hana no Namae wo Bokutachi wa Mada Shiranai. 10th Anniversary Project'
    keywords = [title, 'Anohana', 'The Flower We Saw That Day']
    website = 'https://10th.anohana.jp/'
    twitter = 'anohana_project'
    hashtags = ['anohana', 'あの花']
    folder_name = 'anohana2'
    enabled = False

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
        news_url = self.PAGE_PREFIX + 'news/'
        stop = False
        try:
            results = []
            news_obj = self.get_last_news_log_object()
            page_url = news_url
            for page in range(1, 100, 1):
                soup = self.get_soup(page_url, decode=True)
                lis = soup.select('div.news_list ul li.news_list__item')
                for li in lis:
                    tag_date = li.find('p', class_='news_date')
                    tag_title = li.find('p', class_='news_title')
                    a_tag = li.find('a')
                    if tag_date and tag_title:
                        article_id = ''
                        if a_tag and a_tag.has_attr('href'):
                            article_id = news_url + a_tag['href'].replace('./', '').split('&p=')[0]
                        date = self.format_news_date(tag_date.text.strip())
                        if len(date) == 0:
                            continue
                        title = tag_title.text.strip()
                        if date.startswith('2020') or (news_obj and
                                                       ((news_obj['id'] == article_id and news_obj['title'] == title)
                                                        or date < news_obj['date'])):
                            stop = True
                            break
                        results.append(self.create_news_log_object(date, title, article_id))
                if stop:
                    break
                btn_next = soup.find('p', class_='btn_next')
                if btn_next is None:
                    break
                btn_next_a_tag = btn_next.find('a')
                if btn_next_a_tag is None or not btn_next_a_tag.has_attr('href'):
                    break
                page_url = news_url + btn_next_a_tag['href'].replace('./', '')
            success_count = 0
            for result in reversed(results):
                process_result = self.create_news_log_from_news_log_object(result)
                if process_result == 0:
                    success_count += 1
            if len(results) > 0:
                self.create_news_log_cache(success_count, results[0])
        except Exception as e:
            self.print_exception(e, 'News')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('teaser', 'https://pbs.twimg.com/media/ExRRykWU4AEZ6Cy?format=jpg&name=large')
        self.add_to_image_list('teaser_tw', self.PAGE_PREFIX + 'assets/images/pc/teaser/img_kv.png')
        self.download_image_list(folder)


# ATRI -My Dear Moments-
class AtriDownload(UnconfirmedDownload):
    title = 'ATRI -My Dear Moments-'
    keywords = [title]
    website = 'https://atri-anime.com/'
    twitter = 'ATRI_anime'
    hashtags = 'ATRI'
    folder_name = 'atri'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('ATRI_visual', 'https://ogre.natalie.mu/media/news/comic/2022/0924/ATRI_visual.jpg')
        self.add_to_image_list('kv_kv_wide', self.PAGE_PREFIX + 'assets/img/kv/kv_wide.png')
        self.download_image_list(folder)


# Buta no Liver wa Kanetsu Shiro
class ButaLiverDownload(UnconfirmedDownload, NewsTemplate):
    title = 'Buta no Liver wa Kanetsu Shiro'
    keywords = [title, 'Heat the Pig Liver']
    website = 'https://butaliver-anime.com/'
    twitter = 'butaliver_anime'
    hashtags = '豚レバ'
    folder_name = 'butaliver'

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
        news_url = self.PAGE_PREFIX + 'news/'
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.l-news__list-item',
                                    date_select='.p-in-data', title_select='.p-in-title', id_select='a',
                                    a_tag_prefix=news_url)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.add_to_image_list('tz', self.PAGE_PREFIX + 'assets/img/visual.png')
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FjefZkkVQAAq-_0?format=jpg&name=4096x4096')
        self.download_image_list(folder)


# Dekoboko Majo no Oyako Jijou
class DekobokoMajoDownload(UnconfirmedDownload, NewsTemplate):
    title = 'Dekoboko Majo no Oyako Jijou'
    keywords = [title]
    website = 'https://dekoboko-majo-anime.jp/'
    twitter = 'DEKOBOKO_anime'
    hashtags = ['でこぼこ魔女の親子事情']
    folder_name = 'dekoboko-majo'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='#news article', date_select='time',
                                    title_select='h3', id_select=None, id_has_id=True, news_prefix='')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('teaser-visual', self.PAGE_PREFIX + 'images/teaser-visual.jpg')
        self.add_to_image_list('mainimg', self.PAGE_PREFIX + 'images/mainimg.jpg')
        self.download_image_list(folder)


# Dosanko Gal wa Namara Menkoi
class DosankoGalDownload(UnconfirmedDownload, NewsTemplate):
    title = 'Dosanko Gal wa Namara Menkoi'
    keywords = [title, 'Hokkaido Gals Are Super Adorable!', 'dosakoi']
    website = 'https://dosankogal-pr.com/'
    twitter = 'dosankogal_pr'
    hashtags = ['道産子ギャル', 'どさこい']
    folder_name = 'dosankogal'

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
        # Paging logic not known
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.md-list__news li',
                                    date_select='.txt--date', title_select='.txt--ttl', id_select='a')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FkJnLbAVUAERF5S?format=jpg&name=4096x4096')
        # self.add_to_image_list('tz_news', self.PAGE_PREFIX + 'wp/wp-content/uploads/2022/12/dosankogal_teaser_logoc-scaled-1.jpg')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('.fv--v source[srcset], .fv--v img[src]')
            for image in images:
                if image.has_attr('srcset'):
                    if image['srcset'].endswith('.webp'):
                        continue
                    image_url = self.PAGE_PREFIX + image['srcset'][1:]
                else:
                    image_url = self.PAGE_PREFIX + image['src'][1:]
                if '/images/' not in image_url:
                    continue
                image_name = self.generate_image_name_from_url(image_url, 'images')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')


# Dungeon Meshi
class DungeonMeshiDownload(UnconfirmedDownload, NewsTemplate):
    title = 'Dungeon Meshi'
    keywords = [title, 'Delicious in Dungeon']
    website = 'https://delicious-in-dungeon.com/'
    twitter = 'dun_meshi_anime'
    hashtags = ['ダンジョン飯', 'deliciousindungeon']
    folder_name = 'dungeon-meshi'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.content-entry',
                                    title_select='.entry-title span', date_select='.entry-date span',
                                    id_select=None, id_has_id=True, news_prefix='news.html')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        template = self.PAGE_PREFIX + 'assets/top/t%s/vis.jpg'
        for i in range(1, 10, 1):
            image_name = f'top_t{i}_vis'
            if self.is_image_exists(image_name, folder):
                continue
            image_url = template % str(i)
            result = self.download_image(image_url, folder + '/' + image_name)
            if result == -1:
                break


# Giji Harem
class GijiHaremDownload(UnconfirmedDownload, NewsTemplate2):
    title = "Giji Harem"
    keywords = [title]
    website = 'https://gijiharem.com/'
    twitter = 'GijiHarem'
    hashtags = '疑似ハーレム'
    folder_name = 'gijiharem'

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
        self.download_template_news(self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_kv', self.PAGE_PREFIX + 'core_sys/images/main/tz/kv.jpg')
        self.download_image_list(folder)


# Goblin Slayer 2nd Season
class GoblinSlayer2Download(UnconfirmedDownload):
    title = "Goblin Slayer 2nd Season"
    keywords = [title]
    website = 'http://www.goblinslayer.jp/'
    twitter = 'GoblinSlayer_GA'
    hashtags = 'ゴブスレ'
    folder_name = 'goblin-slayer2'

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
        news_url = self.PAGE_PREFIX + 'news/'
        try:
            soup = self.get_soup(news_url, decode=True)
            articles = soup.select('div.newsbox dl.news')
            news_obj = self.get_last_news_log_object()
            results = []
            for article in articles:
                tag_date = article.find('dt')
                a_tag = article.find('a')
                if tag_date and a_tag and a_tag.has_attr('href'):
                    article_id = a_tag['href']
                    date = self.format_news_date(tag_date.text.strip().replace('/', '.'))
                    if len(date) == 0:
                        continue
                    title = a_tag.text.strip()
                    if date.startswith('2020') or (news_obj and
                                                   (news_obj['id'] == article_id or date < news_obj['date'])):
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

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('teaser', 'https://pbs.twimg.com/media/EtDYBThUYAEBIWI?format=jpg&name=4096x4096')
        self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/FsCxEnRaMAEQ9US?format=jpg&name=4096x4096')
        self.add_to_image_list('kv1', self.PAGE_PREFIX + 'images/top-img.jpg')
        self.download_image_list(folder)


# Hoshikuzu Telepath
class HoshiteleDownload(UnconfirmedDownload, NewsTemplate):
    title = 'Hoshikuzu Telepath'
    keywords = [title, 'Hoshitele']
    website = 'https://hoshitele-anime.com/'
    twitter = 'hoshitele_anime'
    hashtags = ['星テレ', 'hoshitele']
    folder_name = 'hoshitele'

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
        news_url = self.PAGE_PREFIX + 'news/'
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.bl_vertPosts_item',
                                    date_select='.bl_vertPosts_date', title_select='.bl_vertPosts_txt',
                                    id_select='a', a_tag_prefix=news_url, a_tag_start_text_to_remove='./')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.tp_hero img[src]')
            self.image_list = []
            for image in images:
                if '/top/' not in image['src']:
                    continue
                image_name = self.extract_image_name_from_url(image['src'])
                if 'kv' not in image_name:
                    continue
                image_name = self.generate_image_name_from_url(image['src'], 'top')
                image_url = self.PAGE_PREFIX + image['src'].replace('./', '')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

        sub_folder = self.create_custom_directory(folder.split('/')[-1] + '/news')
        cache_filepath = sub_folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        news_url = self.PAGE_PREFIX + 'news/'
        try:
            soup = self.get_soup(news_url)
            items = soup.select('.bl_vertPosts_item a[href]')
            for item in items:
                if not item['href'].startswith('./') or '?id=' not in item['href']:
                    continue
                page_name = item['href'].split('?id=')[-1]
                if len(page_name) == 0:
                    continue
                if page_name in processed:
                    break
                title = item.text.strip()
                if 'ビジュアル' in title:
                    news_soup = self.get_soup(news_url + item['href'].replace('./', ''))
                    if news_soup is not None:
                        images = news_soup.select('.bl_news img[src]')
                        self.image_list = []
                        for image in images:
                            image_url = self.PAGE_PREFIX + image['src'].replace('../', '').split('?')[0]
                            if '/news/' not in image_url:
                                continue
                            image_name = self.generate_image_name_from_url(image_url, 'news')
                            self.add_to_image_list(image_name, image_url)
                        self.download_image_list(sub_folder)
                processed.append(page_name)
        except Exception as e:
            self.print_exception(e, 'Key Visual News')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Highspeed Etoile
class HighspeedEtoileDownload(UnconfirmedDownload, NewsTemplate):
    title = 'Highspeed Etoile'
    keywords = [title]
    website = 'https://highspeed-etoile.com/'
    twitter = 'HSE_Project_PR'
    hashtags = 'ハイスピ'
    folder_name = 'highspeed-etoile'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, news_prefix='', article_select='section.news article',
                                    date_select='time', title_select='h3', id_select=None, id_has_id=True)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/Fponcz0agAs6iMv?format=jpg&name=small')
        self.add_to_image_list('tz2_tw', 'https://pbs.twimg.com/media/FptyYY9aQAIvlvo?format=jpg&name=medium')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('section.introduction div.visual img[src]')
            for image in images:
                image_url = self.PAGE_PREFIX + image['src']
                image_name = self.generate_image_name_from_url(image['src'], None)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'teaser/images/character_%s.png'
        self.download_by_template(folder, template, 2, 1, prefix='tz_')


# Isekai de Mofumofu Nadenade suru Tame ni Ganbattemasu.
class MofunadeDownload(UnconfirmedDownload, NewsTemplate):
    title = 'Isekai de Mofumofu Nadenade suru Tame ni Ganbattemasu.'
    keywords = [title]
    website = 'https://mohunadeanime.com/'
    twitter = 'mohunade_anime'
    hashtags = 'もふなで'
    folder_name = 'mofunade'

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
        news_url = self.PAGE_PREFIX + 'news/'
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.c-news__item',
                                    date_select='.c-news__date', title_select='.c-news__ttl',
                                    id_select='.c-news__link', a_tag_prefix=news_url, paging_type=1,
                                    a_tag_start_text_to_remove='./', next_page_select='.c-Pager__item',
                                    next_page_eval_index_class='-current', next_page_eval_index=-1)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FrwZ2u4aQAMVhBo?format=jpg&name=4096x4096')
        self.add_to_image_list('tz', self.PAGE_PREFIX + 'dist/img/top/kv_img.webp')
        self.download_image_list(folder)


# Jitsu wa Ore, Saikyou deshita?
class JitsuoresaikyouDownload(UnconfirmedDownload, NewsTemplate):
    title = 'Jitsu wa Ore, Saikyou deshita?'
    keywords = [title, 'Am I Actually the Strongest?']
    website = 'https://jitsuhaoresaikyo-anime.com/'
    twitter = 'jitsuoresaikyo'
    hashtags = '実は俺最強でした '
    folder_name = 'jitsuoresaikyo'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()

    def download_episode_preview(self):
        pass
        # self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.c-in-news__item',
                                    date_select='.c-in-news__item-date', title_select='.c-in-news__item-ttl',
                                    id_select='a', a_tag_prefix=self.PAGE_PREFIX, a_tag_start_text_to_remove='../')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FcBIWLTaMAA2GK6?format=jpg&name=large')
        self.add_to_image_list('top_img_main', self.PAGE_PREFIX + 'assets/img/top/img_main.jpg')
        self.download_image_list(folder)


# Keikenzumi na Kimi to, Keiken Zero na Ore ga, Otsukiai suru Hanashi.
class KimizeroDownload(UnconfirmedDownload, NewsTemplate2):
    title = 'Keikenzumi na Kimi to, Keiken Zero na Ore ga, Otsukiai suru Hanashi.'
    keywords = [title, "Kimizero"]
    website = 'https://kimizero.com/'
    twitter = 'kimizero_anime'
    hashtags = 'キミゼロ'
    folder_name = 'kimizero'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FcM7PglaIAA_9Bd?format=jpg&name=4096x4096')
        self.add_to_image_list('tz_kv', self.PAGE_PREFIX + 'core_sys/images/main/tz/kv.jpg')
        self.add_to_image_list('tz_loading_kv', self.PAGE_PREFIX + 'core_sys/images/main/tz/loading_kv.jpg')
        self.download_image_list(folder)

        sub_folder = self.create_custom_directory(folder.split('/')[-1] + '/news')
        cache_filepath = sub_folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'news/')
            while True:
                stop = False
                items = soup.select('#list_01 a[href]')
                for item in items:
                    if not item['href'].startswith('../') or '/news/' not in item['href'] \
                            or not item['href'].endswith('.html'):
                        continue
                    page_name = item['href'].split('/')[-1].split('.html')[0]
                    if page_name in processed:
                        stop = True
                        break
                    title = item.text.strip()
                    if 'ビジュアル' in title or 'イラスト' in title:
                        news_soup = self.get_soup(self.PAGE_PREFIX + item['href'].replace('../', ''))
                        if news_soup is not None:
                            images = news_soup.select('#news_block img[src]')
                            self.image_list = []
                            for image in images:
                                image_url = self.PAGE_PREFIX + image['src'].replace('../', '').split('?')[0]
                                if '/news/' not in image_url:
                                    continue
                                image_name = self.generate_image_name_from_url(image_url, 'news') \
                                    .replace('_block_', '_')
                                self.add_to_image_list(image_name, image_url)
                            self.download_image_list(sub_folder)
                    processed.append(page_name)
                if stop:
                    break
                next_page = soup.select('.nb_nex a[href]')
                if len(next_page) == 0:
                    break
                soup = self.get_soup(self.PAGE_PREFIX + next_page[0]['href'].replace('../', ''))
        except Exception as e:
            self.print_exception(e, 'Key Visual News')
        self.create_cache_file(cache_filepath, processed, num_processed)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('.chara__stand img[src]')
            for image in images:
                if '/chara/' in image['src']:
                    image_url = self.PAGE_PREFIX + image['src']
                    image_name = 'tz_' + self.generate_image_name_from_url(image_url, 'chara')
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Kekkon Yubiwa Monogatari
class KekkonYubiwaDownload(UnconfirmedDownload):
    title = 'Kekkon Yubiwa Monogatari'
    keywords = [title, 'Tales of Wedding Rings']
    website = 'https://talesofweddingrings-anime.jp/'
    twitter = 'weddingringsPR'
    hashtags = '結婚指輪物語'
    folder_name = 'kekkonyubiwa'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        # self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        pass

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz', self.PAGE_PREFIX + 'images/mob02/per_bg.png')
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FsCGtvQaMAEldYZ?format=jpg&name=large')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'images/mob02/chara_%s.png'
        self.download_by_template(folder, template, 2, 1)


# Kimi no Koto ga Daidaidaidaidaisuki na 100-nin no Kanojo
class HyakkanoDownload(UnconfirmedDownload, NewsTemplate):
    title = 'Kimi no Koto ga Daidaidaidaidaisuki na 100-nin no Kanojo'
    keywords = [title, 'The 100 Girlfriends Who Really, Really, Really, Really, Really Love You']
    website = 'https://hyakkano.com/'
    twitter = 'hyakkano_anime'
    hashtags = '100カノ'
    folder_name = 'hyakkano'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        # self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        pass

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz', self.PAGE_PREFIX + 'xUtUy1FY/wp-content/themes/hyakkano_v0/assets/images/common/index/img_mainvisual.png')
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FrGH-A3aUAA0dVE?format=jpg&name=medium')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            images = soup.select('.character-Contents img[src]')
            self.image_list = []
            for image in images:
                image_url = image['src']
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Kusuriya no Hitorigoto
class KusuriyaDownload(UnconfirmedDownload, NewsTemplate):
    title = 'Kusuriya no Hitorigoto'
    keywords = [title, 'The Apothecary Diaries']
    website = 'https://kusuriyanohitorigoto.jp/'
    twitter = 'kusuriya_PR'
    hashtags = ['薬屋のひとりごと']
    folder_name = 'kusuriya'

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
        news_url = self.PAGE_PREFIX + 'news/'
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='li.newsLists__item',
                                    date_select='time', title_select='.newsLists__title', id_select='a',
                                    a_tag_start_text_to_remove='./', a_tag_prefix=news_url)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz', self.PAGE_PREFIX + 'assets/img/top/main/main_visual.jpg')
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/Fo_spzaaIAI3CpS?format=jpg&name=4096x4096')
        self.download_image_list(folder)


# Lv1 Maou to One Room Yuusha
class Lv1RoomDownload(UnconfirmedDownload, NewsTemplate2):
    title = 'Lv1 Maou to One Room Yuusha'
    keywords = [title, 'CLevel 1 Demon Lord and One Room Hero']
    website = 'https://lv1room.com/'
    twitter = 'Lv1room'
    hashtags = 'lv1room'
    folder_name = 'lv1room'

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
        self.download_template_news(self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_kv', self.PAGE_PREFIX + 'core_sys/images/main/tz/kv.webp')
        self.add_to_image_list('tz_kv2', self.PAGE_PREFIX + 'core_sys/images/main/tz/kv2.webp')
        self.download_image_list(folder)


# Seijo no Maryoku wa Bannou Desu 2nd Season
class SeijonoMaryoku2Download(UnconfirmedDownload, NewsTemplate2):
    title = 'Seijo no Maryoku wa Bannou Desu 2nd Season'
    keywords = [title, 'seijonomaryoku', 'seijyonomaryoku', "The Saint's Magic Power is Omnipotent"]
    website = 'https://seijyonomaryoku.jp/'
    twitter = 'seijyonoanime'
    hashtags = ['seijyonoanime', '聖女の魔力は万能です']
    folder_name = 'seijyonomaryoku2'

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
        self.download_template_news(self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_kv', self.PAGE_PREFIX + 'core_sys/images/main/tz/kv.jpg')
        self.add_to_image_list('tz_kv2', self.PAGE_PREFIX + 'core_sys/images/main/tz/kv2.jpg')
        self.download_image_list(folder)


# Seiken Gakuin no Makentsukai
class SeikenGakuinDownload(UnconfirmedDownload):
    title = 'Seiken Gakuin no Makentsukai'
    keywords = [title, 'The Demon Sword Master of Excalibur Academy']
    website = 'https://seikengakuin.com/'
    twitter = 'SEIKEN_MAKEN'
    hashtags = ['聖剣学院の魔剣使い', 'せまつか']
    folder_name = 'seikengakuin'

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
        pass

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz', self.PAGE_PREFIX + 'assets/imgs/index/main_img.jpg')
        self.download_image_list(folder)


# Shy
class ShyDownload(UnconfirmedDownload, NewsTemplate):
    title = 'Shy'
    keywords = [title]
    website = 'https://shy-anime.com/'
    twitter = 'SHY_off'
    hashtags = 'SHY_hero'
    folder_name = 'shy'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-box',
                                    title_select='.news-txt-box', date_select='.news-box-date', id_select='a',
                                    paging_type=0, next_page_select='span.page-numbers', next_page_eval_index=-1,
                                    next_page_eval_index_class='current')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FeTEERvaEAAJmXS?format=jpg&name=large')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        self.image_list = []
        self.add_to_image_list('tz_shy', self.PAGE_PREFIX + 'nE2aBbsJ/wp-content/themes/v0/assets/img/kv/shy.webp')
        self.add_to_image_list('tz_tel', self.PAGE_PREFIX + 'nE2aBbsJ/wp-content/themes/v0/assets/img/kv/tel.webp')
        self.download_image_list(folder)


# Slime Taoshite 300-nen, Shiranai Uchi ni Level Max ni Nattemashita 2nd Season
class Slime3002Download(UnconfirmedDownload, NewsTemplate):
    title = "Slime Taoshite 300-nen, Shiranai Uchi ni Level Max ni Nattemashita 2nd Season"
    keywords = [title, "I've Been Killing Slimes for 300 Years and Maxed Out My Level", "Slime 300", "slime300", '2nd']
    website = 'https://slime300-anime.com'
    twitter = 'slime300_PR'
    hashtags = 'スライム倒して300年'
    folder_name = 'slime300-2'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()

    def download_episode_preview(self):
        pass

    def download_news(self):
        json_url = self.PAGE_PREFIX + '/page-data/news/page-data.json'
        news_obj = self.get_last_news_log_object()
        try:
            json_obj = self.get_json(json_url)
            results = []
            nodes = json_obj['result']['data']['allContentfulNews']['nodes']
            for node in nodes:
                try:
                    date = node['date']
                    if date < '2022.01.04':
                        continue
                    title = node['title']
                    article_id = self.PAGE_PREFIX + '/news/' + node['slug']
                    if news_obj and (news_obj['id'] == article_id or date < news_obj['date']):
                        break
                    results.append(self.create_news_log_object(date, title, article_id))
                except:
                    continue
            success_count = 0
            for result in reversed(results):
                process_result = self.create_news_log_from_news_log_object(result)
                if process_result == 0:
                    success_count += 1
            if len(results) > 0:
                self.create_news_log_cache(success_count, results[0])
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - News")
            print(e)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('announce', self.PAGE_PREFIX + '/static/944a17585cc6d3dccaf125c0201aab71/99383/promo.png')
        self.download_image_list(folder)


# Tensei shitara Dainana Ouji Datta node, Kimama ni Majutsu wo Kiwamemasu
class DainanaojiDownload(UnconfirmedDownload, NewsTemplate):
    title = 'Tensei shitara Dainana Ouji Datta node, Kimama ni Majutsu wo Kiwamemasu'
    keywords = [title, 'I Was Reincarnated as the 7th Prince so I Can Take My Time Perfecting My Magical Ability']
    website = 'https://dainanaoji.com/'
    twitter = 'dainanaoji_pro'
    hashtags = '第七王子'
    folder_name = 'dainanaoji'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='#news-container article',
                                    date_select='.news-box-date', title_select='.news-txt-box', id_select='a',
                                    next_page_select='.pagination .page-numbers',
                                    next_page_eval_index_class='current', next_page_eval_index=-1)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/Fgo-UydUAAAq3qH?format=jpg&name=medium')
        self.add_to_image_list('tz_visual_img', self.PAGE_PREFIX + 'd81Ft6ye/wp-content/themes/v0/assets/img/top/visual/img.webp')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'd81Ft6ye/wp-content/themes/v0/assets/img/character/%s.webp'
        self.download_by_template(folder, template, 1, 0, prefix='tz_')


# Unnamed Memory
class UnnamedMemoryDownload(UnconfirmedDownload, NewsTemplate):
    title = 'Unnamed Memory'
    keywords = [title]
    website = 'https://unnamedmemory.com/'
    twitter = 'Project_UM'
    hashtags = ['UnnamedMemory', 'アンメモ']
    folder_name = 'unnamedmemory'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.content-entry',
                                    title_select='.entry-title span', date_select='.entry-date span',
                                    id_select=None, id_has_id=True, news_prefix='news.html')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/Fj2aPSZVIAEC9LY?format=jpg&name=4096x4096')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.vis source[srcset], .vis img[src]')
            self.image_list = []
            for image in images:
                if image.has_attr('srcset'):
                    image_url = image['srcset']
                else:
                    image_url = image['src']
                if image_url.startswith('./'):
                    image_url = self.PAGE_PREFIX + image_url[2:]
                if '/assets/' not in image_url:
                    continue
                image_name = self.generate_image_name_from_url(image_url, 'assets')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')


# Vlad Love
class VladLoveDownload(UnconfirmedDownload):
    title = 'Vlad Love'
    keywords = [title, "Vladlove"]
    website = 'https://www.vladlove.com/'
    twitter = 'VLADLOVE_ANIME'
    hashtags = ['vladlove', 'ぶらどらぶ']
    folder_name = 'vladlove'
    enabled = False

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('visual01', self.PAGE_PREFIX + 'images/bg_cast.jpg')
        self.add_to_image_list('visual02', self.PAGE_PREFIX + 'images/bg_intro.jpg')
        self.add_to_image_list('visual03', self.PAGE_PREFIX + 'images/bg_character.jpg')
        self.add_to_image_list('visual04', self.PAGE_PREFIX + 'images/img_visual06.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character.html')
            detail_list = soup.find('ul', class_='characterDetailList')
            if detail_list:
                self.image_list = []
                images = detail_list.find_all('img')
                for image in images:
                    if image and image.has_attr('src'):
                        image_url = self.PAGE_PREFIX + image['src']
                        image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                        self.add_to_image_list(image_name, image_url)
                self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Yoru no Kurage wa Oyogenai
class YorukuraDownload(UnconfirmedDownload, NewsTemplate):
    title = 'Yoru no Kurage wa Oyogenai'
    keywords = [title, 'Jellyfish Can’t Swim in the Night']
    website = 'https://yorukura-anime.com/'
    twitter = 'yorukura_anime'
    hashtags = ['ヨルクラ', 'yorukura_anime']
    folder_name = 'yorukura'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, news_prefix='', article_select='#news article',
                                    date_select='time', title_select='h3', id_select=None, id_has_id=True)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        # self.image_list = []
        # self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/Fr6oNgXaIAIDcgR?format=jpg&name=large')
        # self.add_to_image_list('tz', self.PAGE_PREFIX + 'images/mainimg.jpg')
        # self.download_image_list(folder)

        css_url = self.PAGE_PREFIX + 'css/style.min.css'
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            mainslides = soup.select('.mainimg .mainslide[class]')
            _classes = []
            for slide in mainslides:
                for _class in slide['class']:
                    if _class not in ['mainslide', 'swiper-slide']:
                        _classes.append(_class)
                        break
            if len(_classes) > 0:
                self.image_list = []
                css_page = self.get_response(css_url)
                for _class in _classes:
                    search_text = '.mainslide.' + _class + '{background:url('
                    idx = css_page.find(search_text)
                    if idx > 0:
                        right_idx = css_page[idx + len(search_text):].find(')')
                        if right_idx > 0:
                            start_idx = idx + len(search_text)
                            image_url = css_page[start_idx:start_idx + right_idx]
                            if image_url.startswith('../'):
                                image_url = self.PAGE_PREFIX + image_url[3:]
                            image_name = self.extract_image_name_from_url(image_url)
                            self.add_to_image_list(image_name, image_url)
                self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')


# Yozakura-san Chi no Daisakusen
class YozakurasanDownload(UnconfirmedDownload, NewsTemplate2):
    title = 'Yozakura-san Chi no Daisakusen'
    keywords = [title, 'Mission: Yozakura Family']
    website = 'https://mission-yozakura-family.com/'
    twitter = 'OfficialHitsuji'
    hashtags = ['夜桜さんちの大作戦', 'MissionYozakuraFamily']
    folder_name = 'yozakurasan'

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
        self.download_template_news(self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FkJB8aSVEAA5Xd1?format=jpg&name=medium')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.kv__img img[src]')
            self.image_list = []
            for image in images:
                if '/images/' in image['src']:
                    image_url = self.PAGE_PREFIX + image['src']
                    image_name = self.generate_image_name_from_url(image_url, 'images')
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')
