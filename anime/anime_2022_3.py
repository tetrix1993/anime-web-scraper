import os
import requests
from anime.main_download import MainDownload, NewsTemplate, NewsTemplate2
from scan import AniverseMagazineScanner, MocaNewsScanner, EeoMediaScanner
from bs4.element import Tag
from datetime import datetime


# Dungeon ni Deai wo Motomeru no wa Machigatteiru Darou ka IV http://danmachi.com/ #danmachi @danmachi_anime
# Engage Kiss https://engage-kiss.com/ #エンゲージキス #EngageKiss @engage_kiss
# Hataraku Maou-sama!! https://maousama.jp/ #maousama @anime_maousama
# Hoshi no Samidare https://hoshinosamidare.jp/ #惑星のさみだれ @AnimeSamidare
# Isekai Meikyuu de Harem wo https://isekai-harem.com/ #異世界迷宮でハーレムを #異世界迷宮 @isekaiharem_ani
# Isekai Ojisan #いせおじ #異世界おじさん @Isekai_Ojisan
# Isekai Yakkyoku https://isekai-yakkyoku.jp/ #異世界薬局 @isekai_yakkyoku
# Kanojo, Okarishimasu 2nd Season https://kanokari-official.com/2nd/ #かのかり #kanokari @kanokari_anime
# Kinsou no Vermeil: Gakeppuchi Majutsushi wa Saikyou no Yakusai to Mahou Sekai wo Tsukisusumu #ヴェルメイユ #vermeil @vermeil_animePR
# Kumichou Musume to Sewagakari https://kumichomusume.com/ #組長娘と世話係 @kumichomusume
# Kuro no Shoukanshi https://kuronoshokanshi.com/ #黒の召喚士 @kuronoshokanshi
# Lycoris Recoil https://lycoris-recoil.com/ #リコリコ #LycorisRecoil @lycoris_recoil
# Made in Abyss: Retsujitsu no Ougonkyou http://miabyss.com/ #miabyss @miabyss_anime
# Mamahaha no Tsurego ga Motokano datta https://tsurekano-anime.com/ #連れカノ #tsurekano @tsurekano
# Overlord IV https://overlord-anime.com/ #overlord_anime #オーバーロード @over_lord_anime
# Prima Doll https://primadoll.jp/ #プリマドール #PrimaDoll @primadoll_pr
# Saikin Yatotta Maid ga Ayashii https://maid-ga-ayashii.com/ #最近雇ったメイドが怪しい @maidga_ayashii
# Shadows House 2nd Season https://shadowshouse-anime.com/
# Soredemo Ayumu wa Yosetekuru https://soreayu.com/ #それあゆ @soreayu_staff
# Tensei Kenja no Isekai Life: Dai-2 no Shokugyou wo Ete, Sekai Saikyou ni Narimashita https://tenseikenja.com #転生賢者 @tenseikenja_PR
# Utawarerumono: Futari no Hakuoro https://utawarerumono.jp/ #うたわれ @UtawareAnime
# Warau Arsnotoria Sun! https://www.arsnotoria-anime.com/ #アルスノ @arsno_anime
# Yofukashi no Uta https://yofukashi-no-uta.com/ #よふかしのうた @yofukashi_pr
# Youkoso Jitsuryoku Shijou Shugi no Kyoushitsu e S2 http://you-zitsu.com/2nd/ #you_zitsu #よう実 @youkosozitsu


# Summer 2022 Anime
class Summer2022AnimeDownload(MainDownload):
    season = "2022-3"
    season_name = "Summer 2022"
    folder_name = '2022-3'

    def __init__(self):
        super().__init__()


# Dungeon ni Deai wo Motomeru no wa Machigatteiru Darou ka IV: Shin Shou - Meikyuu-hen
class Danmachi4Download(Summer2022AnimeDownload):
    title = 'Dungeon ni Deai wo Motomeru no wa Machigatteiru Darou ka IV: Shin Shou - Meikyuu-hen'
    keywords = [title, 'Danmachi', 'Is It Wrong to Try to Pick Up Girls in a Dungeon? IV', '4th']
    website = 'http://danmachi.com/'
    twitter = 'danmachi_anime'
    hashtags = 'danmachi'
    folder_name = 'danmachi4'

    PAGE_PREFIX = website
    FINAL_EPISODE = 25
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()

    def download_episode_preview(self):
        template = self.PAGE_PREFIX + 'story/images/%s_%s.jpg'
        stop = False
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            for j in range(self.IMAGES_PER_EPISODE):
                image_name = episode + '_' + str(j + 1)
                if self.is_image_exists(image_name):
                    continue
                image_url = template % (episode, str(j + 1).zfill(2))
                result = self.download_image(image_url, self.base_folder + '/' + image_name)
                if result == -1:
                    stop = True
                    break
            if stop:
                break

        misc_folder = self.create_custom_directory('misc')
        story_title_template = self.PAGE_PREFIX + 'story/images/title_story%s.png'
        self.download_by_template(misc_folder, story_title_template, 2, 1)

        # YouTube thumbnails
        yt_folder, yt_episodes = self.init_youtube_thumbnail_variables()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/', decode=True)
            storyConts = soup.select('.storyCont')
            for storyCont in storyConts:
                yt_tag = storyCont.select('.youtubeMovie iframe[src]')
                if len(yt_tag) > 0:
                    image = storyCont.select('h3 img[src]')
                    if len(image) > 0:
                        try:
                            episode = str(int(image[0]['src'].split('story')[1].split('.')[0])).zfill(2)
                        except:
                            continue
                        if yt_tag[0]['src'].lower().startswith('https://www.youtube.com/embed/'):
                            yt_id = yt_tag[0]['src'][30:].split('?')[0]
                            self.download_youtube_thumbnail_by_id(yt_id, yt_folder, episode)
        except Exception as e:
            self.print_exception(e, 'YouTube thumbnails')


