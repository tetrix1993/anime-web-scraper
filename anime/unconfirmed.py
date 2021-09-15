import os
import anime.constants as constants
from anime.main_download import MainDownload, NewsTemplate, NewsTemplate2, NewsTemplate3

# Anohana S2 https://10th.anohana.jp/ #あの花 #anohana @anohana_project
# Deaimon https://deaimon.jp/ #であいもん #deaimon @deaimon_anime
# Do It Yourself!! https://diy-anime.com/ #diyアニメ @diy_anime
# Gaikotsu Kishi-sama, Tadaima Isekai e Odekakechuu https://skeleton-knight.com/ #骸骨騎士様 @gaikotsukishi
# Goblin Slayer S2 http://www.goblinslayer.jp/ #ゴブスレ @GoblinSlayer_GA
# Hataraku Maou-sama! https://maousama.jp/ #maousama @anime_maousama
# Isekai Ojisan #いせおじ #異世界おじさん @Isekai_Ojisan
# Isekai Yakkyoku https://isekai-yakkyoku.jp/ #異世界薬局 @isekai_yakkyoku
# Itai no wa https://bofuri.jp/story/ #防振り #bofuri @bofuri_anime
# Kakkou no Iinazuke https://cuckoos-anime.com/ #カッコウの許嫁 @cuckoo_anime
# Koi wa Sekai Seifuku no Ato de https://koiseka-anime.com/ #恋せか @koiseka_anime
# Kono Healer, Mendokusai https://kono-healer-anime.com/ #このヒーラー @kono_healer
# Maou Gakuin no Futekigousha 2nd Season https://maohgakuin.com/ #魔王学院 @maohgakuin
# Shikkakumon no Saikyou Kenja https://shikkakumon.com/ #失格紋 @shikkakumon_PR
# Shokei Shoujo no Virgin Road http://virgin-road.com/ #処刑少女 #shokei_anime @VirginroadAnime
# Summertime Render https://summertime-anime.com/ #サマータイムレンダ #サマレン @summertime_PR
# Vlad Love https://www.vladlove.com/index.html #ぶらどらぶ #vladlove @VLADLOVE_ANIME
# Yama no Susume: Next Summit https://yamanosusume-ns.com/ #ヤマノススメ @yamanosusume


# Unconfirmed Season Anime
class UnconfirmedDownload(MainDownload):
    season = "9999-9"
    season_name = "Unconfirmed"
    folder_name = 'unconfirmed'

    def __init__(self):
        super().__init__()


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
            print("Error in running " + self.__class__.__name__ + ' - News')
            print(e)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('teaser', 'https://pbs.twimg.com/media/ExRRykWU4AEZ6Cy?format=jpg&name=large')
        self.add_to_image_list('teaser_tw', self.PAGE_PREFIX + 'assets/images/pc/teaser/img_kv.png')
        self.download_image_list(folder)


# Deaimon
class DeaimonDownload(UnconfirmedDownload, NewsTemplate2):
    title = 'Deaimon'
    keywords = [title]
    website = 'https://deaimon.jp/'
    twitter = 'deaimon_anime'
    hashtags = ['であいもん', 'deaimon']
    folder_name = 'deaimon'

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
        self.add_to_image_list('kv_tw', 'https://pbs.twimg.com/media/E_T2HaPUUAIwv3-?format=jpg&name=4096x4096')
        self.add_to_image_list('kv_wide', self.PAGE_PREFIX + 'core_sys/images/main/tz/kv.webp')
        # self.add_to_image_list('kv', self.PAGE_PREFIX + 'core_sys/images/news/00000002/block/00000009/00000003.jpg')
        self.add_to_image_list('kv_sp', self.PAGE_PREFIX + 'core_sys/images/main/tz/kv_sp.png')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('div.charWrap img')
            self.image_list = []
            for image in images:
                if image.has_attr('src'):
                    image_url = self.PAGE_PREFIX + image['src']
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Character')
            print(e)


