from anime.main_download import MainDownload, NewsTemplate, NewsTemplate2
from scan import AniverseMagazineScanner
from datetime import datetime, timedelta
from requests.exceptions import HTTPError
import os
import string

# 16bit Sensation: Another Layer https://16bitsensation-al.com/ #16bitAL #16bitセンセーション @16bit_anime
# Bokura no Ameiro Protocol https://bokuame.com/ #ボクアメ #僕らの雨いろプロトコル @bokuame_anime
# Boukensha ni Naritai to Miyako ni Deteitta Musume ga S-Rank ni Natteta https://s-rank-musume.com/ #Sランク娘 @s_rank_musume
# Boushoku no Berserk https://bousyoku-anime.com/ #暴食 #暴食のベルセルク @bousyoku_anime
# Buta no Liver wa Kanetsu Shiro https://butaliver-anime.com/ #豚レバ @butaliver_anime
# Dekoboko Majo no Oyako Jijou https://dekoboko-majo-anime.jp/ @DEKOBOKO_anime #でこぼこ魔女の親子事情
# Goblin Slayer S2 http://www.goblinslayer.jp/ #ゴブスレ #いせれべ @GoblinSlayer_GA
# Hametsu no Oukoku https://hametsu-anime.com/ #はめつのおうこく #はめつ @hametsu_anime
# Hikikomari Kyuuketsuki no Monmon https://hikikomari.com/ #ひきこまり @komarin_PR
# Hoshikuzu Telepath https://hoshitele-anime.com/ #星テレ #hoshitele @hoshitele_anime
# Kage no Jitsuryokusha ni Naritakute! 2nd Season https://shadow-garden.jp/ #陰の実力者 @Shadowgarden_PR
# Kanojo mo Kanojo Season 2 https://kanokano-anime.com/ #kanokano #カノジョも彼女 @kanokano_anime
# Keikenzumi na Kimi to, Keiken Zero na Ore ga, Otsukiai suru Hanashi. https://kimizero.com/ #キミゼロ @kimizero_anime
# Kikansha no Mahou wa Tokubetsu desu https://returners-magic.com/ #帰還者 #returnersmagic @returners_magic
# Kimi no Koto ga Daidaidaidaidaisuki na 100-nin no Kanojo https://hyakkano.com/ @hyakkano_anime #100カノ
# Konyaku Haki sareta Reijou wo Hirotta Ore ga, Ikenai koto wo Oshiekomu https://ikenaikyo.com/ #イケナイ教 @ikenaikyo_anime
# Kusuriya no Hitorigoto https://kusuriyanohitorigoto.jp/ #薬屋のひとりごと @kusuriya_PR
# Potion-danomi de Ikinobimasu! https://potion-anime.com/ #ポーション頼み @potion_APR
# Ragna Crimson https://ragna-crimson.com/ @ragnacrimson_PR #ラグナクリムゾン #RagnaCrimson
# Saihate no Paladin: Tetsusabi no Yama no Ou https://farawaypaladin.com/ #最果てのパラディン #faraway_paladin @faraway_paladin
# Seijo no Maryoku wa Bannou Desu S2 https://seijyonomaryoku.jp/ #seijyonoanime @seijyonoanime
# Seiken Gakuin no Makentsukai https://seikengakuin.com/ #聖剣学院の魔剣使い #せまつか @SEIKEN_MAKEN
# Shangri-La Frontier: Kusoge Hunter, Kamige ni Idoman to su https://anime.shangrilafrontier.com/ #シャンフロ @ShanFro_Comic
# Shy https://shy-anime.com/ #SHY_hero @SHY_off
# Sousou no Frieren https://frieren-anime.jp/ #フリーレン #frieren @Anime_Frieren
# Spy x Family Season 2 https://spy-family.net/tvseries/ #SPY_FAMILY #スパイファミリー @spyfamily_anime
# Tate no Yuusha no Nariagari Season 3 http://shieldhero-anime.jp/ #shieldhero #盾の勇者の成り上がり @shieldheroanime
# Tearmoon Teikoku Monogatari https://tearmoon-pr.com/ #ティアムーン @tearmoon_pr
# Toaru Ossan no VRMMO Katsudouki https://toaru-ossan.com/ #とあるおっさん @toaru_ossan_pr
# Undead Unluck https://undead-unluck.net/ #アンデラ @undeadunluck_an
# Under Ninja https://under-ninja.jp/ #アンダーニンジャ @UNDERNINJAanime
# Watashi no Oshi wa Akuyaku Reijou. https://wataoshi-anime.com/ #わたおし #wataoshi #ILTV @wataoshi_anime


# Fall 2023 Anime
class Fall2023AnimeDownload(MainDownload):
    season = "2023-4"
    season_name = "Fall 2023"
    folder_name = '2023-4'

    def __init__(self):
        super().__init__()


# 16bit Sensation: Another Layer
class SixteenBitSensationDownload(Fall2023AnimeDownload, NewsTemplate):
    title = '16bit Sensation: Another Layer'
    keywords = [title]
    website = 'https://16bitsensation-al.com/'
    twitter = '16bit_anime'
    hashtags = ['16bitAL', '16bitセンセーション']
    folder_name = '16bitsensation'

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
            stories = soup.select('.page_tab__item')
            for story in stories:
                try:
                    episode = str(int(story.select('a[href]')[0].text)).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                if 'is_current' in story['class']:
                    ep_soup = soup
                else:
                    a_tag = story.select('a[href]')
                    if len(a_tag) == 0:
                        continue
                    story_url = a_tag['href']
                    if story_url.startswith('./'):
                        story_url = story_prefix + story_url[2:]
                    ep_soup = self.get_soup(story_url)
                if ep_soup is None:
                    continue
                self.image_list = []
                images = ep_soup.select('.story_image_main img[src]')
                for i in range(len(images)):
                    image_name = episode + '_' + str(i + 1)
                    image_url = story_prefix + images[i]['src']
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        news_prefix = self.PAGE_PREFIX + 'news/'
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news_list__item',
                                    date_select='.news_list__item-date', title_select='.news_list__item-title',
                                    id_select='a', a_tag_start_text_to_remove='./', a_tag_prefix=news_prefix,
                                    paging_type=1, next_page_select='.news_pager_list__item',
                                    next_page_eval_index_class='is_current', next_page_eval_index=-1,
                                    date_func=lambda x: x[0:4] + '.' + x[5:])

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('top_kv', self.PAGE_PREFIX + 'assets/img/top/kv.jpg')
        self.add_to_image_list('top_kv_pc', self.PAGE_PREFIX + 'assets/img/top/kv_pc.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            images = soup.select('.character_image-image img[src]')
            self.image_list = []
            for image in images:
                image_url = self.clear_resize_in_url(self.PAGE_PREFIX + image['src'][1:])
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')

    def download_media(self):
        folder = self.create_media_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        for page in ['shop', '01', '02', '03', '04', '05', '06']:
            try:
                if page in processed:
                    continue
                page_url = self.PAGE_PREFIX + 'package/'
                if page != '01':
                    page_url += '?page=' + page
                soup = self.get_soup(page_url)
                images = soup.select('.package_wrapper img[src]')
                self.image_list = []
                for image in images:
                    image_url = self.PAGE_PREFIX + image['src'][1:].split('?')[0]
                    if not '/package/' in image_url:
                        continue
                    image_name = self.generate_image_name_from_url(image_url, 'package')
                    self.add_to_image_list(image_name, image_url)
                if page.isnumeric() and len(self.image_list) > 0:
                    processed.append(page)
                elif page.isnumeric():
                    break
                self.download_image_list(folder)
            except Exception as e:
                self.print_exception(e, f'Blu-ray - {page}')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Bokura no Ameiro Protocol
class BokuameDownload(Fall2023AnimeDownload, NewsTemplate):
    title = 'Bokura no Ameiro Protocol'
    keywords = [title, 'Our Rainy Protocol']
    website = 'https://bokuame.com/'
    twitter = 'bokuame_anime'
    hashtags = ['ボクアメ', '僕らの雨いろプロトコル']
    folder_name = 'bokuame'

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
            story_prefix = self.PAGE_PREFIX + 'episodes/'
            soup = self.get_soup(story_prefix)
            stories = soup.select('nav[data-type="archive"] a[href]')
            for story in stories:
                try:
                    episode = str(int(story.text)).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                ep_soup = self.get_soup(story['href'])
                if ep_soup is None:
                    continue
                self.image_list = []
                images = ep_soup.select('.mainss img[src],.subss img[src]')
                for i in range(len(images)):
                    image_name = episode + '_' + str(i + 1)
                    image_url = images[i]['src']
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.md-li__article',
                                    date_select='time', title_select='.ttl', id_select='a', news_prefix='topics/')

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
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.fv--v source[srcset][type]')
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
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.chardata source[srcset][type]')
            self.image_list = []
            for image in images:
                image_url = self.clear_resize_in_url(self.PAGE_PREFIX + image['srcset'][1:])
                if not image_url.endswith('.webp') or image_url.endswith('_sp.webp'):
                    continue
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')

    def download_media(self):
        folder = self.create_media_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'bd/')
            images = soup.select('.bd img[src]')
            self.image_list = []
            for image in images:
                image_url = self.clear_resize_in_url(self.PAGE_PREFIX + image['src'][1:])
                if '/bd/' not in image_url:
                    continue
                image_name = self.generate_image_name_from_url(image_url, 'bd')
                if image_name.startswith('np_'):
                    continue
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


