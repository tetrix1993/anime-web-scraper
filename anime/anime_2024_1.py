import os
import re
from anime.main_download import MainDownload, NewsTemplate, NewsTemplate2, NewsTemplate4
from datetime import datetime, timedelta
from scan import AniverseMagazineScanner
from requests.exceptions import HTTPError

# Akuyaku Reijou Level 99 https://akuyakulv99-anime.com/ #akuyakuLV99 @akuyakuLV99
# Ao no Exorcist: Shimane Illuminati-hen https://ao-ex.com/ #青エク #aoex @aoex_anime
# Chiyu Mahou no Machigatta Tsukaikata https://chiyumahou-anime.com/ #治癒魔法 @chiyumahou_PR
# Dosanko Gal wa Namara Menkoi https://dosankogal-pr.com/ #道産子ギャル #どさこい @dosankogal_pr
# Dungeon Meshi https://delicious-in-dungeon.com/ #ダンジョン飯 #deliciousindungeon @dun_meshi_anime
# Gekai Elise https://surgeon-elise.com/ #外科医エリーゼ #surgeon_elise @surgeon_elise
# Himesama "Goumon" no Jikan desu https://himesama-goumon.com/ #姫様拷問の時間です @himesama_goumon
# Kekkon Yubiwa Monogatari https://talesofweddingrings-anime.jp/ #結婚指輪物語 @weddingringsPR
# Ishura https://ishura-anime.com/ #異修羅 @ishura_anime
# Jaku-Chara Tomozaki-kun 2nd Stage http://tomozaki-koushiki.com/ #友崎くん @tomozakikoshiki
# Kingdom 5th Season https://kingdom-anime.com/story/ #キングダム @kingdom_animePR
# Loop 7-kaime no Akuyaku Reijou wa, Moto Tekikoku de Jiyuu Kimama na Hanayome Seikatsu wo Mankitsu suru https://7th-timeloop.com/ #ルプなな @7th_timeloop
# Mahou Shoujo ni Akogarete https://mahoako-anime.com/ #まほあこ #まほあこアニメ @mahoako_anime
# Majo to Yajuu https://www.tbs.co.jp/anime/majo/ #魔女と野獣 @majo_yajuu
# Mato Seihei no Slave https://mabotai.jp/ #魔都精兵のスレイブ #まとスレ @mabotai_kohobu
# Metallic Rogue https://metallicrouge.jp/ #メタリックルージュ @MetallicRouge
# Nozomanu Fushi no Boukensha https://nozomanufushi-anime.jp/ #望まぬ不死 #TUUA @nozomanufushiPR
# Ore dake Level Up na Ken https://sololeveling-anime.net/ #俺レベ #SoloLeveling @sololeveling_pr
# Oroka na Tenshi wa Akuma to Odoru https://kanaten-anime.com/ #かな天 #kanaten @kanaten_PR
# Pon no Michi https://ponnomichi-pr.com/ #ぽんのみち @ponnomichi_pr
# Saijaku Tamer wa Gomi Hiroi no Tabi wo Hajimemashita. https://saijakutamer-anime.com/ #最弱テイマー @saijakutamer
# Saikyou Tank no Meikyuu Kouryaku https://saikyo-tank.com/ #最強タンク @saikyo_tank
# Sasaki to Pii-chan https://sasapi-anime.com/ #ささピー @sasaki_pichan
# Sengoku Youko https://sengoku-youko.com/ #戦国妖狐 @sengoku_youko
# Shin no Nakama ja Nai to Yuusha no Party wo Oidasareta node, Henkyou de Slow Life suru Koto ni Shimashita 2nd https://shinnonakama.com/ #真の仲間 @shinnonakama_tv
# Sokushi Cheat ga Saikyou sugite, Isekai no Yatsura ga Marude Aite ni Naranai n desu ga. https://sokushicheat-pr.com/ #即死チート @sokushicheat_pr
# Tsuki ga Michibiku Isekai Douchuu 2nd Season https://tsukimichi.com/ #ツキミチ @tsukimichi_PR
# Urusei Yatsura (2022) 2nd Season https://uy-allstars.com/ #うる星やつら @uy_allstars
# Youkoso Jitsuryoku Shijou Shugi no Kyoushitsu e S3 http://you-zitsu.com/ #you_zitsu #よう実 @youkosozitsu
# Yubisaki to Renren https://yubisaki-pr.com/ #ゆびさきと恋々 @yubisaki_pr


# Winter 2024 Anime
class Winter2024AnimeDownload(MainDownload):
    season = "2024-1"
    season_name = "Winter 2024"
    folder_name = '2024-1'

    def __init__(self):
        super().__init__()


# Akuyaku Reijou Level 99
class AkuyakuLv99Download(Winter2024AnimeDownload, NewsTemplate2):
    title = 'Akuyaku Reijou Level 99'
    keywords = [title, 'Villainess Level 99']
    website = 'https://akuyakulv99-anime.com/'
    twitter = 'akuyakuLV99'
    hashtags = 'akuyakuLV99'
    folder_name = 'akuyakulv99'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
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
            soup = self.get_soup(self.PAGE_PREFIX + 'story/01.html')
            a_tags = soup.select('#ContentsListUnit02 a[href]')
            for a_tag in a_tags:
                try:
                    episode = str(int(a_tag.text.replace('#', ''))).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                if episode == '01':
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(self.PAGE_PREFIX + a_tag['href'].replace('../', ''))
                if ep_soup is None:
                    continue
                self.image_list = []
                images = ep_soup.select('.tp5 img[src]')
                for i in range(len(images)):
                    image_url = self.PAGE_PREFIX + images[i]['src'].split('?')[0].replace('../', '').replace('sn_', '')
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(self.PAGE_PREFIX)

    def download_episode_preview_guess(self):
        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'core_sys/images/contents/%s/block/%s/%s.jpg'
        is_successful = False
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1'):
                continue
            is_success = False
            first = 24 + i
            second = 48 + 4 * i
            third = 62 + 6 * i
            for j in range(self.IMAGES_PER_EPISODE):
                image_url = template % (str(first).zfill(8), str(second).zfill(8), str(third + j).zfill(8))
                image_name = episode + '_' + str(j + 1)
                if not self.is_content_length_in_range(image_url, more_than_amount=13000):
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

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/Fr-S3r0aQAAH2xA?format=jpg&name=medium')
        self.add_to_image_list('tzkv', self.PAGE_PREFIX + 'core_sys/images/main/home/tzkv.png')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.mainImg__kv source[type][srcset]')
            self.image_list = []
            for image in images:
                if '/main/' not in image['srcset']:
                    continue
                image_name = self.extract_image_name_from_url(image['srcset'])
                if 'kv' not in image_name:
                    continue
                image_name = self.generate_image_name_from_url(image['srcset'], 'main')
                image_url = self.PAGE_PREFIX + image['srcset'].split('?')[0].replace('./', '')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.charaStand source[type][srcset], .charaFace source[type][srcset]')
            self.image_list = []
            for image in images:
                if '/chara/' not in image['srcset']:
                    continue
                image_name = self.generate_image_name_from_url(image['srcset'], 'chara')
                image_url = self.PAGE_PREFIX + image['srcset'].split('?')[0].replace('./', '')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')

    def download_media(self):
        folder = self.create_media_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        for page in ['privilege', 'campaign', '01', '02', '03']:
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
                    image_url = self.PAGE_PREFIX + image['src'].replace('../', '').split('?')[0]
                    if '/bd/' in image_url:
                        image_name = self.generate_image_name_from_url(image_url, 'bd')
                    else:
                        image_name = self.extract_image_name_from_url(image_url)
                    if not self.is_content_length_in_range(image_url, more_than_amount=13500):
                        continue
                    self.add_to_image_list(image_name, image_url)
                if page.isnumeric() and len(self.image_list) > 0:
                    processed.append(page)
                elif page.isnumeric():
                    break
                self.download_image_list(folder)
            except Exception as e:
                self.print_exception(e, f'Blu-ray - {page}')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Ao no Exorcist: Shimane Illuminati-hen
class Aoex3Download(Winter2024AnimeDownload, NewsTemplate):
    title = 'Ao no Exorcist: Shimane Illuminati-hen'
    keywords = [title, 'aoex', 'Blue Exorcist: Shimane Illuminati Saga']
    website = 'https://ao-ex.com/'
    twitter = 'aoex_anime'
    hashtags = ['青エク', 'aoex']
    folder_name = 'aoex3'

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
            story_prefix = self.PAGE_PREFIX + 'story/'
            soup = self.get_soup(story_prefix)
            stories = soup.select('.storyNavList')
            for story in stories:
                try:
                    episode = str(int(story.select('.storyNavList__linktxt')[0].text)).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_5'):
                    continue
                if '--is-current' in story['class']:
                    ep_soup = soup
                else:
                    a_tag = story.select('a[href]')
                    if len(a_tag) == 0:
                        continue
                    story_url = a_tag[0]['href']
                    if story_url.startswith('./'):
                        story_url = story_prefix + story_url[2:]
                    ep_soup = self.get_soup(story_url)
                if ep_soup is None:
                    continue
                self.image_list = []
                images = ep_soup.select('.storyImageList img[src]')
                for i in range(len(images)):
                    image_name = episode + '_' + str(i + 1)
                    image_url = story_prefix + images[i]['src']
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='li.newsList',
                                    date_select='.newsList__date', title_select='.newsList__title', id_select='a',
                                    a_tag_prefix=self.PAGE_PREFIX + 'news/', paging_type=1,
                                    next_page_select='.pagerList a', next_page_eval_index=-1,
                                    next_page_eval_index_class='current')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.visualImage img[src*="/visual/"]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].replace('./', '').split('?')[0]
                if 'visual1_layer' in image_url:
                    continue
                image_name = self.generate_image_name_from_url(image_url, 'visual')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'assets/img/top/character/chara%s_main.png'
        self.download_by_template(folder, template, 1, 1)

    def download_media(self):
        folder = self.create_media_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        for page in ['tokuten', '1', '2']:
            try:
                if page in processed:
                    continue
                page_url = self.PAGE_PREFIX + 'bddvd/'
                if page.isnumeric():
                    page_url += 'vol'
                page_url += page + '.html'
                soup = self.get_soup(page_url)
                images = soup.select('.bddvdArticle img[src*="/bddvd/"]')
                self.image_list = []
                for image in images:
                    image_url = self.PAGE_PREFIX + image['src'].replace('../', '').split('?')[0]
                    if '_noimg' in image_url:
                        continue
                    image_name = self.generate_image_name_from_url(image_url, 'bddvd')
                    self.add_to_image_list(image_name, image_url)
                if page.isnumeric() and len(self.image_list) > 0:
                    processed.append(page)
                elif page.isnumeric():
                    break
                self.download_image_list(folder)
            except Exception as e:
                self.print_exception(e, f'Blu-ray - {page}')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Boku no Kokoro no Yabai Yatsu Season 2
