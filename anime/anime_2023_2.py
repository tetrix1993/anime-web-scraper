from anime.main_download import MainDownload, NewsTemplate, NewsTemplate2
from scan import AniverseMagazineScanner, AnimagePlusScanner
from requests.exceptions import HTTPError
from datetime import datetime, timedelta
import os
import re


# Alice Gear Aegis Expansion https://colopl.co.jp/alicegearaegis/tv-anime/ @alice_anime_nzm #アリスギア #アリスギアEX
# Ao no Orchestra https://aooke-anime.com/ #青のオーケストラ @aooke_anime
# Boku no Kokoro no Yabai Yatsu https://bokuyaba-anime.com/ #僕ヤバ #僕の心のヤバイやつ @bokuyaba_anime
# Dead Mount Death Play https://dmdp-anime.jp/ #DMDP @DMDP_anime
# Edomae Elf https://edomae-elf.com/ #江戸前エルフ @edomae_elf
# Isekai de Cheat Skill wo Te ni Shita Ore wa https://iseleve.com　@iseleve_anime
# Isekai One Turn Kill Neesan https://onekillsister.com/ #一撃姉 @onekillsister
# Isekai Shoukan wa Nidome desu https://isenido.com/ #いせにど @isenido_anime
# Isekai wa Smartphone to Tomo ni. 2 http://isesuma-anime.jp/ #イセスマ @isesumaofficial
# Jijou wo Shiranai Tenkousei ga Guigui Kuru. https://guiguikuru.com/ #転校生がグイグイくる @guiguikuru_pr
# Kaminaki Sekai no Kamisama Katsudou https://kamikatsu-anime.jp/ #カミカツ @kamikatsu_anime
# Kawaisugi Crisis https://kawaisugi.com/ #カワイスギクライシス @kawaisugicrisis
# Kimi wa Houkago Insomnia https://kimisomu-anime.com/ #君ソム @kimisomu_anime
# Kono Subarashii Sekai ni Bakuen wo! http://konosuba.com/bakuen/ #konosuba #このすば @konosubaanime
# Kanojo ga Koushaku-tei ni Itta Riyuu https://koshakutei.com/ #公爵邸 @koshakutei
# Kuma Kuma Kuma Bear Punch! https://kumakumakumabear.com/ #くまクマ熊ベアー #kumabear @kumabear_anime
# Megami no Cafe Terrace https://goddess-cafe.com/ #女神のカフェテラス @goddess_cafe_PR
# Mashle https://mashle.pw/ #マッシュル @mashle_official
# My Home Hero https://myhomehero-anime.com/ #マイホームヒーロー @myhomehero_pr
# Oshi no Ko https://ichigoproduction.com/ #推しの子 @anime_oshinoko
# Otonari ni Ginga https://otonari-anime.com/ #おとなりに銀河 @otonariniginga
# Skip to Loafer https://skip-and-loafer.com/ #スキップとローファー #スキロー @skip_and_loafer
# Tensei Kizoku no Isekai Boukenroku https://www.tensei-kizoku.jp/ #転生貴族 @tenseikizoku
# Tonikaku Kawaii S2 http://tonikawa.com/ #トニカクカワイイ #tonikawa @tonikawa_anime
# Watashi no Yuri wa Oshigoto desu! https://watayuri-anime.com/ #わたゆり #私の百合はお仕事です @watayuri_anime
# Yamada-kun to Lv999 no Koi wo Suru https://yamadalv999-anime.com/ #山田999 @yamada999_anime
# Yuusha ga Shinda! https://heroisdead.com/ #勇者が死んだ @yuusyagasinda


# Spring 2023 Anime
class Spring2023AnimeDownload(MainDownload):
    season = "2023-2"
    season_name = "Spring 2023"
    folder_name = '2023-2'

    def __init__(self):
        super().__init__()


# Alice Gear Aegis Expansion
class AliceGearDownload(Spring2023AnimeDownload, NewsTemplate):
    title = 'Alice Gear Aegis Expansion'
    keywords = [title]
    website = 'https://colopl.co.jp/alicegearaegis/tv-anime/'
    twitter = 'alice_anime_nzm'
    hashtags = ['アリスギア', 'アリスギアEX']
    folder_name = 'alicegear'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, news_prefix='',
                                    article_select='ul.news__list .list__item',
                                    date_select='.item__date', title_select='.item__txt',
                                    id_select='a', date_func=lambda x: x[0:4] + '.' + x[4:])

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('keyvisual_img', self.PAGE_PREFIX + 'assets/img/top/keyvisual_img.webp')
        self.download_image_list(folder)

        template = self.PAGE_PREFIX + 'assets/img/top/keyvisual_img_%s.webp'
        self.download_by_template(folder, template, 2, 2)

    def download_character(self):
        folder = self.create_character_directory()
        prefix = 'https://colopl.co.jp'
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            images = soup.select('.character__img_inner source[srcset]')
            self.image_list = []
            for image in images:
                image_url = prefix + image['srcset'].split('?')[0]
                if '/character/detail/' not in image_url:
                    continue
                image_name = self.generate_image_name_from_url(image_url, 'detail')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Ao no Orchestra
class AookeDownload(Spring2023AnimeDownload, NewsTemplate):
    title = 'Ao no Orchestra'
    keywords = [title, 'Blue Orchestra']
    website = 'https://aooke-anime.com/'
    twitter = 'aooke_anime'
    hashtags = '青のオーケストラ'
    folder_name = 'aooke'

    PAGE_PREFIX = website
    FINAL_EPISODE = 24
    IMAGES_PER_EPISODE = 4

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_guess()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            stories = soup.select('.story_nav a[href]')
            for story in stories:
                try:
                    episode = str(int(story.text)).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                if story.has_attr('class') and 'on' in story['class']:
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(story['href'])
                if ep_soup is None:
                    continue
                images = ep_soup.select('.bxslider li img[src]')
                self.image_list = []
                for i in range(len(images)):
                    image_url = self.clear_resize_in_url(images[i]['src'])
                    if 'dummy' in image_url:
                        continue
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_guess(self):
        try:
            template = self.PAGE_PREFIX + 'story/.assets/%s-%s.jpg'
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (str(i + 1), str(j + 1))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news/'
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news_item',
                                    date_select='time', title_select='.ttl',
                                    id_select=None, a_tag_start_text_to_remove='./', a_tag_prefix=news_url)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('ta_mainv', self.PAGE_PREFIX + 'common/img/ta_mainv.jpg')
        self.add_to_image_list('news_kv', self.PAGE_PREFIX + 'news/img/20230224_01.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'common/img/chara_full_%s.png'
        face1_template = self.PAGE_PREFIX + 'common/img/chara_face_%s_01.png'
        face2_template = self.PAGE_PREFIX + 'common/img/chara_face_%s_02.png'
        self.download_by_template(folder, [template, face1_template, face2_template], 2, 1)


# Boku no Kokoro no Yabai Yatsu
class BokuyabaDownload(Spring2023AnimeDownload, NewsTemplate):
    title = 'Boku no Kokoro no Yabai Yatsu'
    keywords = [title, 'The Dangers in My Heart', 'Bokuyaba']
    website = 'https://bokuyaba-anime.com/'
    twitter = 'bokuyaba_anime'
    hashtags = ['僕ヤバ', '僕の心のヤバイやつ']
    folder_name = 'bokuyaba'

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
        story_url = self.PAGE_PREFIX + 'story/'
        yt_folder, yt_episodes = self.init_youtube_thumbnail_variables()
        try:
            soup = self.get_soup(story_url)
            stories = soup.select('a[href].p-story_card')
            for story in stories:
                if 'detail' not in story['href']:
                    continue
                title = story.select('.p-story_card__title')
                if len(title) == 0:
                    continue
                try:
                    episode = str(int(re.sub('\D', '', title[0].text.split('】')[0]))).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1') and episode in yt_episodes:
                    continue
                ep_soup = self.get_soup(story_url + story['href'])
                if ep_soup is None:
                    continue
                self.image_list = []
                images = ep_soup.select('.p-story_in__inner img[src]')
                for i in range(len(images)):
                    image_url = images[i]['src']
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
                yt_tags = ep_soup.select('iframe[src]')
                for yt_tag in yt_tags:
                    if 'youtube' in yt_tag['src']:
                        yt_id = yt_tag['src'].split('/')[-1]
                        self.download_youtube_thumbnail_by_id(yt_id, yt_folder, episode)
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_external(self):
        keywords = ['僕の心のヤバイやつ']
        AniverseMagazineScanner(keywords, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20230328', download_id=self.download_id).run()

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.p-news__list-item',
                                    date_select='.p-news_data__date', title_select='.p-news_data__title',
                                    id_select='a', a_tag_start_text_to_remove='/', a_tag_prefix=self.PAGE_PREFIX,
                                    date_func=lambda x: x[0:4] + '.' + x[5:])

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('.p-hero_kv_visual__main img[src]')
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].replace('./', '')
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'assets/img/character/chara_stand_%s.png'
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            self.image_list = []
            images = soup.select('img.u-lazy[data-src]')
            for image in images:
                img_name = image['data-src'].split('/')[-1].split('.')[0].split('_')[-1]
                image_url = template % img_name
                image_name = 'chara_stand_' + img_name
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')

    def download_media(self):
        folder = self.create_media_directory()
        bd_url = self.PAGE_PREFIX + 'blu-ray/'
        pages = ['novelty', '1019715', '1019721', '1019722']
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        for i in range(len(pages)):
            if str(i) in processed:
                continue
            try:
                if i == 0:
                    soup = self.get_soup(bd_url + pages[0] + '/')
                else:
                    soup = self.get_soup(bd_url + 'detail/?id=' + pages[i])
                self.image_list = []
                images = soup.select(".l-in__container img[src], .l-in__container img[data-src]")
                for image in images:
                    if image.has_attr('src'):
                        image_url = image['src']
                    else:
                        image_url = image['data-src']
                    if not image_url.startswith('http'):
                        continue
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
                if len(self.image_list) > 0:
                    processed.append(str(i))
                self.download_image_list(folder)
            except Exception as e:
                self.print_exception(e, 'Blu-ray')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Dead Mount Death Play