# Boukensha ni Naritai to Miyako ni Deteitta Musume ga S-Rank ni Natteta
class SRankMusumeDownload(Fall2023AnimeDownload, NewsTemplate):
    title = 'Boukensha ni Naritai to Miyako ni Deteitta Musume ga S-Rank ni Natteta'
    keywords = [title, 'My Daughter Left the Nest and Returned an S-Rank Adventurer']
    website = 'https://s-rank-musume.com/'
    twitter = 's_rank_musume'
    hashtags = 'Sランク娘'
    folder_name = 'srankmusume'

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

    def download_episode_preview(self):
        soup = None
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            sections = soup.select('section.js-oneStory')
            for section in sections:
                try:
                    episode = str(int(section.select('.storyCont__title--num')[0].text.replace('#', ''))).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                self.image_list = []
                images = section.select('.storyImgLists img[src]')
                for i in range(len(images)):
                    image_url = self.clear_resize_in_url(self.PAGE_PREFIX + images[i]['src'][1:])
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)
        return soup

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.newsLists__item',
                                    date_select='.newsLists__time', title_select='.newsLists__title',
                                    id_select='a', a_tag_start_text_to_remove='/', a_tag_prefix=self.PAGE_PREFIX)

    def download_episode_preview_guess(self, print_invalid=False, download_valid=False):
        if self.is_image_exists(str(self.FINAL_EPISODE).zfill(2) + '_' + str(self.IMAGES_PER_EPISODE)):
            return

        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'wordpress/wp-content/uploads/%s/%s/%s_%s.jpg'
        current_date = datetime.now() + timedelta(hours=1)
        year = current_date.strftime('%Y')
        month = current_date.strftime('%m')
        is_successful = False
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            existing_image_name = episode + '_' + str(self.IMAGES_PER_EPISODE)
            if self.is_image_exists(existing_image_name) or self.is_image_exists(existing_image_name, folder):
                continue
            episode_success = False
            valid_urls = []
            for j in range(self.IMAGES_PER_EPISODE):
                image_url = template % (year, month, episode, str(j + 1).zfill(2))
                if self.is_valid_url(image_url, is_image=True):
                    print('VALID - ' + image_url)
                    episode_success = True
                    valid_urls.append({'num': str(j + 1), 'url': image_url})
                elif print_invalid:
                    print('INVALID - ' + image_url)
            if download_valid and len(valid_urls) > 0:
                for valid_url in valid_urls:
                    image_name = episode + '_' + valid_url['num']
                    self.download_image(valid_url['url'], folder + '/' + image_name)
            if not episode_success:
                break
            is_successful = True
        if is_successful:
            print(self.__class__.__name__ + ' - Guessed correctly!')
        return is_successful

    def download_key_visual(self, soup=None):
        folder = self.create_key_visual_directory()
        try:
            if soup is None:
                soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.visualListsWrap img[src]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'][1:]
                if '/top/' not in image_url:
                    continue
                image_name = self.generate_image_name_from_url(image_url, 'top')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')
        return soup

    def download_character(self, soup):
        folder = self.create_character_directory()
        try:
            if soup is None:
                soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.charaDetail__stand img[src], .charaDetail__faceLists img[src]')
            self.image_list = []
            for image in images:
                image_url = self.clear_resize_in_url(self.PAGE_PREFIX + image['src'][1:])
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')
        return soup


# Boushoku no Berserk
class BoushokunoBerserkDownload(Fall2023AnimeDownload, NewsTemplate):
    title = 'Boushoku no Berserk'
    keywords = [title, 'Berserk of Gluttony']
    website = 'https://bousyoku-anime.com/'
    twitter = 'bousyoku_anime'
    hashtags = ['暴食', '暴食のベルセルク']
    folder_name = 'boushokunoberserk'

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
            template = self.PAGE_PREFIX + 'assets/images/story/ep%s/ep%s_%s.webp'
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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-list li',
                                    date_select='.news-list-ymd', title_select='.news-list-title', id_select='a',
                                    next_page_select='.nav-links a.next.page-numbers', paging_type=3,
                                    paging_suffix='?paged=%s', date_separator='-')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        index_css = self.PAGE_PREFIX + 'assets/css/index.css'
        try:
            content = self.get_response(index_css)
            image_url = self.PAGE_PREFIX + content.split('.main-visual-inner{background:url(')[1]\
                .split(')')[0].replace('../', '')
            image_name = self.extract_image_name_from_url(image_url)
            self.download_image(image_url, folder + '/' + image_name)
        except Exception as e:
            pass
            # self.print_exception(e)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            images = soup.select('.character-main img[src].character-thumbnail')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'][1:]
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Buta no Liver wa Kanetsu Shiro
class ButaLiverDownload(Fall2023AnimeDownload, NewsTemplate):
    title = 'Buta no Liver wa Kanetsu Shiro'
    keywords = [title, 'Heat the Pig Liver', 'Butareba: The Story of a Man Who Turned into a Pig']
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
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        try:
            story_prefix = self.PAGE_PREFIX + 'story/'
            soup = self.get_soup(story_prefix)
            stories = soup.select('.p-story__tab li')
            for story in stories:
                try:
                    episode = str(int(story.select('.p-in_num')[0].text)).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_5'):
                    continue
                if 'is-current' in story['class']:
                    ep_soup = soup
                else:
                    a_tag = story.select('a[href]')
                    if len(a_tag) == 0:
                        continue
                    story_url = a_tag[0]['href']
                    if story_url.startswith('/'):
                        story_url = self.PAGE_PREFIX + story_url[1:]
                    ep_soup = self.get_soup(story_url)
                if ep_soup is None:
                    continue
                self.image_list = []
                images = ep_soup.select('.p-story__scene-item img[src]')
                for i in range(len(images)):
                    image_name = episode + '_' + str(i + 1)
                    image_url = story_prefix + images[i]['src']
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news/'
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.l-news__list-item',
                                    date_select='.p-in-data', title_select='.p-in-text', id_select='a',
                                    a_tag_prefix=news_url, next_page_select='ul.p-news_list__content-nav-list li',
                                    next_page_eval_index_class='is__current', next_page_eval_index=-1,
                                    paging_type=1)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        # self.add_to_image_list('tz', self.PAGE_PREFIX + 'assets/img/visual.png')
        #self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FjefZkkVQAAq-_0?format=jpg&name=4096x4096')
        # self.download_image_list(folder)
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.p-kv__image-content-list-item-image img[src]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'][1:]
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            images = soup.select('.p-in-image img[src],.p-in-face img[src]')
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
        for page in ['special', '01', '02', '03', '04', '05', '06']:
            try:
                if page in processed:
                    continue
                page_url = self.PAGE_PREFIX + 'bddvd/'
                if page.isnumeric():
                    page_url += 'vol'
                page_url += page + '.html'
                soup = self.get_soup(page_url)
                images = soup.select('.p-bddvd__content img[src]')
                self.image_list = []
                for image in images:
                    image_url = self.PAGE_PREFIX + image['src'].replace('../', '').split('?')[0]
                    if '/bddvd/' in image_url:
                        image_name = self.generate_image_name_from_url(image_url, 'bddvd')
                    else:
                        image_name = self.extract_image_name_from_url(image_url)
                    if image_name.startswith('np_'):
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


# Dekoboko Majo no Oyako Jijou
class DekobokoMajoDownload(Fall2023AnimeDownload, NewsTemplate):
    title = 'Dekoboko Majo no Oyako Jijou'
    keywords = [title]
    website = 'https://dekoboko-majo-anime.jp/'
    twitter = 'DEKOBOKO_anime'
    hashtags = ['でこぼこ魔女の親子事情']
    folder_name = 'dekoboko-majo'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 4

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='#news article', date_select='time',
                                    title_select='h3', id_select=None, id_has_id=True, news_prefix='')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        # self.image_list = []
        # self.add_to_image_list('teaser-visual', self.PAGE_PREFIX + 'images/teaser-visual.jpg')
        # self.add_to_image_list('mainimg', self.PAGE_PREFIX + 'images/mainimg.jpg')
        # self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.mainimg img[src]')
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
        prefix = self.PAGE_PREFIX + 'assets/images/character/'
        template = [prefix + 'img_%s.png', prefix + 'face_%s.png']
        self.download_by_template(folder, template, 2, 1)

    def download_media(self):
        folder = self.create_media_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'blu-ray/')
            images = soup.select('#blu-ray>div img[src]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                image_name = self.extract_image_name_from_url(image_url)
                if 'nowprinting' in image_name:
                    continue
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


# Goblin Slayer 2nd Season
class GoblinSlayer2Download(Fall2023AnimeDownload, NewsTemplate):
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
        self.download_media()

    def download_episode_preview(self):
        try:
            story_prefix = self.PAGE_PREFIX + 'story/'
            soup = self.get_soup(story_prefix)
            stories = soup.select('.pgnavlist a[href]')
            for story in stories:
                try:
                    episode = str(int(story.text.replace('#', ''))).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                ep_soup = self.get_soup(story['href'])
                if ep_soup is None:
                    continue
                self.image_list = []
                images = ep_soup.select('.boxthum img[src]')
                for i in range(len(images)):
                    image_name = episode + '_' + str(i + 1)
                    image_url = images[i]['src']
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.newsliste li',
                                    date_select='.newstime', title_select='.newstitle', id_select='a',
                                    paging_type=3, paging_suffix='/?pg=%s', next_page_select='.ban_pgnext')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('teaser', 'https://pbs.twimg.com/media/EtDYBThUYAEBIWI?format=jpg&name=4096x4096')
        self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/FsCxEnRaMAEQ9US?format=jpg&name=4096x4096')
        self.add_to_image_list('kv1', self.PAGE_PREFIX + 'images/top-img.jpg')
        self.add_to_image_list('kv2_tw', 'https://pbs.twimg.com/media/F5feM8EawAAXTEY?format=jpg&name=large')
        self.download_image_list(folder)

    def download_media(self):
        folder = self.create_media_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        for page in ['tokuten', 'campaign', '01', '02', '03']:
            try:
                if page in processed:
                    continue
                page_url = self.PAGE_PREFIX + 'bd/'
                if page != '01':
                    page_url += page + '.html'
                soup = self.get_soup(page_url)
                images = soup.select('.mobinner img[src]')
                self.image_list = []
                for image in images:
                    image_url = self.PAGE_PREFIX + image['src'].replace('../', '').split('?')[0]
                    if '/bd/' in image_url:
                        image_name = self.generate_image_name_from_url(image_url, 'bd')
                    else:
                        image_name = self.extract_image_name_from_url(image_url)
                    if image_name == 'keyart':
                        continue
                    self.add_to_image_list(image_name, image_url)
                if (page.isnumeric() or page == 'campaign') and len(self.image_list) > 0:
                    processed.append(page)
                elif page.isnumeric():
                    break
                self.download_image_list(folder)
            except Exception as e:
                self.print_exception(e, f'Blu-ray - {page}')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Hametsu no Oukoku
