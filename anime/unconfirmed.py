import os
import requests
import anime.constants as constants
from anime.main_download import MainDownload, NewsTemplate, NewsTemplate2, NewsTemplate3

# Anohana S2 https://10th.anohana.jp/ #あの花 #anohana @anohana_project
# ATRI -My Dear Moments- https://atri-anime.com/ #ATRI @ATRI_anime
# Dungeon Meshi https://delicious-in-dungeon.com/ #ダンジョン飯 #deliciousindungeon @dun_meshi_anime
# Eiyuu Kyoushitsu https://eiyukyoushitsu-anime.com/ #英雄教室 #eiyu_anime @eiyu_anime
# Goblin Slayer S2 http://www.goblinslayer.jp/ #ゴブスレ #いせれべ @GoblinSlayer_GA
# Isekai de Cheat Skill wo Te ni Shita Ore wa https://iseleve.com　@iseleve_anime
# Isekai One Turn Kill Neesan https://onekillsister.com/ #一撃姉 @onekillsister
# Isekai Shoukan wa Nidome desu https://isenido.com/ #いせにど @isenido_anime
# Itai no wa https://bofuri.jp/story/ #防振り #bofuri @bofuri_anime
# Jitsu wa Ore, Saikyou deshita? https://jitsuhaoresaikyo-anime.com/ @jitsuoresaikyo
# Kaiko sareta Ankoku Heishi (30-dai) no Slow na Second Life https://ankokuheishi-anime.com/ #暗黒兵士 @ankokuheishi_PR
# Keikenzumi na Kimi to, Keiken Zero na Ore ga, Otsukiai suru Hanashi. https://kimizero.com/ #キミゼロ @kimizero_anime
# Masamune-kun no Revenge R https://masamune-tv.com/ #MASA_A @masamune_tv
# Mato Seihei no Slave https://mabotai.jp/ #魔都精兵のスレイブ #まとスレ @mabotai_kohobu
# Oshi no Ko https://ichigoproduction.com/ #推しの子 @anime_oshinoko
# Otonari ni Ginga https://otonari-anime.com/ #おとなりに銀河 @otonariniginga
# Otonari no Tenshi-sama ni Itsunomanika Dame Ningen ni Sareteita Ken https://otonarino-tenshisama.jp/ #お隣の天使様 @tenshisama_PR
# Slime Taoshite 300-nen, Shiranai Uchi ni Level Max ni Nattemashita 2nd Season https://slime300-anime.com/ #スライム倒して300年 @slime300_PR
# Sousou no Frieren https://frieren-anime.jp/ #フリーレン #frieren @Anime_Frieren
# Spy Kyoushitsu https://spyroom-anime.com/ #スパイ教室 #spyroom #SpyClassroom @spyroom_anime
# Tearmoon Teikoku Monogatari: Dantoudai kara Hajimaru, Hime no Tensei Gyakuten Story https://tearmoon-pr.com/ #ティアムーン @tearmoon_pr
# Tensei Oujo to Tensai Reijou no Mahou Kakumei https://tenten-kakumei.com/ #転天アニメ @tenten_kakumei
# Tonikaku Kawaii S2 http://tonikawa.com/ #トニカクカワイイ #tonikawa @tonikawa_anime
# Vlad Love https://www.vladlove.com/index.html #ぶらどらぶ #vladlove @VLADLOVE_ANIME
# Watashi no Yuri wa Oshigoto desu! https://watayuri-anime.com/ #わたゆり #私の百合はお仕事です @watayuri_anime
# Yamada-kun to Lv999 no Koi wo Suru https://yamadalv999-anime.com/ #山田999 @yamada999_anime
# Yuusha ga Shinda! https://heroisdead.com/ #勇者が死んだ @yuusyagasinda


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


# Eiyuu Kyoushitsu
class EiyuKyoushitsuDownload(UnconfirmedDownload):
    title = 'Eiyuu Kyoushitsu'
    keywords = [title, 'Classroom for Heroes']
    website = 'https://eiyukyoushitsu-anime.com/'
    twitter = 'eiyu_anime'
    hashtags = ['英雄教室', 'eiyu_anime']
    folder_name = 'eiyukyoushitsu'

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
        self.add_to_image_list('eiyukyoushitsu_KV', self.PAGE_PREFIX + 'images/eiyukyoushitsu_KV.jpg')
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
        self.download_image_list(folder)