# Engage Kiss
class EngageKissDownload(Summer2022AnimeDownload, NewsTemplate):
    title = 'Engage Kiss'
    keywords = [title]
    website = 'https://engage-kiss.com/'
    twitter = 'engage_kiss'
    hashtags = ['エンゲージキス', 'EngageKiss']
    folder_name = 'engage-kiss'

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
        yt_folder, yt_episodes = self.init_youtube_thumbnail_variables()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/', decode=True)
            li_tags = soup.select('.page_tab li')
            for li in li_tags:
                ep_soup = None
                try:
                    episode = str(int(li.text)).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_5') and (episode == '01' or episode in yt_episodes):
                    continue
                if li.has_attr('class') and 'current' in li['class']:
                    ep_soup = soup
                else:
                    a_tag = li.find('a[href]')
                    if a_tag is not None:
                        ep_soup = self.get_soup(self.PAGE_PREFIX + a_tag['href'][1:])
                if ep_soup is not None and episode is not None:
                    images = ep_soup.select('.story_slider img[src]')
                    self.image_list = []
                    for i in range(len(images)):
                        image_url = self.PAGE_PREFIX + images[i]['src'][1:]
                        image_name = episode + '_' + str(i + 1)
                        self.add_to_image_list(image_name, image_url)
                    self.download_image_list(self.base_folder)

                    yt_tag = ep_soup.select('.movie_thumb[data-modal]')
                    if len(yt_tag) > 0 and yt_tag[0]['data-modal'].lower().startswith('youtube:'):
                        yt_id = yt_tag[0]['data-modal'][8:]
                        self.download_youtube_thumbnail_by_id(yt_id, yt_folder, episode)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news/'
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='li.news_list__item',
                                    title_select='.news_title', date_select='.news_date', id_select='a',
                                    a_tag_start_text_to_remove='./', a_tag_prefix=news_url, paging_type=1,
                                    date_func=lambda x: x[0:4] + '.' + x[5:],
                                    next_page_select='div.pagination__nav-button.-next',
                                    next_page_eval_index_class='is-disabled', next_page_eval_index=-1)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FOvCuo3VQAUdR2A?format=jpg&name=large')
        self.add_to_image_list('tz_img_main_2x_pc', self.PAGE_PREFIX + 'assets/img/top/img_main_2x_pc.png')
        self.add_to_image_list('top_img_main', self.PAGE_PREFIX + 'assets/img/top/img_main.jpg')
        self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/FRGmZwRVUAE2E5p?format=png&name=900x900')
        self.add_to_image_list('kv2_tw', 'https://pbs.twimg.com/media/FUZvKpqVUAAJ9fc?format=jpg&name=4096x4096')
        self.add_to_image_list('top_img_main_pc', self.PAGE_PREFIX + 'assets/img/top/img_main_pc.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()

        character_url = self.PAGE_PREFIX + 'character/'
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            nav_items = soup.select('.chara_navi__item[data-target]')
            for item in nav_items:
                target = item['data-target']
                if target in processed:
                    continue
                if target == 'shuu':
                    chara_soup = soup
                else:
                    a_tag = item.select('a[href]')
                    if len(a_tag) == 0:
                        continue
                    chara_soup = self.get_soup(character_url + a_tag[0]['href'].replace('./', ''))
                if chara_soup is None:
                    continue
                images = chara_soup.select('.chara_img img[src]')
                self.image_list = []
                for image in images:
                    image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
                    if target == 'kisara':
                        devil_image_url = image_url.replace('img_kisara', 'img_kisara-devil')
                        devil_image_name = self.extract_image_name_from_url(devil_image_url)
                        if devil_image_name != image_name:
                            self.add_to_image_list(devil_image_name, devil_image_url)
                if len(self.image_list) > 0:
                    processed.append(target)
                self.download_image_list(folder)

            '''
            a_tags = soup.select('.chara_navi__item a[href]')
            chara_names = []
            for a_tag in a_tags:
                index = a_tag['href'].rfind('?chara=')
                if index > 0 and len(a_tag['href'][index + 7:]) > 0:
                    chara_names.append(a_tag['href'][index + 7:])
            chara_prefix = self.PAGE_PREFIX + 'assets/img/character/'
            self.image_list = []
            for chara_name in chara_names:
                image_name = 'img_' + chara_name
                image_url = chara_prefix + image_name + '.png'
                self.add_to_image_list('tz_' + image_name, image_url)
            self.download_image_list(folder)
            '''
        except Exception as e:
            self.print_exception(e, 'Character')
        self.create_cache_file(cache_filepath, processed, num_processed)

    def download_media(self):
        folder = self.create_media_directory()

        # Blu-ray
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        bd_urls = ['shop', '01', '02', '03', '04', '05', '06']
        try:
            for i in range(len(bd_urls)):
                bd_url = self.PAGE_PREFIX + 'bddvd/?page=' + bd_urls[i]
                if i > 0 and str(i) in processed:
                    continue
                soup = self.get_soup(bd_url)
                if soup is not None:
                    images = soup.select('.bddvd_wrap img[src]')
                    self.image_list = []
                    for image in images:
                        if not image['src'].endswith('img_nopri_s.jpg')\
                                and not image['src'].endswith('img_nowpri.jpg')\
                                and not image['src'].endswith('arrow.png')\
                                and 'bnr_' not in image['src']:
                            image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                            image_name = 'bddvd_' + self.generate_image_name_from_url(image_url, 'bddvd')
                            self.add_to_image_list(image_name, image_url)
                    if i >= 1:
                        if len(self.image_list) > 1:
                            processed.append(str(i))
                        elif len(self.image_list) == 0:
                            break
                    self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')
        self.create_cache_file(cache_filepath, processed, num_processed)

        # Countdown
        countdown_folder = folder + '/countdown'
        if not os.path.exists(countdown_folder):
            os.makedirs(countdown_folder)
        template = self.PAGE_PREFIX + 'assets/img/special/countdown/%s.jpg'
        month = 6
        day = 18
        for i in range(14):
            image_name = 'img_' + str(month).zfill(2) + str(day).zfill(2)
            image_url = template % image_name
            if not self.is_image_exists(image_name, countdown_folder):
                result = self.download_image(image_url, countdown_folder + '/' + image_name)
                if result == -1:
                    break
            day += 1
            if day == 31:
                month = 7
                day = 1


# Hataraku Maou-sama!!
class HatarakuMaousama2Download(Summer2022AnimeDownload, NewsTemplate):
    title = 'Hataraku Maou-sama!!'
    keywords = [title, 'Maousama', 'The Devil is a Part-Timer!', '2nd']
    website = 'https://maousama.jp/'
    twitter = 'anime_maousama'
    hashtags = 'maousama'
    folder_name = 'hataraku-maousama2'

    PAGE_PREFIX = website
    FINAL_EPISODE = 24

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_external()
        self.download_news()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            stories = soup.select('.storyDetail')
            for story in stories:
                try:
                    episode = str(int(story.select('.story_num')[0].text.replace('#', ''))).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                self.image_list = []
                images = story.select('.story_imgList img[src]')
                for i in range(len(images)):
                    image_url = images[i]['src']
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_external(self):
        jp_title = 'はたらく魔王さま'
        AniverseMagazineScanner(jp_title, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20220708', download_id=self.download_id).run()

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='li.newsList',
                                    date_select='.newsDate', title_select='.newsList_title', id_select='a')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('teaser_tw', 'https://pbs.twimg.com/media/EvyqsA_UcAcPT9B?format=jpg&name=large')
        self.add_to_image_list('teaser', self.PAGE_PREFIX + 'assets/img/top/visual.jpg')
        self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/FGaCXWqVUAA4-Iz?format=jpg&name=large')
        self.add_to_image_list('kv1_moca', 'https://moca-news.net/article/20211212/2021121221300a_/image/001-aiic5e.jpg', is_mocanews=True)
        self.add_to_image_list('kv2_tw', 'https://pbs.twimg.com/media/FU3AmQ3UEAAi_51?format=jpg&name=large')
        self.download_image_list(folder)

        template = self.PAGE_PREFIX + 'assets/img/top/visual%s.jpg'
        self.download_by_template(folder, template, 2, 1)

    def download_character(self):
        folder = self.create_character_directory()
        character_prefix = self.PAGE_PREFIX + 'assets/img/character/'
        template1 = character_prefix + 'character%s_main.png'
        template2 = character_prefix + 'character%s_face1.png'
        template3 = character_prefix + 'character%s_face2.png'
        self.download_by_template(folder, [template1, template2, template3], 2, 1)

    def download_media(self):
        folder = self.create_media_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'bd/')
            images = soup.select('.bdDetailWrap img[src]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                image_name = self.extract_image_name_from_url(image_url)
                if self.is_image_exists(image_name, folder):
                    continue
                if self.is_matching_content_length(image_url, 33850):
                    continue
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


# Hoshi no Samidare
class HoshinoSamidareDownload(Summer2022AnimeDownload):
    title = 'Hoshi no Samidare'
    keywords = [title, 'Lucifer and the Biscuit Hammer']
    website = 'https://hoshinosamidare.jp/'
    twitter = 'AnimeSamidare'
    hashtags = '惑星のさみだれ'
    folder_name = 'hoshinosamidare'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        api_url = 'https://samidare-api.hoshinosamidare.jp/api/story'
        try:
            obj = self.get_json(api_url)
            if 'list' in obj and len(obj['list']) > 0:
                for item in obj['list']:
                    if 'episode_num' not in item or 'thumbnail' not in item:
                        continue
                    try:
                        episode = str(int(item['episode_num'])).zfill(2)
                    except:
                        continue
                    if self.is_image_exists(episode + '_1'):
                        continue
                    self.image_list = []
                    for i in range(len(item['thumbnail'])):
                        image_url = item['thumbnail'][i]
                        image_name = episode + '_' + str(i + 1)
                        self.add_to_image_list(image_name, image_url)
                    self.download_image_list(self.base_folder)
        except Exception as e:
            print(e)

    def download_news(self):
        api_template = 'https://samidare-api.hoshinosamidare.jp/api/article?page=%s&limit=10'
        try:
            results = []
            news_obj = self.get_last_news_log_object()
            stop = False
            for page in range(1, 100, 1):
                api_url = api_template % str(page)
                obj = self.get_json(api_url)
                if 'list' in obj and len(obj['list']) > 0:
                    for item in obj['list']:
                        if 'uuid' not in item or 'title' not in item or 'publish_start_at' not in item:
                            continue
                        dt = item['publish_start_at']
                        if len(dt) < 10:
                            continue
                        uuid = self.PAGE_PREFIX + 'news/' + item['uuid']
                        title = ' '.join(item['title'].strip().split())
                        dt = dt[0:10].replace('-', '.')
                        if news_obj is not None and ((news_obj and news_obj['id'] == uuid) or dt < news_obj['date']):
                            stop = True
                            break
                        results.append(self.create_news_log_object(dt, title, uuid))
                    if stop:
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
            self.print_exception(e, 'News')


# Isekai Meikyuu de Harem wo
class IsekaiMeikyuuHaremDownload(Summer2022AnimeDownload, NewsTemplate):
    title = "Isekai Meikyuu de Harem wo"
    keywords = [title, 'Harem in the Labyrinth of Another World']
    website = 'https://isekai-harem.com/'
    twitter = 'isekaiharem_ani'
    hashtags = ['異世界迷宮', '異世界迷宮でハーレムを']
    folder_name = 'isekai-harem'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 10

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_episode_preview_external()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        image_url_template = self.PAGE_PREFIX + 'img/story/ep%s_img%s.jpg'
        stop = False
        for i in range(self.FINAL_EPISODE):
            no_download_count = 0
            for j in range(self.IMAGES_PER_EPISODE):
                image_name = str(i + 1).zfill(2) + '_' + str(j + 1).zfill(2)
                if not self.is_image_exists(image_name):
                    image_url = image_url_template % (str(i + 1).zfill(2), str(j + 1).zfill(2))
                    result = self.download_image(image_url, self.base_folder + '/' + image_name)
                    if result == -1:
                        no_download_count += 1
                    if no_download_count > 2:
                        stop = True
                        break
            if stop:
                break

        yt_folder, yt_episodes = self.init_youtube_thumbnail_variables(['01'])
        try:
            soup = MainDownload.get_soup(self.PAGE_PREFIX + 'story.html')
            tag = soup.select('#story02')[0]
            episode = '02'
            while tag.nextSibling is not None:
                tag = tag.nextSibling
                if isinstance(tag, Tag):
                    if 'class' not in tag.attrs:
                        continue
                    if tag.name == 'h3' and 'story_title' in tag.attrs['class']:
                        try:
                            episode = str(int(tag.select('.number')[0].text.replace('#', ''))).zfill(2)
                        except:
                            continue
                    elif tag.name == 'div' and 'detail-yt-wrapper' in tag.attrs['class']:
                        if episode in yt_episodes:
                            continue
                        iframe = tag.select('iframe[src]')
                        if len(iframe) > 0:
                            yt_id = iframe[0]['src'].split('/')[-1]
                            self.download_youtube_thumbnail_by_id(yt_id, yt_folder, episode)
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_external(self):
        jp_title = '異世界迷宮でハーレムを'
        AniverseMagazineScanner(jp_title, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20220624', download_id=self.download_id).run()

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, news_prefix='news.html',
                                    article_select='.newslist_contents li', title_select='a', date_select='.date',
                                    date_func=lambda x: x[0:4] + '.' + x[4:], id_select='a',
                                    a_tag_prefix=self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FOqDU-7acAIc7XG?format=jpg&name=medium')
        self.add_to_image_list('tz_aniverse', 'https://aniverse-mag.com/wp-content/uploads/2022/03/5ccd88c2e4c32c6ce3ad9c226feaadaa-e1648178675368.jpg')
        self.add_to_image_list('teaser_mv_img', self.PAGE_PREFIX + 'img/teaser_mv_img.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        templates = [self.PAGE_PREFIX + 'img/chara/illust_%s.png', self.PAGE_PREFIX + 'img/chara/face_%s.png']
        self.download_by_template(folder, templates, 2, 1)

        tz_template = self.PAGE_PREFIX + 'img/teaser_chara_contents%s.png'
        self.download_by_template(folder, tz_template, 2, 1)

    def download_media(self):
        folder = self.create_media_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'bluray.html')
            images = soup.select('div.page_wrapper img[src]')
            self.image_list = []
            for image in images:
                if '/news/' in image['src']:
                    continue
                image_url = self.PAGE_PREFIX + image['src'].split('?')[0]
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


# Isekai Ojisan
class IsekaiOjisanDownload(Summer2022AnimeDownload, NewsTemplate2):
    title = 'Isekai Ojisan'
    keywords = [title, 'Uncle from Another World']
    website = 'https://isekaiojisan.com/'
    twitter = 'Isekai_Ojisan'
    hashtags = ['いせおじ', '異世界おじさん']
    folder_name = 'isekaiojisan'

    PAGE_PREFIX = website
    FINAL_EPISODE = 13
    IMAGES_PER_EPISODE = 8

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_external()
        self.download_episode_preview_guess()
        self.download_news()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        yt_folder, yt_episodes = self.init_youtube_thumbnail_variables(['01'])
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/01.html')
            trs = soup.select('#ContentsListUnit02 tr[class]')
            for tr in trs:
                a_tags = tr.select('a[href]')
                if len(a_tags) == 0:
                    continue
                try:
                    episode = str(int(a_tags[0].text.replace('#', ''))).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1') and episode in yt_episodes:
                    continue
                if 'is-crt' in tr['class']:
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(self.PAGE_PREFIX + a_tags[0]['href'].replace('../', ''))
                if ep_soup is None:
                    continue
                self.image_list = []
                images = ep_soup.select('ul.tp5 img[src]')
                for i in range(len(images)):
                    image_url = self.PAGE_PREFIX + images[i]['src'].split('?')[0].replace('../', '').replace('sn_', '')
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)

                yt_tag = ep_soup.select('.contInner iframe[src]')
                if len(yt_tag) > 0 and 'youtube' in yt_tag[0]['src']:
                    yt_id = yt_tag[0]['src'].split('/')[-1]
                    self.download_youtube_thumbnail_by_id(yt_id, yt_folder, episode)
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_external(self):
        jp_title = '異世界おじさん'
        AniverseMagazineScanner(jp_title, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20220708', download_id=self.download_id).run()

    def download_episode_preview_guess(self):
        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'core_sys/images/contents/%s/block/%s/%s.jpg'
        is_successful = False
        for i in range(1, self.FINAL_EPISODE + 1, 1):
            episode = str(i).zfill(2)
            is_success = False
            if self.is_image_exists(episode + '_1'):
                continue
            first = 23 + (i - 1)
            second = 37 + 3 * (i - 1)
            third = 40 + 6 * (i - 1)
            third2 = 153 + 2 * (i - 1)
            for j in range(self.IMAGES_PER_EPISODE):
                if j < 6:
                    third_ = third + j
                else:
                    if i > 2:
                        third_ = third2 + j - 5
                    else:
                        third_ = third2 + j - 6
                image_url = template % (str(first).zfill(8), str(second).zfill(8), str(third_).zfill(8))
                image_name = episode + '_' + str(j + 1)
                result = self.download_image(image_url, folder + '/' + image_name)
                if result == 0:
                    is_success = True
                    is_successful = True
                elif result == -1:
                    break
            if is_success:
                print(self.__class__.__name__ + ' - Guessed successfully!')
            else:
                if len(os.listdir(folder)) == 0:
                    os.rmdir(folder)
                return
        if len(os.listdir(folder)) == 0:
            os.rmdir(folder)
        return is_successful

    def download_news(self):
        self.download_template_news(self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_kv', self.PAGE_PREFIX + 'core_sys/images/main/tz/kv.png')
        self.add_to_image_list('tz_kv2', self.PAGE_PREFIX + 'core_sys/images/main/tz/kv2.png')
        self.add_to_image_list('tz_kv_', self.PAGE_PREFIX + 'core_sys/images/main/tz/kv.jpg')
        self.add_to_image_list('home_kv', self.PAGE_PREFIX + 'core_sys/images/main/home/kv.jpg')
        self.download_image_list(folder)

        template = self.PAGE_PREFIX + 'core_sys/images/main/tz/kv%s.jpg'
        self.download_by_template(folder, template, 1, 4, prefix='tz_')

    def download_character(self):
        folder = self.create_character_directory()

        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'chara/')
            a_tags = soup.select('#ContentsListUnit01 .nwu_box a[href]')
            for a_tag in a_tags:
                if not a_tag['href'].endswith('.html'):
                    continue
                page_name = a_tag['href'].split('/')[-1].replace('.html', '')
                if page_name in processed:
                    continue
                if page_name == 'index':
                    page_soup = soup
                else:
                    page_soup = self.get_soup(self.PAGE_PREFIX + a_tag['href'].replace('../', ''))
                images = page_soup.select('.chara__img img[src]')
                self.image_list = []
                for image in images:
                    image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                    image_name = self.extract_image_name_from_url(image_url)
                    if 'btn_' in image_name:
                        continue
                    self.add_to_image_list(image_name, image_url)
                if len(self.image_list) > 0:
                    processed.append(page_name)
                self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')
        self.create_cache_file(cache_filepath, processed, num_processed)

    def download_media(self):
        folder = self.create_media_directory()

        # Blu-rays
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        for page in ['01', '02', '03', 'campaign']:
            try:
                if page in processed:
                    continue
                page_url = self.PAGE_PREFIX + 'bd/'
                if page != '01':
                    page_url += page + '.html'
                soup = self.get_soup(page_url)
                images = soup.select('.block_inner img[src]')
                self.image_list = []
                for image in images:
                    if 'nowprinting' in image['src']:
                        continue
                    image_url = self.PAGE_PREFIX + image['src'].replace('../', '').split('?')[0]
                    if '/bddvd/' in image_url:
                        image_name = self.generate_image_name_from_url(image_url, 'bddvd')
                    else:
                        image_name = self.extract_image_name_from_url(image_url)
                    if not self.is_content_length_in_range(image_url, more_than_amount=60000):
                        continue
                    self.add_to_image_list(image_name, image_url)
                if len(self.image_list) > 0:
                    processed.append(page)
                self.download_image_list(folder)
            except Exception as e:
                self.print_exception(e, f'Blu-ray Bonus - {page}')
        self.create_cache_file(cache_filepath, processed, num_processed)

        # Blu-ray Bonus
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'bd/privilege.html')
            images = soup.select('.block_inner img[src]')
            self.image_list = []
            for image in images:
                if 'nowprinting' in image['src']:
                    continue
                image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray Bonus')


# Isekai Yakkyoku
class IsekaiYakkyokuDownload(Summer2022AnimeDownload, NewsTemplate2):
    title = 'Isekai Yakkyoku'
    keywords = [title, 'Parallel World Pharmacy']
    website = 'https://isekai-yakkyoku.jp/'
    twitter = 'isekai_yakkyoku'
    hashtags = '異世界薬局'
    folder_name = 'isekai-yakkyoku'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_external()
        self.download_episode_preview_guess()
        self.download_news()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            stories = soup.select('#ContentsListUnit02 a[href]')
            for story in stories:
                try:
                    episode = str(int(story.text.replace('#', ''))).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                ep_soup = self.get_soup(self.PAGE_PREFIX + story['href'].replace('../', ''))
                if ep_soup is None:
                    continue
                self.image_list = []
                images = ep_soup.select('ul.tp5 img[src]')
                for i in range(len(images)):
                    image_url = self.PAGE_PREFIX + images[i]['src'].replace('../', '').split('?')[0]
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_external(self):
        jp_title = '異世界薬局'
        AniverseMagazineScanner(jp_title, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20220709', download_id=self.download_id).run()

    def download_episode_preview_guess(self):
        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'core_sys/images/contents/%s/block/%s/%s.jpg'
        is_successful = False
        for i in range(1, self.FINAL_EPISODE + 1, 1):
            episode = str(i).zfill(2)
            is_success = False
            if self.is_image_exists(episode + '_1'):
                continue
            first = 16 + (i - 1)
            second = 19 + 4 * (i - 1)
            third = 29 + 6 * (i - 1)
            for j in range(self.IMAGES_PER_EPISODE):
                third_ = third + j
                image_url = template % (str(first).zfill(8), str(second).zfill(8), str(third_).zfill(8))
                image_name = episode + '_' + str(j + 1)
                content_length = self.get_content_length(image_url)
                if content_length < 10000:
                    break
                result = self.download_image(image_url, folder + '/' + image_name)
                if result == 0:
                    is_success = True
                    is_successful = True
                elif result == -1:
                    break
            if is_success:
                print(self.__class__.__name__ + ' - Guessed successfully!')
            else:
                if len(os.listdir(folder)) == 0:
                    os.rmdir(folder)
                return
        if len(os.listdir(folder)) == 0:
            os.rmdir(folder)
        return is_successful

    def download_news(self):
        self.download_template_news(self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('teaser', 'https://pbs.twimg.com/media/E6Rh8S_VcAQWTLG?format=jpg&name=4096x4096')
        self.add_to_image_list('tz_kv', self.PAGE_PREFIX + 'core_sys/images/main/tz/kv.jpg')
        self.add_to_image_list('kv_home', self.PAGE_PREFIX + 'core_sys/images/main/home/kv.jpg')
        self.add_to_image_list('kv_sp_home', self.PAGE_PREFIX + 'core_sys/images/main/home/kv_sp.jpg')
        self.add_to_image_list('kv_news', self.PAGE_PREFIX + 'core_sys/images/news/00000007/block/00000011/00000006.jpg')
        self.add_to_image_list('kv_tw', 'https://pbs.twimg.com/media/FR-4FD6aQAAjOP3?format=jpg&name=large')
        self.download_image_list(folder)

        kv_template = self.PAGE_PREFIX + 'core_sys/images/main/tz/kv%s'
        kv_template1 = kv_template + '.jpg'
        kv_template2 = kv_template + '.png'
        self.download_by_template(folder, [kv_template1, kv_template2], 1, 2, prefix='tz_')

    def download_character(self):
        folder = self.create_character_directory()
        prefix = self.PAGE_PREFIX + 'core_sys/images/main/cont/chara/chara'
        self.download_by_template(folder, prefix + '%s_stand.png', 2, 1)

        tz_prefix = self.PAGE_PREFIX +'core_sys/images/main/tz/chara/'
        templates = [tz_prefix + '%s_stand.png', tz_prefix + '%s_face.png']
        self.download_by_template(folder, templates, 2, 1, prefix='tz_')

    def download_media(self):
        folder = self.create_media_directory()

        # Blu-rays
        bd_template = self.PAGE_PREFIX + 'core_sys/images/contents/%s/block/%s/%s.jpg'
        tuples = [(28, 66, 101), (29, 70, 102), (30, 72, 103)]
        try:
            for i in range(len(tuples)):
                image_name = 'bd_vol' + str(i + 1)
                if self.is_image_exists(image_name, folder):
                    continue
                tp = tuples[i]
                image_url = bd_template % (str(tp[0]).zfill(8), str(tp[1]).zfill(8), str(tp[2]).zfill(8))
                if not self.is_matching_content_length(image_url, 30538):
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')

        # Blu-ray Bonus
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'bd/privilege.html')
            images = soup.select('.block_inner img[src]')
            self.image_list = []
            for image in images:
                if 'nowprinting' in image['src']:
                    continue
                image_url = self.PAGE_PREFIX + image['src'].replace('../', '').split('?')[0]
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray Bonus')


# Kanojo, Okarishimasu 2nd Season
class Kanokari2Download(Summer2022AnimeDownload, NewsTemplate):
    title = "Kanojo, Okarishimasu 2nd Season"
    keywords = [title, "Kanokari", "Rent-a-Girlfriend"]
    website = 'https://kanokari-official.com/2nd/'
    twitter = 'kanokari_anime'
    hashtags = ['彼女お借りします', 'かのかり', 'kanokari']
    folder_name = 'kanokari2'

    PAGE_PREFIX = 'https://kanokari-official.com/'
    PAGE_PREFIX_2 = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        yt_folder, yt_episodes = self.init_youtube_thumbnail_variables(['13'])
        try:
            soup = self.get_soup(self.PAGE_PREFIX_2 + 'story/')
            lis = soup.select('.story--nav li')
            curr = soup.select('.story--ttl__num em')
            curr_ep = '12'
            if len(curr) > 0:
                curr_ep = curr[0].text.strip()
            for li in lis:
                span = li.select('span')
                if len(span) == 0:
                    continue
                try:
                    episode = str(int(span[0].text)).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_6') and episode in yt_episodes:
                    continue
                if curr_ep == episode:
                    ep_soup = soup
                else:
                    a_tag = li.select('a[href]')
                    if len(a_tag) == 0:
                        continue
                    ep_soup = self.get_soup(a_tag[0]['href'])
                if ep_soup is not None:
                    self.image_list = []
                    images = ep_soup.select('.ss img[src]')
                    for i in range(len(images)):
                        image_url = images[i]['src']
                        image_name = episode + '_' + str(i + 1)
                        self.add_to_image_list(image_name, image_url)
                    self.download_image_list(self.base_folder)

                    yt_tag = ep_soup.select('.md-movie[data-youtubeid]')
                    if len(yt_tag) > 0 and len(yt_tag[0]['data-youtubeid']) > 0:
                        yt_id = yt_tag[0]['data-youtubeid']
                        self.download_youtube_thumbnail_by_id(yt_id, yt_folder, episode)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX_2, article_select='.md-news__li',
                                    title_select='.postttl', date_select='time', id_select='a', stop_date='2021.02.26',
                                    paging_type=0, next_page_select='ul.pagenation-list li', next_page_eval_index=-1,
                                    next_page_eval_index_class='is__current')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        # self.image_list = []
        # self.add_to_image_list('tz', self.PAGE_PREFIX + '2nd/wp-content/themes/kanokari-2nd/_assets/images/fv/fv_pc.jpg')

        try:
            soup = self.get_soup(self.PAGE_PREFIX_2)
            images = soup.select('.fv--visual img[src]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'][1:].split('?')[0]
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

        characters = ['chizuru', 'mami', 'ruka', 'sumi']
        for chara in characters:
            image_url = f'{self.PAGE_PREFIX}2nd/wp-content/themes/kanokari-2nd/_assets/images/loader/{chara}_pc.png'
            image_name = f'loader_{chara}'
            self.add_to_image_list(image_name, image_url)
        self.download_image_list(folder)

        # self.download_youtube_thumbnails(self.PAGE_PREFIX, folder)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX_2 + 'character/')
            images = soup.select('.char .v img[src]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'][1:]
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')

    def download_media(self):
        folder = self.create_media_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        bd_prefix = self.PAGE_PREFIX_2 + 'bd/'
        try:
            soup = self.get_soup(bd_prefix)
            lis = soup.select('.bd--lineup li')
            for li in lis:
                a_tag = li.select('a[href]')
                img_tag = li.select('img[src]')
                if len(a_tag) == 0 or len(img_tag) == 0 or 'nowprinting' in img_tag[0]['src']:
                    continue
                bd_url = a_tag[0]['href']
                bd_page_name = bd_url.replace(bd_prefix, '').replace('/', '')
                if bd_page_name in processed:
                    continue
                bd_soup = self.get_soup(bd_url)
                if bd_soup is None:
                    continue
                images = bd_soup.select('.bd--main img[src]')
                self.image_list = []
                for image in images:
                    if 'nowprinting' in image['src']:
                        continue
                    if image['src'].startswith('/'):
                        image_url = self.PAGE_PREFIX + image['src'][1:]
                    else:
                        image_url = image['src']
                    if image_url.endswith(');'):
                        image_url = image_url[:-2]
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
                if len(self.image_list) > 0:
                    processed.append(bd_page_name)
                self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')
        self.create_cache_file(cache_filepath, processed, num_processed)

        # Blu-ray Bonus
        try:
            soup = self.get_soup(bd_prefix + 'store/')
            images = soup.select('.store--lineup img[src]')
            self.image_list = []
            for image in images:
                if 'nowprinting' in image['src']:
                    continue
                image_url = image['src']
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray Bonus')


# Kinsou no Vermeil: Gakeppuchi Majutsushi wa Saikyou no Yakusai to Mahou Sekai wo Tsukisusumu
class VermeilDownload(Summer2022AnimeDownload, NewsTemplate):
    title = 'Kinsou no Vermeil: Gakeppuchi Majutsushi wa Saikyou no Yakusai to Mahou Sekai wo Tsukisusumu'
    keywords = [title, 'Vermeil in Gold']
    website = 'https://vermeilingold.jp/'
    twitter = 'vermeil_animePR'
    hashtags = ['ヴェルメイユ', 'vermeil']
    folder_name = 'vermeil'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 7

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        template = self.PAGE_PREFIX + 'images/story/%s/ph%s.jpg'
        try:
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_1'):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (episode, str(j + 1).zfill(2))
                    image_name = episode + '_' + str(j + 1)
                    result = self.download_image(image_url, self.base_folder + '/' + image_name)
                    if result == -1:
                        return
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, paging_type=3, paging_suffix='?pg=%s',
                                    article_select='ul.newsliste li', title_select='a', date_select='.newstime',
                                    id_select='a', next_page_select='.bantright')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FNdPFJ6VgAA2C0l?format=jpg&name=4096x4096')
        self.add_to_image_list('tz_tmp_img_off', self.PAGE_PREFIX + 'images/tmp_img_off.png')
        self.add_to_image_list('tz_tmp_img_on', self.PAGE_PREFIX + 'images/tmp_img_on.png')
        self.add_to_image_list('kv', self.PAGE_PREFIX + 'images/top-img.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'images/pre_h%s.png'
        self.download_by_template(folder, template, 2, 1)


# Kumichou Musume to Sewagakari
class KumichoMusumeDownload(Summer2022AnimeDownload, NewsTemplate):
    title = 'Kumichou Musume to Sewagakari'
    keywords = [title, 'kumichomusume', "The Yakuza's Guide to Babysitting"]
    website = 'https://kumichomusume.com/'
    hashtags = '組長娘と世話係'
    twitter = 'kumichomusume'
    folder_name = 'kumichomusume'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_external()
        self.download_news()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            divs = soup.select('.episode')
            for div in divs:
                number = div.select('.number')
                try:
                    episode = str(int(number[0].text.replace('#', ''))).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                self.image_list = []
                images = div.select('.image img[src]')
                for i in range(len(images)):
                    image_url = images[i]['src']
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_external(self):
        jp_title = '組長娘と世話係'
        AniverseMagazineScanner(jp_title, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20220707', download_id=self.download_id).run()

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='div.archive li', date_select='.date',
                                    title_select='.title', id_select='a')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_main', self.PAGE_PREFIX + 'assets/images/pc/img_keyvisual.jpg')
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FF95CKrVUAAvycn?format=jpg&name=large')
        self.add_to_image_list('tz_aniverse', 'https://aniverse-mag.com/wp-content/uploads/2021/12/KtoS_KV_1_TATE_WH_re_72dpi-e1638846766594.jpg')
        self.download_image_list(folder)

        template = self.PAGE_PREFIX + 'wordpress/wp-content/themes/kumichomusume/assets/images/pc/index/img_kv_%s.jpg'
        self.download_by_template(folder, template, 1, 1)

    def download_character(self):
        folder = self.create_character_directory()
        main_template = self.PAGE_PREFIX + 'wordpress/wp-content/themes/kumichomusume/assets/images/common/character/%s/img.png'
        closeup_template = self.PAGE_PREFIX + 'wordpress/wp-content/themes/kumichomusume/assets/images/common/character/%s/img_close-up_%s.png'
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            a_tags = soup.select('.list a[href]')
            self.image_list = []
            for a_tag in a_tags:
                href = a_tag['href']
                if href.endswith('/'):
                    href = href[:-1]
                chara_name = href.split('/')[-1]
                if len(chara_name) > 0:
                    main_image_name = chara_name + '_' + 'img'
                    main_image_url = main_template % chara_name
                    self.add_to_image_list(main_image_name, main_image_url)
                    for i in range(3):
                        closeup_image_name = chara_name + '_img_close-up_' + str(i + 1)
                        closeup_image_url = closeup_template % (chara_name, str(i + 1))
                        self.add_to_image_list(closeup_image_name, closeup_image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')

    def download_media(self):
        folder = self.create_media_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'music-bd/bd-dvd/')
            images = soup.select('.musicBd-Index img[src]')
            self.image_list = []
            for image in images:
                image_url = image['src']
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


# Kuro no Shoukanshi
class KuronoShoukanshiDownload(Summer2022AnimeDownload, NewsTemplate):
    title = 'Kuro no Shoukanshi'
    keywords = [title, 'Black Summoner']
    website = 'https://kuronoshokanshi.com/'
    twitter = 'kuronoshokanshi'
    hashtags = '黒の召喚士'
    folder_name = 'kuronoshokanshi'

    PAGE_PREFIX = website

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story')
            boxes = soup.select('.str-Box_Inner')
            for box in boxes:
                try:
                    episode = str(int(box.select('.number')[0].text.replace('#', ''))).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                self.image_list = []
                images = box.select('.swiper-slide img[src]')
                for i in range(len(images)):
                    image_url = self.clear_resize_in_url(images[i]['src'])
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-item',
                                    date_select='.news-date', title_select='.news-title', id_select='a',
                                    date_func=lambda x: x[0:4] + '.' + x[5:], next_page_select='div.sw-Pagination span',
                                    next_page_eval_index_class='current', next_page_eval_index=-1)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        template = self.PAGE_PREFIX + 'wordpress/wp-content/themes/kuronoshokanshi/assets/images/pc/index/img_kv_%s.jpg'
        self.download_by_template(folder, template, 2, 1)

        self.image_list = []
        self.add_to_image_list('tz_aniverse', 'https://aniverse-mag.com/wp-content/uploads/2022/02/633e750a4b48dc2fd8f0466f51b44078.jpg')
        self.add_to_image_list('kv1_twitter', 'https://pbs.twimg.com/media/FQiLQU6VQAkgT8i?format=jpg&name=medium')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'wordpress/wp-content/themes/kuronoshokanshi/assets/images/common/character/img_chara_%s.png'
        self.download_by_template(folder, template, 2, 1)