class HametsuDownload(Fall2023AnimeDownload, NewsTemplate):
    title = 'Hametsu no Oukoku'
    keywords = [title, 'The Kingdoms of Ruin']
    website = 'https://hametsu-anime.com/'
    twitter = 'hametsu_anime'
    hashtags = ['はめつのおうこく', 'はめつ']
    folder_name = 'hametsu'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.content-entry',
                                    title_select='.entry-title span', date_select='.entry-date span',
                                    id_select=None, id_has_id=True, news_prefix='news.html')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/Fn261mwaQAAWJst?format=jpg&name=4096x4096')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.vis source[srcset]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['srcset'].replace('./', '').split('?')[0]
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
            self.PAGE_PREFIX + 'assets/character/%sf.webp',
            self.PAGE_PREFIX + 'assets/character/%ss.webp'
        ]
        self.download_by_template(folder, templates, 1, 1)

    def download_media(self):
        folder = self.create_media_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'bluray.html')
            self.image_list = []
            images = soup.select('.sub-content-container img[src]')
            for image in images:
                if '/bluray/' not in image['src'] or 'np-bnf' in image['src']:
                    continue
                image_url = self.PAGE_PREFIX + image['src'].replace('./', '').split('?')[0]
                image_name = self.generate_image_name_from_url(image_url, 'bluray')
                self.add_to_image_list(image_name, image_url, to_jpg=True)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


# Saihate no Paladin: Tetsusabi no Yama no Ou
class SaihatenoPaladin2Download(Fall2023AnimeDownload, NewsTemplate):
    title = 'Saihate no Paladin: Tetsusabi no Yama no Ou'
    keywords = [title, 'The Faraway Paladin', '2nd Season']
    website = 'https://farawaypaladin.com/'
    twitter = 'faraway_paladin'
    hashtags = ['faraway_paladin', '最果てのパラディン']
    folder_name = 'saihate-no-paladin2'

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

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'storys')
            posts = soup.select('div.post')
            for post in posts:
                h1_tag = post.find('h1')
                try:
                    episode = str(int(h1_tag.text.strip().replace('第', '').split('話')[0])).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                ul = post.find('ul')  # Get first ul tag
                if ul:
                    images = ul.select('img[src]')
                    self.image_list = []
                    for i in range(len(images)):
                        image_url = self.clear_resize_in_url(images[i]['src'])
                        image_name = episode + '_' + str(i + 1)
                        self.add_to_image_list(image_name, image_url)
                    self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='#news dd', date_select='i',
                                    title_select='span', id_select='a', stop_date='2022',
                                    date_func=lambda x: x.replace('年', '.').replace('月', '.').replace('日', ''),
                                    next_page_select='.wp-pagenavi *', next_page_eval_index_class='current',
                                    next_page_eval_index=-1)

    def download_episode_preview_guess(self):
        if self.is_image_exists(str(self.FINAL_EPISODE).zfill(2) + '_1'):
            return
        folder = self.create_custom_directory('guess')
        cache_filepath = folder + '/cache'
        month = 10
        ep_num = 1
        episode = '01'
        while ep_num <= self.FINAL_EPISODE:
            if self.is_image_exists(episode + '_1'):
                ep_num += 1
                episode = str(ep_num).zfill(2)
            else:
                break
        ep_num_to_save = ep_num
        try:
            if os.path.exists(cache_filepath):
                with open(cache_filepath, 'r') as f:
                    items = f.read().split(',')
                    month = int(items[0])
                    last_ep_num = int(items[1]) + 1
                    if ep_num < last_ep_num:
                        ep_num = last_ep_num
                        ep_num_to_save = last_ep_num - 1
        except:
            pass

        jp_nums = '０１２３４５６７８９'
        template = self.PAGE_PREFIX + 'wp/wp-content/uploads/2023/%s/%s話先行カット-%s.jpg'
        month_to_save = month
        is_successful = False
        try:
            while ep_num <= self.FINAL_EPISODE:
                stop = False
                jp_num = jp_nums[ep_num % 10]
                if ep_num > 9:
                    jp_num = jp_nums[1] + jp_num
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (str(month).zfill(2), jp_num, str(j + 1))
                    image_name = str(ep_num).zfill(2) + '_' + str(j + 1)
                    result = self.download_image(image_url, folder + '/' + image_name)
                    if result == -1:
                        if month == month_to_save:
                            month += 1
                            ep_num -= 1
                        else:
                            stop = True
                        break
                    else:
                        if month_to_save != month or ep_num_to_save != ep_num:
                            is_successful = True
                        month_to_save = month
                        ep_num_to_save = ep_num
                if stop:
                    break
                ep_num += 1

            with open(cache_filepath, 'w+') as f:
                f.write(str(month_to_save) + ',' + str(ep_num_to_save))
        except Exception as e:
            self.print_exception(e, 'Guess')
        if is_successful:
            print(self.__class__.__name__ + ' - Guessed correctly!')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.js_subImg img[src]')
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
        template = self.PAGE_PREFIX + 'wp/wp-content/themes/farawaypaladin_v5/img/cara%s.png'
        self.download_by_template(folder, template, 1)


# Hikikomari Kyuuketsuki no Monmon
class HikikomariDownload(Fall2023AnimeDownload, NewsTemplate):
    title = 'Hikikomari Kyuuketsuki no Monmon'
    keywords = [title]
    website = 'https://hikikomari.com/'
    twitter = 'komarin_PR'
    hashtags = ['ひきこまり']
    folder_name = 'hikikomari'

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
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            stories = soup.select('.story-nav__list .story-nav__list-item a[href]')
            for story in stories:
                try:
                    ahref = story['href']
                    if ahref.endswith('/'):
                        ahref = ahref[:-1]
                    episode = str(int(ahref.split('/')[-1])).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                ep_url = story['href']
                if ep_url.startswith('/'):
                    ep_url = self.PAGE_PREFIX + ep_url[1:]
                ep_soup = self.get_soup(ep_url)
                if ep_soup is None:
                    continue
                self.image_list = []
                images = ep_soup.select('.imglist img[src]')
                for i in range(len(images)):
                    image_url = self.PAGE_PREFIX + images[i]['src'][1:]
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='article.news-lineup__block',
                                    date_select='dt', title_select='h2', id_select='a', a_tag_prefix=self.PAGE_PREFIX,
                                    a_tag_start_text_to_remove='/')

    def download_episode_preview_guess(self):
        template = self.PAGE_PREFIX + 'assets/img/story/%s/pic%s.jpg'
        folder = self.create_custom_directory('guess')
        is_successful = False
        stop = False
        try:
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_1') or self.is_image_exists(episode + '_1', folder):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (episode, str(j + 1).zfill(2))
                    if not self.is_content_length_in_range(image_url, more_than_amount=3000):
                        stop = True
                        break
                    image_name = episode + '_' + str(j + 1)
                    result = self.download_image(image_url, folder + '/' + image_name)
                    if result != -1:
                        is_successful = True
                if stop:
                    break
        except:
            pass
        if is_successful:
            print(self.__class__.__name__ + ' - Guessed correctly!')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.mv-pc.pc source[srcset]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['srcset'][1:]
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'assets/img/%s.png'
        try:
            for i in range(20):
                img_num = str(i + 1).zfill(2)
                is_successful = False
                for j in string.ascii_uppercase:
                    image_name = 'character-detail-img' + img_num + j
                    if self.is_image_exists(image_name, folder):
                        is_successful = True
                        break
                    image_url = template % image_name
                    result = self.download_image(image_url, folder + '/' + image_name)
                    if result != -1:
                        is_successful = True
                    else:
                        break
                if not is_successful:
                    break
        except Exception as e:
            self.print_exception(e, 'Character')

    def download_media(self):
        folder = self.create_media_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        for page in ['tokuten', '01', '02', '03']:
            try:
                if page.isnumeric() and page in processed:
                    continue
                soup = self.get_soup(self.PAGE_PREFIX + 'blu-ray/' + page + '.html')
                images = soup.select('.bluray-main img[src]')
                self.image_list = []
                for image in images:
                    image_url = image['src']
                    if not image_url.startswith('http'):
                        if image_url.startswith('/'):
                            image_url = self.PAGE_PREFIX + image_url[1:]
                        else:
                            continue
                    image_name = self.extract_image_name_from_url(image_url)
                    if '-demo' in image_name:
                        continue
                    self.add_to_image_list(image_name, image_url)
                if page.isnumeric():
                    if len(self.image_list) > 0:
                        processed.append(page)
                    else:
                        break
                self.download_image_list(folder)
            except Exception as e:
                self.print_exception(e, f'Blu-ray - {page}')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Hoshikuzu Telepath
class HoshiteleDownload(Fall2023AnimeDownload, NewsTemplate):
    title = 'Hoshikuzu Telepath'
    keywords = [title, 'Hoshitele']
    website = 'https://hoshitele-anime.com/'
    twitter = 'hoshitele_anime'
    hashtags = ['星テレ', 'hoshitele']
    folder_name = 'hoshitele'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.bl_vertPosts_item',
                                    date_select='.bl_vertPosts_date', title_select='.bl_vertPosts_txt',
                                    id_select='a', a_tag_prefix=news_url, a_tag_start_text_to_remove='./')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('picture.js_heroImg source[type][srcset]')
            self.image_list = []
            for image in images:
                if '/top/' not in image['srcset']:
                    continue
                image_name = self.extract_image_name_from_url(image['srcset'])
                if 'kv' not in image_name:
                    continue
                image_name = self.generate_image_name_from_url(image['srcset'], 'top')
                image_url = self.PAGE_PREFIX + image['srcset'].split('?')[0].replace('./', '')
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
                if 'ビジュアル' in title or 'KV' in title.upper():
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

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'dist/img/character/character%s/stand.webp'
        try:
            for i in range(20):
                image_url = template % str(i + 1)
                image_name = 'character' + str(i + 1) + '_stand'
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
            images = soup.select('.tp_bd_media img[src],.tp_bd_media source[srcset]')
            self.image_list = []
            for image in images:
                srcset = 'srcset'
                if image.has_attr('src'):
                    srcset = 'src'
                if '/bd/' not in image[srcset]:
                    continue
                image_url = self.PAGE_PREFIX + image[srcset].replace('./', '').split('?')[0]
                image_name = self.generate_image_name_from_url(image_url, 'bd')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