# Isekai de Cheat Skill wo Te ni Shita Ore wa, Genjitsu Sekai wo mo Musou Suru: Level Up wa Jinsei wo Kaeta
class IseleveDownload(UnconfirmedDownload):
    title = 'Isekai de Cheat Skill wo Te ni Shita Ore wa, Genjitsu Sekai wo mo Musou Suru: Level Up wa Jinsei wo Kaeta'
    keywords = [title, 'I Got a Cheat Skill in Another World and Became Unrivaled in The Real World, Too', 'iseleve']
    website = 'https://www.iseleve.com/'
    twitter = 'iseleve_anime'
    hashtags = 'いせれべ'
    folder_name = 'iseleve'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        # self.download_news()
        self.download_key_visual()
        self.download_media()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz', 'https://pbs.twimg.com/media/FagU_nNVQAAy78W?format=jpg&name=medium')
        self.add_to_image_list('tz_main_visual01', self.PAGE_PREFIX + 'img/main_visual01.jpg')
        self.add_to_image_list('tz_main_visual02', self.PAGE_PREFIX + 'img/main_visual02.png')
        self.download_image_list(folder)

    def download_media(self):
        folder = self.create_media_directory()
        self.image_list = []
        self.add_to_image_list('teaser_coment_img01', self.PAGE_PREFIX + 'img/teaser_coment_img01.jpg')
        self.add_to_image_list('teaser_coment_img02', self.PAGE_PREFIX + 'img/teaser_coment_img02.jpg')
        self.download_image_list(folder)


# Isekai One Turn Kill Nee-san: Ane Douhan no Isekai Seikatsu Hajimemashita
class OneKillSisterDownload(UnconfirmedDownload, NewsTemplate):
    title = 'Isekai One Turn Kill Nee-san: Ane Douhan no Isekai Seikatsu Hajimemashita'
    keywords = [title, 'My One-Hit Kill Sister']
    website = 'https://onekillsister.com/'
    twitter = 'onekillsister'
    hashtags = '一撃姉'
    folder_name = 'onekillsister'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news article',
                                    date_select='.post_time', title_select='.list-title', id_select='a',
                                    date_func=lambda x: x.replace('年', '.').replace('月', '.').replace('日', ''),
                                    news_prefix='?page_id=62')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz', 'https://i0.wp.com/onekillsister.com/wp-content/uploads/2022/07/%E3%83%86%E3%82%A3%E3%82%B5%E3%82%99%E3%83%BC%E3%83%92%E3%82%99%E3%82%B7%E3%82%99%E3%83%A5%E3%82%A2%E3%83%AB.jpg')
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FZxIaC6VsAAOfL0?format=jpg&name=4096x4096')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('.n2-ss-slide-background-image img[src]')
            for image in images:
                if image['src'].startswith('//'):
                    image_url = 'https:' + image['src']
                else:
                    image_url = image['src']
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Isekai Shoukan wa Nidome desu
class IsenidoDownload(UnconfirmedDownload):
    title = 'Isekai Shoukan wa Nidome desu'
    keywords = [title, 'isenido']
    website = 'https://isenido.com/'
    twitter = 'isenido_anime'
    hashtags = 'いせにど'
    folder_name = 'isenido'

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
        self.add_to_image_list('kv-bg', self.PAGE_PREFIX + 'img/kv-bg.jpg')
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FZxImcZUIAAV8uv?format=jpg&name=4096x4096')
        self.download_image_list(folder)


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
            self.print_exception(e, 'News')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('animation_works', 'https://pbs.twimg.com/media/ErSRQUmVoAAkgt7?format=jpg&name=large')
        self.add_to_image_list('teaser', 'https://pbs.twimg.com/media/ErSKnRwW8AAjOyU?format=jpg&name=4096x4096')
        self.add_to_image_list('aprilfools_tw', 'https://pbs.twimg.com/media/FPOV5F5agAE3czc?format=jpg&name=4096x4096')
        self.add_to_image_list('aprilfools_news', self.PAGE_PREFIX + 'assets/news/65a.jpg')
        self.add_to_image_list('aprilfools_top', self.PAGE_PREFIX + 'images/top-visual/2022apr/all.jpg')
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