class DeadMountDeathPlayDownload(Spring2023AnimeDownload, NewsTemplate):
    title = 'Dead Mount Death Play'
    keywords = [title, 'DMDP']
    website = 'https://dmdp-anime.jp/'
    twitter = 'DMDP_anime'
    hashtags = ['DMDP']
    folder_name = 'dmdp'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 5

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
            template = self.PAGE_PREFIX + 'images/story/%s_%s.jpg'
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (episode, str(j + 1).zfill(2))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_external(self):
        AnimagePlusScanner('デッドマウント・デスプレイ', self.base_folder, last_episode=self.FINAL_EPISODE,
                           end_date='20230331', download_id=self.download_id).run()

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='#news article',
                                    title_select='h3', date_select='time', id_select=None, id_has_id=True)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.mainimg .swiper-wrapper img[src]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src']
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        templates = [
            self.PAGE_PREFIX + 'images/character/img_%s.png',
            self.PAGE_PREFIX + 'images/character/face_%s.png'
        ]
        self.download_by_template(folder, templates, 2, 1)

    def download_media(self):
        folder = self.create_media_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'blu-ray/')
            images = soup.select('.inner img[src]')
            self.image_list = []
            for image in images:
                if 'nowprinting' in image['src']:
                    continue
                image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


# Edomae Elf
class EdomaeElfDownload(Spring2023AnimeDownload, NewsTemplate):
    title = 'Edomae Elf'
    keywords = [title, 'Otaku Elf']
    website = 'https://edomae-elf.com/'
    twitter = 'edomae_elf'
    hashtags = '江戸前エルフ'
    folder_name = 'edomae-elf'

    PAGE_PREFIX = website
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
        try:
            template = self.PAGE_PREFIX + 'assets/story/%s/%s.jpg'
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (str(i + 1), str(j + 1))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_external(self):
        keywords = ['江⼾前エルフ']
        AniverseMagazineScanner(keywords, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20230331', download_id=self.download_id).run()

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='#Entries article',
                                    title_select='.entry-title span', date_select='.entry-date span',
                                    id_select=None, id_has_id=True, news_prefix='news.html',
                                    date_func=lambda x: x.replace('年', '.').replace('月', '.').replace('日', ''))

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.vis source[srcset]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['srcset'].replace('./', '')
                if '/assets/' not in image_url:
                    continue
                image_name = self.generate_image_name_from_url(image_url, 'assets')
                if image_name.endswith('-sp'):
                    continue
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        templates = [
            self.PAGE_PREFIX + 'assets/character/%sc.webp',
            self.PAGE_PREFIX + 'assets/character/%sc2.webp',
            self.PAGE_PREFIX + 'assets/character/%sf.webp',
            self.PAGE_PREFIX + 'assets/character/%sf2.webp'
        ]
        self.download_by_template(folder, templates, 1, 1)

    def download_media(self):
        folder = self.create_media_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'bluray.html')
            self.image_list = []
            images = soup.select('#Entries img[src]')
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].replace('./', '')
                if '/bluray/' not in image_url:
                    continue
                image_name = self.generate_image_name_from_url(image_url, 'bluray')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


# Isekai de Cheat Skill wo Te ni Shita Ore wa, Genjitsu Sekai wo mo Musou Suru: Level Up wa Jinsei wo Kaeta
class IseleveDownload(Spring2023AnimeDownload, NewsTemplate):
    title = 'Isekai de Cheat Skill wo Te ni Shita Ore wa, Genjitsu Sekai wo mo Musou Suru: Level Up wa Jinsei wo Kaeta'
    keywords = [title, 'I Got a Cheat Skill in Another World and Became Unrivaled in The Real World, Too', 'iseleve']
    website = 'https://www.iseleve.com/'
    twitter = 'iseleve_anime'
    hashtags = 'いせれべ'
    folder_name = 'iseleve'

    PAGE_PREFIX = website
    FINAL_EPISODE = 13
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
        try:
            template = self.PAGE_PREFIX + 'story/img/ep%s_img%s.jpg'
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (episode, str(j + 1).zfill(2))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_external(self):
        keywords = ['異世界でチート能力を手にした俺は']
        AniverseMagazineScanner(keywords, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20230331', download_id=self.download_id).run()

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, news_prefix='', article_select='.news a',
                                    date_select='dt', title_select='dd', id_select=None,
                                    a_tag_start_text_to_remove='./', a_tag_prefix=self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz', 'https://pbs.twimg.com/media/FagU_nNVQAAy78W?format=jpg&name=medium')
        # self.add_to_image_list('tz_main_visual01', self.PAGE_PREFIX + 'img/main_visual01.jpg')
        # self.add_to_image_list('tz_main_visual02', self.PAGE_PREFIX + 'img/main_visual02.png')
        self.add_to_image_list('kv_tw', 'https://pbs.twimg.com/media/FhwPyAwUcAEKojn?format=jpg&name=4096x4096')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('.top_mv_navi a[href]')
            for image in images:
                image_url = self.PAGE_PREFIX + image['href']
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        prefix = self.PAGE_PREFIX + 'character/img/'
        templates = [prefix + 'body_%s_upd.png', prefix + 'face_%s_upd.png']
        self.download_by_template(folder, templates, 2, 1)

    def download_media(self):
        folder = self.create_media_directory()
        self.image_list = []
        self.add_to_image_list('teaser_coment_img01', self.PAGE_PREFIX + 'img/teaser_coment_img01.jpg')
        self.add_to_image_list('teaser_coment_img02', self.PAGE_PREFIX + 'img/teaser_coment_img02.jpg')
        self.download_image_list(folder)

    def download_media(self):
        folder = self.create_media_directory()
        bd_url = self.PAGE_PREFIX + 'bluray/'
        try:
            soup = self.get_soup(bd_url)
            self.image_list = []
            images = soup.select('.page_contents_body img[src]')
            for image in images:
                image_url = bd_url + image['src'].replace('./', '')
                if '/common/' in image_url:
                    continue
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


# Isekai One Turn Kill Nee-san: Ane Douhan no Isekai Seikatsu Hajimemashita
class OneKillSisterDownload(Spring2023AnimeDownload, NewsTemplate):
    title = 'Isekai One Turn Kill Nee-san: Ane Douhan no Isekai Seikatsu Hajimemashita'
    keywords = [title, 'My One-Hit Kill Sister']
    website = 'https://onekillsister.com/'
    twitter = 'onekillsister'
    hashtags = '一撃姉'
    folder_name = 'onekillsister'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 10

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        try:
            template = self.PAGE_PREFIX + 'wp-content/themes/otks/assets/img/story/%s/okn%s_%s.jpg'
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE).zfill(2)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (episode, episode, str(j + 1).zfill(2))
                    image_name = episode + '_' + str(j + 1).zfill(2)
                    if self.download_image(image_url, self.base_folder + '/' + image_name) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-list__item',
                                    date_select='.news-list__item-data', title_select='.news-list__item-text',
                                    id_select='a', date_separator='/', next_page_select='div.pagination .page-numbers',
                                    next_page_eval_index_class='current', next_page_eval_index=-1)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz', self.PAGE_PREFIX + 'wp-content/uploads/2022/07/%E3%83%86%E3%82%A3%E3%82%B5%E3%82%99%E3%83%BC%E3%83%92%E3%82%99%E3%82%B7%E3%82%99%E3%83%A5%E3%82%A2%E3%83%AB.jpg')
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FZxIaC6VsAAOfL0?format=jpg&name=4096x4096')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.main__mv img[src]')
            self.image_list = []
            for image in images:
                image_url = image['src']
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character')
            self.image_list = []
            images = soup.select('ul.gallery img[src]')
            for image in images:
                image_url = image['src']
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Isekai Shoukan wa Nidome desu
class IsenidoDownload(Spring2023AnimeDownload, NewsTemplate):
    title = 'Isekai Shoukan wa Nidome desu'
    keywords = [title, 'isenido']
    website = 'https://isenido.com/'
    twitter = 'isenido_anime'
    hashtags = 'いせにど'
    folder_name = 'isenido'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 5

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            stories = soup.select('.story-unit__number a[href]')
            for story in stories:
                try:
                    episode = str(int(story.text)).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                if story.has_attr('class') and '-current' in story['class']:
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(story['href'])
                self.image_list = []
                images = ep_soup.select('.story-unit__slick-item img[src]')
                for i in range(len(images)):
                    image_url = images[i]['src']
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-lists__item',
                                    date_select='.news-lists__sub', title_select='.news-lists__text', id_select='a',
                                    date_separator='/')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('kv-bg', self.PAGE_PREFIX + 'img/kv-bg.jpg')
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FZxImcZUIAAV8uv?format=jpg&name=4096x4096')
        self.download_image_list(folder)

        self.image_list = []
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.kv-main__wrap .js_kv-img img[src]')
            for image in images:
                if image.has_attr('class') and '-sp' in image['class']:
                    continue
                if not image['src'].startswith('/img/'):
                    continue
                image_url = self.PAGE_PREFIX + image['src'][1:]
                image_name = self.generate_image_name_from_url(image_url, 'img')
                self.add_to_image_list(image_name, image_url)
        except Exception as e:
            self.print_exception(e, 'Key Visual')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('.c-feature__img img[src]')
            for image in images:
                if '/character/' not in image['src']:
                    continue
                image_url = self.PAGE_PREFIX + image['src']
                image_name = self.generate_image_name_from_url(image_url, 'character')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Isekai wa Smartphone to Tomo ni. 2