class Bokuyaba2Download(Winter2024AnimeDownload, NewsTemplate):
    title = 'Boku no Kokoro no Yabai Yatsu Season 2'
    keywords = [title, 'The Dangers in My Heart', 'Bokuyaba', '2nd']
    website = 'https://bokuyaba-anime.com/'
    twitter = 'bokuyaba_anime'
    hashtags = ['僕ヤバ', '僕の心のヤバイやつ']
    folder_name = 'bokuyaba2'

    PAGE_PREFIX = website
    FIRST_EPISODE = 13
    FINAL_EPISODE = 24

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_external()
        self.download_news()
        self.download_key_visual()
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
                    ep_num = int(re.sub('\D', '', title[0].text.split('】')[0]))
                    episode = str(ep_num).zfill(2)
                except:
                    continue
                if ep_num < self.FIRST_EPISODE:
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
                                end_date='20240104', download_id=self.download_id).run()

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.p-news__list-item',
                                    date_select='.p-news_data__date', title_select='.p-news_data__title',
                                    id_select='a', a_tag_start_text_to_remove='/', a_tag_prefix=self.PAGE_PREFIX,
                                    date_func=lambda x: x[0:4] + '.' + x[5:], stop_date='2023.06.16')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('.p-hero_kv_visual__main img[src]')
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].replace('./', '')
                image_name = self.extract_image_name_from_url(image_url)
                if image_name in ['kv01', 'kv02', 'kv03', 'kv04']:
                    continue
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_media(self):
        folder = self.create_media_directory()
        bd_url = self.PAGE_PREFIX + 'blu-ray/'
        pages = ['novelty2', '1020118', '1020119', '1020120']
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
                    if not image_url.startswith('http') or '/shop/' in image_url:
                        continue
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
                if len(self.image_list) > 0:
                    processed.append(str(i))
                self.download_image_list(folder)
            except Exception as e:
                self.print_exception(e, 'Blu-ray')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Chiyu Mahou no Machigatta Tsukaikata
class ChiyuMahouDownload(Winter2024AnimeDownload, NewsTemplate):
    title = 'Chiyu Mahou no Machigatta Tsukaikata'
    keywords = [title, 'The Wrong Way to Use Healing Magic']
    website = 'https://chiyumahou-anime.com/'
    twitter = 'chiyumahou_PR'
    hashtags = ['治癒魔法']
    folder_name = 'chiyumahou'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_episode_preview_guess(print_invalid=False, download_valid=True)
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            eps = soup.select('ul.story-TabList a[href]')
            for ep in eps:
                try:
                    episode = str(int(ep.text.replace('#', ''))).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                if ep.has_attr('class') and 'is-current' in ep['class']:
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(self.PAGE_PREFIX + ep['href'][1:])
                if ep_soup is None:
                    continue
                images = ep_soup.select('#gallery-main img[src]')
                self.image_list = []
                for i in range(len(images)):
                    image_url = images[i]['src'].split('?')[0]
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.newsArchive-Item',
                                    date_select='.date', title_select='.title', id_select='a',
                                    next_page_select='.nextpostslink')

    def download_episode_preview_guess(self, print_invalid=False, download_valid=False):
        if self.is_image_exists(str(self.FINAL_EPISODE).zfill(2) + '_' + str(self.IMAGES_PER_EPISODE)):
            return

        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'wp-content/uploads/%s/%s/%s'
        current_date = datetime.now() + timedelta(hours=1)
        year = current_date.strftime('%Y')
        month = current_date.strftime('%m')
        image_folder = folder + '/' + year + '/' + month
        is_successful = False
        valid_urls = []

        for i in range(self.FINAL_EPISODE):
            ep_num = i + 1
            episode = str(ep_num).zfill(2)
            if self.is_image_exists(episode + '_1')\
                    or self.is_image_exists('img_story_ep' + str(ep_num) + '-1', image_folder):
                continue
            is_success = False
            for j in range(self.IMAGES_PER_EPISODE):
                image_name = 'img_story_ep%s-%s' % (str(ep_num), str(j + 1))
                image_url = template % (year, month, image_name + '.jpg')
                if self.is_valid_url(image_url, is_image=True):
                    print('VALID - ' + image_url)
                    is_successful = True
                    is_success = True
                    valid_urls.append({'name': image_name, 'url': image_url, 'folder': image_folder})
                elif print_invalid:
                    print('INVALID - ' + image_url)
                    break
            if not is_success:
                break
        if download_valid and len(valid_urls) > 0:
            for valid_url in valid_urls:
                image_name = valid_url['name']
                image_folder = valid_url['folder']
                if not os.path.exists(image_folder):
                    os.makedirs(image_folder)
                self.download_image(valid_url['url'], image_folder + '/' + image_name)
        if is_successful:
            print(self.__class__.__name__ + ' - Guessed correctly!')
        return is_successful

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        # self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FwP_QYPaQAMBkyd?format=jpg&name=medium')
        self.add_to_image_list('tz', self.PAGE_PREFIX + 'wp-content/themes/chiyumahou-anime_teaser/assets/images/pc/index/img_hero.jpg')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.visual img[src]')
            self.image_list = []
            for image in images:
                if '/pc/' not in image['src']:
                    continue
                image_url = image['src'].split('?')[0]
                image_name = self.generate_image_name_from_url(image_url, 'pc')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            a_tags = soup.select('.character-List li>a[href]')
            for a_tag in a_tags:
                chara_url = a_tag['href']
                if chara_url.endswith('/'):
                    chara_name = chara_url[:-1].split('/')[-1]
                else:
                    chara_name = chara_url.split('/')[-1]
                if chara_name in processed:
                    continue
                chara_soup = self.get_soup(self.PAGE_PREFIX + chara_url[1:])
                if chara_soup is not None:
                    images = chara_soup.select('.character-Detail img[src]')
                    for image in images:
                        image_url = image['src']
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

    def download_media(self):
        folder = self.create_media_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'product/')
            images = soup.select('.products-Index img[src*="/products/"]')
            self.image_list = []
            for image in images:
                image_url = image['src'].split('?')[0]
                image_name = self.generate_image_name_from_url(image_url, 'products')
                if 'nowprinting' in image_name:
                    continue
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


# Dosanko Gal wa Namara Menkoi
class DosankoGalDownload(Winter2024AnimeDownload, NewsTemplate):
    title = 'Dosanko Gal wa Namara Menkoi'
    keywords = [title, 'Hokkaido Gals Are Super Adorable!', 'dosakoi']
    website = 'https://dosankogal-pr.com/'
    twitter = 'dosankogal_pr'
    hashtags = ['道産子ギャル', 'どさこい']
    folder_name = 'dosankogal'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        soup = self.download_episode_preview()
        self.download_news()
        self.download_episode_preview_guess(print_invalid=False, download_valid=True)
        soup = self.download_key_visual(soup)
        self.download_character(soup)
        self.download_media()

    def download_episode_preview(self):
        soup = None
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            script = soup.select('style[type="text/css"]')[0].text
            split1 = script.split('#js-epsodes-slider[data-ep="')
            for s in split1:
                if '.js--ss' not in s:
                    continue
                try:
                    episode = str(int(s.split('"')[0])).zfill(2)
                except:
                    continue
                split2 = s.split('{')
                if len(split2) < 2:
                    continue
                try:
                    pic_num = str(int(s.split('.js--ss')[1].split('{')[0]))
                except:
                    continue
                image_name = episode + '_' + pic_num
                if self.is_image_exists(image_name):
                    continue
                if 'background-image: url(' in split2[1] and ');' in split2[1] \
                        and split2[1].index('background-image: url(') < split2[1].index(');'):
                    image_url = split2[1].split('background-image: url(')[1].split(');')[0]
                    image_name = episode + '_' + pic_num
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)
        return soup

    def download_news(self):
        # Paging logic not known
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.md-list__news li',
                                    date_select='.txt--date', title_select='.txt--ttl', id_select='a')

    def download_episode_preview_guess(self, print_invalid=False, download_valid=False):
        if self.is_image_exists(str(self.FINAL_EPISODE).zfill(2) + '_' + str(self.IMAGES_PER_EPISODE)):
            return

        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'wp/wp-content/uploads/%s/%s/%s.jpg'
        current_date = datetime.now() + timedelta(hours=1)
        year = current_date.strftime('%Y')
        month = current_date.strftime('%m')
        is_successful = False
        valid_urls = []
        for j in range(self.IMAGES_PER_EPISODE):
            k = 0
            while k < 20:
                if k == 0:
                    append = ''
                else:
                    append = '-' + str(k)
                image_folder = folder + '/' + year + '/' + month
                image_name = str(j + 1).zfill(2) + append
                if not self.is_image_exists(image_name, image_folder):
                    image_url = template % (year, month, image_name)
                    if self.is_valid_url(image_url, is_image=True):
                        print('VALID - ' + image_url)
                        is_successful = True
                        valid_urls.append({'name': image_name, 'url': image_url, 'folder': image_folder})
                    elif print_invalid:
                        print('INVALID - ' + image_url)
                        break
                k += 1
        if download_valid and len(valid_urls) > 0:
            for valid_url in valid_urls:
                image_name = valid_url['name']
                image_folder = valid_url['folder']
                if not os.path.exists(image_folder):
                    os.makedirs(image_folder)
                self.download_image(valid_url['url'], image_folder + '/' + image_name)
        if is_successful:
            print(self.__class__.__name__ + ' - Guessed correctly!')
        return is_successful

    def download_key_visual(self, soup=None):
        folder = self.create_key_visual_directory()
        # self.image_list = []
        # self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FkJnLbAVUAERF5S?format=jpg&name=4096x4096')
        # self.add_to_image_list('tz_news', self.PAGE_PREFIX + 'wp/wp-content/uploads/2022/12/dosankogal_teaser_logoc-scaled-1.jpg')
        # self.download_image_list(folder)

        try:
            if soup is None:
                soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.fvslide source[srcset]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['srcset'][1:]
                if '/images/' not in image_url:
                    continue
                image_name = self.generate_image_name_from_url(image_url, 'images')
                if image_name.endswith('_sp'):
                    continue
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')
        return soup

    def download_character(self, soup=None):
        folder = self.create_character_directory()
        try:
            if soup is None:
                soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.chardata--inner source[srcset]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['srcset'][1:]
                if '/images/' not in image_url:
                    continue
                image_name = self.generate_image_name_from_url(image_url, 'images')
                if image_name.endswith('_sp'):
                    continue
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')

    def download_media(self):
        folder = self.create_media_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        for page in ['store', '1', '2', '3']:
            try:
                if page in processed:
                    continue
                page_url = self.PAGE_PREFIX + 'bd/'
                if page.isnumeric():
                    page_url += 'vol'
                page_url += page
                soup = self.get_soup(page_url)
                images = soup.select('.bd img[src]')
                self.image_list = []
                for image in images:
                    image_url = self.PAGE_PREFIX + image['src'][1:]
                    if '/np_' in image_url:
                        continue
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
                if page.isnumeric() and len(self.image_list) > 0:
                    processed.append(page)
                elif page.isnumeric():
                    break
                self.download_image_list(folder)
            except Exception as e:
                self.print_exception(e, f'Blu-ray - {page}')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Dungeon Meshi