# Kaiko sareta Ankoku Heishi (30-dai) no Slow na Second Life
class AnkokuHeishiDownload(UnconfirmedDownload):
    title = 'Kaiko sareta Ankoku Heishi (30-dai) no Slow na Second Life'
    keywords = [title]
    website = 'https://ankokuheishi-anime.com/'
    twitter = 'ankokuheishi_PR'
    hashtags = '暗黒兵士'
    folder_name = 'ankokuheishi'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        # self.download_news()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz', 'https://pbs.twimg.com/media/FagSmPnUEAA4PNg?format=jpg&name=medium')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'img/chara_%s.png'
        self.download_by_template(folder, template, 2, 1, prefix='tz_')

    def download_media(self):
        folder = self.create_media_directory()
        self.image_list = []
        self.add_to_image_list('comment_img', self.PAGE_PREFIX + 'img/comment_img.png')
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


# Masamune-kun no Revenge R
class Masamunekun2Download(UnconfirmedDownload, NewsTemplate):
    title = 'Masamune-kun no Revenge R'
    keywords = [title, "Masamune's Revenge", "2nd"]
    website = 'https://masamune-tv.com/'
    twitter = 'masamune_tv'
    hashtags = ['MASA_A']
    folder_name = 'masamune2'

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
        # Paging logic may need update
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news--lineup article',
                                    date_select='.txt--date', title_select='.txt--ttl', id_select='a')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_kv', self.PAGE_PREFIX + '_assets/images/fv/fv@2x.png')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('.chardata img[src]')
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'][1:]
                image_name = 'tz_' + self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Mato Seihei no Slave
class MatoSlaveDownload(UnconfirmedDownload, NewsTemplate):
    title = 'Mato Seihei no Slave'
    keywords = [title, 'Chained Soldier', 'matoslave', 'mabotai']
    website = 'https://mabotai.jp/'
    twitter = 'mabotai_kohobu'
    hashtags = ['魔都精兵のスレイブ', 'まとスレ']
    folder_name = 'matoslave'

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

    # def download_news(self):
    #    self.download_template_news(self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        # self.image_list = []
        # self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FEiqZdFaUAQyOy4?format=jpg&name=900x900')
        # self.download_image_list(folder)

        teaser_template = self.PAGE_PREFIX + 'img/teaser/visual_%s.jpg'
        for i in range(1, 11, 1):
            image_name = f'tz{i}'
            if self.is_image_exists(image_name, folder):
                continue
            image_url = teaser_template % str(i).zfill(2)
            result = self.download_image(image_url, f'{folder}/{image_name}')
            if result == -1:
                break

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.chara-item__visual img[src]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src']
                if 'character/' in image_url:
                    image_name = self.generate_image_name_from_url(image_url, 'character')
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Oshi no Ko
class OshinokoDownload(UnconfirmedDownload, NewsTemplate2):
    title = 'Oshi no Ko'
    keywords = [title, 'oshinoko']
    website = 'https://ichigoproduction.com/'
    twitter = 'anime_oshinoko'
    hashtags = '推しの子'
    folder_name = 'oshinoko'

    PAGE_PREFIX = website

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
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FU0bJsjaAAAE7Bf?format=jpg&name=large')
        self.add_to_image_list('tz_kv', self.PAGE_PREFIX + 'core_sys/images/main/tz/kv.jpg')
        self.download_image_list(folder)


# Otonari ni Ginga
class OtonariniGingaDownload(UnconfirmedDownload, NewsTemplate):
    title = 'Otonari ni Ginga'
    keywords = [title, 'A Galaxy Next Door']
    website = 'https://otonari-anime.com/'
    twitter = 'otonariniginga'
    hashtags = 'おとなりに銀河'
    folder_name = 'otonariniginga'

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
                                    title_select='h3', date_select='time', id_select=None, id_has_id=True,
                                    date_func=lambda x: x[0:4] + '.' + x[5:7] + '.' + x[8:10])

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FRV6mlUVIAAa9xK?format=jpg&name=medium')
        self.add_to_image_list('tz_mainimg', self.PAGE_PREFIX + 'teaser/images/mainimg.png')
        self.download_image_list(folder)