# Lycoris Recoil
class LycorisRecoilDownload(Summer2022AnimeDownload, NewsTemplate):
    title = 'Lycoris Recoil'
    keywords = [title]
    website = 'https://lycoris-recoil.com/'
    twitter = 'lycoris_recoil'
    hashtags = ['リコリコ', 'LycorisRecoil']
    folder_name = 'lycoris-recoil'

    PAGE_PREFIX = website

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        story_url = self.PAGE_PREFIX + 'story/'
        try:
            soup = self.get_soup(story_url)
            lis = soup.select('.page_tab li')
            for li in lis:
                a_tag = li.select('a[href]')
                if len(a_tag) == 0:
                    continue
                try:
                    episode = str(int(a_tag[0].text)).zfill(2)
                except:
                    continue
                if li.has_attr('class') and 'is-current' in li['class']:
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(story_url + a_tag[0]['href'].replace('./', ''))
                if ep_soup is None:
                    continue
                images = ep_soup.select('li.swiper-slide img[src]')
                self.image_list = []
                for i in range(len(images)):
                    image_url = story_url + images[i]['src']
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='li.p-news__list-item',
                                    date_select='.p-news_data__date', title_select='.p-news_data__title',
                                    id_select='a', a_tag_start_text_to_remove='/', paging_type=1,
                                    a_tag_prefix=self.PAGE_PREFIX,
                                    next_page_select='div.c-pagination__link.-next',
                                    next_page_eval_index_class='is-disable', next_page_eval_index=-1)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        template = self.PAGE_PREFIX + 'assets/img/top/img_main-%s.jpg'
        self.download_by_template(folder, template, 2, 0)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            a_tags = soup.select('.p-chara_nav__list-item a[href]')
            chara_names = []
            for a_tag in a_tags:
                index = a_tag['href'].rfind('?chara=')
                if index > 0 and len(a_tag['href'][index + 7:]) > 0:
                    chara_names.append(a_tag['href'][index + 7:])
            chara_prefix = self.PAGE_PREFIX + 'assets/img/character/'
            suffixes = ['chara_%s.png', 'face_%s.png']
            self.image_list = []
            for chara_name in chara_names:
                for suffix in suffixes:
                    image_url = chara_prefix + suffix % chara_name
                    image_name = (suffix % chara_name).split('.')[0]
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')

    def download_media(self):
        folder = self.create_media_directory()

        # Blu-ray
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        bd_urls = ['special', '01', '02', '03', '04', '05', '06']
        try:
            for i in range(len(bd_urls)):
                bd_url = self.PAGE_PREFIX + 'bddvd/' + bd_urls[i] + '.html'
                if i > 0 and str(i) in processed:
                    continue
                soup = self.get_soup(bd_url)
                if soup is not None:
                    images = soup.select('.p-bddvd img[src]')
                    self.image_list = []
                    for image in images:
                        if not image['src'].endswith('np_tokuten.jpg') and not image['src'].endswith('np_jk.jpg'):
                            image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                            image_name = 'bddvd_' + self.generate_image_name_from_url(image_url, 'bddvd')
                            self.add_to_image_list(image_name, image_url)
                    if i > 1:
                        if len(self.image_list) > 0:
                            processed.append(str(i))
                        else:
                            break
                    elif i == 1:
                        if len(self.image_list) > 1:
                            processed.append(str(i))
                        elif len(self.image_list) == 0:
                            break
                    self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Made in Abyss: Retsujitsu no Ougonkyou