# Do It Yourself!!
class DoItYourselfDownload(UnconfirmedDownload):
    title = 'Do It Yourself!!'
    keywords = [title, 'DIY']
    website = 'https://diy-anime.com/'
    twitter = 'diy_anime'
    hashtags = 'diyアニメ'
    folder_name = 'diy'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index', diff=2)

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news/'
        try:
            page = 0
            stop = False
            news_obj = self.get_last_news_log_object()
            results = []
            curr_news_url = news_url
            while len(curr_news_url) > 0:
                page += 1
                soup = self.get_soup(curr_news_url, decode=True)
                articles = soup.select('li.news_List_Item')
                for article in articles:
                    tag_date = article.find('time', class_='roboto')
                    tag_title = article.find('div', class_='ttl')
                    a_tag = article.find('a')
                    if tag_date and a_tag and a_tag.has_attr('href'):
                        article_id = news_url + a_tag['href']
                        date = self.format_news_date(tag_date.text.strip().replace('/', '.'))
                        if len(date) == 0:
                            continue
                        title = ' '.join(tag_title.text.strip().split())
                        if news_obj and ((news_obj['id'] == article_id and news_obj['title'] == title)
                                         or date < news_obj['date']):
                            stop = True
                            break
                        results.append(self.create_news_log_object(date, title, article_id))

                if stop:
                    break
                next_page = soup.select('div.paging a.next')
                if len(next_page) > 0:
                    try:
                        next_page_num = int(next_page[0]['href'].split('=')[1])
                        if next_page_num == page:
                            break
                        else:
                            curr_news_url = next_page[0]['href']
                    except Exception:
                        break
                else:
                    break
            success_count = 0
            for result in reversed(results):
                process_result = self.create_news_log_from_news_log_object(result)
                if process_result == 0:
                    success_count += 1
            if len(results) > 0:
                self.create_news_log_cache(success_count, results[0])
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - News')
            print(e)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('teaser', 'https://pbs.twimg.com/media/ExRRykWU4AEZ6Cy?format=jpg&name=large')
        self.add_to_image_list('teaser_tw', self.PAGE_PREFIX + 'assets/images/pc/teaser/img_kv.png')
        self.download_image_list(folder)

        template = self.PAGE_PREFIX + 'assets/images/pc/index/img_kv-%s.png'
        self.download_by_template(folder, template, 1)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'assets/images/pc/teaser/img_chara-%s.png'
        self.download_by_template(folder, template, 1, 0)