# Otonari no Tenshi-sama ni Itsunomanika Dame Ningen ni Sareteita Ken
class OtonarinoTenshisamaDownload(UnconfirmedDownload, NewsTemplate):
    title = 'Otonari no Tenshi-sama ni Itsunomanika Dame Ningen ni Sareteita Ken'
    keywords = [title, 'The Angel Next Door Spoils Me Rotten']
    website = 'https://otonarino-tenshisama.jp/'
    twitter = 'tenshisama_PR'
    hashtags = 'お隣の天使様'
    folder_name = 'otonarino-tenshisama'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.allNews__item',
                                    title_select='.allNews__title', date_select='.allNews__date',
                                    id_select='a', next_page_select='a.next.page-numbers')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FIQhzRlagAAxK-X?format=jpg&name=large')
        self.add_to_image_list('tz', self.PAGE_PREFIX + 'wordpress/wp-content/themes/otonari/images/mainvisual.jpg')
        self.add_to_image_list('tz2_tw', 'https://pbs.twimg.com/media/FOtPcAMVkAcoYzY?format=jpg&name=4096x4096')
        self.add_to_image_list('aprilfool_0331_A', self.PAGE_PREFIX + 'wordpress/wp-content/uploads/2022/03/aprilfool_0331_A.jpg')
        self.add_to_image_list('aprilfool_all', self.PAGE_PREFIX + 'wordpress/wp-content/uploads/2022/03/aprilfool_all.jpg')
        self.add_to_image_list('tz3', self.PAGE_PREFIX + 'wordpress/wp-content/themes/otonari/images/mainvisual-v2.jpg')
        self.add_to_image_list('tz3_pc', self.PAGE_PREFIX + 'wordpress/wp-content/themes/otonari/images/mainvisual-v2_pc.jpg')
        self.add_to_image_list('tz3_news', self.PAGE_PREFIX + 'wordpress/wp-content/uploads/2022/05/tenshisama_teser3_title.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'wordpress/wp-content/themes/otonari/images/character-%s.png'
        self.download_by_template(folder, template, 1, prefix='tz_')

    def download_media(self):
        folder = self.create_media_directory()
        # self.add_to_image_list('valentine_tw', 'https://pbs.twimg.com/media/FLfDFR8aQAIWt1u?format=jpg&name=large')
        self.add_to_image_list('valentine_chara', 'https://aniverse-mag.com/wp-content/uploads/2022/02/8e5cda5d29024d4bf78d1e9452225fb6-e1644755501739.png')
        self.add_to_image_list('valentine_pos', self.PAGE_PREFIX + 'wordpress/wp-content/uploads/2022/02/valentine_pos.jpg')
        self.add_to_image_list('valentine', self.PAGE_PREFIX + 'wordpress/wp-content/uploads/2022/02/valentine_sp-kabegami.jpg')
        self.download_image_list(folder)

        # Special
        special_folder = folder + '/special'
        if not os.path.exists(special_folder):
            os.makedirs(special_folder)
        special_cache_filepath = special_folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(special_cache_filepath)
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'special/')
            a_tags = soup.select('li.card a[href]')
            for a_tag in reversed(a_tags):
                href = a_tag['href']
                if '/special/' not in href:
                    continue
                if href.endswith('/'):
                    href = href[:-1]
                page_name = href.split('/')[-1]
                if page_name in processed:
                    continue
                page_soup = self.get_soup(a_tag['href'])
                if page_soup is not None:
                    images = page_soup.select('article img[src]')
                    self.image_list = []
                    for image in images:
                        image_url = self.clear_resize_in_url(image['src'])
                        image_name = self.extract_image_name_from_url(image_url)
                        self.add_to_image_list(image_name, image_url)
                    self.download_image_list(special_folder)
                processed.append(page_name)
        except Exception as e:
            self.print_exception(e, 'Special')
        self.create_cache_file(special_cache_filepath, processed, num_processed)


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


# Sousou no Frieren
class FrierenDownload(UnconfirmedDownload):
    title = 'Sousou no Frieren'
    keywords = [title, "Frieren: Beyond Journey's End"]
    website = 'https://frieren-anime.jp/'
    twitter = 'Anime_Frieren'
    hashtags = ['フリーレン', 'frieren']
    folder_name = 'frieren'

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
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FcgQDbKaAAAEBu_?format=jpg&name=4096x4096')
        self.add_to_image_list('index_visual', self.PAGE_PREFIX + 'assets/img/index/visual.jpg')
        self.download_image_list(folder)