# Kage no Jitsuryokusha ni Naritakute!
class KagenoJitsuryokusha2Download(Fall2023AnimeDownload, NewsTemplate):
    title = 'Kage no Jitsuryokusha ni Naritakute! 2nd Season'
    keywords = [title, 'The Eminence in Shadow']
    website = 'https://shadow-garden.jp/'
    twitter = 'Shadowgarden_PR'
    hashtags = '陰の実力者'
    folder_name = 'kagenojitsuryoku2'

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
            self.image_list = []
            stories = soup.select('.storyImgListsWrap[id]')
            for story in stories:
                try:
                    episode = str(int(story['id'].replace('st', ''))).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                self.image_list = []
                images = story.select('img[src]')
                for i in range(len(images)):
                    image_url = self.PAGE_PREFIX + images[i]['src'].replace('../', '')
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.newsLists__item',
                                    date_select='time', title_select='.newsLists__title', id_select='a',
                                    next_page_select='.nextpostslink', paging_type=3, paging_suffix='?paged=%s',
                                    stop_date='2023.02.16')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('.fvTitleArea__visualLists img[src]')
            for image in images:
                if '/common/' not in image['src']:
                    continue
                image_url = self.PAGE_PREFIX + image['src'].replace('./', '')
                image_name = self.generate_image_name_from_url(image_url, 'common')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        chara_php = self.PAGE_PREFIX + 'character/data/%s.php'
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            self.image_list = []
            a_tags = soup.select('.charaLists__item a[href]')
            for a_tag in a_tags:
                name = a_tag['href'][1:]
                if name in processed:
                    continue
                chara_soup = self.get_soup(chara_php % name)
                if chara_soup is None:
                    continue
                images = chara_soup.select('.charaModal__imgWrap img[src]')
                self.image_list = []
                for image in images:
                    image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
                if len(self.image_list) > 0:
                    processed.append(name)
                self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')
        self.create_cache_file(cache_filepath, processed, num_processed)

    def download_media(self):
        folder = self.create_media_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'bddvd/')
            images = soup.select('#bddvdContWrap img[src]')
            self.image_list = []
            for image in images:
                if '/bddvd/' not in image['src'] or 'np_l.jpg' in image['src']:
                    continue
                image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                image_name = 'bddvd_' + self.generate_image_name_from_url(image_url, 'bddvd')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


# Kanojo mo Kanojo Season 2
class Kanokano2Download(Fall2023AnimeDownload, NewsTemplate):
    title = 'Kanojo mo Kanojo Season 2'
    keywords = [title, 'Kanokano']
    website = 'https://kanokano-anime.com/'
    twitter = 'kanokano_anime'
    hashtags = ['kanokano', 'カノジョも彼女']
    folder_name = 'kanokano2'

    PAGE_PREFIX = website
    IMAGES_PER_EPISODE = 6
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
        try:
            soup = self.get_soup(self.PAGE_PREFIX + '/story/')
            blocks = soup.select('.story-main__detail__block')
            for block in blocks:
                if block.has_attr('id') and block['id'].startswith('StoryBlock'):
                    try:
                        episode = str(int(block['id'].split('StoryBlock')[1].strip())).zfill(2)
                    except:
                        continue
                    if self.is_image_exists(episode + '_1'):
                        continue
                    images = block.select('div.swiper-slide img')
                    self.image_list = []
                    for i in range(len(images)):
                        image_url = self.PAGE_PREFIX + images[i]['src'][1:]
                        image_name = episode + '_' + str(i + 1)
                        self.add_to_image_list(image_name, image_url)
                    self.download_image_list(self.base_folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='article.news-lineup__block',
                                    date_select='dt', title_select='h2', id_select='a', a_tag_prefix=self.PAGE_PREFIX,
                                    a_tag_start_text_to_remove='/')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('mv-img@2x', self.PAGE_PREFIX + 'assets/img/mv-img@2x.png')
        self.add_to_image_list('kv_tw', 'https://pbs.twimg.com/media/F05yoojaEAIdFgG?format=jpg&name=medium')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'assets/img/character-detail-img%s@2x.png'
        self.download_by_template(folder, template, 2)

    def download_media(self):
        folder = self.create_media_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + '/bluraydvd/')
            images = soup.select('.bluraydvd-wrap img[src]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'][1:]
                image_name = self.extract_image_name_from_url(image_url)
                if not image_url.endswith('-np.png'):
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Blu-ray')
            print(e)


# Keikenzumi na Kimi to, Keiken Zero na Ore ga, Otsukiai suru Hanashi.
class KimizeroDownload(Fall2023AnimeDownload, NewsTemplate2):
    title = 'Keikenzumi na Kimi to, Keiken Zero na Ore ga, Otsukiai suru Hanashi.'
    keywords = [title, "Kimizero"]
    website = 'https://kimizero.com/'
    twitter = 'kimizero_anime'
    hashtags = 'キミゼロ'
    folder_name = 'kimizero'

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
            a_tags = soup.select('#ContentsListUnit03 a[href]')
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

    def download_episode_preview_external(self):
        keywords = ['経験済みなキミと']
        AniverseMagazineScanner(keywords, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20231002', download_id=self.download_id).run()

    def download_episode_preview_guess(self):
        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'core_sys/images/contents/%s/block/%s/%s.jpg'
        is_successful = False
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1'):
                continue
            is_success = False
            first = 23 + i
            second = 46 + 6 * i
            third = 38 + 6 * i
            for j in range(self.IMAGES_PER_EPISODE):
                image_url = template % (str(first).zfill(8), str(second).zfill(8), str(third + j).zfill(8))
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

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        # self.image_list = []
        # self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FcM7PglaIAA_9Bd?format=jpg&name=4096x4096')
        # self.add_to_image_list('tz_kv', self.PAGE_PREFIX + 'core_sys/images/main/tz/kv.jpg')
        # self.add_to_image_list('tz_loading_kv', self.PAGE_PREFIX + 'core_sys/images/main/tz/loading_kv.jpg')
        # self.download_image_list(folder)
        
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('.kvSlide source[srcset]')
            for image in images:
                if '/main/' not in image['srcset']:
                    continue
                image_url = self.PAGE_PREFIX + image['srcset']
                image_name = self.generate_image_name_from_url(image_url, 'main')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

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
                images = ep_soup.select('.chara__stand img[src],.chara__face img[src]')
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
                    if page.isnumeric() and not self.is_content_length_in_range(image_url, more_than_amount=18000):
                        continue
                    if page == 'privilege' and not self.is_content_length_in_range(image_url, more_than_amount=26000):
                        continue
                    self.add_to_image_list(image_name, image_url)
                if (page.isnumeric() or page == 'campaign') and len(self.image_list) > 0:
                    processed.append(page)
                elif page.isnumeric():
                    break
                self.download_image_list(folder)
            except Exception as e:
                self.print_exception(e, f'Blu-ray - {page}')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Kikansha no Mahou wa Tokubetsu desu  #帰還者 #returnersmagic @returners_magic
class KikanshaDownload(Fall2023AnimeDownload, NewsTemplate):
    title = 'Kikansha no Mahou wa Tokubetsu desu'
    keywords = [title, "A Returner's Magic Should Be Special"]
    website = 'https://returners-magic.com/'
    twitter = 'returners_magic'
    hashtags = ['帰還者', 'returnersmagic']
    folder_name = 'kikansha'

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
            stories = soup.select('.page_tab__item')
            for story in stories:
                try:
                    episode = str(int(story.select('a[href]')[0].text)).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_5'):
                    continue
                if 'is_current' in story['class']:
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
                images = ep_soup.select('.story_image__main img[src]')
                for i in range(len(images)):
                    image_name = episode + '_' + str(i + 1)
                    image_url = story_prefix + images[i]['src']
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news/'
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news_list__item',
                                    date_select='.-date', title_select='.-title', id_select='a',
                                    a_tag_prefix=news_url, a_tag_start_text_to_remove='./', paging_type=1,
                                    next_page_select='.pager_list__item',
                                    next_page_eval_index_class='is_current', next_page_eval_index=-1,
                                    date_func=lambda x: x[0:4] + '.' + str(self.convert_month_string_to_number(x[5:8])).zfill(2) + '.' + x[9:])

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('kv_news', self.PAGE_PREFIX + 'news/detail/SYS/CONTENTS/be86859e-0fcc-4d49-a781-f58b64303713')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            charas = soup.select('.chara_detail__item')
            for chara in charas:
                has_change = len(chara.select('.chara_detail__change')) > 0
                images = chara.select('.chara_detail__image img[src]')
                self.image_list = []
                for image in images:
                    image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
                    if has_change:
                        new_image_url = image_url.replace('_1.', '_2.')
                        new_image_name = self.extract_image_name_from_url(image_url)
                        self.add_to_image_list(new_image_name, new_image_url)
                self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')

    def download_media(self):
        folder = self.create_media_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        for page in ['shop', '01', '02', '03', '04', '05', '06']:
            try:
                if page in processed:
                    continue
                page_url = self.PAGE_PREFIX + 'bddvd/?page=' + page
                soup = self.get_soup(page_url)
                images = soup.select('.package_wrapper img[src]')
                self.image_list = []
                for image in images:
                    image_url = self.PAGE_PREFIX + image['src'][1:].split('?')[0]
                    if not '/bddvd/' in image_url:
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