class Isesuma2Download(Spring2023AnimeDownload, NewsTemplate):
    title = 'Isekai wa Smartphone to Tomo ni. 2'
    keywords = [title, "In Another World With My Smartphone 2"]
    website = 'http://isesuma-anime.jp/'
    twitter = 'isesumaofficial'
    hashtags = 'イセスマ'
    folder_name = 'isesuma2'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        template = self.PAGE_PREFIX + 'img/story/s%s_p%s.jpg'
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                continue
            success = False
            for j in range(self.IMAGES_PER_EPISODE):
                num = str(j + 1)
                image_url = template % (episode, num)
                image_name = episode + '_' + num
                result = self.download_image(image_url, self.base_folder + '/' + image_name)
                if result != -1:
                    success = True
            if not success:
                break

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.entryArea',
                                    date_select='.date', title_select='.subj', id_select='.notexist')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_main', self.PAGE_PREFIX + 'img/main.jpg')
        self.add_to_image_list('main2chara2', self.PAGE_PREFIX + 'img/main2chara2.png')
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FYQeHycaMAIdyyN?format=jpg&name=medium')
        self.add_to_image_list('kv1', 'https://pbs.twimg.com/media/FiZQEg9acAAZ91t?format=jpg&name=large')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.charaArea img[src]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src']
                image_name = self.generate_image_name_from_url(image_url, 'chara')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')

    def download_media(self):
        folder = self.create_media_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'products/index.html?category=1')
            images = soup.select('.itemThumb img[src]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'][1:].split('?')[0]
                if self.is_content_length_in_range(image_url, less_than_amount=386531, more_than_amount=386531,
                                                   is_or=True):
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')

        # Blu-ray Bonus
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'products/item.html?id=3')
            images = soup.select('.mainArea img[src]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'][1:].split('?')[0]
                if 'icon_bd' in image_url or 'b_back' in image_url:
                    continue
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray Bonus')


# Jijou wo Shiranai Tenkousei ga Guigui Kuru.
class GuiguikuruDownload(Spring2023AnimeDownload, NewsTemplate):
    title = 'Jijou wo Shiranai Tenkousei ga Guigui Kuru.'
    keywords = [title, 'My Clueless First Friend', 'guiguikuru']
    website = 'https://guiguikuru.com/'
    twitter = 'guiguikuru_pr'
    hashtags = '転校生がグイグイくる'
    folder_name = 'guiguikuru'

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
            soup = self.get_soup(self.PAGE_PREFIX + 'story/ep01/')
            stories = soup.select('.story--nav a[href]')
            for story in stories:
                try:
                    episode = str(int(story.text)).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                if episode == '01':
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(story['href'])
                if ep_soup is None:
                    continue
                self.image_list = []
                images = ep_soup.select('.story img[src]')
                for i in range(len(images)):
                    image_url = images[i]['src']
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.md-list__news li',
                                    date_select='.date', title_select='.ttl',
                                    id_select='a', next_page_select='.item-next__link')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        template = self.PAGE_PREFIX + '_assets/images/top/fv/webp/fv_%s_pc.webp'
        self.download_by_template(folder, template, 3, 1)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            images = soup.select('.chardata source[type="image/webp"][srcset]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['srcset'][1:]
                image_name = self.extract_image_name_from_url(image_url)
                if image_name.endswith('_pc'):
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')

    def download_episode_preview_guess(self):
        current_date = datetime.now() + timedelta(hours=1)
        year = current_date.strftime('%Y')
        month = current_date.strftime('%m')
        template = self.PAGE_PREFIX + f'wp/wp-content/uploads/{year}/{month}/%s_%s_T%s.jpg'
        for i in range(12):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1'):
                continue
            success = 0
            for j in range(200):
                for k in range(2):
                    url = template % (episode, str(j).zfill(3), str(k + 1))
                    if MainDownload.is_valid_url(url, is_image=True):
                        print('VALID - ' + url)
                        success += 1
                if success == 6:
                    break
            if success == 0:
                break


# Kaminaki Sekai no Kamisama Katsudou
class KamikatsuDownload(Spring2023AnimeDownload, NewsTemplate):
    title = 'Kaminaki Sekai no Kamisama Katsudou'
    keywords = [title, 'kamikatsu']
    website = 'https://kamikatsu-anime.jp/'
    twitter = 'kamikatsu_anime'
    hashtags = ['kamikatsu', 'カミカツ']
    folder_name = 'kamikatsu'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

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
            template = self.PAGE_PREFIX + 'story/_image/story%s_%s.png'
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (episode, str(j + 1).zfill(2))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.newsList li',
                                    date_select='div>i', title_select='div>p', id_select='.abcd',
                                    news_prefix='')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        template = self.PAGE_PREFIX + '_image/kvp%s.png'
        self.download_by_template(folder, template, 1, 1)

        self.image_list = []
        self.add_to_image_list('kv_aniverse', 'https://aniverse-mag.com/wp-content/uploads/2023/03/ffbb6b09910751e8442a50c4f1b40f8b.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        chara_url = self.PAGE_PREFIX + 'character/'
        try:
            soup = self.get_soup(chara_url)
            images = soup.select('#character .swiper-slide img[src]')
            self.image_list = []
            for image in images:
                image_url = chara_url + self.get_image_url_from_srcset(image)
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')

    def download_media(self):
        folder = self.create_media_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        bd_prefix = self.PAGE_PREFIX + 'package/'
        for page in ['', 'prize', 'campaign1', 'campaign2', 'campaign3']:
            try:
                bd_url = bd_prefix
                if len(page) > 0:
                    if page in processed:
                        continue
                    bd_url += page + '.html'
                soup = self.get_soup(bd_url)
                self.image_list = []
                images = soup.select('#bd div>img[srcset], #bd div>img[src]')
                for image in images:
                    if image.has_attr('srcset'):
                        src = image['srcset']
                    else:
                        src = image['src']
                    if src.startswith('/'):
                        image_url = self.PAGE_PREFIX + src[1:]
                    elif src.startswith('http'):
                        image_url = src
                    else:
                        image_url = bd_prefix + src
                    image_name = self.extract_image_name_from_url(image_url)
                    if image_name.startswith('print'):
                        continue
                    self.add_to_image_list(image_name, image_url)
                if len(page) > 0 and page != 'prize' and len(self.image_list) > 0:
                    processed.append(page)
                self.download_image_list(folder)
            except Exception as e:
                self.print_exception(e, 'Blu-ray')
            self.create_cache_file(cache_filepath, processed, num_processed)


# Kawaisugi Crisis https://kawaisugi.com/ #カワイスギクライシス @kawaisugicrisis
class KawaisugiCrisisDownload(Spring2023AnimeDownload, NewsTemplate):
    title = 'Kawaisugi Crisis'
    keywords = [title, 'Too Cute Crisis']
    website = 'https://kawaisugi.com/'
    twitter = 'kawaisugicrisis'
    hashtags = 'カワイスギクライシス'
    folder_name = 'kawaisugicrisis'

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
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            stories = soup.select('#kwsg_contents_introduction_list li')
            for story in stories:
                a_tag = story.select('a[href]')
                if len(a_tag) == 0:
                    continue
                try:
                    episode = str(int(re.sub('\D', '', a_tag[0].text))).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue

                if story.has_attr('class') and 'current' in story['class']:
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(a_tag[0]['href'])
                    if ep_soup is None:
                        continue
                self.image_list = []
                images = ep_soup.select('.story_thumbs img[srcset]')
                for i in range(len(images)):
                    image_url = self.PAGE_PREFIX[:-1] + self.get_image_url_from_srcset(images[i])
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.kwsg_contents_top_news_list_item',
                                    date_select='.kwsg_contents_top_news_list_item_left',
                                    title_select='.kwsg_contents_top_news_list_item_right', id_select='a',
                                    next_page_select='.page-numbers', next_page_eval_index=-1,
                                    next_page_eval_index_class='current')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        template = self.PAGE_PREFIX + 'common/images/top_kv%s.jpg'
        self.download_by_template(folder, template, 2, 2)

    def download_character(self):
        folder = self.create_character_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character')
            a_tags = soup.select('#kwsg_contents_character_list a[href]')
            for a_tag in a_tags:
                if '/character/' not in a_tag['href']:
                    continue
                page = a_tag['href'].split('/')[-1]
                if page in processed:
                    continue
                chara_soup = self.get_soup(a_tag['href'])
                if chara_soup is None:
                    continue
                self.image_list = []
                images = chara_soup.select('#kwsg_contents_character_body img[src]')
                for image in images:
                    image_url = image['src']
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
                if len(self.image_list) > 0:
                    processed.append(page)
                self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')
        self.create_cache_file(cache_filepath, processed, num_processed)

    def download_media(self):
        folder = self.create_media_directory()
        bd_url = self.PAGE_PREFIX + 'blu-ray'
        try:
            soup = self.get_soup(bd_url)
            self.image_list = []
            images = soup.select('#kwsg_contents_main img[src]')
            for image in images:
                if image['src'].endswith('.svg'):
                    continue
                image_url = image['src']
                image_name = self.extract_image_name_from_url(image_url)
                if not self.is_content_length_in_range(image_url, more_than_amount=20000):
                    continue
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