# Spy Kyoushitsu
class SpyroomDownload(UnconfirmedDownload, NewsTemplate2):
    title = "Spy Kyoushitsu"
    keywords = [title, "Spy Classroom", "Spyroom"]
    website = 'https://spyroom-anime.com/'
    twitter = 'spyroom_anime'
    hashtags = ['スパイ教室', 'spyroom', 'SpyClassroom']
    folder_name = 'spyroom'

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
        self.add_to_image_list('tz_kv_chara', self.PAGE_PREFIX + 'core_sys/images/main/tz/kv_chara.png')
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FNuvFFSaAAkbDy3?format=jpg&name=4096x4096')
        self.add_to_image_list('home_kv', self.PAGE_PREFIX + 'core_sys/images/main/home/kv.png')
        self.add_to_image_list('tz_kv', self.PAGE_PREFIX + 'core_sys/images/news/00000015/block/00000031/00000005.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'chara/lily.html')
            a_tags = soup.select('#ContentsListUnit02 a[href]')
            for a_tag in a_tags:
                chara_url = self.PAGE_PREFIX + a_tag['href'].replace('../', '')
                chara_name = chara_url.split('/')[-1].replace('.html', '')
                if chara_name in processed:
                    continue
                if chara_name == 'lily':
                    chara_soup = soup
                else:
                    chara_soup = self.get_soup(chara_url)
                if chara_soup is not None:
                    images = chara_soup.select('.chara__img img[src]')
                    for image in images:
                        image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                        image_name = self.extract_image_name_from_url(image_url)
                        self.add_to_image_list(image_name, image_url)
                    if len(self.image_list) > 0:
                        processed.append(chara_name)
                    self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Tearmoon Teikoku Monogatari: Dantoudai kara Hajimaru, Hime no Tensei Gyakuten Story
class TearmoonDownload(UnconfirmedDownload, NewsTemplate):
    title = 'Tearmoon Teikoku Monogatari: Dantoudai kara Hajimaru, Hime no Tensei Gyakuten Story'
    keywords = [title, 'Tearmoon Empire']
    website = 'https://tearmoon-pr.com/'
    twitter = 'tearmoon_pr'
    hashtags = 'ティアムーン'
    folder_name = 'tearmoon'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='ul.news--list li',
                                    date_select='.txt--date', title_select='.txt--ttl', id_select='a')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/Fb9eKCbaIAAj66L?format=jpg&name=large')
        self.download_image_list(folder)

        visual_prefix = self.PAGE_PREFIX + '_assets/images/top/fv/fv_%s_pc.'
        templates = [visual_prefix + 'png', visual_prefix + 'jpg']
        self.download_by_template(folder, templates, 3, 1)

    def download_character(self):
        folder = folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.chardata img[src]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'][1:]
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Tensei Oujo to Tensai Reijou no Mahou Kakumei
class TentenKakumeiDownload(UnconfirmedDownload, NewsTemplate):
    title = 'Tensei Oujo to Tensai Reijou no Mahou Kakumei'
    keywords = [title, 'tenten kakumei', 'The Magical Revolution of the Reincarnated Princess and the Genius Young Lady']
    website = 'https://tenten-kakumei.com/'
    twitter = 'tenten_kakumei'
    hashtags = '転天アニメ'
    folder_name = 'tenten-kakumei'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='article.element',
                                    title_select='.title', date_select='.day', id_select='a',
                                    date_separator='/', news_prefix='news.html', a_tag_prefix=self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('top_visual_01_v_001_pc', self.PAGE_PREFIX + 'images/top/visual_01/v_001_pc.jpg')
        self.download_image_list(folder)

        template = self.PAGE_PREFIX + 'images/news/p_%s.jpg'
        self.download_by_template(folder, template, 3, 1, prefix='news_')

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'chara.html')
            a_tags = soup.select('.chara_list_wrap a[href]')
            for a_tag in a_tags:
                image = a_tag.select('img[src]')
                if len(image) == 0:
                    continue
                front_image_url = self.PAGE_PREFIX + image[0]['src']
                front_image_name = self.extract_image_name_from_url(front_image_url)
                split1 = front_image_name.split('.')[0].split('_')
                if len(split1) == 2 and split1[1].isnumeric() and len(split1[0]) > 0:
                    chara_name = split1[0]
                    if self.is_image_exists(chara_name + '_01', folder):
                        continue
                    image_prefix = self.PAGE_PREFIX + 'images/chara/'
                    self.image_list = []
                    self.add_to_image_list(chara_name + '_01', image_prefix + f'list01/{chara_name}_01.png')
                    self.add_to_image_list(chara_name + '_02', image_prefix + f'{chara_name}_02.png')
                    self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Tonikaku Kawaii S2