# Kimi no Koto ga Daidaidaidaidaisuki na 100-nin no Kanojo
class HyakkanoDownload(Fall2023AnimeDownload, NewsTemplate):
    title = 'Kimi no Koto ga Daidaidaidaidaisuki na 100-nin no Kanojo'
    keywords = [title, 'The 100 Girlfriends Who Really, Really, Really, Really, Really Love You']
    website = 'https://hyakkano.com/'
    twitter = 'hyakkano_anime'
    hashtags = '100カノ'
    folder_name = 'hyakkano'

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
            soup = self.get_soup(self.PAGE_PREFIX + 'story/season1/')
            stories = soup.select('.story-Wrapper[id]')
            for story in stories:
                try:
                    episode = str(story['id'].replace('ep', '')).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
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

    def download_episode_preview_external(self):
        keywords = ['君のことが大大大大大好きな100人の彼女']
        AniverseMagazineScanner(keywords, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20230928', download_id=self.download_id).run()

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-List li',
                                    date_select='.date', title_select='.title', id_select='a')

    def download_episode_preview_guess(self, print_invalid=False, download_valid=False):
        if self.is_image_exists(str(self.FINAL_EPISODE).zfill(2) + '_' + str(self.IMAGES_PER_EPISODE)):
            return

        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'xUtUy1FY/wp-content/uploads/%s/%s/%s.jpg'
        current_date = datetime.now() + timedelta(hours=1)
        year = current_date.strftime('%Y')
        month = current_date.strftime('%m')
        is_successful = False
        valid_urls = []
        prefixes = ['01_main', '02_sub1', '03_sub2', '04_sub3', '05_sub4', '06_sub5']
        for j in range(self.IMAGES_PER_EPISODE):
            k = 0
            while k < 20:
                if k == 0:
                    append = ''
                else:
                    append = '-' + str(k)
                image_folder = folder + '/' + year + '/' + month
                image_name = prefixes[j] + append
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

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz', self.PAGE_PREFIX + 'xUtUy1FY/wp-content/themes/hyakkano_v0/assets/images/common/index/img_mainvisual.png')
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FrGH-A3aUAA0dVE?format=jpg&name=medium')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('.index-Mainvisual-Inner img[src]')
            for image in images:
                if '/images/' not in image['src']:
                    continue
                image_url = image['src']
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
            charas = soup.select('.chara-select-Btn a[href][class]')
            for chara in charas:
                if chara['href'].endswith('/'):
                    page_url = chara['href'][:-1]
                else:
                    page_url = chara['href']
                chara_name = page_url.split('/')[-1]
                if chara_name in processed:
                    continue
                if 'current' in chara['class']:
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(page_url)
                if ep_soup is None:
                    continue
                images = ep_soup.select('.character-Item img[src]')
                self.image_list = []
                for image in images:
                    image_url = image['src']
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(folder)
                processed.append(chara_name)
        except Exception as e:
            self.print_exception(e, 'Character')
        self.create_cache_file(cache_filepath, processed, num_processed)

    def download_media(self):
        folder = self.create_media_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'blu-ray/')
            # Bonus
            self.image_list = []
            images = soup.select('.bonus-Images img[src]')
            for image in images:
                image_url = self.clear_resize_in_url(image['src'])
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)

            # Blu-ray
            bds = soup.select('.blu-ray-List li')
            for bd in reversed(bds):
                a_tags = bd.select('a[href]')
                if len(a_tags) == 0:
                    continue
                bd_url = a_tags[0]['href']
                if bd_url.endswith('/'):
                    bd_url = bd_url[:-1]
                page = bd_url.split('/')[-1]
                if page in processed:
                    continue
                if len(bd.select('img[src*="nowprinting"]')) > 0:
                    continue
                bd_soup = self.get_soup(bd_url)
                if bd_soup is None:
                    continue
                self.image_list = []
                images = bd_soup.select('.bluray-Images img[src]')
                for image in images:
                    image_url = self.clear_resize_in_url(image['src'])
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
                if len(self.image_list) > 0:
                    processed.append(page)
                self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Konyaku Haki sareta Reijou wo Hirotta Ore ga, Ikenai koto wo Oshiekomu
class IkenaikyoDownload(Fall2023AnimeDownload, NewsTemplate):
    title = 'Konyaku Haki sareta Reijou wo Hirotta Ore ga, Ikenai koto wo Oshiekomu'
    keywords = [title, "ikenaikyo", "I’m Giving the Disgraced Noble Lady I Rescued a Crash Course in Naughtiness"]
    website = 'https://ikenaikyo.com/'
    twitter = 'ikenaikyo_anime'
    hashtags = ['イケナイ教']
    folder_name = 'ikenaikyo'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 4

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
            btns = soup.select('.infoTag a[class]')
            for btn in btns:
                try:
                    episode = str(int(btn.text.replace('第', '').replace('話', ''))).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                class__ = None
                for class_ in btn['class']:
                    if class_.startswith('group'):
                        class__ = class_
                        break
                if class__ is None:
                    continue
                self.image_list = []
                images = soup.select(f'.{class__} img[src]:not(.main img[src])')
                for i in range(len(images)):
                    image_url = images[i]['src']
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.infoList a',
                                    date_select='span', title_select='li', id_select=None)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz', self.PAGE_PREFIX + 'manage/wp-content/uploads/2023/04/KV.jpg')
        self.add_to_image_list('main_visual2', self.PAGE_PREFIX + 'manage/wp-content/uploads/2023/08/main_visual2.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        chara_prefix = self.PAGE_PREFIX + 'images/character/chara'
        templates = [
            chara_prefix + '%s.png',
            chara_prefix + '%s-1.png',
            chara_prefix + '%s-2.png'
        ]
        self.download_by_template(folder, templates, 2, 1)

    def download_media(self):
        folder = self.create_media_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'bd-dvd/')
            images = soup.select('.group0 img[src],.group1 img[src]')
            self.image_list = []
            for image in images:
                image_url = image['src']
                if '/bd-dvd/' not in image_url or 'nowprinting' in image_url:
                    continue
                if image_url.startswith('/'):
                    image_url = self.PAGE_PREFIX + image_url[1:]
                image_name = self.generate_image_name_from_url(image_url, 'bd-dvd')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


# Kusuriya no Hitorigoto
class KusuriyaDownload(Fall2023AnimeDownload, NewsTemplate):
    title = 'Kusuriya no Hitorigoto'
    keywords = [title, 'The Apothecary Diaries']
    website = 'https://kusuriyanohitorigoto.jp/'
    twitter = 'kusuriya_PR'
    hashtags = ['薬屋のひとりごと']
    folder_name = 'kusuriya'

    PAGE_PREFIX = website
    FINAL_EPISODE = 24
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
            template = self.PAGE_PREFIX + 'episodes/img/%s/%s.jpg'
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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='li.newsLists__item',
                                    date_select='time', title_select='.newsLists__title', id_select='a',
                                    a_tag_start_text_to_remove='./', a_tag_prefix=news_url)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('main_visual', self.PAGE_PREFIX + 'assets/img/top/main/main_visual.jpg')
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/Fo_spzaaIAI3CpS?format=jpg&name=4096x4096')
        self.add_to_image_list('kv', 'https://pbs.twimg.com/media/F0Z-4uZaUAArQ7_?format=jpg&name=4096x4096')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'assets/img/top/chara/chara%s_img.png'
        self.download_by_template(folder, template, 1, 1)

    def download_media(self):
        folder = self.create_media_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        bd_prefix = self.PAGE_PREFIX + 'blu-ray/'
        for page in ['benefit', '1', '2', '3', '4']:
            try:
                if page in processed:
                    continue
                soup = self.get_soup(bd_prefix + page + '.html')
                images = soup.select('.subContOne img[src]')
                self.image_list = []
                for image in images:
                    image_url = image['src'].split('?')[0]
                    if image_url.startswith('./'):
                        image_url = bd_prefix + image_url[2:]
                    image_name = self.extract_image_name_from_url(image_url)
                    if image_name.startswith('np_'):
                        continue
                    self.add_to_image_list(image_name, image_url)
                if page.isnumeric():
                    if len(self.image_list) > 0:
                        processed.append(page)
                    else:
                        break
                self.download_image_list(folder)
            except Exception as e:
                self.print_exception(e, f'Blu-ray - {page}')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Potion-danomi de Ikinobimasu!
class PotionDanomiDownload(Fall2023AnimeDownload, NewsTemplate):
    title = 'Potion-danomi de Ikinobimasu!'
    keywords = [title, 'I Shall Survive Using Potions!']
    website = 'https://potion-anime.com/'
    twitter = 'potion_APR'
    hashtags = 'ポーション頼み'
    folder_name = 'potiondanomi'

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

    def download_episode_preview(self, print_http_error=False):
        if self.is_image_exists(str(self.FINAL_EPISODE) + '_1') and self.is_image_exists('01_1'):
            return

        try:
            objs = self.get_json(
                self.PAGE_PREFIX + 'news/wp-json/wp/v2/pages?orderby=date&order=asc&acf_format=standard&per_page=100&parent=83')
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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-list a',
                                    date_select='.news-list-item__date', title_select='.news-list-item__title',
                                    id_select=None, a_tag_start_text_to_remove='/', a_tag_prefix=self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('.home-visual__visual source[srcset]')
            for image in images:
                if '/img/' in image['srcset']:
                    image_url = self.PAGE_PREFIX + image['srcset'].split('?')[0].replace('./', '')
                    image_name = self.generate_image_name_from_url(image_url, 'img')
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
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        for page in range(1, 4, 1):
            try:
                if page != 1 and str(page) in processed:
                    continue
                page_url = self.PAGE_PREFIX + f'product/bd/bd_{page}/'
                soup = self.get_soup(page_url)
                images = soup.select('.c-article-visual__item img[src], .c-card__thumb[data-bg]')
                image_count = 0
                self.image_list = []
                for image in images:
                    if image.has_attr('src'):
                        image_url = image['src']
                        if 'nowprinting' in image_url:
                            continue
                        image_count += 1
                    elif page != 1:
                        continue
                    else:
                        image_url = image['data-bg']
                        if '/bd/' not in image_url or 'nowprinting' in image_url:
                            continue
                    if image_url.startswith('./'):
                        image_url = page_url + image_url[1:]
                    elif image_url.startswith('/'):
                        image_url = self.PAGE_PREFIX + image_url[1:]
                    elif image_url.startswith('../'):
                        image_url = self.PAGE_PREFIX + image_url.replace('../', '')
                    image_name = self.generate_image_name_from_url(image_url, 'bd')
                    self.add_to_image_list(image_name, image_url)
                if page != 1:
                    if image_count > 0:
                        processed.append(str(page))
                    else:
                        break
                self.download_image_list(folder)
            except Exception as e:
                self.print_exception(e, f'Blu-ray - {page}')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Ragna Crimson