class DungeonMeshiDownload(Winter2024AnimeDownload, NewsTemplate):
    title = 'Dungeon Meshi'
    keywords = [title, 'Delicious in Dungeon']
    website = 'https://delicious-in-dungeon.com/'
    twitter = 'dun_meshi_anime'
    hashtags = ['ダンジョン飯', 'deliciousindungeon']
    folder_name = 'dungeon-meshi'

    PAGE_PREFIX = website
    FINAL_EPISODE = 24
    IMAGES_PER_EPISODE = 8

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_external()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        try:
            template = self.PAGE_PREFIX + 'assets/story/%s/%s.webp'
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (str(i + 1), str(j + 1))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name, to_jpg=True) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_external(self):
        keywords = ['ダンジョン飯']
        AniverseMagazineScanner(keywords, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20231229', download_id=self.download_id).run()

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.content-entry',
                                    title_select='.entry-title span', date_select='.entry-date span',
                                    id_select=None, id_has_id=True, news_prefix='news.html')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.vis img[src]')
            self.image_list = []
            for image in images:
                if '/assets/' not in image['src']:
                    continue
                image_url = image['src']
                if image_url.startswith('./'):
                    image_url = self.PAGE_PREFIX + image_url[2:]
                image_name = self.generate_image_name_from_url(image_url, 'assets')
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


# Gekai Elise
class GekaiEliseDownload(Winter2024AnimeDownload, NewsTemplate):
    title = 'Gekai Elise'
    keywords = [title, 'Surgeon Elise']
    website = 'https://surgeon-elise.com/'
    twitter = 'surgeon_elise'
    hashtags = ['外科医エリーゼ', 'surgeon_elise']
    folder_name = 'gekaielise'

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
            template = self.PAGE_PREFIX + 'images/story/%s/p_%s.jpg'
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (str(i + 1).zfill(3), str(j + 1).zfill(3))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_external(self):
        keywords = ['外科医エリーゼ']
        AniverseMagazineScanner(keywords, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20231223', download_id=self.download_id).run()

    def download_news(self):
        try:
            results = []
            news_obj = self.get_last_news_log_object()
            json_obj = self.get_json(self.PAGE_PREFIX + 'news.json')
            for item in json_obj:
                if 'day' in item and 'url' in item and 'title' in item:
                    try:
                        date = datetime.strptime(item['day'], "%Y/%m/%d").strftime("%Y.%m.%d")
                    except:
                        continue
                    title = item['title']
                    url = self.PAGE_PREFIX + item['url']
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

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('.visual_wrap img[src*="/visual/"]')
            for image in images:
                image_url = self.PAGE_PREFIX + image['src']
                if '/top/' not in image_url:
                    continue
                image_name = self.generate_image_name_from_url(image_url, 'top')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        prefix = self.PAGE_PREFIX + 'images/chara/'
        templates = [prefix + 'a_%s.png', prefix + 'b_%s.png']
        self.download_by_template(folder, templates, 3, 1)

    def download_media(self):
        folder = self.create_media_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'package.html')
            self.image_list = []
            images = soup.select('article img[src*="/package/"]')
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].split('?')[0]
                if 'nowpri' in image_url or 'tokuten/p_000.jpg' in image_url:
                    continue
                image_name = self.generate_image_name_from_url(image_url, 'package')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


# Himesama "Goumon" no Jikan desu
class HimesamaGoumonDownload(Winter2024AnimeDownload, NewsTemplate):
    title = 'Himesama "Goumon" no Jikan desu'
    keywords = [title, '\'Tis Time for "Torture," Princess']
    website = 'https://himesama-goumon.com/'
    twitter = 'himesama_goumon'
    hashtags = ['姫様拷問の時間です']
    folder_name = 'himesamagoumon'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        soup = self.download_episode_preview()
        self.download_news()
        # self.download_episode_preview_guess(print_invalid=False, download_valid=True)
        soup = self.download_key_visual(soup)
        self.download_character(soup)

    def download_episode_preview(self):
        soup = None
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            script = soup.select('style[type="text/css"]')[0].text
            split1 = script.split('#js-epwrap[data-ep="')
            for s in split1:
                if '#js-ep-thumb' not in s:
                    continue
                try:
                    episode = str(int(s.split('"')[0])).zfill(2)
                except:
                    continue
                split2 = s.split('{')
                if len(split2) < 2:
                    continue
                try:
                    pic_num = str(int(s.split('#js-ep-thumb')[1].split('{')[0]))
                except:
                    continue
                image_name = episode + '_' + pic_num
                if self.is_image_exists(image_name):
                    continue
                if 'background-image: url(' in split2[1] and ');' in split2[1]\
                        and split2[1].index('background-image: url(') < split2[1].index(');'):
                    image_url = split2[1].split('background-image: url(')[1].split(');')[0]
                    image_name = episode + '_' + pic_num
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)
        return soup

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.md-li__news li',
                                    date_select='.date', title_select='.ttl', id_select='a')

    def download_episode_preview_guess(self, print_invalid=False, download_valid=False):
        if self.is_image_exists(str(self.FINAL_EPISODE).zfill(2) + '_' + str(self.IMAGES_PER_EPISODE)):
            return

        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'wp/wp-content/uploads/%s/%s/%s.jpg'
        current_date = datetime.now() + timedelta(hours=1)
        year = current_date.strftime('%Y')
        month = current_date.strftime('%m')
        is_successful = False
        valid_urls = []
        for j in range(self.IMAGES_PER_EPISODE):
            k = 0
            while k < 20:
                if k == 0:
                    append = ''
                else:
                    append = '-' + str(k)
                image_folder = folder + '/' + year + '/' + month
                image_name = str(j + 1).zfill(2) + append
                if not self.is_image_exists(image_name, image_folder):
                    image_url = template % (year, month, image_name)
                    if self.is_valid_url(image_url, is_image=True):
                        print('VALID - ' + image_url)
                        is_successful = True
                        valid_urls.append({'name': image_name, 'url': image_url, 'folder': image_folder})
                    elif print_invalid:
                        print('INVALID - ' + image_url)
                        break
                k += 1
        if download_valid and len(valid_urls) > 0:
            for valid_url in valid_urls:
                image_name = valid_url['name']
                image_folder = valid_url['folder']
                if not os.path.exists(image_folder):
                    os.makedirs(image_folder)
                self.download_image(valid_url['url'], image_folder + '/' + image_name)
        if is_successful:
            print(self.__class__.__name__ + ' - Guessed correctly!')
        return is_successful

    def download_key_visual(self, soup=None):
        folder = self.create_key_visual_directory()
        try:
            if soup is None:
                soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('.fv--visual source[srcset]')
            for image in images:
                image_url = self.PAGE_PREFIX + image['srcset'][1:]
                if '/webp/' not in image_url:
                    continue
                image_name = self.extract_image_name_from_url(image_url)
                if image_name.endswith('_sp'):
                    continue
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')
        return soup

    def download_character(self, soup=None):
        folder = self.create_character_directory()
        try:
            if soup is None:
                soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('.chardata--inner .visual source[srcset]')
            for image in images:
                image_url = self.PAGE_PREFIX + image['srcset'][1:]
                if '/webp/' not in image_url:
                    continue
                image_name = self.extract_image_name_from_url(image_url)
                if image_name.endswith('_sp'):
                    continue
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Kekkon Yubiwa Monogatari
class KekkonYubiwaDownload(Winter2024AnimeDownload, NewsTemplate):
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
        self.download_news()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/episode1/')
            eps = soup.select('.pagenav a[href*="/story/"]')
            for ep in eps:
                try:
                    episode = str(int(ep.text)).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                if episode == '01':
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(ep['href'])
                if ep_soup is not None:
                    images = ep_soup.select('.sto_inimg img[src]')
                    self.image_list = []
                    for i in range(len(images)):
                        image_url = images[i]['src'].split('?')[0]
                        image_name = episode + '_' + str(i + 1)
                        self.add_to_image_list(image_name, image_url)
                    self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, news_prefix='', article_select='.newsinlist li',
                                    date_select='.newstime', title_select='a', id_select='a', id_has_id=True,
                                    id_attr='data-cl')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz', self.PAGE_PREFIX + 'images/mob02/per_bg.png')
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FsCGtvQaMAEldYZ?format=jpg&name=large')
        self.download_image_list(folder)

        sub_folder = self.create_custom_directory(folder.split('/')[-1] + '/news')
        cache_filepath = sub_folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        try:
            soup = self.get_soup(self.PAGE_PREFIX, decode=True)
            items = soup.select('.newsinlist li a[data-cl]')
            for item in items:
                page_name = item['data-cl']
                if page_name in processed:
                    break
                title = item.text.strip()
                if 'ビジュアル' in title or 'イラスト' in title:
                    images = soup.select(f'.lbox_com.{page_name} img[src]')
                    self.image_list = []
                    for image in images:
                        image_url = self.PAGE_PREFIX + image['src'].replace('./', '').split('?')[0]
                        if '/news/' not in image_url or image_url.endswith('.svg'):
                            continue
                        image_name = self.generate_image_name_from_url(image_url, 'news')
                        self.add_to_image_list(image_name, image_url)
                    self.download_image_list(sub_folder)
                processed.append(page_name)
        except Exception as e:
            self.print_exception(e, 'Key Visual News')
        self.create_cache_file(cache_filepath, processed, num_processed)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'images/mob02/chara_%s.png'
        self.download_by_template(folder, template, 2, 1)

    def download_media(self):
        folder = self.create_media_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'product/bd/')
            self.image_list = []
            images = soup.select('.pgincontent img[src*="/images/"]')
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].replace('../', '').split('?')[0]
                if 'nowprinting' in image_url:
                    continue
                image_name = self.generate_image_name_from_url(image_url, 'images')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')

        # Story Visuals
        special_folder = folder + '/special'
        if not os.path.exists(special_folder):
            os.makedirs(special_folder)
        template = self.PAGE_PREFIX + 'images/special/p%s.jpg'
        self.download_by_template(special_folder, template, 2, 1)


# Isekai de Mofumofu Nadenade suru Tame ni Ganbattemasu.
class MofunadeDownload(Winter2024AnimeDownload, NewsTemplate):
    title = 'Isekai de Mofumofu Nadenade suru Tame ni Ganbattemasu.'
    keywords = [title, 'Fluffy Paradise']
    website = 'https://mohunadeanime.com/'
    twitter = 'mohunade_anime'
    hashtags = 'もふなで'
    folder_name = 'mofunade'

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
        self.download_media()

    def download_episode_preview(self):
        try:
            template = self.PAGE_PREFIX + 'dist/img/story/ep%s/img%s.jpg'
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
        self.add_to_image_list('kv', self.PAGE_PREFIX + 'dist/img/news/article/article7/img01.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'dist/img/character/character%s/img2.webp'
        try:
            for i in range(20):
                image_url = template % str(i + 1)
                image_name = str(i + 1).zfill(2)
                if self.is_image_exists(image_name, folder):
                    continue
                result = self.download_image(image_url, folder + '/' + image_name)
                if result == -1:
                    break
        except Exception as e:
            self.print_exception(e, 'Character')

    def download_media(self):
        folder = self.create_media_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('.tab-bd_container img[src]')
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].replace('./', '')
                if '_smaple' in image_url:
                    continue
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