class MadeInAbyss2Download(Summer2022AnimeDownload, NewsTemplate):
    title = 'Made in Abyss: Retsujitsu no Ougonkyou'
    keywords = [title, 'The Golden City of the Scorching Sun']
    website = 'http://miabyss.com/'
    twitter = 'miabyss_anime'
    hashtags = 'miabyss'
    folder_name = 'miabyss2'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()

    def download_episode_preview(self):
        template = self.PAGE_PREFIX + 'images/tv2nd/story/%s/p_%s.jpg'
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1'):
                continue
            ep_template = template % (str(i + 1).zfill(3), '%s')
            for j in range(self.IMAGES_PER_EPISODE):
                image_url = ep_template % str(j + 1).zfill(3)
                image_name = episode + '_' + str(j + 1)
                result = self.download_image(image_url, self.base_folder + '/' + image_name)
                if result == -1:
                    return

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.newsPaging article',
                                    title_select='.news_title', date_select='.news_day',
                                    id_select='a', a_tag_prefix=self.PAGE_PREFIX, date_separator='/',
                                    news_prefix='news.html', stop_date='2021.04')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('#visual_core01 img[src]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src']
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')


# Mamahaha no Tsurego ga Motokano datta
class TsurekanoDownload(Summer2022AnimeDownload, NewsTemplate):
    title = 'Mamahaha no Tsurego ga Motokano datta'
    keywords = [title, "My Stepmom's Daughter Is My Ex", 'tsurekano']
    website = 'https://tsurekano-anime.com/'
    twitter = 'tsurekano'
    hashtags = ['連れカノ', 'tsurekano']
    folder_name = 'tsurekano'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_episode_preview_external()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        yt_folder, yt_episodes = self.init_youtube_thumbnail_variables()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            items = soup.select('.detail__item')
            for item in items:
                num = item.select('.num')
                if len(num) == 0:
                    continue
                try:
                    episode = str(int(num[0].text.replace('#', ''))).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1') and episode in yt_episodes:
                    continue
                images = item.select('.mainSwiper img[src]')
                self.image_list = []
                for i in range(len(images)):
                    image_url = self.PAGE_PREFIX + images[i]['src'].replace('../', '')
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)

                yt_tag = item.select('.detail__movie iframe[src]')
                if len(yt_tag) > 0:
                    yt_id = yt_tag[0]['src'].split('?')[0].split('/')[-1]
                    self.download_youtube_thumbnail_by_id(yt_id, yt_folder, episode)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news__list-item',
                                    date_select='time', title_select='.body__article-title',
                                    id_select='a', date_separator='/')

    def download_episode_preview_external(self):
        keywords = ['継母の連れ子が元カノだった', '先行カット']
        EeoMediaScanner(keywords, self.base_folder, last_episode=self.FINAL_EPISODE, download_id=self.download_id).run()
        # AniverseMagazineScanner(keywords, self.base_folder, last_episode=self.FINAL_EPISODE,
        #                        end_date='20220602', download_id=self.download_id).run()

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FKA8xQ1aAAEmNl3?format=jpg&name=4096x4096')
        self.add_to_image_list('top_kv_1', self.PAGE_PREFIX + 'img/top/kv_1.png')
        self.add_to_image_list('kv2', self.PAGE_PREFIX + 'news/wp-content/uploads/2022/04/tsurekano_KV02.jpg')
        self.add_to_image_list('kv2_tw', 'https://pbs.twimg.com/media/FQ8EIMpacAAaPsz?format=jpg&name=4096x4096')
        self.add_to_image_list('kv_yume_tw', 'https://pbs.twimg.com/media/FWI65uKagAAasvD?format=jpg&name=4096x4096')
        self.download_image_list(folder)
        self.download_youtube_thumbnails(self.PAGE_PREFIX, folder)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            self.image_list = []
            lis = soup.select('.character__list li[data-modal_name]')
            for li in lis:
                image_tag = li.select('img[src]')
                if len(image_tag) > 0:
                    image_url = self.PAGE_PREFIX + image_tag[0]['src'].replace('../', '')
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
                if len(li['data-modal_name']) > 0:
                    image_url = self.PAGE_PREFIX + f'dist/img/character/{li["data-modal_name"]}_picture.png'
                    image_name = f'{li["data-modal_name"]}_picture'
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')

    def download_media(self):
        folder = self.create_media_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'bddvd/')
            self.image_list = []
            images = soup.select('.bddvd__image img[src],.item__image img[src]')
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].replace('../', '').split('?')[0]
                if self.is_matching_content_length(image_url, 234752):
                    continue
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