class RagnaCrimsonDownload(Fall2023AnimeDownload, NewsTemplate):
    title = 'Ragna Crimson'
    keywords = [title]
    website = 'https://ragna-crimson.com/'
    twitter = 'ragnacrimson_PR'
    hashtags = ['ラグナクリムゾン', 'RagnaCrimson']
    folder_name = 'ragnacrimson'

    PAGE_PREFIX = website
    FINAL_EPISODE = 24
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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.list li',
                                    date_select='time', title_select='a', id_select='a',
                                    date_func=lambda x: x[0:10], a_tag_start_text_to_remove='../',
                                    a_tag_prefix=self.PAGE_PREFIX, paging_type=3, paging_suffix='/page%s.html',
                                    paging_suffix_zfill=2, next_page_select='a.next')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('.mainimg img[src]')
            for image in images:
                image_url = image['src']
                if image_url.startswith('./'):
                    image_url = self.PAGE_PREFIX + image_url[2:]
                if '/images/' not in image_url:
                    continue
                image_name = self.generate_image_name_from_url(image_url, 'images')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        templates = [
            self.PAGE_PREFIX + 'assets/images/character/img_%s.png',
            self.PAGE_PREFIX + 'assets/images/character/face_%s.png'
        ]
        self.download_by_template(folder, templates, 2, 1)

    def download_media(self):
        folder = self.create_media_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        for page in ['', '02']:
            try:
                if len(page) > 0 and page in processed:
                    continue
                bd_url = self.PAGE_PREFIX + 'blu-ray/'
                if len(page) > 0:
                    bd_url += page + '.html'
                soup = self.get_soup(bd_url)
                images = soup.select('.inner img[src]')
                self.image_list = []
                for image in images:
                    if '/blu-ray/' not in image['src'] or 'nowprinting' in image['src']:
                        continue
                    image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                    image_name = self.generate_image_name_from_url(image_url, 'blu-ray')
                    self.add_to_image_list(image_name, image_url)
                if len(page) > 0:
                    if len(self.image_list) > 0:
                        processed.append(page)
                    else:
                        break
                self.download_image_list(folder)
            except Exception as e:
                self.print_exception(e, f'Blu-ray - {page}')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Seijo no Maryoku wa Bannou Desu 2nd Season
class SeijonoMaryoku2Download(Fall2023AnimeDownload, NewsTemplate2):
    title = 'Seijo no Maryoku wa Bannou Desu 2nd Season'
    keywords = [title, 'seijonomaryoku', 'seijyonomaryoku', "The Saint's Magic Power is Omnipotent"]
    website = 'https://seijyonomaryoku.jp/'
    twitter = 'seijyonoanime'
    hashtags = ['seijyonoanime', '聖女の魔力は万能です']
    folder_name = 'seijyonomaryoku2'

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
            trs = soup.select('#ContentsListUnit02 tr[class]')
            for tr in trs:
                a_tags = tr.select('a[href]')
                if len(a_tags) == 0:
                    continue
                try:
                    episode = str(int(a_tags[0].text.replace('Episode', ''))).zfill(2)
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
            first = 20 + i
            second = 31 + 4 * i
            third = 31 + 6 * i
            for j in range(self.IMAGES_PER_EPISODE):
                image_url = template % (str(first).zfill(8), str(second).zfill(8), str(third + j).zfill(8))
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

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_kv', self.PAGE_PREFIX + 'core_sys/images/main/tz/kv.jpg')
        self.add_to_image_list('tz_kv2', self.PAGE_PREFIX + 'core_sys/images/main/tz/kv2.jpg')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('.kv__img source[srcset]')
            for image in images:
                image_url = self.PAGE_PREFIX + image['srcset']
                if '/main/' not in image_url:
                    continue
                image_name = self.generate_image_name_from_url(image_url, 'main')
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
                    if page.isnumeric() and not self.is_content_length_in_range(image_url, more_than_amount=57000):
                        continue
                    if page == 'privilege' and not self.is_content_length_in_range(image_url, more_than_amount=80000):
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


# Seiken Gakuin no Makentsukai
class SeikenGakuinDownload(Fall2023AnimeDownload, NewsTemplate):
    title = 'Seiken Gakuin no Makentsukai'
    keywords = [title, 'The Demon Sword Master of Excalibur Academy']
    website = 'https://seikengakuin.com/'
    twitter = 'SEIKEN_MAKEN'
    hashtags = ['聖剣学院の魔剣使い', 'せまつか']
    folder_name = 'seikengakuin'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 4

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        # self.download_episode_preview_guess(print_invalid=False, download_valid=True)
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            entries = soup.select('article.entry')
            for entry in entries:
                try:
                    episode_text = ''
                    title_number_text = entry.select('.ep_title-number')[0].text
                    for c in title_number_text:
                        if c.isnumeric():
                            episode_text += c
                    episode = str(int(episode_text)).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                self.image_list = []
                images = entry.select('.thumb_img[data-src]')
                for i in range(len(images)):
                    image_url = images[i]['data-src']
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_guess(self, print_invalid=False, download_valid=False):
        if self.is_image_exists(str(self.FINAL_EPISODE).zfill(2) + '_' + str(self.IMAGES_PER_EPISODE)):
            return

        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'sgwp/wp-content/uploads/%s/%s/HP使用%s_SK%s_%s.jpg'
        current_date = datetime.now() + timedelta(hours=1)
        year = current_date.strftime('%Y')
        month = current_date.strftime('%m')
        is_successful = False
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            existing_image_name = episode + '_' + str(self.IMAGES_PER_EPISODE)
            if self.is_image_exists(existing_image_name) or self.is_image_exists(existing_image_name, folder):
                continue
            episode_success = False
            valid_urls = []
            for j in range(self.IMAGES_PER_EPISODE):
                for k in range(400):
                    image_url = template % (year, month, str(j + 1).zfill(2), episode, str(k).zfill(3))
                    if self.is_valid_url(image_url, is_image=True):
                        print('VALID - ' + image_url)
                        episode_success = True
                        valid_urls.append({'num': str(j + 1), 'url': image_url})
                        break
                    elif print_invalid:
                        print('INVALID - ' + image_url)
                if not episode_success:
                    break
            if download_valid and len(valid_urls) > 0:
                for valid_url in valid_urls:
                    image_name = episode + '_' + valid_url['num']
                    self.download_image(valid_url['url'], folder + '/' + image_name)
            if not episode_success:
                break
            is_successful = True
        if is_successful:
            print(self.__class__.__name__ + ' - Guessed correctly!')
        return is_successful

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='article.entry',
                                    date_select='.entry-date', title_select='.entry-title', id_select='a')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('.kv_img img[src]')
            for image in images:
                image_url = image['src']
                if '/imgs/' not in image_url:
                    continue
                image_name = self.generate_image_name_from_url(image_url, 'imgs')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'sgwp/wp-content/themes/seikengakuin/assets/imgs/character/chara%s.png'
        self.download_by_template(folder, template, 2, 1)

    def download_media(self):
        folder = self.create_media_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'goods/blu-ray/')
            images = soup.select('article.entry img[src]')
            self.image_list = []
            for image in images:
                image_url = image['src']
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


# Shangri-La Frontier: Kusoge Hunter, Kamige ni Idoman to su
class ShangriLaFrontierDownload(Fall2023AnimeDownload, NewsTemplate):
    title = 'Shangri-La Frontier: Kusoge Hunter, Kamige ni Idoman to su'
    keywords = [title]
    website = 'https://anime.shangrilafrontier.com/'
    twitter = 'ShanFro_Comic'
    hashtags = ['シャンフロ']
    folder_name = 'shangrilafrontier'

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
            a_tags = soup.select('nav[data-type="archive"] a[href]')
            for a_tag in a_tags:
                try:
                    episode = str(int(a_tag.text)).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                em_tag = soup.select('.story em')
                ep_soup = None
                try:
                    if int(em_tag[0].text) == int(a_tag.text):
                        ep_soup = soup
                except:
                    pass
                if ep_soup is None:
                    ep_soup = self.get_soup(a_tag['href'])
                if ep_soup is None:
                    continue
                self.image_list = []
                images = ep_soup.select('.story picture img[src]')
                for i in range(len(images)):
                    image_url = images[i]['src'].split('?')[0]
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.topics li',
                                    title_select='.ttl', date_select='.date', id_select='a', news_prefix='topics/',
                                    paging_type=0, next_page_select='.pagenation-list li', next_page_eval_index=-1,
                                    next_page_eval_index_class='is__current')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('.fv .visual source[srcset]')
            for image in images:
                image_url = image['srcset']
                if '/images/' not in image_url:
                    continue
                if image_url.startswith('/'):
                    image_url = self.PAGE_PREFIX + image_url[1:]
                image_name = self.generate_image_name_from_url(image_url, 'images')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            self.image_list = []
            images = soup.select('.chardata--inner source[srcset]')
            for image in images:
                image_url = image['srcset']
                if '/webp/' not in image_url:
                    continue
                if image_url.startswith('/'):
                    image_url = self.PAGE_PREFIX + image_url[1:]
                image_name = self.generate_image_name_from_url(image_url, 'webp')
                if not image_name.endswith('_sp'):
                    continue
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Shy
class ShyDownload(Fall2023AnimeDownload, NewsTemplate):
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
        self.download_media()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story')
            stories = soup.select('.story-episode-item a[href]')
            for story in stories:
                story_url = story['href']
                if story_url.endswith('/'):
                    story_url = story_url[:-1]
                try:
                    episode = str(int(story_url.split('/')[-1])).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                ep_soup = self.get_soup(story['href'])
                if ep_soup is None:
                    continue
                self.image_list = []
                images = ep_soup.select('.story-thumb-item img[src]')
                for i in range(len(images)):
                    image_url = images[i]['src'].split('?')[0]
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url, to_jpg=True)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

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

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('#kv>img[src]')
            for image in images:
                image_url = image['src']
                if '/img/' not in image_url:
                    continue
                image_name = self.generate_image_name_from_url(image_url, 'img')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        self.image_list = []
        self.add_to_image_list('tz_shy', self.PAGE_PREFIX + 'nE2aBbsJ/wp-content/themes/v0/assets/img/kv/shy.webp')
        self.add_to_image_list('tz_tel', self.PAGE_PREFIX + 'nE2aBbsJ/wp-content/themes/v0/assets/img/kv/tel.webp')
        self.download_image_list(folder)

        template = self.PAGE_PREFIX + 'nE2aBbsJ/wp-content/themes/v1/assets/img/character/%s/%s.png'
        for i in range(30):
            is_successful = False
            for j in ['img', 'face']:
                image_name = str(i).zfill(2) + '_' + j
                if self.is_image_exists(image_name, folder):
                    is_successful = True
                    continue
                image_url = template % (str(i), j)
                result = self.download_image(image_url, folder + '/' + image_name)
                if result != -1:
                    is_successful = True
            if not is_successful:
                break

    def download_media(self):
        folder = self.create_media_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        for page in ['tokuten', '1', '2', '3']:
            try:
                if page in processed:
                    continue
                page_url = self.PAGE_PREFIX + 'bd/'
                if page.isnumeric():
                    page_url += 'vol'
                page_url += page
                soup = self.get_soup(page_url)
                images = soup.select('#contents-main img[src]')
                self.image_list = []
                for image in images:
                    image_url = self.clear_resize_in_url(image['src'])
                    if 'noimage' in image_url or 'coming' in image_url:
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