# Kimi wa Houkago Insomnia
class KimisomuDownload(Spring2023AnimeDownload, NewsTemplate):
    title = 'Kimi wa Houkago Insomnia'
    keywords = [title, 'Insomniacs After School', 'kimisomu']
    website = 'https://kimisomu-anime.com/'
    twitter = 'kimisomu_anime'
    hashtags = ['kimisomu', '君ソム']
    folder_name = 'kimisomu'

    PAGE_PREFIX = website
    FINAL_EPISODE = 13
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_episode_preview_guess()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            self.image_list = []
            stories = soup.select('.story-Contents')
            for story in stories:
                try:
                    episode = str(int(story.select('.number')[0].text.replace('#', ''))).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                self.image_list = []
                images = story.select('.swiper-slide img[src]')
                for i in range(len(images)):
                    image_url = images[i]['src']
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

        '''
        try:
            template = self.PAGE_PREFIX + 'wp/wp-content/themes/insomnia_v0/assets/images/common/story/story_%s-%s.png'
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (str(i + 1), str(j + 1))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)
        '''

    def download_episode_preview_guess(self):
        current_date = datetime.now() + timedelta(hours=1)
        year = current_date.strftime('%Y')
        month = current_date.strftime('%m')
        prefix = self.PAGE_PREFIX + f'wp/wp-content/uploads/{year}/{month}/story_%s-1.'
        templates = [prefix + 'png', prefix + 'jpg']
        for i in range(12):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1'):
                continue
            success = 0
            for j in range(len(templates)):
                url = templates[j] % str(i + 1)
                if MainDownload.is_valid_url(url, is_image=True):
                    success = 1
                    ext = templates[j].split('.')[-1]
                    for k in range(self.IMAGES_PER_EPISODE):
                        image_url = self.PAGE_PREFIX + f'wp/wp-content/uploads/{year}/{month}/story_{i + 1}-{k + 1}.{ext}'
                        image_name = episode + '_' + str(k + 1)
                        self.download_image(image_url, self.base_folder + '/' + image_name)
            if success == 0:
                break

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-List_Item',
                                    date_select='time', title_select='.ttl', id_select='a',
                                    date_func=lambda x: x[0:4] + '.' + x[4:], next_page_select='.nextpostslink')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('img_kv_02', self.PAGE_PREFIX + 'wp/wp-content/themes/insomnia_v0/assets/images/pc/index/img_kv_02.png')
        self.add_to_image_list('img_kv_03', self.PAGE_PREFIX + 'wp/wp-content/themes/insomnia_v0/assets/images/pc/index/img_kv_03.png')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            a_tags = soup.select('.chara-List li>a[href]')
            for a_tag in a_tags:
                chara_url = a_tag['href']
                if chara_url.endswith('/'):
                    chara_url = chara_url[:-1]
                chara_name = chara_url.split('/')[-1]
                if chara_name in processed:
                    continue
                chara_soup = self.get_soup(chara_url)
                if chara_soup is None:
                    continue
                images = chara_soup.select('.chara-Detail_Img_Body img[src], .chara-Detail_Face img[src]')
                self.image_list = []
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
            soup = self.get_soup(self.PAGE_PREFIX + 'products/')
            self.image_list = []
            images = soup.select('.products img[src]')
            for image in images:
                image_url = image['src']
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


# Kono Subarashii Sekai ni Bakuen wo!
class KonoSubaBakuenDownload(Spring2023AnimeDownload, NewsTemplate):
    title = 'Kono Subarashii Sekai ni Bakuen wo!'
    keywords = [title, 'KonoSuba', 'An Explosion on This Wonderful World!']
    website = 'http://konosuba.com/bakuen/'
    twitter = 'konosubaanime'
    hashtags = ['konosuba', 'このすば']
    folder_name = 'konosuba-bakuen'

    PAGE_PREFIX = website
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
        story_url = self.PAGE_PREFIX + 'story/'
        try:
            soup = self.get_soup(story_url)
            stories = soup.select('.sub-nav__li a[href]')
            for story in stories:
                try:
                    episode = str(int(story.text.replace('第', '').replace('話', ''))).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                ep_soup = self.get_soup(story_url + story['href'])
                if ep_soup is None:
                    continue
                self.image_list = []
                images = ep_soup.select('.swiper-slide img[src]')
                for i in range(len(images)):
                    image_url = story_url + images[i]['src']
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_guess(self):
        try:
            template = self.PAGE_PREFIX + 'story/img/story%s/%s.jpg'
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (str(i + 1), str(j + 1).zfill(2))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_external(self):
        keywords = ['この素晴らしい世界に爆焔を']
        AniverseMagazineScanner(keywords, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20230328', download_id=self.download_id).run()

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news/'
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-list__item',
                                    date_select='.news-list__date', title_select='.news-list__title',
                                    id_select='a', a_tag_prefix=news_url,
                                    next_page_select='div.pagination .page-numbers',
                                    next_page_eval_index_class='current', next_page_eval_index=-1)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            divs = soup.select('section.top-main div')
            for div in divs:
                if not div.has_attr('class'):
                    continue
                has_mv = False
                for _class in div['class']:
                    if 'mv' in _class and 'logo' not in _class:
                        has_mv = True
                        break
                if not has_mv:
                    continue
                images = div.select('img[src]')
                self.image_list = []
                for image in images:
                    image_url = image['src']
                    if '/img/' not in image_url or image_url.endswith('.svg'):
                        continue
                    image_name = self.generate_image_name_from_url(image_url, 'img')
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        chara_url = self.PAGE_PREFIX + 'character/'
        try:
            soup = self.get_soup(chara_url)
            images = soup.select('.chara-list__item img[src]')
            self.image_list = []
            for image in images:
                image_url = chara_url + image['src']
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')

    def download_media(self):
        folder = self.create_media_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        bd_prefix = self.PAGE_PREFIX + 'bd/'
        for page in ['shop', 'cmp', 'bd1', 'bd2', 'bd3']:
            try:
                if page.startswith('bd') and page in processed:
                    continue
                bd_url = bd_prefix + '?mode=' + page
                soup = self.get_soup(bd_url)
                images = soup.select('.c-box img[src]')
                self.image_list = []
                for image in images:
                    image_url = image['src']
                    if image_url.endswith('np.png'):
                        continue
                    if not image_url.startswith('http://') and not image_url.startswith('https://'):
                        image_url = bd_prefix + image_url
                    if '/img/' in image_url:
                        image_name = self.generate_image_name_from_url(image_url, 'img')
                    else:
                        image_name = self.extract_image_name_from_url(image_url)
                    if self.is_image_exists(image_name, folder):
                        continue
                    self.add_to_image_list(image_name, image_url)
                if page.startswith('bd'):
                    if len(self.image_list) == 0:
                        break
                    else:
                        processed.append(page)
                self.download_image_list(folder)
            except Exception as e:
                self.print_exception(e, f'Blu-ray - {page}')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Kanojo ga Koushaku-tei ni Itta Riyuu