# Ishura
class IshuraDownload(Winter2024AnimeDownload, NewsTemplate):
    title = 'Ishura'
    keywords = [title]
    website = 'https://ishura-anime.com/'
    twitter = 'ishura_anime'
    hashtags = '異修羅'
    folder_name = 'ishura'

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
            template = self.PAGE_PREFIX + 'assets/story/%s/%s.webp'
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (str(i + 1), str(j + 1))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name, to_jpg=True) == -1:
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
            images = soup.select('.vis-grp .vis source[srcset],.vis-grp .mono source[srcset]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['srcset'].replace('./', '').split('?')[0]
                image_name = self.extract_image_name_from_url(image_url)
                if '-sp' in image_name:
                    continue
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        prefix = self.PAGE_PREFIX + 'assets/character/c'
        templates = [prefix + '%sr.webp', prefix + 'f%s.webp']
        self.download_by_template(folder, templates, 1, 1)

    def download_media(self):
        folder = self.create_media_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'bddvd.html')
            self.image_list = []
            images = soup.select('#BdData img[src*="/bddvd/"]')
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].split('?')[0].replace('./', '')
                if '/np.png' in image_url:
                    continue
                image_name = self.generate_image_name_from_url(image_url, 'bddvd')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


# Jaku-Chara Tomozaki-kun 2nd Stage
class TomozakiKun2Download(Winter2024AnimeDownload, NewsTemplate):
    title = "Jaku-Chara Tomozaki-kun 2nd Stage"
    keywords = [title, 'Bottom-Tier Character Tomozaki', 'Tomozaki-kun']
    website = 'http://tomozaki-koushiki.com/'
    twitter = 'tomozakikoshiki'
    hashtags = '友崎くん'
    folder_name = 'tomozakikun2'

    PAGE_PREFIX = website
    FINAL_EPISODE = 13
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()

    def download_episode_preview(self):
        try:
            template = self.PAGE_PREFIX + 'img/story/story2-%s/img%s.jpg'
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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.box_main',
                                    date_select='time', title_select='.box_title', id_select='nothing')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        template = self.PAGE_PREFIX + 'img/index/vis_img%s.jpg'
        self.download_by_template(folder, template, 1, 1)


# Kingdom 5th Season
class Kingdom5Download(Winter2024AnimeDownload):
    title = "Kingdom 5th Season"
    keywords = [title]
    website = 'https://kingdom-anime.com/'
    twitter = 'kingdom_animePR'
    hashtags = 'キングダム'
    folder_name = 'kingdom5'

    STORY_PAGE = "https://kingdom-anime.com/story/"
    FINAL_EPISODE = 26

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_external()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.STORY_PAGE)
            ep_list = soup.find('ul', id='ep_list').find_all('li')
            for ep in ep_list:
                try:
                    episode = self.get_episode_number(ep.find('span', class_='hd').text)
                    if episode is None:
                        continue
                    if self.is_file_exists(self.base_folder + "/" + episode + "_0.jpg") or self.is_file_exists(
                            self.base_folder + "/" + episode + "_0.png"):
                        continue
                    a_tag = ep.find('a')
                    try:
                        thumb_image_url = a_tag.find('div', class_='ep_thumb')['style'].split('(')[1].split(')')[0]
                        self.download_image(thumb_image_url, self.base_folder + '/' + episode + '_0')
                    except:
                        continue
                    ep_url = self.STORY_PAGE + a_tag['href']
                    ep_soup = self.get_soup(ep_url)
                    images = ep_soup.find('div', id='episodeCont').find_all('img')
                    for j in range(len(images)):
                        image_url = images[j]['src']
                        file_path_without_extension = self.base_folder + '/' + episode + '_' + str(j + 1)
                        self.download_image(image_url, file_path_without_extension)
                except:
                    continue
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_external(self):
        jp_title = 'キングダム'
        AniverseMagazineScanner(jp_title, self.base_folder, last_episode=self.FINAL_EPISODE, prefix='',
                                end_date='20240104', download_id=self.download_id).run()


# Loop 7-kaime no Akuyaku Reijou wa, Moto Tekikoku de Jiyuu Kimama na Hanayome Seikatsu wo Mankitsu suru
class Loop7KaimeDownload(Winter2024AnimeDownload, NewsTemplate):
    title = 'Loop 7-kaime no Akuyaku Reijou wa, Moto Tekikoku de Jiyuu Kimama na Hanayome Seikatsu wo Mankitsu suru'
    keywords = [title, '7th Time Loop: The Villainess Enjoys a Carefree Life Married to Her Worst Enemy!']
    website = 'https://7th-timeloop.com/'
    twitter = '7th_timeloop'
    hashtags = ['ルプなな']
    folder_name = 'loop7kaime'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        soup = self.download_episode_preview()
        self.download_news()
        self.download_episode_preview_guess(print_invalid=False, download_valid=True)
        self.download_key_visual(soup)
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        soup = None
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            nums = soup.select('.story_epnumList a[href]')
            for num in nums:
                if not num['href'].startswith('#'):
                    continue
                try:
                    episode = str(int(num.select('.storyNum_txt')[0].text.replace('#', ''))).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                post_num = num['href'][1:]
                self.image_list = []
                images = soup.select(f'#{post_num} .storyImageList img[src]')
                for i in range(len(images)):
                    image_url = self.clear_resize_in_url(self.PAGE_PREFIX + images[i]['src'][1:])
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)
        return soup

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='li.ef',
                                    date_select='.article__listsTime', title_select='.article__listsFullTitle',
                                    id_select='a[a]')

    def download_episode_preview_guess(self, print_invalid=False, download_valid=False):
        if self.is_image_exists(str(self.FINAL_EPISODE).zfill(2) + '_' + str(self.IMAGES_PER_EPISODE)):
            return

        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'wordpress/wp-content/uploads/%s/%s/%s'
        current_date = datetime.now() + timedelta(hours=1)
        year = current_date.strftime('%Y')
        month = current_date.strftime('%m')
        image_folder = folder + '/' + year + '/' + month
        is_successful = False
        valid_urls = []

        for i in range(self.FINAL_EPISODE):
            ep_num = i + 1
            episode = str(ep_num).zfill(2)
            if self.is_image_exists(episode + '_1')\
                    or self.is_image_exists('story' + episode + '_1', image_folder):
                continue
            is_success = False
            for j in range(self.IMAGES_PER_EPISODE):
                image_name = 'story%s_%s' % (episode, str(j + 1))
                image_url = template % (year, month, image_name + '.jpg')
                if self.is_valid_url(image_url, is_image=True):
                    print('VALID - ' + image_url)
                    is_successful = True
                    is_success = True
                    valid_urls.append({'name': image_name, 'url': image_url, 'folder': image_folder})
                elif print_invalid:
                    print('INVALID - ' + image_url)
                    break
            if not is_success:
                break
        if download_valid and len(valid_urls) > 0:
            for valid_url in valid_urls:
                image_name = valid_url['name']
                image_folder = valid_url['folder']
                if not os.path.exists(image_folder):
                    os.makedirs(image_folder)
                self.download_image(valid_url['url'], image_folder + '/' + image_name)
        if is_successful:
            print(self.__class__.__name__ + ' - Guessed correctly!')
        return is_successful

    def download_key_visual(self, soup=None):
        folder = self.create_key_visual_directory()
        try:
            if soup is None:
                soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.kv__imgList img[src]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].split('?')[0][1:]
                if '/img/' not in image_url:
                    continue
                image_name = self.generate_image_name_from_url(image_url, 'img')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'wordpress/wp-content/themes/7th-timeloop/assets/img/character/c%s_main.png'
        self.download_by_template(folder, template, 1, 1)

    def download_media(self):
        folder = self.create_media_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'bdbox/')
            self.image_list = []
            images = soup.select('#music img[src]')
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'][1:]
                if 'nowpri' in image_url:
                    continue
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


# Mahou Shoujo ni Akogarete
class MahoakoDownload(Winter2024AnimeDownload, NewsTemplate):
    title = 'Mahou Shoujo ni Akogarete'
    keywords = [title, 'Gushing over Magical Girls', 'mahoako']
    website = 'https://mahoako-anime.com/'
    twitter = 'mahoako_anime'
    hashtags = ['まほあこ' ,'まほあこアニメ']
    folder_name = 'mahoako'

    PAGE_PREFIX = website
    FINAL_EPISODE = 13
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
            template = self.PAGE_PREFIX + 'assets/story/%s/%s.webp'
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_name = episode + '_' + str(j + 1)
                    image_url = template % (str(i + 1), str(j + 1))
                    if self.download_image(image_url, self.base_folder + '/' + image_name, to_jpg=True) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='#Entries article',
                                    title_select='.entry-title span', date_select='.entry-date span',
                                    id_select=None, id_has_id=True, news_prefix='news.html', date_separator='-')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.vis source[srcset]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['srcset'].replace('./', '').split('?')[0]
                if not image_url.endswith('.webp') or '/top/' not in image_url:
                    continue
                image_name = self.generate_image_name_from_url(image_url, 'top')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

        sub_folder = self.create_custom_directory(folder.split('/')[-1] + '/news')
        cache_filepath = sub_folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        temp_processed = set()  # Some of the id is not unique
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'news.html')
            items = soup.select('#Entries article')
            for item in items:
                date = item.select('.entry-date span')
                if len(date) == 0:
                    continue
                page_name = item['id']
                if page_name in processed:
                    break
                title = item.select('.entry-title span')
                if len(title) == 0:
                    continue
                if ('ビジュアル' in title[0].text or 'イラスト' in title[0].text)\
                        and 'キャラクタービジュアル' not in title[0].text:
                    images = item.select('img[data-src*="/news/"]')
                    self.image_list = []
                    for image in images:
                        image_url = self.PAGE_PREFIX + image['data-src'].replace('./', '').split('?')[0]
                        image_name = self.generate_image_name_from_url(image_url, 'news')
                        self.add_to_image_list(image_name, image_url)
                    self.download_image_list(sub_folder)
                temp_processed.add(page_name)
        except Exception as e:
            self.print_exception(e, 'Key Visual News')
        for page_name in temp_processed:
            processed.append(page_name)
        self.create_cache_file(cache_filepath, processed, num_processed)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'assets/character/%sc.webp'
        self.download_by_template(folder, template, 1, 1, prefix='chara_')

    def download_media(self):
        folder = self.create_media_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'bddvd.html')
            images = soup.select('.sub-bddvd-container img[src*="/bddvd/"]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].replace('./', '').split('?')[0]
                image_name = self.generate_image_name_from_url(image_url, 'bddvd')
                if 'np' == image_name:
                    continue
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')

        sub_folder = self.create_custom_directory(folder.split('/')[-1] + '/blockgame')
        template = self.PAGE_PREFIX + 'blockgame/img/%s.jpg'
        self.image_list = []
        for i in ['M', 'L']:
            for j in ['a', 'b']:
                for k in ['1', '2']:
                    image_name = i + '_' + j + k
                    self.add_to_image_list(image_name, template % image_name)
        self.download_image_list(sub_folder)


# Mashle 2nd Season
class Mashle2Download(Winter2024AnimeDownload, NewsTemplate):
    title = 'Mashle 2nd Season'
    keywords = [title, 'Magic and Muscles']
    website = 'https://mashle.pw/'
    twitter = 'mashle_official'
    hashtags = ['マッシュル', 'mashle']
    folder_name = 'mashle2'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
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
                                    next_page_eval_index_class='is--last', next_page_eval_index=-1,
                                    stop_date='2023.11.03')

    def download_media(self):
        folder = self.create_media_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        for page in ['special', '01', '02', '03', '04']:
            try:
                if page != 'special' and page in processed:
                    continue
                page_url = self.PAGE_PREFIX + 'bddvd/2nd-' + page + '.html'
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