# Sousou no Frieren
class FrierenDownload(Fall2023AnimeDownload, NewsTemplate):
    title = 'Sousou no Frieren'
    keywords = [title, "Frieren: Beyond Journey's End"]
    website = 'https://frieren-anime.jp/'
    twitter = 'Anime_Frieren'
    hashtags = ['フリーレン', 'frieren']
    folder_name = 'frieren'

    PAGE_PREFIX = website
    FINAL_EPISODE = 28
    IMAGES_PER_EPISODE = 10

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_episode_preview_external()
        self.download_episode_preview_guess(print_invalid=False, download_valid=True)
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            stories = soup.select('.storyLists__item a[href]')
            for story in stories:
                try:
                    href = story['href']
                    if href.endswith('/'):
                        href = story['href'][:-1]
                    episode = str(int(href.split('/')[-1].replace('ep', ''))).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_01'):
                    continue
                ep_url = story['href']
                if ep_url.startswith('/'):
                    ep_url = self.PAGE_PREFIX + ep_url[1:]
                ep_soup = self.get_soup(ep_url)
                if ep_soup is None:
                    continue
                self.image_list = []
                images = ep_soup.select('.storyPhotoLists img[src]')
                for i in range(len(images)):
                    image_url = self.PAGE_PREFIX + images[i]['src'][1:]
                    image_name = episode + '_' + str(i + 1).zfill(2)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='li.newsLists__item',
                                    date_select='.newsLists__time', title_select='.newsLists__title', id_select='a',
                                    a_tag_start_text_to_remove='/', a_tag_prefix=self.PAGE_PREFIX)

    def download_episode_preview_external(self):
        keywords = ['葬送のフリーレン']
        AniverseMagazineScanner(keywords, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20231010', download_id=self.download_id).run()

    def download_episode_preview_guess(self, print_invalid=False, download_valid=False):
        if self.is_image_exists(str(self.FINAL_EPISODE).zfill(2) + '_' + str(self.IMAGES_PER_EPISODE)):
            return

        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'wp-content/uploads/%s/%s/%s_%s.jpg'
        current_date = datetime.now() + timedelta(hours=1)
        year = current_date.strftime('%Y')
        month = current_date.strftime('%m')
        is_successful = False
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            existing_image_name = episode + '_01'
            if self.is_image_exists(existing_image_name) or self.is_image_exists(existing_image_name, folder):
                continue
            episode_success = False
            valid_urls = []
            for j in range(self.IMAGES_PER_EPISODE):
                k = 0
                while k < 20:
                    if k == 0:
                        append = ''
                    else:
                        append = '-' + str(k)
                    image_url = template % (year, month, str(i + 1).zfill(2), str(j + 1).zfill(2) + append)
                    if self.is_valid_url(image_url, is_image=True):
                        print('VALID - ' + image_url)
                        episode_success = True
                        valid_urls.append({'num': str(j + 1).zfill(2) + append, 'url': image_url})
                    elif print_invalid:
                        print('INVALID - ' + image_url)
                        break
                    k += 1
            if download_valid and len(valid_urls) > 0:
                for valid_url in valid_urls:
                    image_name = episode + '_' + valid_url['num']
                    self.download_image(valid_url['url'], folder + '/' + image_name)
            if not episode_success:
                break
            is_successful = True
        if is_successful:
            print(self.__class__.__name__ + ' - Guessed correctly!')
        return is_successful

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FcgQDbKaAAAEBu_?format=jpg&name=4096x4096')
        self.add_to_image_list('tz2_tw', 'https://pbs.twimg.com/media/FqqKOB3aQAMhTCs?format=jpg&name=4096x4096')
        self.add_to_image_list('index_visual', self.PAGE_PREFIX + 'assets/img/index/visual.jpg')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('.visualLists__imgWrap img[src]')
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].replace('./', '')
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        prefix = self.PAGE_PREFIX + 'assets/img/character/chara'
        templates = [
            prefix + '%s_full1.png', prefix + '%s_full2.png', prefix + '%s_full.png',
            prefix + '%s_face1.jpg', prefix + '%s_face2.jpg', prefix + '%s_face.jpg'
        ]
        self.download_by_template(folder, templates, 1, 1)

    def download_media(self):
        folder = self.create_media_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        for page in ['benefit', '1', '2', '3', '4', '5', '6', '7']:
            try:
                if page.isnumeric():
                    if page in processed:
                        continue
                    page_url = self.PAGE_PREFIX + 'bddvd/vol' + page + '/'
                else:
                    page_url = self.PAGE_PREFIX + 'bddvd/' + page + '/'
                soup = self.get_soup(page_url)
                images = soup.select('.bddvdContent img[src]')
                self.image_list = []
                for image in images:
                    image_url = self.PAGE_PREFIX + image['src'][1:].split('?')[0]
                    if '/bddvd/' not in image_url:
                        continue
                    image_name = self.extract_image_name_from_url(image_url)
                    if 'np_' in image_name:
                        continue
                    image_name = self.generate_image_name_from_url(image_url, 'bddvd')
                    self.add_to_image_list(image_name, image_url)
                if page.isnumeric():
                    if len(self.image_list) > 1:
                        processed.append(page)
                    else:
                        break
                self.download_image_list(folder)
            except Exception as e:
                self.print_exception(e, f'Blu-ray - {page}')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Spy x Family Season 2
class SpyFamily2Download(Fall2023AnimeDownload, NewsTemplate):
    title = 'Spy x Family Season 2'
    keywords = [title]
    website = 'https://spy-family.net/tvseries/'
    twitter = 'spyfamily_anime'
    hashtags = ['SPY_FAMILY', 'スパイファミリー']
    folder_name = 'spy-family2'

    website_domain = 'https://spy-family.net/'
    PAGE_PREFIX = website
    FIRST_EPISODE = 26
    FINAL_EPISODE = 37  # 25 + 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_media()

    def download_episode_preview(self):
        image_url_template = self.PAGE_PREFIX + 'assets/img/episodes/episode%s_%s.jpg'
        for i in range(self.FIRST_EPISODE, self.FINAL_EPISODE + 1, 1):
            for j in range(self.IMAGES_PER_EPISODE):
                image_name = str(i).zfill(2) + '_' + str(j + 1)
                if not self.is_image_exists(image_name):
                    image_url = image_url_template % (str(i), str(j + 1))
                    result = self.download_image(image_url, self.base_folder + '/' + image_name)
                    if result == -1:
                        return

    def download_news(self):
        self.download_template_news(page_prefix=self.website_domain, article_select='li.newsLists__item',
                                    date_select='time', title_select='.newsLists--title', id_select='a',
                                    paging_type=3, paging_suffix='?paged=%s', next_page_select='.wp-pagenavi *',
                                    next_page_eval_index_class='current', next_page_eval_index=-1,
                                    stop_date='2022.12.17')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('top_mv_p_s2', self.PAGE_PREFIX + 'assets/img/top/mv_p_s2.jpg')
        self.download_image_list(folder)

    def download_media(self):
        folder = self.create_media_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        for page in ['tokuten', '1', '2', '3']:
            try:
                if page.isnumeric() and str(page) in processed:
                    continue
                page_url = self.PAGE_PREFIX + 'bddvd/bddvd'
                if not page.isnumeric():
                    page_url += '_'
                page_url += page + '.php'
                soup = self.get_soup(page_url)
                images = soup.select('.bddvdDetailWrap img[src]')
                image_count = 0
                self.image_list = []
                for image in images:
                    image_url = image['src']
                    if 'nowprinting' in image_url or '/bddvd/' not in image_url:
                        continue
                    if image_url.startswith('../'):
                        image_url = self.PAGE_PREFIX + image_url.replace('../', '')
                    image_name = self.generate_image_name_from_url(image_url, 'bddvd')
                    self.add_to_image_list(image_name, image_url)
                if page.isnumeric():
                    if image_count > 0:
                        processed.append(str(page))
                    else:
                        break
                self.download_image_list(folder)
            except Exception as e:
                self.print_exception(e, f'Blu-ray - {page}')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Tate no Yuusha no Nariagari Season 3
class TateNoYuusha3Download(Fall2023AnimeDownload):
    title = "Tate no Yuusha no Nariagari Season 3"
    keywords = [title, "The Rising of the Shield Hero", "3rd"]
    website = "http://shieldhero-anime.jp/"
    twitter = 'shieldheroanime'
    hashtags = ['shieldhero', '盾の勇者の成り上がり']
    folder_name = 'tate-no-yuusha3'

    PAGE_PREFIX = website + '/3rd'
    FINAL_EPISODE = 13
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        soup = self.download_key_visual()
        soup = self.download_character(soup)
        self.download_media(soup)

    def download_episode_preview(self):
        try:
            template = self.website + 'assets/img/3rd/story/ss/ep%s/%s.jpg'
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
                    if date.startswith('2022.07') or (news_obj
                                                      and (news_obj['id'] == article_id or date < news_obj['date'])):
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

    def download_key_visual(self, soup=None):
        folder = self.create_key_visual_directory()
        try:
            if soup is None:
                soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.fvimgslide source[srcset]')
            self.image_list = []
            for image in images:
                if '/fv/' not in image['srcset']:
                    continue
                image_name = self.generate_image_name_from_url(image['srcset'], 'fv')
                image_url = self.PAGE_PREFIX + image['srcset'].split('?')[0][1:]
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
                if '/webp/' not in image['srcset']:
                    continue
                image_name = self.generate_image_name_from_url(image['srcset'], 'webp')
                image_url = self.PAGE_PREFIX + image['srcset'].split('?')[0][1:]
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
            images = soup.select('.bddata source[srcset]')
            self.image_list = []
            for image in images:
                if '/bd/webp/' not in image['srcset']:
                    continue
                image_name = self.generate_image_name_from_url(image['srcset'], 'webp')
                if image_name in ['np_wide', 'np_slim']:
                    continue
                image_url = self.PAGE_PREFIX + image['srcset'].split('?')[0][1:]
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')
        return soup