# Overlord IV
class Overlord4Download(Summer2022AnimeDownload):
    title = 'Overlord IV'
    keywords = [title, '4th']
    website = 'https://overlord-anime.com/'
    twitter = 'over_lord_anime'
    hashtags = ['overlord_anime', 'オーバーロード']
    folder_name = 'overlord4'

    PAGE_PREFIX = 'https://overlord-anime.com/'
    FINAL_EPISODE = 13
    IMAGES_PER_EPISODE = 6

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_external()

    def download_episode_preview(self):
        template = self.PAGE_PREFIX + 'assets/story/%s/%s.jpg'
        try:
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_1'):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (str(i + 1), str(j + 1))
                    image_name = episode + '_' + str(j + 1)
                    result = self.download_image(image_url, self.base_folder + '/' + image_name)
                    if result == -1:
                        return
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_external(self):
        jp_title = 'オーバーロードⅣ'
        AniverseMagazineScanner(jp_title, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20220702', download_id=self.download_id).run()


# Prima Doll
class PrimaDollDownload(Summer2022AnimeDownload, NewsTemplate):
    title = 'Prima Doll'
    keywords = [title]
    website = 'https://primadoll.jp/'
    twitter = 'primadoll_pr'
    hashtags = ['プリマドール', 'PrimaDoll']
    folder_name = 'primadoll'

    PAGE_PREFIX = website
    ASSETS_URL = 'https://storage.googleapis.com/primadoll-official/assets/'
    ASSETS_IMAGE_URL = ASSETS_URL + 'image/'
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_external()
        self.download_news()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        template = self.ASSETS_IMAGE_URL + 'story_%s_img%s.jpg'
        try:
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_1'):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (episode, str(j + 1).zfill(2))
                    image_name = episode + '_' + str(j + 1)
                    result = self.download_image(image_url, self.base_folder + '/' + image_name)
                    if result == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

        # YouTube thumbnails
        yt_folder, yt_episodes = self.init_youtube_thumbnail_variables(['01'])
        story_url = self.PAGE_PREFIX + 'story/'
        try:
            soup = self.get_soup(story_url + '02.html', decode=True)
            a_tags = soup.select('.story_anchor a[href]')
            for a_tag in a_tags:
                try:
                    episode = str(int(a_tag.text.replace('第', '').replace('話', ''))).zfill(2)
                except:
                    continue
                if episode in yt_episodes and self.is_image_exists(episode + '_6'):
                    continue
                if episode == '02':
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(story_url + a_tag['href'])
                if ep_soup is None:
                    continue
                images = ep_soup.select('.center-item_gallery_cg img[src]')
                self.image_list = []
                for i in range(len(images)):
                    image_name = episode + '_' + str(i + 1)
                    if self.is_image_exists(image_name):
                        continue
                    image_url = images[i]['src'].split('?')[0]
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)

                yt_tag = ep_soup.select('.news_img iframe[src]')
                if len(yt_tag) > 0:
                    yt_id = yt_tag[0]['src'].split('/')[-1]
                    self.download_youtube_thumbnail_by_id(yt_id, yt_folder, episode)
        except Exception as e:
            self.print_exception(e, 'YouTube thumbnails')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.top_news_item_style1',
                                    date_select='.top_news_text_style1', title_select='.top_news_text_style2',
                                    id_select='a', news_prefix='news/news.html', a_tag_prefix=self.PAGE_PREFIX,
                                    a_tag_start_text_to_remove='../')

    def download_episode_preview_external(self):
        jp_title = 'プリマドール'
        last_date = datetime.strptime('20221101', '%Y%m%d')
        today = datetime.today()
        if today < last_date:
            end_date = today
        else:
            end_date = last_date
        MocaNewsScanner(jp_title, self.base_folder, '20220702', end_date.strftime('%Y%m%d'),
                        download_id=self.download_id).run()

        # AniverseMagazineScanner(jp_title, self.base_folder, last_episode=self.FINAL_EPISODE,
        #                        end_date='20220702', download_id=self.download_id).run()

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FKHiPhoagAEoQXI?format=jpg&name=4096x4096')
        self.add_to_image_list('prima_eats_main_img', self.ASSETS_URL + 'uber_eats/image/prima_eats_main_img.jpg')
        tz_template = self.ASSETS_IMAGE_URL + '%s_img_pc.jpg'
        for time in ['night', 'morning', 'noon', 'evening']:
            self.add_to_image_list('tz_' + time, tz_template % time)

        self.add_to_image_list('main_2_img_pc', self.ASSETS_IMAGE_URL + 'main_2_img_pc.jpg')
        self.add_to_image_list('kv_tw', 'https://pbs.twimg.com/media/FUsbotOagAAXpMu?format=jpg&name=4096x4096')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        chara_names = []
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'haizakura.html')
            a_tags = soup.select('.character_icon_list_box a[href]')
            for a_tag in a_tags:
                chara_names.append(a_tag['href'].replace('.html', '').strip())
        except:
            pass

        self.image_list = []
        js_file = self.PAGE_PREFIX + 'common/js/character.js'
        try:
            r = requests.get(js_file)
            r.raise_for_status()
            split1 = str(r.content).split("imgs = ['")
            for i in range(1, len(split1), 1):
                split2 = split1[i].split("'];")
                if len(split2) > 0:
                    split3 = split2[0].replace("'", '').replace(' ', '').split(',')
                    for j in range(len(split3)):
                        image_url = self.ASSETS_IMAGE_URL + split3[j]
                        dot_index = split3[j].rfind('.')
                        image_name = split3[j][0:dot_index] if dot_index > 0 else split3[j]
                        if self.is_image_exists(image_name, folder):
                            continue
                        chara_name_found = False
                        for chara_name in chara_names:
                            if chara_name in image_name:
                                chara_name_found = True
                                break
                        if not chara_name_found or self.is_matching_content_length(image_url, 17474):
                            continue
                        self.add_to_image_list(image_name, image_url)
        except Exception as e:
            self.print_exception(e, 'Character')
        self.download_image_list(folder)

    def download_media(self):
        folder = self.create_media_directory()

        # Blu-ray
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        bd_urls = ['tokuten', 'campaign', '01', '02', '03', '04', '05', '06']
        try:
            for i in range(len(bd_urls)):
                bd_url = self.PAGE_PREFIX + 'bd/' + bd_urls[i] + '.html'
                if i > 1 and str(i) in processed:
                    continue
                soup = self.get_soup(bd_url)
                if soup is not None:
                    images = soup.select('.bd_wrapper img[src]')
                    self.image_list = []
                    for image in images:
                        if not image['src'].endswith('bd_nowprinting_img.jpg'):
                            image_url = image['src']
                            image_name = self.extract_image_name_from_url(image_url)
                            self.add_to_image_list(image_name, image_url)
                    if i > 2:
                        if len(self.image_list) > 0:
                            processed.append(str(i))
                        else:
                            break
                    elif i == 2:
                        if len(self.image_list) > 1:
                            processed.append(str(i))
                        else:
                            break
                    self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Saikin Yatotta Maid ga Ayashii