# Majo to Yajuu
class MajotoYajuuDownload(Winter2024AnimeDownload, NewsTemplate):
    title = 'Majo to Yajuu'
    keywords = [title, 'The Witch and the Beast']
    website = 'https://www.tbs.co.jp/anime/majo/'
    twitter = 'majo_yajuu'
    hashtags = ['魔女と野獣']
    folder_name = 'majotoyajuu'

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
            template = self.PAGE_PREFIX + 'story/img/story%s/%s.jpg'
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_name = episode + '_' + str(j + 1)
                    image_url = template % (episode, str(j + 1).zfill(2))
                    if self.download_image(image_url, self.base_folder + '/' + image_name) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news/'
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.newsall-block',
                                    date_select='.newsall-date', title_select='.newsall-title',
                                    id_select='a', a_tag_prefix=news_url)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('visual_key@2x', self.PAGE_PREFIX + 'img/visual_key@2x.jpg')
        self.download_image_list(folder)


# Mato Seihei no Slave
class MatoSlaveDownload(Winter2024AnimeDownload, NewsTemplate):
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
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self, print_http_error=False):
        try:
            objs = self.get_json(self.PAGE_PREFIX + 'news/story_data')
            for obj in objs:
                if 'acf' in obj:
                    acf = obj['acf']
                    if 'number' in acf and 'images' in acf and isinstance(acf['images'], list):
                        try:
                            episode = str(int(acf['number'].split('第')[1].split('話')[0])).zfill(2)
                        except:
                            continue
                        for i in range(len(acf['images'])):
                            image_url = acf['images'][i]
                            image_name = episode + '_' + str(i + 1)
                            self.add_to_image_list(image_name, image_url)
                        self.download_image_list(self.base_folder)
        except HTTPError:
            if print_http_error:
                print(self.__class__.__name__ + ' - 403 Error when retrieving story API.')
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-list-item',
                                    date_select='.news-list-item__date', title_select='.news-list-item__title',
                                    id_select='a', a_tag_start_text_to_remove='/', a_tag_prefix=self.PAGE_PREFIX,
                                    date_func=lambda x: x.replace('年', '.').replace('月', '.').replace('日', ''))

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        # self.image_list = []
        # self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FEiqZdFaUAQyOy4?format=jpg&name=900x900')
        # self.download_image_list(folder)

        teaser_template = self.PAGE_PREFIX + 'img/home/visual_%s.webp'
        for i in range(1, 11, 1):
            image_name = f'home_visual_{i}'
            if self.is_image_exists(image_name, folder):
                continue
            image_url = teaser_template % str(i).zfill(2)
            result = self.download_image(image_url, f'{folder}/{image_name}')
            if result == -1:
                break

    def download_character(self):
        folder = self.create_character_directory()
        char_url = self.PAGE_PREFIX + 'character'
        json_url = char_url + '/chara_data.php'
        self.image_list = []
        try:
            json_obj = self.get_json(json_url)
            if 'charas' in json_obj and isinstance(json_obj['charas'], list):
                for chara in json_obj['charas']:
                    if 'images' in chara:
                        if 'visuals' in chara['images'] and isinstance(chara['images']['visuals'], list):
                            for visual in chara['images']['visuals']:
                                if 'image' in visual:
                                    image_url = char_url + visual['image'][1:].split('?')[0]
                                    image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                                    self.add_to_image_list(image_name, image_url)
                        if 'faces' in chara['images'] and isinstance(chara['images']['faces'], list):
                            for face in chara['images']['faces']:
                                image_url = char_url + face[1:].split('?')[0]
                                image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                                self.add_to_image_list(image_name, image_url)
        except Exception as e:
            self.print_exception(e, 'Character')
        self.download_image_list(folder)


# Metallic Rouge
class MetallicRougeDownload(Winter2024AnimeDownload, NewsTemplate):
    title = 'Metallic Rouge'
    keywords = [title]
    twitter = 'MetallicRouge'
    website = 'https://metallicrouge.jp/'
    hashtags = ['メタリックルージュ']
    folder_name = 'metallicrouge'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 8

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        soup = self.download_key_visual()
        self.download_character(soup)

    def download_episode_preview(self):
        try:
            template = self.PAGE_PREFIX + 'assets/img/episodes/%s/episodes%s.jpg'
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_name = episode + '_' + str(j + 1)
                    image_url = template % (episode, str(j + 1))
                    if self.download_image(image_url, self.base_folder + '/' + image_name) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news/'
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news__lists-item',
                                    date_select='time', title_select='p', id_select='a', a_tag_prefix=news_url)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        soup = None
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.mv__visual img[src*="/img/"]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].replace('./', '')
                image_name = self.generate_image_name_from_url(image_url, 'img')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')
        return soup

    def download_character(self, soup=None):
        folder = self.create_character_directory()
        try:
            if soup is None:
                soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.character__img img[src*="/character/"]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].replace('./', '')
                image_name = self.generate_image_name_from_url(image_url, 'character')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Nozomanu Fushi no Boukensha #望まぬ不死 #TUUA @nozomanufushiPR
class NozomanuFushiDownload(Winter2024AnimeDownload, NewsTemplate2):
    title = 'Nozomanu Fushi no Boukensha'
    keywords = [title, 'The Unwanted Undead Adventurer']
    twitter = 'nozomanufushiPR'
    website = 'https://nozomanufushi-anime.jp/'
    hashtags = ['望まぬ不死', 'TUUA']
    folder_name = 'nozomanufushi'

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
            soup = self.get_soup(self.PAGE_PREFIX + 'story/01.html')
            a_tags = soup.select('#ContentsListUnit02 a[href]')
            for a_tag in a_tags:
                try:
                    episode = str(int(a_tag['href'].split('/')[-1].replace('.html', ''))).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                if episode == '01':
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(self.PAGE_PREFIX + a_tag['href'].replace('../', ''))
                if ep_soup is None:
                    continue
                self.image_list = []
                images = ep_soup.select('.tp5 img[src]')
                for i in range(len(images)):
                    image_url = self.PAGE_PREFIX + images[i]['src'].split('?')[0].replace('../', '').replace('sn_', '')
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.mainImg__kv source[srcset]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['srcset'].split('?')[0]
                if '/images/' not in image_url or not image_url.endswith('.webp'):
                    continue
                image_name = self.generate_image_name_from_url(image_url, 'images')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            pages = soup.select('#list_06 .title a[href]')
            for page in pages:
                if not page['href'].endswith('.html') or not page['href'].startswith('../'):
                    continue
                page_url = self.PAGE_PREFIX + page['href'].replace('../', '')
                page_name = page_url.split('/')[-1].split('.html')[0]
                if page_name in processed:
                    continue
                ep_soup = self.get_soup(page_url)
                if ep_soup is None:
                    continue
                images = ep_soup.select('.chara__stand img[src],.chara__face img[src]')
                self.image_list = []
                for image in images:
                    image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                    if '/chara/' not in image_url:
                        continue
                    image_name = self.generate_image_name_from_url(image_url, 'chara')
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(folder)
                processed.append(page_name)
        except Exception as e:
            self.print_exception(e, 'Character')
        self.create_cache_file(cache_filepath, processed, num_processed)

    def download_media(self):
        folder = self.create_media_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        for page in ['tokuten', '01', '02', '03']:
            try:
                if page in processed:
                    continue
                page_url = self.PAGE_PREFIX + 'bddvd/' + page + '.html'
                soup = self.get_soup(page_url)
                images = soup.select('#cms_block img[src*="/block/"]')
                self.image_list = []
                for image in images:
                    image_url = self.PAGE_PREFIX + image['src'].split('?')[0].replace('../', '').replace('sn_', '')
                    if not self.is_content_length_in_range(image_url, more_than_amount=39000):
                        continue
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
                if page.isnumeric() and len(self.image_list) > 0:
                    processed.append(page)
                elif page.isnumeric():
                    break
                self.download_image_list(folder)
            except Exception as e:
                self.print_exception(e, f'Blu-ray - {page}')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Ore dake Level Up na Ken
class SoloLevelingDownload(Winter2024AnimeDownload, NewsTemplate):
    title = 'Ore dake Level Up na Ken'
    keywords = [title, 'Solo Leveling']
    website = 'https://sololeveling-anime.net/'
    twitter = 'sololeveling_pr'
    hashtags = ['俺レベ', 'SoloLeveling']
    folder_name = 'sololeveling'

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
            story_prefix = self.PAGE_PREFIX + 'story/'
            soup = self.get_soup(story_prefix)
            stories = soup.select('.storyNavList')
            for story in stories:
                try:
                    episode = str(int(story.select('.storyNavList__linktxt')[0].text)).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_5'):
                    continue
                if '--is-current' in story['class']:
                    ep_soup = soup
                else:
                    a_tag = story.select('a[href]')
                    if len(a_tag) == 0:
                        continue
                    story_url = a_tag[0]['href']
                    if story_url.startswith('./'):
                        story_url = story_prefix + story_url[2:]
                    ep_soup = self.get_soup(story_url)
                if ep_soup is None:
                    continue
                self.image_list = []
                images = ep_soup.select('.storyImageList img[src]')
                for i in range(len(images)):
                    image_name = episode + '_' + str(i + 1)
                    image_url = story_prefix + images[i]['src']
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news/'
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news__lists li',
                                    title_select='p', date_select='time', id_select='a',
                                    a_tag_prefix=news_url, paging_type=1, next_page_select='.paging__nav--next')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        template = self.PAGE_PREFIX + 'assets/img/top/visual%s.jpg'
        self.download_by_template(folder, template, 1, 1)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'assets/img/character/c%s_main1.png'
        self.download_by_template(folder, template, 1, 1)