class KoshakuteiDownload(Spring2023AnimeDownload, NewsTemplate):
    title = 'Kanojo ga Koushaku-tei ni Itta Riyuu'
    keywords = [title, "The Reason Why Raeliana Ended up at the Duke's Mansion"]
    website = 'https://koshakutei.com/'
    twitter = 'koshakutei'
    hashtags = ['公爵邸']
    folder_name = 'koshakutei'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()

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
            stories = soup.select('.storyNavi li')
            for story in stories:
                try:
                    episode = str(int(story.select('span')[0].text)).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                a_tag = story.select('a[href]')
                if len(a_tag) == 0:
                    continue
                ep_soup = self.get_soup(a_tag[0]['href'])
                if ep_soup is None:
                    continue
                self.image_list = []
                images = ep_soup.select('.gallery-top .swiper-slide img[src]')
                for i in range(len(images)):
                    image_url = self.clear_resize_in_url(images[i]['src'])
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='#contents li',
                                    title_select='dd', date_select='span', id_select='a')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('keyV', self.PAGE_PREFIX + 'wp-content/themes/koshakutei-anime/images/top/keyV.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        chara_prefix = self.PAGE_PREFIX + 'character/'
        try:
            soup = self.get_soup(chara_prefix)
            a_tags = soup.select('.character__nav a[href]')
            for a_tag in a_tags:
                chara_url = a_tag['href']
                if not chara_url.startswith(chara_prefix):
                    continue
                chara_name = chara_url[len(chara_prefix):].split('/')[0]
                if len(chara_name) == 0:
                    chara_name = 'leliana'
                if chara_name in processed:
                    continue
                if chara_name == 'leliana':
                    chara_soup = soup
                else:
                    chara_soup = self.get_soup(chara_url)
                if chara_soup is not None:
                    images = chara_soup.select('.character__img img[src], .chara__Face img[src]')
                    for image in images:
                        image_url = self.PAGE_PREFIX + image['src'][1:].split('?')[0]
                        if '/character/' not in image_url:
                            continue
                        image_name = self.generate_image_name_from_url(image_url, 'character')
                        self.add_to_image_list(image_name, image_url)
                    if len(self.image_list) > 0:
                        processed.append(chara_name)
                    self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Kuma Kuma Kuma Bear Punch!
class KumaBear2Download(Spring2023AnimeDownload, NewsTemplate2):
    title = 'Kuma Kuma Kuma Bear Punch!'
    keywords = [title, "2nd"]
    website = 'https://kumakumakumabear.com/'
    twitter = 'kumabear_anime'
    hashtags = ['くまクマ熊ベアー', 'kumabear']
    folder_name = 'kumabear2'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_guess()
        self.download_news()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/01.html')
            trs = soup.select('#ContentsListUnit01 tr[class]')
            for tr in trs:
                a_tags = tr.select('a[href]')
                if len(a_tags) == 0:
                    continue
                try:
                    episode = str(int(a_tags[0].text.replace('#', ''))).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                if episode == '01':
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
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_guess(self):
        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'core_sys/images/contents/%s/block/%s/%s.jpg'
        is_successful = False
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1'):
                continue
            is_success = False
            first = 5 + i
            second = 19 + 5 * i
            third = 29 + 7 * i
            for j in range(self.IMAGES_PER_EPISODE):
                image_url = template % (str(first).zfill(8), str(second).zfill(8), str(third + j).zfill(8))
                if not self.is_content_length_in_range(image_url, more_than_amount=7000):
                    break
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
        # self.add_to_image_list('kv_aniverse', 'https://aniverse-mag.com/wp-content/uploads/2022/11/96785c9962f5ef9863dc77113ebdf26f.jpg')
        self.add_to_image_list('tz_kv', self.PAGE_PREFIX + 'core_sys/images/main/tz/kv.webp')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.loading__kv source[srcset]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['srcset']
                if '/main/' in image_url:
                    image_name = self.generate_image_name_from_url(image_url, 'main')
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        self.image_list = []
        self.add_to_image_list('tz_yuna', 'https://aniverse-mag.com/wp-content/uploads/2022/11/aade6f0c762346c7e43719675da36208.png')
        self.add_to_image_list('tz_fina', 'https://aniverse-mag.com/wp-content/uploads/2022/11/de14b80b290bdc786e18e6150c323d0e.png')
        self.download_image_list(folder)

        template = self.PAGE_PREFIX + 'core_sys/images/main/tz/chara_%s.png'
        self.download_by_template(folder, template, 2, 1, prefix='tz_')

    def download_media(self):
        folder = self.create_media_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        for page in ['privilege', 'campaign', '01', '02', '03']:
            try:
                if page != 'privilege' and page in processed:
                    continue
                page_url = self.PAGE_PREFIX + 'bddvd/' + page + '.html'
                soup = self.get_soup(page_url)
                images = soup.select('.block_inner img[src]')
                self.image_list = []
                for image in images:
                    image_url = self.PAGE_PREFIX + image['src'].replace('../', '').split('?')[0]
                    if '/bddvd/' in image_url:
                        image_name = self.generate_image_name_from_url(image_url, 'bddvd')
                    else:
                        image_name = self.extract_image_name_from_url(image_url)
                    if image_name in ['kawase', 'waki']:
                        continue
                    if self.is_image_exists(image_name, folder):
                        continue
                    if (page.isnumeric() and not self.is_content_length_in_range(image_url, more_than_amount=8100))\
                            or (page == 'privilege' and not self.is_content_length_in_range(image_url, more_than_amount=6400)):
                        continue
                    self.add_to_image_list(image_name, image_url)
                if page != 'privilege' and len(self.image_list) > 0:
                    processed.append(page)
                if page.isnumeric() and len(self.image_list) == 0:
                    break
                self.download_image_list(folder)
            except Exception as e:
                self.print_exception(e, f'Blu-ray - {page}')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Megami no Café Terrace
class MegamiCafeDownload(Spring2023AnimeDownload, NewsTemplate):
    title = 'Megami no Café Terrace'
    keywords = [title, 'Cafe', 'The Cafe Terrace and its Goddesses']
    website = 'https://goddess-cafe.com/'
    twitter = 'goddess_cafe_PR'
    hashtags = '女神のカフェテラス'
    folder_name = 'megami-cafe'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        # self.download_episode_preview_guess()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            a_tags = soup.select('.story__cnt--storyArea--linkArea a[href]')
            for a_tag in a_tags:
                try:
                    episode = str(int(a_tag.text)).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                if a_tag.has_attr('class') and ('current' in a_tag['class'] or 'currentLast' in a_tag['class']):
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(a_tag['href'])
                if ep_soup is not None and episode is not None:
                    images = ep_soup.select('.swiper-slide img[src]')
                    self.image_list = []
                    for i in range(len(images)):
                        image_url = images[i]['src']
                        image_name = episode + '_' + str(i + 1)
                        self.add_to_image_list(image_name, image_url)
                    self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.newsArchive__cts--flex--item',
                                    title_select='.txt', date_select='.time', id_select='a',
                                    next_page_select='.pagination .next')

    def download_episode_preview_guess(self, print_invalid=False, download_valid=False):
        if self.is_image_exists(str(self.FINAL_EPISODE).zfill(2) + '_1'):
            return

        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'wp/wp-content/uploads/%s/%s/megami_cafeterrace_%s_%s.jpg'
        current_date = datetime.now() + timedelta(hours=1)
        year = current_date.strftime('%Y')
        month = current_date.strftime('%m')
        is_successful = False
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1') or self.is_image_exists(episode + '_1', folder):
                continue
            image_count = 0
            j = 0
            valid_urls = []
            episode_success = False
            while image_count < self.IMAGES_PER_EPISODE and j <= 200:
                image_url = template % (year, month, episode, str(j).zfill(3))
                if self.is_valid_url(image_url, is_image=True):
                    print('VALID - ' + image_url)
                    episode_success = True
                    image_count += 1
                    valid_urls.append(image_url)
                elif print_invalid:
                    print('INVALID - ' + image_url)
                j += 1
            if download_valid and len(valid_urls) > 0:
                for k in range(len(valid_urls)):
                    image_name = episode + '_' + str(k + 1)
                    self.download_image(valid_urls[k], folder + '/' + image_name)
            if not episode_success:
                break
            is_successful = True
        if is_successful:
            print(self.__class__.__name__ + ' - Guessed correctly!')
        return is_successful

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FhMLJOMUUAAlbav?format=jpg&name=large')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.main-visual-large img[src]')
            self.image_list = []
            for image in images:
                image_url = image['src']
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.character-image img[src]')
            self.image_list = []
            for image in images:
                image_url = image['src']
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')

    def download_media(self):
        folder = self.create_media_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'bluray')
            self.image_list = []
            images = soup.select('.bluray__cnt--area img[src]')
            for image in images:
                image_url = image['src']
                if '/bluray/' not in image_url:
                    continue
                if image_url.startswith('/'):
                    image_url = self.PAGE_PREFIX + image_url[1:]
                image_name = self.generate_image_name_from_url(image_url, 'bluray')
                if not self.is_content_length_in_range(image_url, more_than_amount=65000):
                    continue
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')

        # Blu-ray Bonus
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'store')
            self.image_list = []
            images = soup.select('.store__list--img img[src]')
            for image in images:
                image_url = image['src']
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray Bonus')