# Gaikotsu Kishi-sama, Tadaima Isekai e Odekakechuu
class GaikotsuKishiDownload(UnconfirmedDownload):
    title = 'Gaikotsu Kishi-sama, Tadaima Isekai e Odekakechuu'
    keywords = [title, 'Skeleton Knight in Another World', 'Gaikotsukishi']
    website = 'https://skeleton-knight.com/'
    twitter = 'gaikotsukishi'
    hashtags = '骸骨騎士様'
    folder_name = 'gaikotsukishi'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('kv', 'https://aniverse-mag.com/wp-content/uploads/2021/04/key_visual.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('#character img')
            self.image_list = []
            for image in images:
                if image.has_attr('src'):
                    image_url = self.PAGE_PREFIX + image['src']
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Character')
            print(e)

    def download_media(self):
        folder = self.create_media_directory()
        self.download_by_template(folder, self.PAGE_PREFIX + 'img/snap%s.jpg', 1, 1, 4)


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
            print("Error in running " + self.__class__.__name__ + ' - News')
            print(e)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('teaser', 'https://pbs.twimg.com/media/EtDYBThUYAEBIWI?format=jpg&name=4096x4096')
        self.download_image_list(folder)


# Hataraku Maou-sama!
class HatarakuMaousama2Download(UnconfirmedDownload):
    title = 'Hataraku Maou-sama! 2nd Season'
    keywords = [title, 'Maousama', 'The Devil is a Part-Timer!']
    website = 'https://maousama.jp/'
    twitter = 'anime_maousama'
    hashtags = 'maousama'
    folder_name = 'hataraku-maousama2'

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
        self.add_to_image_list('teaser_tw', 'https://pbs.twimg.com/media/EvyqsA_UcAcPT9B?format=jpg&name=large')
        self.add_to_image_list('teaser', self.PAGE_PREFIX + 'assets/img/top/visual.jpg')
        self.download_image_list(folder)


# Isekai Ojisan
class IsekaiOjisanDownload(UnconfirmedDownload):
    title = 'Isekai Ojisan'
    keywords = [title, 'Ojisan In Another World']
    website = 'https://isekaiojisan.com/'
    twitter = 'Isekai_Ojisan'
    hashtags = ['いせおじ', '異世界おじさん']
    folder_name = 'isekaiojisan'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_kv', self.PAGE_PREFIX + 'core_sys/images/main/tz/kv.png')
        self.add_to_image_list('tz_kv2', self.PAGE_PREFIX + 'core_sys/images/main/tz/kv2.png')
        self.add_to_image_list('tz_kv_', self.PAGE_PREFIX + 'core_sys/images/main/tz/kv.jpg')
        self.download_image_list(folder)


# Isekai Yakkyoku
class IsekaiYakkyokuDownload(UnconfirmedDownload, NewsTemplate2):
    title = 'Isekai Yakkyoku'
    keywords = [title]
    website = 'https://isekai-yakkyoku.jp/'
    twitter = 'isekai_yakkyoku'
    hashtags = '異世界薬局'
    folder_name = 'isekai-yakkyoku'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_news(self):
        self.download_template_news(self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('teaser', 'https://pbs.twimg.com/media/E6Rh8S_VcAQWTLG?format=jpg&name=4096x4096')
        self.add_to_image_list('kv', self.PAGE_PREFIX + 'core_sys/images/main/tz/kv.jpg')
        self.download_image_list(folder)

        kv_template = self.PAGE_PREFIX + 'core_sys/images/main/tz/kv%s'
        kv_template1 = kv_template + '.jpg'
        kv_template2 = kv_template + '.png'
        self.download_by_template(folder, [kv_template1, kv_template2], 1, 2)


# Itai no wa Iya nano de Bougyoryoku ni Kyokufuri Shitai to Omoimasu. 2nd Season
class Bofuri2Download(UnconfirmedDownload):
    title = "Itai no wa Iya nano de Bougyoryoku ni Kyokufuri Shitai to Omoimasu. 2nd Season"
    keywords = [title, 'bofuri', "BOFURI: I Don't Want to Get Hurt, so I'll Max Out My Defense.", '2nd']
    website = "https://bofuri.jp/"
    twitter = 'bofuri_anime'
    hashtags = ['bofuri', '#防振り']
    folder_name = 'bofuri2'

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
            articles = soup.select('section.news-data')
            news_obj = self.get_last_news_log_object()
            results = []
            for article in articles:
                tag_date = article.find('div', class_='date')
                tag_title = article.find('div', class_='title')
                a_tag = article.find('a')
                if tag_date and tag_title and a_tag and a_tag.has_attr('href'):
                    article_id = news_url + a_tag['href'].replace('./', '')
                    date = self.format_news_date(tag_date.text.strip().replace('/', '.'))
                    if len(date) == 0:
                        continue
                    title = tag_title.text.strip()
                    if date.startswith('2021.01.04') or (news_obj and
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
            print("Error in running " + self.__class__.__name__ + ' - News')
            print(e)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('animation_works', 'https://pbs.twimg.com/media/ErSRQUmVoAAkgt7?format=jpg&name=large')
        self.add_to_image_list('teaser', 'https://pbs.twimg.com/media/ErSKnRwW8AAjOyU?format=jpg&name=4096x4096')
        self.download_image_list(folder)


# Kakkou no Iinazuke
class KakkounoIinazukeDownload(UnconfirmedDownload, NewsTemplate3):
    title = 'Kakkou no Iinazuke'
    keywords = [title, 'A Couple of Cuckoos']
    website = 'https://cuckoos-anime.com/'
    twitter = 'cuckoo_anime'
    hashtags = 'カッコウの許嫁'
    folder_name = 'kakkou-no-iinazuke'

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
        template = self.PAGE_PREFIX + 'assets/news/kv%s.jpg'
        self.download_by_template(folder, template, 1, 1)

        for i in range(20):
            image_url = self.PAGE_PREFIX + f'assets/top/main-t{i + 1}/vis.jpg'
            result = self.download_image(image_url, f'{folder}/vis{i + 1}')
            if result == -1:
                break

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'assets/top/character/c%s.png'
        self.download_by_template(folder, template, 1)


# Koi wa Sekai Seifuku no Ato de
class KoisekaDownload(UnconfirmedDownload, NewsTemplate):
    title = 'Koi wa Sekai Seifuku no Ato de'
    keywords = [title, 'Koiseka', 'Love After World Domination']
    website = 'https://koiseka-anime.com/'
    twitter = 'koiseka_anime'
    hashtags = ['恋せか', 'koiseka']
    folder_name = 'koiseka'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='li.news_list_item',
                                    date_select='time', title_select='p.article_ttl', id_select='a')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/E-RYA-6VkAUwmYY?format=jpg&name=4096x4096')
        # self.add_to_image_list('kv1_tw', self.PAGE_PREFIX + 'news/wp-content/uploads/2021/08/キービジュアル第1弾.jpg')
        self.download_image_list(folder)

        template = self.PAGE_PREFIX + 'img/top/kv_img%s.jpg'
        self.download_by_template(folder, template, 2, 1)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            self.image_list = []
            images = soup.select('div.chara_media img')
            for image in images:
                if image.has_attr('src') and '/character/' in image['src']:
                    image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Character')
            print(e)


# Kono Healer, Mendokusai
class KonoHealerDownload(UnconfirmedDownload):
    title = 'Kono Healer, Mendokusai'
    keywords = [title, "This Healer's a Handful"]
    website = 'https://kono-healer-anime.com/'
    twitter = 'kono_healer'
    hashtags = 'このヒーラー'
    folder_name = 'kono-healer'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_news(self):
        news_url = self.PAGE_PREFIX
        try:
            soup = self.get_soup(news_url, decode=True)
            articles = soup.select('#nwu_001_t tr')
            news_obj = self.get_last_news_log_object()
            results = []
            for article in articles:
                tag_date = article.find('td', class_='day')
                tag_title = article.find('div', class_='title')
                a_tag = article.find('a')
                if tag_date and tag_title:
                    article_id = ''
                    if a_tag and a_tag.has_attr('href'):
                        article_id = self.PAGE_PREFIX + a_tag['href']
                    date = self.format_news_date(tag_date.text.strip().replace('/', '.'))
                    if len(date) == 0:
                        continue
                    title = tag_title.text.strip()
                    if news_obj and ((news_obj['id'] == article_id and news_obj['title'] == title)
                                     or date < news_obj['date']):
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
            print("Error in running " + self.__class__.__name__ + ' - News')
            print(e)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('teaser', 'https://pbs.twimg.com/media/Ey5yDx_VgAUuHlX?format=jpg&name=large')
        self.add_to_image_list('tz_visual', self.PAGE_PREFIX + 'core_sys/images/main/tz/tz_visual.png')
        self.download_image_list(folder)


# Maou Gakuin no Futekigousha: Shijou Saikyou no Maou no Shiso, Tensei shite Shison-tachi no Gakkou e
class Maohgakuin2Download(UnconfirmedDownload):
    title = "Maou Gakuin no Futekigousha: Shijou Saikyou no Maou no Shiso, Tensei shite Shison-tachi no Gakkou e 2nd Season"
    keywords = [title, 'Maohgakuin', 'The Misfit of Demon King Academy']
    website = "https://maohgakuin.com/"
    twitter = 'maohgakuin'
    hashtags = '魔王学院'
    folder_name = 'maohgakuin2'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news/'
        stop = False
        try:
            results = []
            news_obj = self.get_last_news_log_object()
            for page in range(1, 100, 1):
                page_url = news_url
                if page > 1:
                    page_url = news_url + '?p=' + str(page)
                soup = self.get_soup(page_url, decode=True)
                articles = soup.select('div.news_list li')
                for article in articles:
                    tag_date = article.find('p', class_='date')
                    tag_title = article.find('p', class_='title')
                    a_tag = article.find('a')
                    if tag_date and tag_title and a_tag and a_tag.has_attr('href'):
                        article_id = news_url + a_tag['href'].replace('./', '')
                        date = self.format_news_date(tag_date.text.strip())
                        if len(date) == 0:
                            continue
                        title = ' '.join(tag_title.text.strip().split())
                        if date.startswith('2021.02') or\
                                (news_obj and (news_obj['id'] == article_id or date < news_obj['date'])):
                            stop = True
                            break
                        results.append(self.create_news_log_object(date, title, article_id))
                if stop or len(soup.select('div.news_pager p.next')) == 0:
                    break
            success_count = 0
            for result in reversed(results):
                process_result = self.create_news_log_from_news_log_object(result)
                if process_result == 0:
                    success_count += 1
            if len(results) > 0:
                self.create_news_log_cache(success_count, results[0])
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - News')
            print(e)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('teaser', self.PAGE_PREFIX + 'assets/img/img_main.jpg')
        # self.add_to_image_list('teaser_tw', 'https://pbs.twimg.com/media/EvylQFOVkAID_0B?format=jpg&name=medium')
        self.download_image_list(folder)


# Shikkakumon no Saikyou Kenja
class ShikkakumonDownload(UnconfirmedDownload, NewsTemplate2):
    title = 'Shikkakumon no Saikyou Kenja'
    keywords = [title]
    website = 'https://shikkakumon.com/'
    twitter = 'shikkakumon_PR'
    hashtags = '失格紋'
    folder_name = 'shikkakumon'

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
        self.add_to_image_list('teaser', self.PAGE_PREFIX + 'core_sys/images/main/tz/kv.png')
        self.add_to_image_list('teaser_tw', 'https://pbs.twimg.com/media/EtDguMkU0AQjk4b?format=jpg&name=4096x4096')
        self.download_image_list(folder)


# Shokei Shoujo no Virgin Road
class ShokeiShoujoDownload(UnconfirmedDownload):
    title = 'Shokei Shoujo no Virgin Road'
    keywords = [title]
    website = 'http://virgin-road.com/'
    twitter = 'VirginroadAnime'
    hashtags = ['shokei_anime', '処刑少女']
    folder_name = 'shokeishoujo'

    PAGE_PREFIX = website

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('teaser', self.PAGE_PREFIX + 'core_sys/images/main/tz/kv.png')
        self.add_to_image_list('teaser_tw', 'https://pbs.twimg.com/media/EtDn9lYU0AAKje-?format=jpg&name=4096x4096')
        self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/E6Ur9dWVIAEE3Ee?format=jpg&name=4096x4096')
        self.download_image_list(folder)

        kv_template = self.PAGE_PREFIX + 'core_sys/images/main/tz/kv%s'
        kv_template1 = kv_template + '.jpg'
        kv_template2 = kv_template + '.png'
        self.download_by_template(folder, [kv_template1, kv_template2], 1, 1)

    def download_character(self):
        folder = self.create_character_directory()
        template1 = self.PAGE_PREFIX + 'core_sys/images/main/tz/char_%s.png'
        template2 = self.PAGE_PREFIX + 'core_sys/images/main/tz/char_%sface.png'
        self.download_by_template(folder, [template1, template2], 1, 1, prefix='tz_')


# Summertime Render
class SummertimeRenderDownload(UnconfirmedDownload, NewsTemplate):
    title = 'Summertime Render'
    keywords = [title]
    website = 'https://summertime-anime.com/'
    twitter = 'summertime_PR'
    hashtags = ['サマータイムレンダ', 'サマレン']
    folder_name = 'summertime-render'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='article.md-article__li',
                                    date_select='time', title_select='h5', id_select='a',
                                    next_page_select='ul.pagenation-list li',
                                    next_page_eval_index_class='is__current', next_page_eval_index=-1)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz', self.PAGE_PREFIX + 'wp/wp-content/themes/summertime-teaser/_assets/images/kv/kv_pc.jpg')
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/E63h3z-VEAMtJYy?format=jpg&name=medium')
        self.download_image_list(folder)


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
            print("Error in running " + self.__class__.__name__ + " - Character")
            print(e)


# Yama no Susume: Next Summit
class YamaNoSusume4Download(UnconfirmedDownload):
    title = 'Yama no Susume: Next Summit'
    keywords = [title, "Encouragement of Climb"]
    website = 'https://yamanosusume-ns.com/'
    twitter = 'yamanosusume'
    hashtags = 'ヤマノススメ'
    folder_name = 'yamanosusume4'

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
        news_url = self.PAGE_PREFIX
        try:
            soup = self.get_soup(news_url, decode=True)
            articles = soup.select('#nwu_001_t tr')
            news_obj = self.get_last_news_log_object()
            results = []
            for article in articles:
                tag_date = article.find('td', class_='day')
                tag_title = article.find('div', class_='title')
                a_tag = article.find('a')
                if tag_date and tag_title:
                    article_id = ''
                    if a_tag and a_tag.has_attr('href'):
                        article_id = self.PAGE_PREFIX + a_tag['href']
                    date = self.format_news_date(tag_date.text.strip().replace('/', '.'))
                    if len(date) == 0:
                        continue
                    title = tag_title.text.strip()
                    if news_obj and ((news_obj['id'] == article_id and news_obj['title'] == title)
                                     or date < news_obj['date']):
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
            print("Error in running " + self.__class__.__name__ + ' - News')
            print(e)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('teaser', self.PAGE_PREFIX + 'core_sys/images/main/tz/kv.png')
        self.download_image_list(folder)