# Oroka na Tenshi wa Akuma to Odoru
class KanatenDownload(Winter2024AnimeDownload, NewsTemplate2):
    title = 'Oroka na Tenshi wa Akuma to Odoru'
    keywords = [title, 'The Foolish Angel Dances with the Devil', 'kanaten']
    website = 'https://kanaten-anime.com/'
    twitter = 'kanaten_PR'
    hashtags = ['かな天', 'kanaten']
    folder_name = 'kanaten'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_episode_preview_external()
        self.download_episode_preview_guess()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/01.html')
            a_tags = soup.select('#ContentsListUnit02 a[href]')
            for a_tag in a_tags:
                try:
                    episode = str(int(a_tag['href'].split('/')[-1].replace('.html', ''))).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                if episode == '01':
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(self.PAGE_PREFIX + a_tag['href'].replace('../', ''))
                if ep_soup is None:
                    continue
                self.image_list = []
                images = ep_soup.select('.tp5 img[src]')
                for i in range(len(images)):
                    image_url = self.PAGE_PREFIX + images[i]['src'].split('?')[0].replace('../', '').replace('sn_', '')
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(self.PAGE_PREFIX)
    
    def download_episode_preview_external(self):
        keywords = ['愚かな天使は悪魔と踊る']
        AniverseMagazineScanner(keywords, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20240104', download_id=self.download_id).run()

    def download_episode_preview_guess(self):
        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'core_sys/images/contents/%s/block/%s/%s.jpg'
        is_successful = False
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1'):
                continue
            is_success = False
            first = 21 + i
            second = 43 + 4 * i
            third = 49 + 6 * i
            for j in range(self.IMAGES_PER_EPISODE):
                image_url = template % (str(first).zfill(8), str(second).zfill(8), str(third + j).zfill(8))
                image_name = episode + '_' + str(j + 1)
                if not self.is_content_length_in_range(image_url, more_than_amount=13000):
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

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.head__kv source[srcset]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['srcset'].split('?')[0]
                if '/images/' not in image_url or not image_url.endswith('.webp'):
                    continue
                image_name = self.generate_image_name_from_url(image_url, 'images')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'chara/')
            pages = soup.select('#ContentsListUnit01 a[href]')
            for page in pages:
                if not page['href'].endswith('.html') or not page['href'].startswith('../'):
                    continue
                page_url = self.PAGE_PREFIX + page['href'].replace('../', '')
                page_name = page_url.split('/')[-1].split('.html')[0]
                if page_name in processed:
                    continue
                if page_name == 'index':
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(page_url)
                if ep_soup is None:
                    continue
                images = ep_soup.select('.chara__img img[src]')
                self.image_list = []
                for image in images:
                    image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(folder)
                processed.append(page_name)
        except Exception as e:
            self.print_exception(e, 'Character')
        self.create_cache_file(cache_filepath, processed, num_processed)

    def download_media(self):
        folder = self.create_media_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        for page in ['privilege', 'campaign', '01', '02', '03']:
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
                    image_url = self.PAGE_PREFIX + image['src'].replace('../', '').split('?')[0]
                    if '/bd/' in image_url:
                        image_name = self.generate_image_name_from_url(image_url, 'bd')
                    else:
                        image_name = self.extract_image_name_from_url(image_url)
                    if page.isnumeric() and not self.is_content_length_in_range(image_url, more_than_amount=51000):
                        continue
                    if page == 'privilege' and not self.is_content_length_in_range(image_url, more_than_amount=39000):
                        continue
                    self.add_to_image_list(image_name, image_url)
                if page.isnumeric() and len(self.image_list) > 0:
                    processed.append(page)
                elif page.isnumeric():
                    break
                self.download_image_list(folder)
            except Exception as e:
                self.print_exception(e, f'Blu-ray - {page}')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Pon no Michi
class PonnoMichiDownload(Winter2024AnimeDownload, NewsTemplate4):
    title = 'Pon no Michi'
    keywords = [title, "Pon no Michi"]
    website = 'https://ponnomichi-pr.com/'
    twitter = 'ponnomichi_pr'
    hashtags = ['ぽんのみち', 'ponnomichi']
    folder_name = 'ponnomichi'

    PAGE_PREFIX = website
    IMAGES_PER_EPISODE = 6
    FINAL_EPISODE = 12

    def __init__(self):
        super().__init__()

    def run(self):
        init_json = self.download_episode_preview()
        self.download_news(init_json)
        self.download_key_visual()
        self.download_episode_preview_guess(print_invalid=False, download_valid=True)
        self.download_character()
        self.download_media()

    def download_episode_preview(self, print_http_error=False):
        try:
            init_json = self.get_json(self.PAGE_PREFIX + 'wp-json/site-data/init')
            for story in init_json['story']:
                episode = story['episode']
                if self.is_image_exists(episode + '_1'):
                    continue
                self.image_list = []
                for i in range(len(story['images'])):
                    image = story['images'][i]
                    image_url = image['image_path']
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
            return init_json
        except HTTPError:
            if print_http_error:
                print(self.__class__.__name__ + ' - 403 Error when retrieving story API.')
        except Exception as e:
            self.print_exception(e)
        return None

    def download_news(self, json_obj=None):
        self.download_template_news('site-data', json_obj=json_obj)

    def download_episode_preview_guess(self, print_invalid=False, download_valid=False):
        if self.is_image_exists(str(self.FINAL_EPISODE).zfill(2) + '_' + str(self.IMAGES_PER_EPISODE)):
            return

        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'wp/wp-content/uploads/%s/%s/%s.jpg'
        current_date = datetime.now() + timedelta(hours=1)
        year = current_date.strftime('%Y')
        month = current_date.strftime('%m')
        is_successful = False
        valid_urls = []
        for j in range(self.IMAGES_PER_EPISODE):
            k = 0
            while k < 20:
                if k == 0:
                    append = ''
                else:
                    append = '-' + str(k)
                image_folder = folder + '/' + year + '/' + month
                image_name = str(j + 1).zfill(2) + append
                if not self.is_image_exists(image_name, image_folder):
                    image_url = template % (year, month, str(j + 1).zfill(2) + append)
                    if self.is_valid_url(image_url, is_image=True):
                        print('VALID - ' + image_url)
                        is_successful = True
                        valid_urls.append({'name': image_name, 'url': image_url, 'folder': image_folder})
                    elif print_invalid:
                        print('INVALID - ' + image_url)
                        break
                k += 1
        if download_valid and len(valid_urls) > 0:
            for valid_url in valid_urls:
                image_name = valid_url['name']
                image_folder = valid_url['folder']
                if not os.path.exists(image_folder):
                    os.makedirs(image_folder)
                self.download_image(valid_url['url'], image_folder + '/' + image_name)
        if is_successful:
            print(self.__class__.__name__ + ' - Guessed correctly!')
        return is_successful

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/Fwy-ZH3aYAAUzwg?format=jpg&name=large')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('div[class*="Visual"] img[srcSet*="kv_"]')
            for image in images:
                image_url = image['srcset']
                if '/static/' not in image_url:
                    continue
                if image_url.startswith('/'):
                    image_url = self.PAGE_PREFIX + image_url[1:]
                image_name = self.generate_image_name_from_url(image_url, 'static')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character')
            self.image_list = []
            images = soup.select('img[src][class*="CharacterImage"]')
            for image in images:
                image_url = image['src']
                if '/static/' not in image_url:
                    continue
                if image_url.startswith('/'):
                    image_url = self.PAGE_PREFIX + image_url[1:]
                image_name = self.generate_image_name_from_url(image_url, 'static')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')

    def download_media(self):
        folder = self.create_media_directory()
        try:
            for i in ['store', '']:
                soup = self.get_soup(self.PAGE_PREFIX + 'bd/' + i)
                images = soup.select('main img[src*="/bd/"]')
                self.image_list = []
                for image in images:
                    if image['src'].endswith('.svg'):
                        continue
                    image_url = self.PAGE_PREFIX + image['src'][1:].split('?')[0]
                    image_name = self.generate_image_name_from_url(image_url, 'bd')
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


# Saijaku Tamer wa Gomi Hiroi no Tabi wo Hajimemashita.
class SaijakuTamerDownload(Winter2024AnimeDownload, NewsTemplate):
    title = 'Saijaku Tamer wa Gomi Hiroi no Tabi wo Hajimemashita.'
    keywords = [title, "The Weakest Tamer Began a Journey to Pick Up Trash"]
    website = 'https://saijakutamer-anime.com/'
    twitter = 'saijakutamer'
    hashtags = ['最弱テイマー']
    folder_name = 'saijakutamer'

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
        jpg_len = [485587, 487372, 487813, 486853, 487229, 487643]
        webp_len = [128224, 129102, 129304, 128692, 128942, 129192]
        try:
            template = self.PAGE_PREFIX + 'dist/img/story/ep%s/img%s.'
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_1'):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_name = episode + '_' + str(j + 1)
                    template_url = template % (str(i + 1), str(j + 1))
                    image_url = template_url + 'jpg'
                    if not self.is_not_matching_content_length(image_url, jpg_len[j])\
                            or self.download_image(image_url, self.base_folder + '/' + image_name,
                                                   min_width=1000) == -1:
                        image_url = template_url + 'webp'
                        if not self.is_not_matching_content_length(image_url, webp_len[j])\
                                or self.download_image(image_url, self.base_folder + '/' + image_name,
                                                       to_jpg=True, min_width=1000) == -1:
                            stop = True
                            break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.c-Post__list',
                                    title_select='.c-Post__title', date_select='.c-Post__date',
                                    id_select='.c-Post__link')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        template = self.PAGE_PREFIX + 'dist/img/top/KV_visual_%s.jpg'
        self.download_by_template(folder, template, 1, 1)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'dist/img/top/chara/visual_chara_%s.webp'
        self.download_by_template(folder, template, 1, 1)


# Saikyou Tank no Meikyuu Kouryaku
class SaikyoTankDownload(Winter2024AnimeDownload, NewsTemplate):
    title = 'Saikyou Tank no Meikyuu Kouryaku'
    keywords = [title, "The Strongest Tank's Labyrinth Raids"]
    website = 'https://saikyo-tank.com/'
    twitter = 'saikyo_tank'
    hashtags = ['最強タンク']
    folder_name = 'saikyotank'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        soup = self.download_character()
        self.download_media(soup)

    def download_episode_preview(self):
        try:
            template = self.PAGE_PREFIX + 'dist/img/top/story/ep%s/img%s.'
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_name = episode + '_' + str(j + 1)
                    template_url = template % (str(i + 1), str(j + 1))
                    image_url = template_url + 'jpg'
                    if self.download_image(image_url, self.base_folder + '/' + image_name, min_width=1000) == -1:
                        image_url = template_url + 'webp'
                        if self.download_image(image_url, self.base_folder + '/' + image_name,
                                               to_jpg=True, min_width=1000) == -1:
                            stop = True
                            break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.p-News__postList a',
                                    date_select='.c-Post__date', title_select='.c-Post__title', id_select=None,
                                    date_func=lambda x: x[0:4] + '.' + x[5:])

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_kv', self.PAGE_PREFIX + 'news/wp-content/uploads/2023/10/STM_01_ティザービジュアル_1@0.3x.png')
        self.add_to_image_list('fv_kv_1', self.PAGE_PREFIX + 'dist/img/top/fv/kv_1.webp')
        self.add_to_image_list('fv_kv_1_v2', self.PAGE_PREFIX + 'dist/img/top/fv/kv_1_v2.webp')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        soup = None
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.p-Chara__charMain source[type][srcset*="/chara/"]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['srcset']
                image_name = self.generate_image_name_from_url(image_url, 'chara')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')
        return soup

    def download_media(self, soup=None):
        folder = self.create_media_directory()
        try:
            if soup is None:
                soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.p-Bd__main img[src*="/bd/"]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src']
                image_name = self.generate_image_name_from_url(image_url, 'bd')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