# Mashle
class MashleDownload(Spring2023AnimeDownload, NewsTemplate):
    title = 'Mashle'
    keywords = [title, 'Magic and Muscles']
    website = 'https://mashle.pw/'
    twitter = 'mashle_official'
    hashtags = ['マッシュル', 'mashle']
    folder_name = 'mashle'

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
        story_url = self.PAGE_PREFIX + 'episode/'
        try:
            soup = self.get_soup(story_url, decode=True)
            lis = soup.select('.localnav__list li')
            for li in lis:
                span_tag = li.select('span')
                try:
                    ep_num = int(span_tag[0].text)
                    if ep_num is None or ep_num < 1:
                        continue
                    episode = str(ep_num).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                if li.has_attr('class') and 'is--current' in li['class']:
                    ep_soup = soup
                else:
                    a_tag = li.select('a[href]')
                    if len(a_tag) == 0:
                        continue
                    ep_soup = self.get_soup(story_url + a_tag[0]['href'].replace('./', ''))
                if ep_soup is not None:
                    images = ep_soup.select('.swiper-wrapper img[src]')
                    self.image_list = []
                    for i in range(len(images)):
                        image_url = story_url + images[i]['src']
                        image_name = episode + '_' + str(i + 1)
                        self.add_to_image_list(image_name, image_url)
                    self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news/'
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news__list li',
                                    date_select='.list--date', title_select='.list--text',
                                    id_select='a', a_tag_prefix=news_url, a_tag_start_text_to_remove='./',
                                    paging_type=1, next_page_select='.news__pager__next',
                                    next_page_eval_index_class='is--last', next_page_eval_index=-1)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz', self.PAGE_PREFIX + "news/SYS/CONTENTS/927ec0b8-5d51-459e-a69f-04381e4f8163")
        self.add_to_image_list('kv1', self.PAGE_PREFIX + "news/SYS/CONTENTS/8aea33dc-da55-4117-9c7f-c6e26af39323")
        self.add_to_image_list('kv2', self.PAGE_PREFIX + "news/SYS/CONTENTS/8fcd3e64-a906-4f4c-af99-fa36ec6afc7b")
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        templates = [
            self.PAGE_PREFIX + 'teaser/img/character/c%s_main.webp',
            self.PAGE_PREFIX + 'teaser/img/character/c%s_sub.png'
        ]
        self.download_by_template(folder, templates, 2, 1)

    def download_media(self):
        folder = self.create_media_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        for page in ['special', '01', '02', '03', '04']:
            try:
                if page != 'special' and page in processed:
                    continue
                page_url = self.PAGE_PREFIX + 'bddvd/' + page + '.html'
                soup = self.get_soup(page_url)
                sections = soup.select('#bddvd-page>section')
                for section in sections:
                    if section.has_attr('class') and 'headline' in section['class']:
                        continue
                    images = section.select('img[src]')
                    self.image_list = []
                    for image in images:
                        image_url = self.PAGE_PREFIX + image['src'].replace('../', '').split('?')[0]
                        if 'np02.jpg' in image_url or 'np.jpg' in image_url:
                            continue
                        if '/bddvd/' in image_url:
                            image_name = self.generate_image_name_from_url(image_url, 'bddvd')
                        else:
                            continue
                        if self.is_image_exists(image_name, folder):
                            continue
                        self.add_to_image_list(image_name, image_url)
                if page.isnumeric():
                    if len(self.image_list) == 0:
                        break
                    else:
                        processed.append(page)
                self.download_image_list(folder)
            except Exception as e:
                self.print_exception(e, f'Blu-ray - {page}')
        self.create_cache_file(cache_filepath, processed, num_processed)


# My Home Hero
class MyHomeHeroDownload(Spring2023AnimeDownload, NewsTemplate):
    title = 'My Home Hero'
    keywords = [title]
    website = 'https://myhomehero-anime.com/'
    twitter = 'myhomehero_pr'
    hashtags = ['MyHomeHero', 'マイホームヒーロー']
    folder_name = 'myhomehero'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        # self.download_episode_preview_external()
        self.download_news()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        yt_folder, yt_episodes = self.init_youtube_thumbnail_variables()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/', decode=True)
            stories = soup.select('.story-box')
            for story in stories:
                try:
                    episode = str(int(story.select('.story-num span')[0].text)).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1') and episode in yt_episodes:
                    continue
                images = story.select('.story-ss img[src]')
                self.image_list = []
                for i in range(len(images)):
                    image_url = images[i]['src']
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)

                # YouTube thumbnail
                try:
                    yt_tag = story.select('.story-movie iframe[src]')
                    if len(yt_tag) > 0 and len(yt_tag[0]['src']) > 0:
                        yt_id = yt_tag[0]['src'].split('/')[-1]
                        self.download_youtube_thumbnail_by_id(yt_id, yt_folder, episode)
                except:
                    pass
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_external(self):
        keywords = ['マイホームヒーロー']
        AniverseMagazineScanner(keywords, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20230331', download_id=self.download_id).run()

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-item',
                                    title_select='p.title', date_select='p.date', id_select='a')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('mhh_honban_images_kv-pc', self.PAGE_PREFIX + "wp/wp-content/themes/mhh-honban/images/kv-pc.jpg")
        self.add_to_image_list('mhh_teaser_images_kv-pc', self.PAGE_PREFIX + "wp/wp-content/themes/mhh-teaser/images/kv-pc.jpg")
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'wp/wp-content/themes/mhh-honban/images/chara-pic%s.png'
        self.download_by_template(folder, template, 2, 1)

    def download_media(self):
        folder = self.create_media_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'bluray/')
            images = soup.select(".section-contents img[src]")
            for image in images:
                image_url = self.PAGE_PREFIX + image['src']
                image_name = self.extract_image_name_from_url(image_url)
                if image_name in ['bluray-jacket', 'privilege-pic']:
                    continue
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


# Oshi no Ko
class OshinokoDownload(Spring2023AnimeDownload, NewsTemplate2):
    title = 'Oshi no Ko'
    keywords = [title, 'oshinoko']
    website = 'https://ichigoproduction.com/'
    twitter = 'anime_oshinoko'
    hashtags = '推しの子'
    folder_name = 'oshinoko'

    PAGE_PREFIX = website
    FINAL_EPISODE = 11
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
            stories = soup.select('#ContentsListUnit03 a[href]')
            for story in stories:
                try:
                    ep_num = self.convert_kanji_to_number(story.text.replace('第', '').replace('話', ''))
                    if ep_num is None:
                        continue
                    episode = str(ep_num).zfill(2)
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
                    image_url = self.PAGE_PREFIX + images[i]['src'].split('?')[0].replace('../', '').replace('sn_', '')
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_external(self):
        keywords = ['推しの子']
        AniverseMagazineScanner(keywords, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20230418', download_id=self.download_id).run()

    def download_episode_preview_guess(self):
        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'core_sys/images/contents/%s/block/%s/%s.jpg'
        is_successful = False
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1'):
                continue
            is_success = False
            first = 25 + i
            second = 68 + 6 * i
            third = 65 + self.IMAGES_PER_EPISODE * i
            break_inner_loop = False
            for k in [0, -1, 1]:
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (str(first).zfill(8), str(second + k).zfill(8), str(third + j).zfill(8))
                    image_name = episode + '_' + str(j + 1)
                    result = self.download_image(image_url, folder + '/' + image_name)
                    if result == 0:
                        is_success = True
                        is_successful = True
                        break_inner_loop = True
                    elif result == -1:
                        break
                if break_inner_loop:
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
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FU0bJsjaAAAE7Bf?format=jpg&name=large')
        self.add_to_image_list('tz_kv', self.PAGE_PREFIX + 'core_sys/images/main/tz/kv.jpg')
        self.add_to_image_list('tz_kv2', self.PAGE_PREFIX + 'core_sys/images/main/tz/kv2/kv.jpg')
        self.add_to_image_list('tz_kv3', self.PAGE_PREFIX + 'core_sys/images/main/kv3/kv3.jpg')
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
                    if 'ビジュアル' in title:
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
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'chara/')
            a_tags = soup.select('#ContentsListUnit01 a[href]')
            for a_tag in a_tags:
                chara_url = self.PAGE_PREFIX + a_tag['href'].replace('../', '')
                chara_name = chara_url.split('/')[-1].replace('.html', '')
                if chara_name in processed:
                    continue
                if chara_name == 'index':
                    chara_soup = soup
                else:
                    chara_soup = self.get_soup(chara_url)
                if chara_soup is not None:
                    images = chara_soup.select('.ph img[src]')
                    for image in images:
                        image_url = self.PAGE_PREFIX + image['src'].replace('../', '').split('?')[0]
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
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        privilege_names = ['00000137', '00000138', '00000139', '00000140', '00000141']
        for page in ['privilege', 'campaign', '01', '02', '03', '04', '05', '06']:
            try:
                if page != 'privilege' and page in processed:
                    continue
                page_url = self.PAGE_PREFIX + 'bd/'
                if page != '01':
                    page_url += page + '.html'
                soup = self.get_soup(page_url)
                images = soup.select('.block_inner img[src]')
                self.image_list = []
                for image in images:
                    image_url = self.PAGE_PREFIX + image['src'].replace('../', '').split('?')[0]
                    if '/bddvd/' in image_url:
                        image_name = self.generate_image_name_from_url(image_url, 'bddvd')
                    else:
                        image_name = self.extract_image_name_from_url(image_url)
                    if self.is_image_exists(image_name, folder):
                        if page.startswith('privilege') and image_name in privilege_names:
                            self.download_image_with_different_length(image_url, image_name, 'old', folder)
                        continue
                    if (page.isnumeric() and not self.is_content_length_in_range(image_url, more_than_amount=25000))\
                            or (page == 'privilege' and not self.is_content_length_in_range(image_url, more_than_amount=13000)):
                        continue
                    self.add_to_image_list(image_name, image_url)
                if page != 'privilege' and len(self.image_list) > 0:
                    processed.append(page)
                if page.isnumeric() and len(self.image_list) == 0:
                    break
                self.download_image_list(folder)
            except Exception as e:
                self.print_exception(e, f'Blu-ray - {page}')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Otonari ni Ginga