class Tonikawa2Download(UnconfirmedDownload, NewsTemplate):
    title = "Tonikaku Kawaii 2nd Season"
    keywords = [title, "Tonikawa", "Cawaii", "Fly Me to the Moon", "Over the Moon for You", "2nd"]
    website = 'http://tonikawa.com/'
    twitter = 'tonikawa_anime'
    hashtags = ['トニカクカワイイ', 'tonikawa']
    folder_name = 'tonikawa2'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='div.archive li',
                                    date_select='.date', title_select='.title p', id_select='a',
                                    a_tag_prefix=self.PAGE_PREFIX, a_tag_start_text_to_remove='/',
                                    stop_date='2021.10.08')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FDf9oGkaIAE7jnd?format=jpg&name=large')
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
            self.print_exception(e, 'Character')


# Watashi no Yuri wa Oshigoto desu!
class WatayuriDownload(UnconfirmedDownload):
    title = 'Watashi no Yuri wa Oshigoto desu!'
    keywords = [title, 'watayuri', 'Yuri is My Job!']
    website = 'https://watayuri-anime.com/'
    twitter = 'watayuri_anime'
    hashtags = ['わたゆり', '私の百合はお仕事です']
    folder_name = 'watayuri'

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
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FStxiD1VIAEX1nk?format=jpg&name=4096x4096')
        self.add_to_image_list('tz_mv1', self.PAGE_PREFIX + 'assets/img/top/mv1.jpg')
        self.add_to_image_list('tz_mv2', self.PAGE_PREFIX + 'assets/img/top/mv2.jpg')
        self.download_image_list(folder)


# Yamada-kun to Lv999 no Koi wo Suru
class Yamada999Download(UnconfirmedDownload, NewsTemplate):
    title = 'Yamada-kun to Lv999 no Koi wo Suru'
    keywords = [title, 'My Love Story with Yamada-kun at Lv999']
    website = 'https://yamadalv999-anime.com/'
    twitter = 'yamada999_anime'
    hashtags = '山田999'
    folder_name = 'yamada999'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='li.c-news__item',
                                    date_select='.c-news__item-date', title_select='.c-news__item-ttl',
                                    id_select='.c-news__item-link', a_tag_prefix=news_url, paging_type=1,
                                    date_func=lambda x: '20' + x, a_tag_start_text_to_remove='./',
                                    next_page_select='.c-pagination__count-item',
                                    next_page_eval_index_class='is-current', next_page_eval_index=-1)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_aniverse', 'https://aniverse-mag.com/wp-content/uploads/2022/09/259436eb01ba6f500f1c86345c70f63d.jpg')
        self.add_to_image_list('teaser_kv', self.PAGE_PREFIX + 'teaser/img/top/kv.jpg')
        self.download_image_list(folder)


# Yuusha ga Shinda!
class YuushagaShindaDownload(UnconfirmedDownload):
    title = 'Yuusha ga Shinda!: Murabito no Ore ga Hotta Otoshiana ni Yuusha ga Ochita Kekka.'
    keywords = [title, 'The Legendary Hero Is Dead!']
    website = 'https://heroisdead.com/'
    twitter = 'yuusyagasinda'
    hashtags = '勇者が死んだ'
    folder_name = 'yuushagashinda'

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
        self.add_to_image_list('tz_aniverse', 'https://aniverse-mag.com/wp-content/uploads/2022/04/4576fa0e88a0464f6a9b6e8844e05dbd-e1651058246996.jpg')
        self.add_to_image_list('tz_visual_01_chara', self.PAGE_PREFIX + 'img/teaser/visual_01_chara.png')
        self.download_image_list(folder)