# Sasaki to Pii-chan
class SasapiDownload(Winter2024AnimeDownload, NewsTemplate):
    title = 'Sasaki to Pii-chan'
    keywords = [title, 'Sasaki and Peeps', 'Sasapi']
    website = 'https://sasapi-anime.com/'
    twitter = 'sasaki_pichan'
    hashtags = ['ささピー']
    folder_name = 'sasapi'

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
            template = self.PAGE_PREFIX + 'images/story/%s/p_%s.jpg'
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (str(i + 1).zfill(3), str(j + 1).zfill(3))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        try:
            results = []
            news_obj = self.get_last_news_log_object()
            json_obj = self.get_json(self.PAGE_PREFIX + 'news.json')
            for item in json_obj:
                if 'day' in item and 'url' in item and 'title' in item:
                    try:
                        date = datetime.strptime(item['day'], "%Y/%m/%d").strftime("%Y.%m.%d")
                    except:
                        continue
                    title = item['title']
                    url = self.PAGE_PREFIX + item['url']
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

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.visual_wrap .style_pc img[src]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src']
                if '/images/' in image_url:
                    image_name = self.generate_image_name_from_url(image_url, 'images')
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self, soup=None):
        folder = self.create_character_directory()
        prefix = self.PAGE_PREFIX + 'images/chara/'
        templates = [prefix + 'list_%s.png', prefix + 'a_%s.png']
        self.download_by_template(folder, templates, 3, 1)
        templates = [prefix + 'd_%s_01.png', prefix + 'd_%s_02.png', prefix + 'd_%s_03.png']
        self.download_by_template(folder, templates, 2, 1)

    def download_media(self):
        folder = self.create_media_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'package.html')
            images = soup.select('.right_wrap img[src*="/package/"]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].split('?')[0]
                image_name = self.generate_image_name_from_url(image_url, 'package')
                if 'nowpri' in image_name:
                    continue
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


# Sengoku Youko
class SengokuYoukoDownload(Winter2024AnimeDownload, NewsTemplate):
    title = 'Sengoku Youko'
    keywords = [title]
    website = 'https://sengoku-youko.com/'
    twitter = 'sengoku_youko'
    hashtags = '戦国妖狐'
    folder_name = 'sengokuyouko'

    PAGE_PREFIX = website
    FINAL_EPISODE = 37
    IMAGES_PER_EPISODE = 4

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        try:
            template = self.PAGE_PREFIX + 'dist/img/story/ep%s/img%s.webp'
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_name = episode + '_' + str(j + 1)
                    image_url = template % (str(i + 1), str(j + 1).zfill(2))
                    if self.download_image(image_url, self.base_folder + '/' + image_name, to_jpg=True) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.bl_horizPosts_item',
                                    date_select='.bl_horizPosts_date', title_select='.bl_horizPosts_txt',
                                    id_select='a', paging_type=3, paging_suffix='?page=%s',
                                    next_page_select='.l_pager_next[href*="page"]')


# Shin no Nakama ja Nai to Yuusha no Party wo Oidasareta node, Henkyou de Slow Life suru Koto ni Shimashita 2nd
class ShinnoNakama2Download(Winter2024AnimeDownload, NewsTemplate):
    title = 'Shin no Nakama ja Nai to Yuusha no Party wo Oidasareta node, Henkyou de Slow Life suru Koto ni Shimashita 2nd'
    keywords = [title, 'Shinnonakama', "Banished From The Heroes' Party"]
    website = 'https://shinnonakama.com/'
    twitter = 'shinnonakama_tv'
    hashtags = '真の仲間'
    folder_name = 'shinnonakama2'

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
            soup = self.get_soup(self.PAGE_PREFIX + '/story/')
            sections = soup.select('section[data-ep]')
            for section in sections:
                try:
                    episode = str(int(section['data-ep'])).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                images = section.select('.storyThumbList img[src]')
                self.image_list = []
                for i in range(len(images)):
                    image_url = self.PAGE_PREFIX + images[i]['src'].replace('../', '')
                    image_name = f'{episode}_{i + 1}'
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_external(self):
        keywords = ['真の仲間じゃないと勇者のパーティーを追い出されたので']
        AniverseMagazineScanner(keywords, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20231228', download_id=self.download_id).run()

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news/'
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='ul.newsListsWrap li',
                                    date_select='p.update_time', title_select='p.update_ttl',
                                    id_select='a', a_tag_prefix=news_url, a_tag_start_text_to_remove='./',
                                    stop_date='2022.03')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('kv_2nd_2', self.PAGE_PREFIX + 'assets/img/top/visual/kv_2nd_2.jpg')
        self.download_image_list(folder)

        sub_folder = self.create_custom_directory(folder.split('/')[-1] + '/news')
        cache_filepath = sub_folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        news_url = self.PAGE_PREFIX + 'news/'
        try:
            soup = self.get_soup(news_url)
            items = soup.select('ul.newsListsWrap li')
            for item in items:
                date = item.select('p.update_time')
                if len(date) == 0 or date[0].text.startswith('2022.3') or date[0].text.startswith('2022.03'):
                    break
                a_tag = item.select('a[href]')
                if len(a_tag) == 0:
                    continue
                if not a_tag[0]['href'].startswith('./') or not a_tag[0]['href'].endswith('.html'):
                    continue
                page_name = a_tag[0]['href'].split('/')[-1].split('.html')[0]
                if page_name in processed:
                    break
                title = a_tag[0].text.strip()
                if 'ビジュアル' in title:
                    news_soup = self.get_soup(news_url + a_tag[0]['href'].replace('./', ''))
                    if news_soup is not None:
                        images = news_soup.select('.newsDetailWrap img[src]')
                        self.image_list = []
                        for image in images:
                            image_url = news_url + image['src'].replace('./', '').split('?')[0]
                            image_name = self.generate_image_name_from_url(image_url, 'news')
                            self.add_to_image_list(image_name, image_url)
                        self.download_image_list(sub_folder)
                processed.append(page_name)
        except Exception as e:
            self.print_exception(e, 'Key Visual News')
        self.create_cache_file(cache_filepath, processed, num_processed)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'assets/img/top/character/chara2nd_%s.png'
        self.download_by_template(folder, template, 1, 1)

    def download_media(self):
        folder = self.create_media_directory()
        # Blu-ray
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'bddvd/')
            images = soup.select('#season2 img[src*="/bddvd/"]')
            self.image_list = []
            for image in images:
                if not image['src'].endswith('/now.jpg'):
                    image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                    image_name = self.generate_image_name_from_url(image_url, 'bddvd')
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


# Sokushi Cheat ga Saikyou sugite, Isekai no Yatsura ga Marude Aite ni Naranai n desu ga.
class SokushiCheatDownload(Winter2024AnimeDownload, NewsTemplate):
    title = "Sokushi Cheat ga Saikyou sugite, Isekai no Yatsura ga Marude Aite ni Naranai n desu ga."
    keywords = [title, "My Instant Death Ability Is So Overpowered, No One in This Other World Stands a Chance Against Me!"]
    website = 'https://sokushicheat-pr.com/'
    twitter = '即死チート'
    hashtags = 'ツキミチ'
    folder_name = 'sokushicheat'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_external()
        self.download_news()
        self.download_episode_preview_guess(print_invalid=False, download_valid=True)
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            stories = soup.select('.story-box')
            for story in reversed(stories):
                try:
                    episode = str(int(story.select('.num span')[0].text)).zfill(2)
                except:
                    continue
                self.image_list = []
                images = story.select('.ss-pic-item img[src]')
                for i in range(len(images)):
                    image_url = images[i]['src']
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_external(self):
        keywords = ['即死チートが最強すぎて']
        AniverseMagazineScanner(keywords, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20231228', download_id=self.download_id).run()

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-item',
                                    date_select='.date', title_select='.title', id_select='a')

    def download_episode_preview_guess(self, print_invalid=False, download_valid=False):
        if self.is_image_exists(str(self.FINAL_EPISODE).zfill(2) + '_' + str(self.IMAGES_PER_EPISODE)):
            return

        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'wp/wp-content/uploads/%s/%s/%s.jpg'
        current_date = datetime.now() + timedelta(hours=1)
        year = current_date.strftime('%Y')
        month = current_date.strftime('%m')
        is_successful = False
        valid_urls = []
        for j in range(self.IMAGES_PER_EPISODE):
            k = 0
            while k < 20:
                if k == 0:
                    append = ''
                else:
                    append = '-' + str(k)
                image_folder = folder + '/' + year + '/' + month
                image_name = str(j + 1).zfill(2) + append
                if not self.is_image_exists(image_name, image_folder):
                    image_url = template % (year, month, str(j + 1).zfill(2) + append)
                    if self.is_valid_url(image_url, is_image=True):
                        print('VALID - ' + image_url)
                        is_successful = True
                        valid_urls.append({'name': image_name, 'url': image_url, 'folder': image_folder})
                    elif print_invalid:
                        print('INVALID - ' + image_url)
                        break
                k += 1
        if download_valid and len(valid_urls) > 0:
            for valid_url in valid_urls:
                image_name = valid_url['name']
                image_folder = valid_url['folder']
                if not os.path.exists(image_folder):
                    os.makedirs(image_folder)
                self.download_image(valid_url['url'], image_folder + '/' + image_name)
        if is_successful:
            print(self.__class__.__name__ + ' - Guessed correctly!')
        return is_successful

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('vizyuaru', self.PAGE_PREFIX + 'wp/wp-content/uploads/2023/11/vizyuaru.jpg')
        self.download_image_list(folder)

        template = self.PAGE_PREFIX + 'wp/wp-content/themes/sokushicheat_teaser/images/kv%s.jpg'
        self.download_by_template(folder, template, 1, 1, prefix='teaser_')
        template = self.PAGE_PREFIX + 'wp/wp-content/themes/sokushicheat_honban/images/kv%s.jpg'
        self.download_by_template(folder, template, 1, 1, prefix='honban_')

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'wp/wp-content/themes/sokushicheat_teaser/images/chara-pic%s.png'
        self.download_by_template(folder, template, 2, 1)