class OtonariniGingaDownload(Spring2023AnimeDownload, NewsTemplate):
    title = 'Otonari ni Ginga'
    keywords = [title, 'A Galaxy Next Door']
    website = 'https://otonari-anime.com/'
    twitter = 'otonariniginga'
    hashtags = 'おとなりに銀河'
    folder_name = 'otonariniginga'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 8

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
            template = self.PAGE_PREFIX + 'assets/images/story/%s_%s.jpg'
            files = os.listdir(self.base_folder)

            image_count = {}
            for file in files:
                if os.path.isfile(self.base_folder + '/' + file) and '_' in file:
                    split1 = file.split('.')[0].split('_')
                    if len(split1) == 2 and split1[0].isnumeric() and split1[1].isnumeric() and len(split1[0]) == 2:
                        ep_num = split1[0]
                        if ep_num in image_count:
                            image_count[ep_num] += 1
                        else:
                            image_count[ep_num] = 1

            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if episode in image_count and image_count[episode] == self.IMAGES_PER_EPISODE:
                    continue
                success = False
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (episode, str(j + 1))
                    image_name = episode + '_' + str(j + 1)
                    if self.is_image_exists(image_name):
                        success = True
                        continue
                    if self.download_image(image_url, self.base_folder + '/' + image_name) == -1:
                        continue
                    else:
                        success = True
                if not success:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='#news article',
                                    title_select='h3', date_select='time', id_select=None, id_has_id=True,
                                    date_func=lambda x: x[0:4] + '.' + x[4:])

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FRV6mlUVIAAa9xK?format=jpg&name=medium')
        self.add_to_image_list('tz_mainimg', self.PAGE_PREFIX + 'teaser/images/mainimg.png')
        self.add_to_image_list('kv_tw', 'https://pbs.twimg.com/media/FgjBzJOaAAADdI_?format=jpg&name=medium')
        self.download_image_list(folder)

        template = self.PAGE_PREFIX + 'assets/images/top/mainimg%s.jpg'
        self.download_by_template(folder, template, 1, 1, prefix='top_')

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'assets/images/character/img_%s.png'
        self.download_by_template(folder, template, 2, 1)

    def download_media(self):
        folder = self.create_media_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'blu-ray/')
            self.image_list = []
            images = soup.select(".inner img[src]")
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                image_name = self.extract_image_name_from_url(image_url)
                if 'nowprinting' in image_name:
                    continue
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


# Skip to Loafer
class SkipLoaferDownload(Spring2023AnimeDownload, NewsTemplate):
    title = 'Skip to Loafer'
    keywords = [title, 'Skip and Loafer']
    website = 'https://skip-and-loafer.com/'
    twitter = 'skip_and_loafer'
    hashtags = ['スキップとローファー', 'スキロー']
    folder_name = 'skip-loafer'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        try:
            template = self.PAGE_PREFIX + 'assets/story/%s/%s.jpg'
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (str(i + 1), str(j + 1))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='#Entries article',
                                    title_select='.entry-title span', date_select='.entry-date span',
                                    id_select=None, id_has_id=True, news_prefix='news.html')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.vis source[srcset]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['srcset'].replace('./', '')
                if '/assets/' not in image_url:
                    continue
                image_name = self.generate_image_name_from_url(image_url, 'assets')
                if image_name.endswith('-sp'):
                    continue
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        templates = [
            self.PAGE_PREFIX + 'assets/character/%sc.png',
            self.PAGE_PREFIX + 'assets/character/%sf.png'
        ]
        self.download_by_template(folder, templates, 1, 1)


# Tensei Kizoku no Isekai Boukenroku
class TenseiKizokuDownload(Spring2023AnimeDownload, NewsTemplate):
    title = 'Tensei Kizoku no Isekai Boukenroku'
    keywords = [title, "Chronicles of an Aristocrat Reborn in Another World"]
    website = 'https://www.tensei-kizoku.jp/'
    twitter = 'tenseikizoku'
    hashtags = '転生貴族'
    folder_name = 'tenseikizoku'

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
            soup = self.get_soup(self.PAGE_PREFIX + 'story.html')
            stories = soup.select('div.introduction')
            for story in stories:
                h4 = story.select('h4')
                if len(h4) == 0:
                    continue
                try:
                    episode = str(int(h4[0].text.replace('第', '').replace('話', ''))).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                images = story.select('.story-img img[src]')
                stop = False
                for i in range(len(images)):
                    image_url = self.PAGE_PREFIX + images[i]['src']
                    image_name = episode + '_' + str(i + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name, to_jpg=True) == -1:
                        stop = True
                        break
                    webp_image_file = self.base_folder + '/' + episode + '_' + str(i + 1) + '.webp'
                    if os.path.exists(webp_image_file):
                        try:
                            self.convert_image_to_jpg(webp_image_file)
                        except Exception as e:
                            self.print_exception(e, 'Error in converting webp to jpg.')
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-list li',
                                    date_select='.news-date', title_select='.news-title', id_select='a',
                                    news_prefix='news.html', reverse_article_list=True)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        # self.add_to_image_list('kv', self.PAGE_PREFIX + 'img/kv.png')
        self.add_to_image_list('top_illust_alpha', self.PAGE_PREFIX + 'assets/images/top_illust_alpha.webp')
        self.add_to_image_list('kv2', 'https://pbs.twimg.com/media/FqX1jaNaIAIqtSE?format=jpg&name=large')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + '/character.html')
            self.image_list = []
            images = soup.select('ul[name=chara] img[src]')
            for image in images:
                if '/chara/' in image['src'] and '/name/' not in image['src']:
                    image_url = self.PAGE_PREFIX + image['src']
                    image_name = self.generate_image_name_from_url(image_url, 'chara')
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')

    def download_media(self):
        folder = self.create_media_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'bluray.html')
            images = soup.select(".blueray-detail img[src]")
            for image in images:
                image_url = self.PAGE_PREFIX + image['src']
                if '/blueray/' not in image_url:
                    continue
                image_name = self.generate_image_name_from_url(image_url, 'blueray')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


# Tonikaku Kawaii S2
class Tonikawa2Download(Spring2023AnimeDownload, NewsTemplate):
    title = "Tonikaku Kawaii 2nd Season"
    keywords = [title, "Tonikawa", "Cawaii", "Fly Me to the Moon", "Over the Moon for You", "2nd"]
    website = 'http://tonikawa.com/'
    twitter = 'tonikawa_anime'
    hashtags = ['トニカクカワイイ', 'tonikawa']
    folder_name = 'tonikawa2'

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
        try:
            template = self.PAGE_PREFIX + 'assets/images/common/story/season2/ep%s/img_%s.jpg'
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (episode, str(j + 1))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='div.archive li',
                                    date_select='.date', title_select='.title p', id_select='a',
                                    a_tag_prefix=self.PAGE_PREFIX, a_tag_start_text_to_remove='/',
                                    stop_date='2021.10.08')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FDf9oGkaIAE7jnd?format=jpg&name=large')
        self.add_to_image_list('kv_seifuku', self.PAGE_PREFIX + 'assets/images/common/news/news-67/img_kv_l.jpg')
        self.add_to_image_list('tz2_tw', 'https://pbs.twimg.com/media/FiE3-1yVIAA8Scs?format=jpg&name=large')
        self.add_to_image_list('tz2', self.PAGE_PREFIX + 'assets/images/common/news/news-70/thumb_kv3_l.jpg')
        self.add_to_image_list('kv_tw', 'https://pbs.twimg.com/media/Fo6mnWmaYAE8cfj?format=jpg&name=large')
        self.download_image_list(folder)


# Watashi no Yuri wa Oshigoto desu!
class WatayuriDownload(Spring2023AnimeDownload, NewsTemplate):
    title = 'Watashi no Yuri wa Oshigoto desu!'
    keywords = [title, 'watayuri', 'Yuri is My Job!']
    website = 'https://watayuri-anime.com/'
    twitter = 'watayuri_anime'
    hashtags = ['わたゆり', '私の百合はお仕事です']
    folder_name = 'watayuri'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 8

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_external()
        # self.download_episode_preview_guess()
        self.download_news()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        story_url = self.PAGE_PREFIX + 'story/'
        yt_folder, yt_episodes = self.init_youtube_thumbnail_variables()
        try:
            soup = self.get_soup(story_url, decode=True)
            stories = soup.select('.storyDetail')
            for story in stories:
                try:
                    episode = str(int(re.sub('\D', '', story['id']))).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)) and episode in yt_episodes:
                    continue
                images = story.select('.story_imageList img[src]')
                self.image_list = []
                for i in range(len(images)):
                    image_url = images[i]['src']
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
                yt_tag = story.select('.story_movie button[onclick]')
                if len(yt_tag) > 0:
                    try:
                        yt_id = yt_tag[0]['onclick'].split("'")[1]
                        self.download_youtube_thumbnail_by_id(yt_id, yt_folder, episode)
                    except:
                        pass
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_external(self):
        keywords = ['私の百合はお仕事です']
        AniverseMagazineScanner(keywords, self.base_folder, last_episode=self.FINAL_EPISODE, prefix='シフト.', suffix='',
                                end_date='20230330', download_id=self.download_id).run()

    def download_episode_preview_guess(self):
        folder = self.create_custom_directory('aniverse')
        current_date = datetime.now() + timedelta(hours=1)
        year = current_date.strftime('%Y')
        month = current_date.strftime('%m')
        max_search = 20
        for i in range(12):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1') or self.is_image_exists(episode + '_01', folder):
                continue
            template = f'https://aniverse-mag.com/wp-content/uploads/{year}/{month}/watayuri_ep{episode}_CAP%s.jpeg'
            urls = []
            for j in range(200):
                url = template % str(j).zfill(3)
                if MainDownload.is_valid_url(url, is_image=True):
                    print('VALID - ' + url)
                    urls.append(url)
                if len(urls) >= self.IMAGES_PER_EPISODE or (j == max_search and len(urls) == 0):
                    break
            if len(urls) == 0:
                break
            self.image_list = []
            for k in range(len(urls)):
                image_url = urls[k]
                image_name = episode + '_' + str(k + 1).zfill(2)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.newsList',
                                    date_select='time', title_select='.news__title', id_select='a')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FStxiD1VIAEX1nk?format=jpg&name=4096x4096')
        self.add_to_image_list('top_visual_mv1_p1', self.PAGE_PREFIX + 'assets/img/top/top/visual/mv1_p1.jpg')
        self.add_to_image_list('top_visual_mv1_p2', self.PAGE_PREFIX + 'assets/img/top/top/visual/mv1_p2.jpg')
        self.add_to_image_list('top_visual_mv2', self.PAGE_PREFIX + 'assets/img/top/top/visual/mv2.jpg')
        self.add_to_image_list('news_23_kv', self.PAGE_PREFIX + 'liebe/wp-content/uploads/2022/12/75f074420bc90cf826a501bd011f8312.jpg')
        self.add_to_image_list('kv_tw', 'https://pbs.twimg.com/media/Fo6mh3saUAIVZPF?format=jpg&name=large')
        self.add_to_image_list('mv_aprilfool__2304010000_gRr2UWbQGQcX', self.PAGE_PREFIX + 'assets/img/top/aprilfool/mv_aprilfool__2304010000_gRr2UWbQGQcX.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            a_tags = soup.select('li.characterList a[href]')
            for a_tag in a_tags:
                if not a_tag['href'].startswith("javascript:chara('") or not a_tag['href'].endswith("');"):
                    continue
                page = a_tag['href'][18:-3]
                if len(page) == 0:
                    continue
                if page in processed:
                    continue
                chara_soup = self.get_soup(self.PAGE_PREFIX + 'character/data/chara_' + page + '.html')
                if chara_soup is None:
                    continue
                self.image_list = []
                images = chara_soup.select('.charaImage_stand img[src], .charaFaceImg img[src]')
                for image in images:
                    image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
                if len(self.image_list) > 0:
                    processed.append(page)
                self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')
        self.create_cache_file(cache_filepath, processed, num_processed)

    def download_media(self):
        folder = self.create_media_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'bd/')
            self.image_list = []
            images = soup.select('.bdContents img[src]')
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                if '/bd/' not in image_url:
                    continue
                image_name = self.generate_image_name_from_url(image_url, 'bd')
                if image_name.startswith('print'):
                    continue
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