class MaidgaAyashiiDownload(Summer2022AnimeDownload, NewsTemplate):
    title = 'Saikin Yatotta Maid ga Ayashii'
    keywords = [title, 'The Maid I Hired Recently Is Mysterious']
    website = 'https://maid-ga-ayashii.com/'
    twitter = 'maidga_ayashii'
    hashtags = '最近雇ったメイドが怪しい'
    folder_name = 'maid-ga-ayashii'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            a_tags = soup.select('.story--nav a[href]')
            for a_tag in a_tags:
                try:
                    episode = str(int(a_tag.text)).zfill(2)
                except:
                    continue
                i_tag = soup.select('i.num')
                if len(i_tag) > 0 and i_tag[0].text.strip() == episode:
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(a_tag['href'])
                if ep_soup is None:
                    continue
                self.image_list = []
                images = ep_soup.select('.ss img[src]')
                for i in range(len(images)):
                    image_url = images[i]['src']
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.md-news--li',
                                    date_select='time', title_select='h4', id_select='a', news_prefix='topics/',
                                    date_func=lambda x: x.replace(' ', ''))

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FS7YNC_UEAAn92e?format=jpg&name=large')
        self.add_to_image_list('tz_visual_pc', self.PAGE_PREFIX + '_assets/images/fv/visual/visual_pc.jpg')
        self.add_to_image_list('tz_visual_sp', self.PAGE_PREFIX + '_assets/images/fv/visual/visual_sp.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.chardata--inner .v picture img[src]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src']
                image_name = 'tz_' + self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Shadows House 2nd Season
class ShadowsHouse2Download(Summer2022AnimeDownload, NewsTemplate):
    title = "Shadows House 2nd Season"
    keywords = [title]
    website = 'https://shadowshouse-anime.com/'
    twitter = 'shadowshouse_yj'
    hashtags = 'シャドーハウス'
    folder_name = 'shadows-house2'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_media()

    def download_episode_preview(self):
        yt_folder, yt_episodes = self.init_youtube_thumbnail_variables()
        story_url = self.PAGE_PREFIX + 'story/'
        try:
            soup = self.get_soup(story_url)
            page_tabs = soup.select('.page_tab li')
            for page_tab in page_tabs:
                try:
                    episode = str(int(page_tab.select('p')[0].text)).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1') and episode in yt_episodes:
                    continue
                if page_tab.has_attr('class') and 'is-current' in page_tab['class']:
                    ep_soup = soup
                else:
                    a_tag = page_tab.select('a[href]')
                    if len(a_tag) == 0:
                        continue
                    ep_soup = self.get_soup(story_url + a_tag[0]['href'].replace('./', ''))
                if ep_soup is None:
                    continue
                self.image_list = []
                images = ep_soup.select('.swiper-slide img[src]')
                for i in range(len(images)):
                    image_url = story_url + images[i]['src']
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)

                yt_tag = ep_soup.select('.p-movie_item[data-video-id]')
                if len(yt_tag) > 0:
                    yt_id = yt_tag[0]['data-video-id']
                    self.download_youtube_thumbnail_by_id(yt_id, yt_folder, episode)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news/'
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.p-in-news__list-item',
                                    date_select='.p-in-news_data__date', title_select='.p-in-news_data__title',
                                    id_select='a', a_tag_prefix=news_url, a_tag_start_text_to_remove='./',
                                    paging_type=1, stop_date='2021', next_page_select='.c-pagination_arrow__next',
                                    next_page_eval_index_class='.is-disable', next_page_eval_index=-1)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        # self.add_to_image_list('tz_modal', self.PAGE_PREFIX + 'assets/img/kv_modal.png')
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FIT7cvQaUAUw-RP?format=jpg&name=large')
        self.add_to_image_list('tz', self.PAGE_PREFIX + 'assets/img/main_00.jpg')
        self.add_to_image_list('kv_tw', 'https://pbs.twimg.com/media/FUJUvxmVIAAd734?format=jpg&name=large')
        self.add_to_image_list('kv1st_00', self.PAGE_PREFIX + 'assets/img/kv1st_00.jpg')
        self.download_image_list(folder)

    def download_media(self):
        folder = self.create_media_directory()

        # Blu-ray
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        bd_urls = ['special', 'vol01', 'vol02', 'vol03', 'vol04', 'vol05', 'vol06']
        try:
            for i in range(len(bd_urls)):
                bd_url = self.PAGE_PREFIX + 'bddvd/' + bd_urls[i] + '.html'
                if i > 0 and str(i) in processed:
                    continue
                soup = self.get_soup(bd_url)
                if soup is not None:
                    images = soup.select('.p-in-bddvd img[src]')
                    self.image_list = []
                    for image in images:
                        if not image['src'].endswith('/np.jpg'):
                            image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                            image_name = self.generate_image_name_from_url(image_url, 'bddvd')
                            self.add_to_image_list(image_name, image_url)
                    if i > 1:
                        if len(self.image_list) > 0:
                            processed.append(str(i))
                        else:
                            break
                    elif i == 1:
                        if len(self.image_list) > 1:
                            processed.append(str(i))
                        elif len(self.image_list) == 0:
                            break
                    self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Soredemo Ayumu wa Yosetekuru