# Tearmoon Teikoku Monogatari
class TearmoonDownload(Fall2023AnimeDownload, NewsTemplate):
    title = 'Tearmoon Teikoku Monogatari'
    keywords = [title, 'Tearmoon Empire']
    website = 'https://tearmoon-pr.com/'
    twitter = 'tearmoon_pr'
    hashtags = 'ティアムーン'
    folder_name = 'tearmoon'

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
            story_prefix = self.PAGE_PREFIX + 'story/'
            soup = self.get_soup(story_prefix)
            stories = soup.select('nav[data-type="archive"] a[href]')
            for story in stories:
                try:
                    episode = str(int(story.text)).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                ep_soup = self.get_soup(story['href'])
                if ep_soup is None:
                    continue
                self.image_list = []
                images = ep_soup.select('.ssimg img[src]')
                for i in range(len(images)):
                    image_name = episode + '_' + str(i + 1)
                    image_url = images[i]['src']
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='ul.news--list li',
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
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/Fb9eKCbaIAAj66L?format=jpg&name=large')
        self.download_image_list(folder)

        template = self.PAGE_PREFIX + '_assets/images/top/fv/webp/fv_%s_pc.webp'
        self.download_by_template(folder, template, 3, 1)

    def download_character(self):
        folder = self.create_character_directory()
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

    def download_media(self):
        folder = self.create_media_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        for page in ['store1', 'store2', 'bd1', 'bd2', 'bd3', 'bd4']:
            try:
                if page != 'store1' and page in processed:
                    continue
                soup = self.get_soup(self.PAGE_PREFIX + 'bd/' + page + '/')
                images = soup.select('.bd img[src]')
                self.image_list = []
                for image in images:
                    image_url = image['src']
                    if not image_url.startswith('http'):
                        if image_url.startswith('/'):
                            image_url = self.PAGE_PREFIX + image_url[1:]
                        else:
                            continue
                    image_name = self.extract_image_name_from_url(image_url)
                    if image_name.startswith('np_'):
                        continue
                    self.add_to_image_list(image_name, image_url)
                if page != 'store1':
                    if len(self.image_list) > 0:
                        processed.append(page)
                    else:
                        break
                self.download_image_list(folder)
            except Exception as e:
                self.print_exception(e, f'Blu-ray - {page}')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Toaru Ossan no VRMMO Katsudouki
class ToaruOssanDownload(Fall2023AnimeDownload, NewsTemplate):
    title = 'Toaru Ossan no VRMMO Katsudouki'
    keywords = [title, "A Playthrough of a Certain Dude’s VRMMO Life"]
    website = 'https://toaru-ossan.com/'
    twitter = 'toaru_ossan_pr'
    hashtags = ['とあるおっさん']
    folder_name = 'toaruossan'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 9

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
        news_url = self.PAGE_PREFIX + 'news/'
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='#news li',
                                    date_select='time', title_select='p', id_select='a', a_tag_prefix=news_url,
                                    a_tag_start_text_to_remove='../')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        template = self.PAGE_PREFIX + 'assets/images/top/mainimg_%s.jpg'
        self.download_by_template(folder, template, 2, 0)

    def download_character(self):
        folder = self.create_character_directory()
        prefix = self.PAGE_PREFIX + 'assets/images/character/'
        templates = [prefix + 'img_%s.png', prefix + 'face_%s.png']
        self.download_by_template(folder, templates, 2, 1)

    def download_media(self):
        folder = self.create_media_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'blu-ray')
            self.image_list = []
            images = soup.select('.inner img[src]')
            for image in images:
                if '/blu-ray/' not in image['src'] or 'nowprinting' in image['src']:
                    continue
                image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                image_name = self.generate_image_name_from_url(image_url, 'blu-ray')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


# Undead Unluck
class UndeadUnluckDownload(Fall2023AnimeDownload, NewsTemplate):
    title = 'Undead Unluck'
    keywords = [title]
    website = 'https://undead-unluck.net/'
    twitter = 'undeadunluck_an'
    hashtags = ['アンデラ']
    folder_name = 'undeadunluck'

    PAGE_PREFIX = website
    FINAL_EPISODE = 24
    IMAGES_PER_EPISODE = 4

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        try:
            # assets/img/episode/ep01/ep01_img4.jpg
            template = self.PAGE_PREFIX + 'assets/img/episode/ep%s/ep%s_img%s.jpg'
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (episode, episode, str(j + 1))
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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='li.newsList',
                                    date_select='.newsList_date', title_select='.newsList_title', id_select='a',
                                    a_tag_start_text_to_remove='./', a_tag_prefix=news_url)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.visualLists img[src]')
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
        template = self.PAGE_PREFIX + 'assets/img/top/character/character%s_main.png'
        self.download_by_template(folder, template, 1, 1)


# Under Ninja
class UnderNinjaDownload(Fall2023AnimeDownload, NewsTemplate):
    title = 'Under Ninja'
    keywords = [title]
    website = 'https://under-ninja.jp/'
    twitter = 'UNDERNINJAanime'
    hashtags = ['アンダーニンジャ']
    folder_name = 'underninja'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 8

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_episode_preview_guess(print_invalid=False, download_valid=True)
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            stories = soup.select('.episode-item[id]')
            for story in stories:
                try:
                    episode = str(story['id'].replace('ep', '')).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                self.image_list = []
                images = story.select('.change-scale img[src]')
                for i in range(len(images)):
                    image_url = images[i]['src']
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url, to_jpg=True)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-list li',
                                    date_select='.news-date', title_select='.news-title', id_select='a',
                                    next_page_select='.pagination-btn.next')

    def download_episode_preview_guess(self, print_invalid=False, download_valid=False):
        if self.is_image_exists(str(self.FINAL_EPISODE).zfill(2) + '_' + str(self.IMAGES_PER_EPISODE)):
            return

        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'wp-content/uploads/%s/%s/ep%s_%s.'
        templates = [template + 'png', template + 'jpg']
        current_date = datetime.now() + timedelta(hours=1)
        year = current_date.strftime('%Y')
        month = current_date.strftime('%m')
        is_successful = False
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            existing_image_name = episode + '_' + str(self.IMAGES_PER_EPISODE)
            if self.is_image_exists(existing_image_name) or self.is_image_exists(existing_image_name, folder):
                continue
            episode_success = False
            valid_urls = []
            for j in range(self.IMAGES_PER_EPISODE):
                for tem in templates:
                    image_url = tem % (year, month, str(i + 1), str(j + 1).zfill(2))
                    if self.is_valid_url(image_url, is_image=True):
                        print('VALID - ' + image_url)
                        episode_success = True
                        valid_urls.append({'num': str(j + 1), 'url': image_url})
                        break
                    elif print_invalid:
                        print('INVALID - ' + image_url)
            if download_valid and len(valid_urls) > 0:
                for valid_url in valid_urls:
                    image_name = episode + '_' + valid_url['num']
                    self.download_image(valid_url['url'], folder + '/' + image_name)
            if not episode_success:
                break
            is_successful = True
        if is_successful:
            print(self.__class__.__name__ + ' - Guessed correctly!')
        return is_successful

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('kv', self.PAGE_PREFIX + 'wp-content/uploads/2023/08/UNkeycopy0817-scaled.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            pages = soup.select('.character-list-item a[href]')
            for page in pages:
                chara_url = page['href']
                if chara_url.endswith('/'):
                    chara_url = chara_url[:-1]
                name = chara_url.split('/')[-1]
                if name in processed:
                    continue
                chara_soup = self.get_soup(chara_url)
                images = chara_soup.select('.character-detail__inner img[src]')
                self.image_list = []
                for image in images:
                    image_url = image['src']
                    image_name = self.extract_image_name_from_url(image_url)
                    if 'shadow' in image_name:
                        continue
                    self.add_to_image_list(image_name, image_url)
                if len(self.image_list) > 0:
                    processed.append(name)
                self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Watashi no Oshi wa Akuyaku Reijou.
class WataoshiDownload(Fall2023AnimeDownload, NewsTemplate):
    title = 'Watashi no Oshi wa Akuyaku Reijou.'
    keywords = [title, 'I\'m in Love with the Villainess']
    website = 'https://wataoshi-anime.com/'
    twitter = 'wataoshi_anime'
    hashtags = ['わたおし', 'wataoshi', 'ILTV']
    folder_name = 'wataoshi'

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
            template = self.PAGE_PREFIX + 'assets/images/story/%s_%s.jpg'
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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.inner.list li',
                                    date_select='time', title_select='p', id_select='a', a_tag_prefix=self.PAGE_PREFIX,
                                    a_tag_start_text_to_remove='../')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        # self.image_list = []
        # self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/Fj120y9VIAAx9Jp?format=jpg&name=medium')
        # self.add_to_image_list('kv1', 'https://pbs.twimg.com/media/Fv6DLpYaQAACtjt?format=jpg&name=large')
        # self.add_to_image_list('img_visual1.jpg', self.PAGE_PREFIX + 'images/img_visual1.jpg')
        # self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.mainimg .swiper-slide img[src]')
            for image in images:
                if '/top/' not in image['src']:
                    continue
                image_url = self.PAGE_PREFIX + image['src'][1:]
                image_name = self.generate_image_name_from_url(image_url, 'top')
                if 'img' not in image_name:
                    continue
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        prefix = self.PAGE_PREFIX + 'assets/images/character/'
        templates = [prefix + 'chara_%s.png', prefix + 'face_%s.png']
        self.download_by_template(folder, templates, 2, 1)

    def download_media(self):
        folder = self.create_media_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'blu-ray')
            self.image_list = []
            images = soup.select('.inner img[src]')
            for image in images:
                if '/blu-ray/' not in image['src']:
                    continue
                image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                image_name = self.generate_image_name_from_url(image_url, 'blu-ray')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')

        # Voices
        voice_folder = folder + '/voice'
        if not os.path.exists(voice_folder):
            os.makedirs(voice_folder)
        for i in range(99):
            audio_name = f'chara_{str(i + 1).zfill(2)}.mp3'
            audio_url = self.PAGE_PREFIX + 'assets/mp3/' + audio_name
            result = self.download_content(audio_url, voice_folder + '/' + audio_name)
            if result == -1:
                break