# Yamada-kun to Lv999 no Koi wo Suru
class Yamada999Download(Spring2023AnimeDownload, NewsTemplate):
    title = 'Yamada-kun to Lv999 no Koi wo Suru'
    keywords = [title, 'Loving Yamada at Lv999']
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
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        story_url = self.PAGE_PREFIX + 'story/'
        try:
            soup = self.get_soup(story_url, decode=True)
            story_list = soup.select('.p-story__nav')
            if len(story_list) > 0:
                lis = story_list[0].select('li')
                for li in lis:
                    span_tag = li.select('span')
                    try:
                        ep_num = int(span_tag[0].text)
                        if ep_num is None or ep_num < 1:
                            continue
                        episode = str(ep_num).zfill(2)
                    except:
                        continue
                    if self.is_image_exists(episode + '_1'):
                        continue
                    if li.has_attr('class') and 'is-current' in li['class']:
                        ep_soup = soup
                    else:
                        a_tag = li.select('a[href]')
                        if len(a_tag) == 0:
                            continue
                        ep_soup = self.get_soup(story_url + a_tag[0]['href'].replace('./', ''))
                    if ep_soup is not None:
                        images = ep_soup.select('.swiper-wrapper img[src]')
                        self.image_list = []
                        for i in range(len(images)):
                            image_url = story_url + images[i]['src']
                            image_name = episode + '_' + str(i + 1)
                            self.add_to_image_list(image_name, image_url)
                        self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

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
        self.add_to_image_list('top_kv', self.PAGE_PREFIX + 'teaser/img/top/kv.jpg')
        self.add_to_image_list('top_kv_2', self.PAGE_PREFIX + 'teaser/img/top/kv_2.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            images = soup.select('.p-chara_data__whole-img img[src]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')

    def download_media(self):
        folder = self.create_media_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        for page in ['01', '02', '03', '04', '05', '06', '07']:
            try:
                if page != '01' and page in processed:
                    continue
                page_url = self.PAGE_PREFIX + 'bddvd/'
                if page != '01':
                    page_url += page + '.html'
                soup = self.get_soup(page_url)
                if page == '01':
                    images = soup.select('.p-bddvd img[src], .p-bddvd__shop img[src]')
                else:
                    images = soup.select('.p-bddvd__maininfo img[src]')
                self.image_list = []
                for image in images:
                    image_url = self.PAGE_PREFIX + image['src'].replace('../', '').split('?')[0]
                    if image_url.endswith('.svg') or '/bddvd/' not in image_url:
                        continue
                    image_name = self.generate_image_name_from_url(image_url, 'bddvd')
                    self.add_to_image_list(image_name, image_url)
                if page != '01':
                    if len(self.image_list) == 0:
                        break
                    else:
                        processed.append(page)
                self.download_image_list(folder)
            except Exception as e:
                self.print_exception(e, f'Blu-ray - {page}')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Yuusha ga Shinda!
class YuushagaShindaDownload(Spring2023AnimeDownload, NewsTemplate):
    title = 'Yuusha ga Shinda!'
    keywords = [title, 'The Legendary Hero Is Dead!']
    website = 'https://heroisdead.com/'
    twitter = 'yuusyagasinda'
    hashtags = '勇者が死んだ'
    folder_name = 'yuushagashinda'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_episode_preview_guess()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        if self.is_image_exists(str(self.FINAL_EPISODE) + '_1') and self.is_image_exists('01_1'):
            return

        try:
            objs = self.get_json('https://heroisdead.com/news/wp-json/wp/v2/pages?orderby=date&order=asc&acf_format=standard&per_page=100&parent=39')
            for obj in objs:
                if 'acf' in obj:
                    acf = obj['acf']
                    if 'number' in acf and '<span>' in acf['number'] and '</span>' in acf['number']\
                            and 'images' in acf and isinstance(acf['images'], list):
                        try:
                            episode = str(int(acf['number'].split('</span>')[0].split('<span>')[1])).zfill(2)
                        except:
                            continue
                        for i in range(len(acf['images'])):
                            image_url = acf['images'][i]
                            image_name = episode + '_' + str(i + 1)
                            self.add_to_image_list(image_name, image_url)
                        self.download_image_list(self.base_folder)
        except HTTPError:
            print(self.__class__.__name__ + ' - 403 Error when retrieving story API.')
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_guess(self):
        current_date = datetime.now() + timedelta(hours=1)
        year = current_date.strftime('%Y')
        month = current_date.strftime('%m')
        prefix = self.PAGE_PREFIX + f'news/wp/wp-content/uploads/{year}/{month}/'
        thigh_prefix = prefix + 'Yuusyagasinda_ep%s-thigh1.'
        normal_prefix = prefix + 'Yuusyagasinda_ep%s-pre1.'
        templates = [thigh_prefix + 'jpg', thigh_prefix + 'jpeg', normal_prefix + 'jpg', normal_prefix + 'jpeg']
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1'):
                continue
            success = 0
            for j in range(len(templates)):
                url = templates[j] % episode
                if MainDownload.is_valid_url(url, is_image=True):
                    print('VALID - ' + url)
            if success == 0:
                break

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-list-item',
                                    date_select='.news-list-item__date', title_select='.news-list-item__title',
                                    id_select='a', a_tag_start_text_to_remove='/', a_tag_prefix=self.PAGE_PREFIX,
                                    date_func=lambda x: x.replace('年', '.').replace('月', '.').replace('日', ''))

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'special/')
            a_tags = soup.select('div.l-grid a[href]')
            for a_tag in a_tags:
                href = a_tag['href']
                if not href.startswith('../special/') or not href.endswith('.jpg'):
                    continue
                image_url = self.PAGE_PREFIX + href.replace('../', '')
                image_name = self.generate_image_name_from_url(image_url, 'special')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

        self.image_list = []
        # self.add_to_image_list('tz_aniverse', 'https://aniverse-mag.com/wp-content/uploads/2022/04/4576fa0e88a0464f6a9b6e8844e05dbd-e1651058246996.jpg')
        # self.add_to_image_list('tz_visual_01_chara', self.PAGE_PREFIX + 'img/teaser/visual_01_chara.png')
        # self.add_to_image_list('vis_kneesock', 'https://pbs.twimg.com/media/FilDh8XagAQnZU0?format=jpg&name=large')
        self.add_to_image_list('kv2_tw', 'https://pbs.twimg.com/media/FkGRdxEUcAECPlX?format=jpg&name=large')
        self.download_image_list(folder)

        # template = self.PAGE_PREFIX + 'img/home/visual_%s_chara.webp'
        # self.download_by_template(folder, template, 2, 1, prefix='home_')

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
        bd_url = self.PAGE_PREFIX + 'product/bdbox/'
        try:
            soup = self.get_soup(bd_url)
            self.image_list = []
            images = soup.select('article img[src]')
            for image in images:
                if image['src'].endswith('.svg') or image['src'].startswith('http') or image['src'].startswith('../'):
                    continue
                image_url = bd_url + image['src']
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')