class SoreayuDownload(Summer2022AnimeDownload, NewsTemplate):
    title = "Soredemo Ayumu wa Yosetekuru"
    keywords = [title, "Soreayu", "When Will Ayumu Make His Move?"]
    website = 'https://soreayu.com/'
    twitter = 'soreayu_staff'
    hashtags = 'それあゆ'
    folder_name = 'soreayu'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        image_prefix = self.PAGE_PREFIX + '_nuxt/'
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            js_urls = soup.select('link[rel=preload][href]')
            js_file_content = None
            for url in reversed(js_urls):
                test_url = url['href'][1:] if url['href'].startswith('/') else url['href']
                file_content = self.get_response(self.PAGE_PREFIX + test_url)
                if 'img/story1_' in file_content:
                    js_file_content = file_content
                    break
            if js_file_content is None:
                return
            for ep in range(self.FINAL_EPISODE):
                episode = str(ep + 1).zfill(2)
                if self.is_image_exists(episode + '_1'):
                    continue
                js_split = js_file_content.split('img/story' + str(ep + 1) + '_')
                if len(js_split) > 5:
                    self.image_list = []
                    for j in range(1, len(js_split), 1):
                        split2 = js_split[j].split('"')[0]
                        if split2.endswith('.jpg') or split2.endswith('.png'):
                            image_url = image_prefix + 'img/story' + str(ep + 1) + '_' + split2
                            image_name = episode + '_' + str(j)
                            self.add_to_image_list(image_name, image_url)
                    self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='div.news-page-news',
                                    date_select='div.date-label span', title_select='div.page-link h2',
                                    id_select='div.nullclass')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('teaser', self.PAGE_PREFIX + '_nuxt/img/key_visual.7d7640c.jpg')
        self.add_to_image_list('teaser_big', 'https://firebasestorage.googleapis.com/v0/b/pj-ayumu.appspot.com/o/articles%2F1625582107153?alt=media&token=2561cd21-5081-471b-9019-11f379fff1f7')
        self.add_to_image_list('kv1', 'https://storage.googleapis.com/pj-ayumu.appspot.com/articles/1653114275017')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character')
            links = soup.select('link')
            if len(links) == 0:
                return
            js_file = self.PAGE_PREFIX + links[-1]['href'][1:]
            r = requests.get(js_file)
            r.raise_for_status()
            results = r.content.decode().split('"img/')
            self.image_list = []
            for i in range(len(results)):
                if i == 0:
                    continue
                image_name_with_extension = results[i].split('"')[0]
                if '_full' in image_name_with_extension or '_expression' in image_name_with_extension:
                    image_url = self.PAGE_PREFIX + '_nuxt/img/' + image_name_with_extension
                    image_name = self.extract_image_name_from_url(image_name_with_extension)
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')

    def download_media(self):
        folder = self.create_media_directory()
        pages = ['bd1', 'bd2']
        try:
            for i in range(len(pages)):
                soup = self.get_soup(self.PAGE_PREFIX + 'cd-bd/' + pages[i])

                # Blu-ray Bonus
                if i == 0:
                    self.image_list = []
                    images = soup.select('.benefits-table img[src]')
                    for image in images:
                        image_url = self.PAGE_PREFIX + image['src'][1:]
                        image_name = self.extract_image_name_from_url(image_url)
                        self.add_to_image_list(image_name, image_url)
                    self.download_image_list(folder)

                # Blu-ray
                images = soup.select('.product img[src]')
                if len(images) > 0:
                    self.image_list = []
                    for image in images:
                        image_url = self.PAGE_PREFIX + image['src'][1:]
                        if self.is_matching_content_length(image_url, 146157):
                            continue
                        image_name = self.extract_image_name_from_url(image_url)
                        self.add_to_image_list(image_name, image_url)
                    if len(self.image_list) > 0:
                        self.download_image_list(folder)
                    else:
                        break
                else:
                    break
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


# Tensei Kenja no Isekai Life: Dai-2 no Shokugyou wo Ete, Sekai Saikyou ni Narimashita
class TenseiKenjaDownload(Summer2022AnimeDownload, NewsTemplate):
    title = 'Tensei Kenja no Isekai Life: Dai-2 no Shokugyou wo Ete, Sekai Saikyou ni Narimashita'
    keywords = [title, 'tenseikenja', 'My Isekai Life']
    website = 'https://tenseikenja.com/'
    twitter = 'tenseikenja_PR'
    hashtags = '転生賢者'
    folder_name = 'tenseikenja'

    PAGE_PREFIX = website

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            a_tags = soup.select('.story-Index_Nav li a[href]')
            for a_tag in a_tags:
                try:
                    episode = str(int(a_tag.text.strip().replace('#', ''))).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                if a_tag.has_attr('class') and 'current' in a_tag['class']:
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(a_tag['href'])
                if ep_soup is not None:
                    images = ep_soup.select('.swiper img[src]')
                    self.image_list = []
                    for i in range(len(images)):
                        image_url = self.clear_resize_in_url(images[i]['src'])
                        image_name = episode + '_' + str(i + 1)
                        self.add_to_image_list(image_name, image_url)
                    self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='div.sw-News_Archive li',
                                    date_select='.date', title_select='.title p', id_select='a',
                                    next_page_select='.nextpostslink')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/E_cSGeTVQAIKvu2?format=jpg&name=medium')
        self.add_to_image_list('kv1_aniverse', 'https://aniverse-mag.com/wp-content/uploads/2022/01/396ee90ad1118539e82a6b4caab11c11.jpg')
        # self.add_to_image_list('img_kv_teaser', self.PAGE_PREFIX + 'wp/wp-content/themes/tenseikenja/assets/images/common/index/img_kv_teaser.jpg')
        self.add_to_image_list('img_kv_yuji', self.PAGE_PREFIX + 'wp/wp-content/themes/tenseikenja_april/assets/images/pc/index/img_kv_yuji.jpg')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('div.visual-Content img')
            self.image_list = []
            for image in images:
                if image.has_attr('src'):
                    image_url = image['src'].split('?')[0]
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            chara_list = soup.select('div.character-Index li a')
            self.image_list = []
            template = self.PAGE_PREFIX + 'wp/wp-content/themes/tenseikenja/assets/images/common/character/%s/img.png'
            for chara in chara_list:
                if chara.has_attr('href'):
                    href = chara['href']
                    if href.endswith('/'):
                        href = href[0:len(href)-1]
                    chara_name = href.split('/')[-1]
                    if len(chara_name) > 1:
                        self.add_to_image_list(f'img_{chara_name}', template % chara_name)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')

    def download_media(self):
        folder = self.create_media_directory()
        bd_url = self.PAGE_PREFIX + 'product/'
        for page in [('', 'Blu-ray'), ('oritoku/', 'Blu-ray Bonus')]:
            try:
                soup = self.get_soup(bd_url + page[0])
                images = soup.select('.product-Section img[src]')
                self.image_list = []
                for image in images:
                    image_url = image['src']
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(folder)
            except Exception as e:
                self.print_exception(e, page[1])


# Utawarerumono: Futari no Hakuoro
class Utawarerumono3Download(Summer2022AnimeDownload, NewsTemplate):
    title = 'Utawarerumono: Futari no Hakuoro'
    keywords = [title, 'Utawarerumono: Mask of Truth', '3rd']
    website = 'https://utawarerumono.jp/'
    twitter = 'UtawareAnime'
    hashtags = 'うたわれ'
    folder_name = 'utawarerumono3'

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
        yt_folder, yt_episodes = self.init_youtube_thumbnail_variables()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            lis = soup.select('.story--nav li')
            curr = soup.select('.story--epttl__num')
            curr_ep = '00'
            if len(curr) > 0:
                curr_ep = curr[0].text.strip().zfill(2)
            for li in lis:
                a_tag = li.select('a[href]')
                if len(a_tag) == 0:
                    continue
                try:
                    episode = str(int(a_tag[0].text)).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_6') and episode in yt_episodes:
                    continue
                if curr_ep == episode:
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(a_tag[0]['href'])
                if ep_soup is not None:
                    self.image_list = []
                    images = ep_soup.select('.ss img[src]')
                    for i in range(len(images)):
                        image_url = images[i]['src']
                        image_name = episode + '_' + str(i + 1)
                        self.add_to_image_list(image_name, image_url)
                    self.download_image_list(self.base_folder)

                    yt_tag = ep_soup.select('.story--next__btn[data-youtubeid]')
                    if len(yt_tag) > 0 and len(yt_tag[0]['data-youtubeid']) > 0:
                        yt_id = yt_tag[0]['data-youtubeid']
                        self.download_youtube_thumbnail_by_id(yt_id, yt_folder, episode)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.md-news__article',
                                    date_select='time', title_select='h3', id_select='a', news_prefix='topics/',
                                    date_func=lambda x: x.replace(' ', ''), date_separator='/')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FE9Ma5NaAAABavo?format=jpg&name=4096x4096')
        self.add_to_image_list('fv@2x', self.PAGE_PREFIX + 'manage/wp-content/themes/hakuoro/_assets/images/fv/fv@2x.png')
        self.add_to_image_list('mainvisual_tw', 'https://pbs.twimg.com/media/FRPB5W0VIAA1nYW?format=jpg&name=4096x4096')
        self.add_to_image_list('mainvisual', self.PAGE_PREFIX + 'manage/wp-content/uploads/2022/04/うたわれるもの-二人の白皇_メインビジュアル.jpg')
        self.download_image_list(folder)

        template = self.PAGE_PREFIX + 'manage/wp-content/themes/hakuoro-new/_assets/images/fv/visual/visual_%s@2x'
        templates = [template + '.png', template + '.png']
        self.download_by_template(folder, templates, 3, 1)

    def download_character(self):
        folder = self.create_character_directory()

        prefix = self.PAGE_PREFIX + 'manage/wp-content/themes/hakuoro'
        template = prefix + '/_assets/images/char/detail/char%s_pc.png'
        self.download_by_template(folder, template, 2, 1)

        template2 = prefix + '-new/_assets/images/contents/char/detail/char_%s_pc.png'
        self.download_by_template(folder, template2, 3, 1)

    def download_media(self):
        folder = self.create_media_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('.bddata img[src]')
            for image in images:
                image_url = image['src']
                image_name = self.extract_image_name_from_url(image_url)
                if 'bd_np' in image_name:
                    continue
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')

        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'store/')
            self.image_list = []
            images = soup.select('.store picture img[src]')
            for image in images:
                image_url = image['src']
                image_name = self.extract_image_name_from_url(image_url)
                if 'bd_np' in image_name:
                    continue
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray Bonus')