# Tsuki ga Michibiku Isekai Douchuu 2nd Season
class Tsukimichi2Download(Winter2024AnimeDownload, NewsTemplate):
    title = "Tsuki ga Michibiku Isekai Douchuu 2nd Season"
    keywords = [title, "Tsukimichi", "Moonlit Fantasy"]
    website = 'https://tsukimichi.com/'
    twitter = 'tsukimichi_PR'
    hashtags = 'ツキミチ'
    folder_name = 'tsukimichi2'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_episode_preview_guess(print_invalid=False, download_valid=True)
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            eps = soup.select('.story nav a[href]')
            for i in range(len(eps)):
                ep = eps[i]
                try:
                    episode = str(int(ep.text)).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                if i == len(eps) - 1:  # Last index
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(ep['href'])
                self.image_list = []
                images = ep_soup.select('.ssslide img[src]')
                for j in range(len(images)):
                    image_url = images[j]['src']
                    image_name = episode + '_' + str(j + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        # Paging logic unknown
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news article',
                                    date_select='.date', title_select='.ttl', id_select='a')

    def download_episode_preview_guess(self, print_invalid=False, download_valid=False):
        if self.is_image_exists(str(self.FINAL_EPISODE).zfill(2) + '_' + str(self.IMAGES_PER_EPISODE)):
            return

        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + '2ndwp/wp-content/uploads/%s/%s/%s.jpg'
        current_date = datetime.now() + timedelta(hours=1)
        year = current_date.strftime('%Y')
        month = current_date.strftime('%m')
        is_successful = False
        valid_urls = []
        for j in range(self.IMAGES_PER_EPISODE):
            k = 0
            while k < 20:
                if k == 0:
                    append = ''
                else:
                    append = '-' + str(k)
                image_folder = folder + '/' + year + '/' + month
                image_name = str(j + 1).zfill(2) + append
                if not self.is_image_exists(image_name, image_folder):
                    image_url = template % (year, month, str(j + 1).zfill(2) + append)
                    if self.is_valid_url(image_url, is_image=True):
                        print('VALID - ' + image_url)
                        is_successful = True
                        valid_urls.append({'name': image_name, 'url': image_url, 'folder': image_folder})
                    elif print_invalid:
                        print('INVALID - ' + image_url)
                        break
                k += 1
        if download_valid and len(valid_urls) > 0:
            for valid_url in valid_urls:
                image_name = valid_url['name']
                image_folder = valid_url['folder']
                if not os.path.exists(image_folder):
                    os.makedirs(image_folder)
                self.download_image(valid_url['url'], image_folder + '/' + image_name)
        if is_successful:
            print(self.__class__.__name__ + ' - Guessed correctly!')
        return is_successful

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.fvslide source[srcset][type]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['srcset'][1:]
                if not image_url.endswith('.webp') or image_url.endswith('_sp.webp'):
                    continue
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            images = soup.select('.chardata--inner .v source[srcset]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['srcset'][1:]
                if not image_url.endswith('.webp'):
                    continue
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')

    def download_media(self):
        folder = self.create_media_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        for page in ['store', '1', '2', '3']:
            try:
                if page in processed:
                    continue
                page_url = self.PAGE_PREFIX + 'bd/'
                if page.isnumeric():
                    page_url += 'vol'
                page_url += page
                soup = self.get_soup(page_url)
                images = soup.select('.bd img[src]')
                self.image_list = []
                for image in images:
                    image_url = image['src']
                    if 'jacket_sample' in image_url or 'sample_square' in image_url:
                        continue
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
                if page.isnumeric() and len(self.image_list) > 0:
                    processed.append(page)
                elif page.isnumeric():
                    break
                self.download_image_list(folder)
            except Exception as e:
                self.print_exception(e, f'Blu-ray - {page}')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Urusei Yatsura (2022) 2nd Season
class UruseiYatsura2Download(Winter2024AnimeDownload, NewsTemplate):
    title = 'Urusei Yatsura (2022) 2nd Season'
    keywords = [title]
    website = 'https://uy-allstars.com/'
    twitter = 'uy_allstars'
    hashtags = 'うる星やつら'
    folder_name = 'uruseiyatsura2'

    PAGE_PREFIX = website
    FIRST_EPISODE = 24
    FINAL_EPISODE = 46
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_guess(print_invalid=False, download_valid=True)

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            a_tags = soup.select('.story--nav a[href]')
            for a_tag in a_tags:
                try:
                    episode = str(int(a_tag.text)).zfill(2)
                except:
                    continue
                if int(episode) < self.FIRST_EPISODE or self.is_image_exists(episode + '_1'):
                    continue
                story_num = soup.select('.story--num')
                ep_soup = None
                if len(story_num) > 0:
                    try:
                        episode_num = str(int(story_num[0].text)).zfill(2)
                        if episode == episode_num:
                            ep_soup = soup
                    except:
                        pass
                if ep_soup is None:
                    ep_soup = self.get_soup(a_tag['href'])
                    if ep_soup is None:
                        continue
                self.image_list = []
                images = ep_soup.select('.ss img[src]')
                for i in range(len(images)):
                    image_url = images[i]['src'].split('?')[0]
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_guess(self, print_invalid=False, download_valid=False, min_limit=20, max_limit=100):
        if self.is_image_exists(str(self.FINAL_EPISODE).zfill(2) + '_' + str(self.IMAGES_PER_EPISODE)):
            return

        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'wp/wp-content/uploads/%s/%s/UY_ep%s_cap-%s.jpg'
        current_date = datetime.now() + timedelta(hours=1)
        year = current_date.strftime('%Y')
        month = current_date.strftime('%m')
        is_successful = False
        valid_urls = []
        for i in range(self.FIRST_EPISODE, self.FINAL_EPISODE + 1, 1):
            episode = str(i).zfill(2)
            episode_image_name = episode + '_' + str(self.IMAGES_PER_EPISODE)
            if self.is_image_exists(episode_image_name) or self.is_image_exists(episode_image_name, folder):
                continue
            image_count = 0
            j = 0
            while j < max_limit:
                image_url = template % (year, month, episode, str(j).zfill(3))
                if self.is_valid_url(image_url, is_image=True):
                    print('VALID - ' + image_url)
                    image_count += 1
                    valid_urls.append({'num': str(image_count), 'url': image_url})
                elif print_invalid:
                    print('INVALID - ' + image_url)
                if image_count == self.IMAGES_PER_EPISODE or (image_count == 0 and j > min_limit):
                    break
                j += 1
            if image_count == 0:
                break
            if download_valid and len(valid_urls) > 0:
                for valid_url in valid_urls:
                    image_name = episode + '_' + valid_url['num']
                    self.download_image(valid_url['url'], folder + '/' + image_name)
            is_successful = True
        if is_successful:
            print(self.__class__.__name__ + ' - Guessed correctly!')
        return is_successful


# Youkoso Jitsuryoku Shijou Shugi no Kyoushitsu e S3
class Youzitsu3Download(Winter2024AnimeDownload, NewsTemplate):
    title = "Youkoso Jitsuryoku Shijou Shugi no Kyoushitsu e 3rd Season"
    keywords = ["Youkoso Jitsuryoku Shijou Shugi no Kyoushitsu e", "Youzitsu", "Youjitsu",
                "Classroom of the Elite"]
    website = 'http://you-zitsu.com/'
    twitter = 'youkosozitsu'
    hashtags = ['you_zitsu', 'よう実', 'ClassroomOfTheElite']
    folder_name = 'youzitsu3'

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
        try:
            template = self.PAGE_PREFIX + 'assets/story/%s/%s.webp'
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_name = episode + '_' + str(j + 1)
                    image_url = template % (str(i + 1), str(j + 1))
                    if self.download_image(image_url, self.base_folder + '/' + image_name, to_jpg=True) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='article.content-entry',
                                    title_select='h2.entry-title span', date_select='div.entry-date span',
                                    id_select=None, id_has_id=True, news_prefix='news.html')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.vis img[src]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].replace('./', '').split('?')[0]
                if not image_url.endswith('.webp') or '/top/' not in image_url:
                    continue
                image_name = self.generate_image_name_from_url(image_url, 'top')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_media(self):
        folder = self.create_media_directory()

        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'bddvd.html')
            images = soup.select('img[src*="/bddvd/"]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].split('?')[0].replace('./', '')
                if 'np.png' in image_url:
                    continue
                image_name = self.generate_image_name_from_url(image_url, 'bddvd')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')

        # Calendar project
        calendar_folder = folder + '/calendar'
        if not os.path.exists(calendar_folder):
            os.makedirs(calendar_folder)
        template = self.PAGE_PREFIX + 'assets/special-calendar/%s.jpg'
        year = 2022
        month = 12
        stop = False
        while year < 2025 and not stop:
            while month <= 12 and not stop:
                image_name = str(year) + str(month).zfill(2)
                month += 1
                if self.is_image_exists(image_name, calendar_folder):
                    continue
                image_url = template % image_name
                result = self.download_image(image_url, calendar_folder + '/' + image_name)
                if result == -1:
                    stop = True
                    break
            month = 1
            year += 1


# Yubisaki to Renren
class YubisakitoRenrenDownload(Winter2024AnimeDownload, NewsTemplate):
    title = "Yubisaki to Renren"
    keywords = ["A Sign of Affection"]
    website = 'https://yubisaki-pr.com/'
    twitter = 'yubisaki_pr'
    hashtags = ['ゆびさきと恋々']
    folder_name = 'yubisakitorenren'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_external()
        self.download_news()
        self.download_episode_preview_guess(print_invalid=False, download_valid=True)
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            stories = soup.select('.story-box')
            for story in reversed(stories):
                try:
                    episode = str(int(story.select('.num span')[0].text)).zfill(2)
                except:
                    continue
                self.image_list = []
                images = story.select('.ss-pic-item img[src]')
                for i in range(len(images)):
                    image_url = images[i]['src']
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-item',
                                    date_select='.date', title_select='.title', id_select='a')

    def download_episode_preview_external(self):
        keywords = ['ゆびさきと恋々']
        AniverseMagazineScanner(keywords, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20240104', download_id=self.download_id, prefix='Sign.', suffix='').run()

    def download_episode_preview_guess(self, print_invalid=False, download_valid=False, min_limit=20, max_limit=100):
        if self.is_image_exists(str(self.FINAL_EPISODE).zfill(2) + '_' + str(self.IMAGES_PER_EPISODE)):
            return

        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'wp/wp-content/uploads/%s/%s/%sYubisakiToRenren_ep%s_still_%s.jpg'
        current_date = datetime.now() + timedelta(hours=1)
        year = current_date.strftime('%Y')
        month = current_date.strftime('%m')
        is_successful = False
        valid_urls = []
        image_folder = folder + '/' + year + '/' + month
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1') or self.is_image_exists(episode + '_1', image_folder):
                continue
            j = 0
            image_count = 0
            valid_nums = []
            while j < max_limit:
                image_url = template % (year, month, '', episode, str(j).zfill(4))
                image_name = episode + '_' + str(image_count + 2)
                if self.is_valid_url(image_url, is_image=True):
                    print('VALID - ' + image_url)
                    is_successful = True
                    valid_urls.append({'name': image_name, 'url': image_url, 'folder': image_folder})
                    image_count += 1
                    valid_nums.append(j)
                elif print_invalid:
                    print('INVALID - ' + image_url)
                j += 1
                if image_count >= self.IMAGES_PER_EPISODE:
                    break
                if j > min_limit and image_count == 0:
                    break
            if image_count == 0:
                break
            elif image_count == 5:
                j = 0
                while j < max_limit:
                    if j in valid_nums:
                        j += 1
                        continue
                    image_url = template % (year, month, '【MAIN】', episode, str(j).zfill(4))
                    image_name = episode + '_1'
                    if self.is_valid_url(image_url, is_image=True):
                        print('VALID - ' + image_url)
                        valid_urls.append({'name': image_name, 'url': image_url, 'folder': image_folder})
                        break
                    elif print_invalid:
                        print('INVALID - ' + image_url)
                    j += 1

        if download_valid and len(valid_urls) > 0:
            for valid_url in valid_urls:
                image_name = valid_url['name']
                image_folder = valid_url['folder']
                if not os.path.exists(image_folder):
                    os.makedirs(image_folder)
                self.download_image(valid_url['url'], image_folder + '/' + image_name)
        if is_successful:
            print(self.__class__.__name__ + ' - Guessed correctly!')
        return is_successful

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.kv img[src]')
            self.image_list = []
            for image in images:
                image_url = image['src']
                if '/images/' not in image_url or 'logo' in image_url:
                    continue
                image_name = self.generate_image_name_from_url(image_url, 'images')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'wp/wp-content/themes/yubisaki_teaser/images/chara-pic%s.png'
        self.download_by_template(folder, template, 1, 1)

    def download_media(self):
        folder = self.create_media_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'bluray/')
            images = soup.select('.section-contents img[src*="/images/"]')
            self.image_list = []
            for image in images:
                image_url = image['src']
                if 'bluray-pic-sample' in image_url or 'privilege-pic-sample' in image_url:
                    continue
                image_name = self.generate_image_name_from_url(image_url, 'images')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')