# Warau Arsnotoria Sun!
class ArsnotoriaDownload(Summer2022AnimeDownload, NewsTemplate):
    title = 'Warau Arsnotoria Sun!'
    keywords = [title, 'Smile of the Arsnotoria the Animation']
    website = 'https://www.arsnotoria-anime.com/'
    twitter = 'arsno_anime'
    hashtags = ['アルスノ', 'すんすん']
    folder_name = 'arsnotoria'

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
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/introduction/')
            a_tags = soup.select('div.m-list-story a[href]')
            for a_tag in a_tags:
                try:
                    episode = str(int(a_tag.text.replace('第', '').replace('話', ''))).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                ep_soup = self.get_soup(a_tag['href'])
                if ep_soup is None:
                    continue
                self.image_list = []
                images = ep_soup.select('.story-wrap .slider-item img[src]')
                for i in range(len(images)):
                    image_url = images[i]['src']
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-list .list-item',
                                    title_select='.item-ttl', date_select='.item-date', id_select='a')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz', self.PAGE_PREFIX + 'wp-content/uploads/2022/05/img.jpg')
        self.add_to_image_list('p_mainv_primary', self.PAGE_PREFIX + 'wcmsp/wp-content/themes/arsnotoria/assets/images/top/p_mainv_primary.png')
        self.add_to_image_list('arsn_key_illonly_0620.jpg', self.PAGE_PREFIX + 'wcmsp/wp-content/uploads/2022/06/arsn_key_illonly_0620.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            a_tags = soup.select('.character-list .list-item a[href]')
            for a_tag in a_tags:
                if a_tag['href'].endswith('/'):
                    chara_url = a_tag['href'][:-1]
                else:
                    chara_url = a_tag['href']
                chara_name = chara_url.split('/')[-1]
                if chara_name in processed:
                    continue
                chara_soup = self.get_soup(chara_url)
                if chara_soup is not None:
                    images = chara_soup.select('.detail-mainv img[src]')
                    for image in images:
                        image_url = image['src']
                        image_name = self.extract_image_name_from_url(image_url)
                        self.add_to_image_list(image_name, image_url)
                    if len(self.image_list) > 0:
                        processed.append(chara_name)
                    self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')
        self.create_cache_file(cache_filepath, processed, num_processed)

    def download_media(self):
        folder = self.create_media_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'goods/cat/bluray/')
            images = soup.select('#u-goods img[src]')
            self.image_list = []
            for image in images:
                image_url = image['src']
                if 'arsn_key_illonly_0620' in image_url:
                    continue
                image_url = image_url.replace('-scaled', '')
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


# Yofukashi no Uta
class YofukashiDownload(Summer2022AnimeDownload, NewsTemplate):
    title = 'Yofukashi no Uta'
    keywords = [title, 'Call of the Night']
    website = 'https://yofukashi-no-uta.com/'
    twitter = 'yofukashi_pr'
    hashtags = 'よふかしのうた'
    folder_name = 'yofukashi'

    PAGE_PREFIX = website
    FINAL_EPISODE = 13

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_external()
        self.download_news()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_episode_preview_external(self):
        jp_title = 'よふかしのうた'
        AniverseMagazineScanner(jp_title, self.base_folder, last_episode=self.FINAL_EPISODE, suffix='夜',
                                end_date='20220705', download_id=self.download_id).run()

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.c-news-list__item',
                                    date_select='.c-news-item__day', title_select='.c-news-item__title',
                                    id_select='a', a_tag_prefix=self.PAGE_PREFIX,
                                    next_page_select='.next')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.home-visual img[src]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].replace('./', '').split('?')[0]
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        prefix = self.PAGE_PREFIX + 'character/'
        self.image_list = []
        try:
            obj = self.get_json(prefix + 'chara_data.php')
            if 'charas' in obj:
                for chara in obj['charas']:
                    if 'images' in chara:
                        if 'visuals' in chara['images']:
                            for visual in chara['images']['visuals']:
                                if 'image' in visual:
                                    image_url = prefix + visual['image'].replace('./', '').split('?')[0]
                                    image_name = self.extract_image_name_from_url(image_url)
                                    self.add_to_image_list(image_name, image_url)
                        if 'faces' in chara['images']:
                            for face in chara['images']['faces']:
                                image_url = prefix + face.replace('./', '').split('?')[0]
                                image_name = self.extract_image_name_from_url(image_url)
                                self.add_to_image_list(image_name, image_url)
        except Exception as e:
            self.print_exception(e, 'Character')
        self.download_image_list(folder)

    def download_media(self):
        folder = self.create_media_directory()

        # Blu-ray
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        bd_urls = ['tokuten', 'vol1', 'vol2']
        try:
            for i in range(len(bd_urls)):
                bd_url = self.PAGE_PREFIX + 'bd/' + bd_urls[i] + '/'
                if i > 0 and str(i) in processed:
                    continue
                soup = self.get_soup(bd_url)
                if soup is not None:
                    images = soup.select('article figure[data-bg],article img[src]')
                    self.image_list = []
                    for image in images:
                        if image.name == 'figure':
                            src = image['data-bg']
                        else:   # img
                            src = image['src']
                        if not src.endswith('np_cd.svg') and not src.endswith('np_bd.svg'):
                            if src.startswith('../'):
                                image_url = self.PAGE_PREFIX + src.replace('../', '')
                            elif src.startswith('http'):
                                image_url = src
                            else:
                                image_url = bd_url + src
                            image_name = self.extract_image_name_from_url(image_url)
                            self.add_to_image_list(image_name, image_url)
                    if i > 1:
                        if len(self.image_list) > 0:
                            processed.append(str(i))
                        else:
                            break
                    elif i == 1:
                        if len(self.image_list) > 1:
                            processed.append(str(i))
                        elif len(self.image_list) == 0:
                            break
                    self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Youkoso Jitsuryoku Shijou Shugi no Kyoushitsu e S2
class Youzitsu2Download(Summer2022AnimeDownload, NewsTemplate):
    title = "Youkoso Jitsuryoku Shijou Shugi no Kyoushitsu e 2nd Season"
    keywords = ["Youkoso Jitsuryoku Shijou Shugi no Kyoushitsu e", "Youzitsu", "Youjitsu",
                "Classroom of the Elite"]
    website = 'http://you-zitsu.com/2nd/'
    twitter = 'youkosozitsu'
    hashtags = ['you_zitsu', 'よう実', 'ClassroomOfTheElite']
    folder_name = 'youzitsu2'

    PAGE_PREFIX = website
    FINAL_EPISODE = 13
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_media()

    def download_episode_preview(self):
        template = self.PAGE_PREFIX + 'assets/story/%s/%s.jpg'
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

        # YouTube thumbnails
        yt_folder, yt_episodes = self.init_youtube_thumbnail_variables(['01'])
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story.html')
            stories = soup.select('.story-data[id]')
            for story in stories:
                try:
                    ep_num = int(story['id'][1:])
                    if ep_num < 2:
                        continue
                    episode = str(ep_num).zfill(2)
                except:
                    continue
                if episode in yt_episodes:
                    continue
                yt_tag = story.select('.ep-trailer a[href]')
                if len(yt_tag) > 0:
                    yt_id = yt_tag[0]['href'].split('/')[-1].split('?')[0]
                    self.download_youtube_thumbnail_by_id(yt_id, yt_folder, episode)
        except Exception as e:
            self.print_exception(e, 'YouTube thumbnails')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='article.content-entry',
                                    title_select='h2.entry-title span', date_select='div.entry-date span',
                                    id_select=None, id_has_id=True, news_prefix='news.html')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        top_prefix = self.PAGE_PREFIX + 'assets/top/'

        self.image_list = []
        #self.add_to_image_list('vis_aniverse', 'https://aniverse-mag.com/wp-content/uploads/2022/05/38426131b5b83e0bbf81006021fe5d77.jpg')
        self.add_to_image_list('t1b_vis-a1ca63', top_prefix + 't1b/vis-a1ca63.jpg')
        self.download_image_list(folder)

        h_template = top_prefix + 'h%s/vis.jpg'
        try:
            for i in range(10):
                image_url = h_template % str(i + 1)
                image_name = 'h' + str(i + 1) + '_vis'
                result = self.download_image(image_url, folder + '/' + image_name)
                if result == -1:
                    break
        except:
            pass

        top_template_prefix = top_prefix + 't%s/vis.'
        news_template_prefix = self.PAGE_PREFIX + 'assets/news/vis-t%s.'

        top_templates = [top_template_prefix + 'jpg', top_template_prefix + 'png']
        news_templates = [news_template_prefix + 'jpg', news_template_prefix + 'png']

        self.download_by_template(folder, news_templates, 1, 1, prefix='news_')

        t1b_template = top_prefix + 't1b/c%s.png'
        self.download_by_template(folder, t1b_template, 1, 1, prefix='t1b_')

        try:
            for i in range(1, 11, 1):
                is_success = False
                for top_template in top_templates:
                    image_url = top_template % str(i)
                    image_name = 'top_vis-t' + str(i)
                    result = self.download_image(image_url, folder + '/' + image_name)
                    if result != -1:
                        is_success = True
                        break
                if not is_success:
                    break
        except Exception as e:
            self.print_exception(e, 'Key Visual')

        # Calendar Visual download
        sub_folder = self.create_custom_directory(folder.split('/')[-1] + '/news')
        cache_filepath = sub_folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'news.html')
            items = soup.select('.content-entry[id]')
            for item in items:
                article_id = item['id']
                if article_id in processed:
                    break
                title_tag = item.select('.entry-title span')
                if len(title_tag) == 0:
                    continue
                title = title_tag[0].text.strip()
                if 'イラスト' in title and 'カレンダー' in title:
                    images = item.select('img[src]')
                    self.image_list = []
                    for image in images:
                        image_url = self.PAGE_PREFIX + image['src'].replace('./', '').split('?')[0]
                        if '/news/' not in image_url:
                            continue
                        image_name = self.generate_image_name_from_url(image_url, 'news')
                        self.add_to_image_list(image_name, image_url)
                    self.download_image_list(sub_folder)
                processed.append(article_id)
        except Exception as e:
            self.print_exception(e, 'Key Visual News')
        self.create_cache_file(cache_filepath, processed, num_processed)

    def download_media(self):
        folder = self.create_media_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'bddvd.html')
            images = soup.select('article.content-entry img[src]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].replace('./', '')
                if '/bddvd/' not in image_url:
                    continue
                if 'np' in image_url.split('/')[-1].split('.')[0]:
                    continue
                image_name = 'bddvd_' + self.generate_image_name_from_url(image_url, 'bddvd')
                if not self.is_image_exists(image_name, folder):
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')

        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'music.html')
            images = soup.select('#OP img[src], #ED img[src]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].replace('./', '')
                if '/music/' not in image_url:
                    continue
                image_name = 'music_' + self.generate_image_name_from_url(image_url, 'music')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Music')
