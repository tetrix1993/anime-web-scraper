import os
import requests
from anime.main_download import MainDownload, NewsTemplate, NewsTemplate2, NewsTemplate3
from scan import AniverseMagazineScanner, MocaNewsScanner
from datetime import datetime


# Aharen-san wa Hakarenai https://aharen-pr.com/ #阿波連さん @aharen_pr
# Deaimon https://deaimon.jp/ #であいもん #deaimon @deaimon_anime
# Gaikotsu Kishi-sama, Tadaima Isekai e Odekakechuu https://skeleton-knight.com/ #骸骨騎士様 @gaikotsukishi
# Honzuki S3 http://booklove-anime.jp/story/ #本好きの下剋上 @anime_booklove
# Kaguya-sama wa Kokurasetai: Ultra Romantic https://kaguya.love/ #かぐや様 @anime_kaguya
# Kakkou no Iinazuke https://cuckoos-anime.com/ #カッコウの許嫁 @cuckoo_anime
# Kawaii dake ja Nai Shikimori-san https://shikimori-anime.com/ #式守さん @anime_shikimori
# Kingdom 4th Season https://kingdom-anime.com/story/ #キングダム @kingdom_animePR
# Koi wa Sekai Seifuku no Ato de https://koiseka-anime.com/ #恋せか @koiseka_anime
# Kono Healer, Mendokusai https://kono-healer-anime.com/ #このヒーラー #kono_healer @kono_healer
# Kunoichi Tsubaki no Mune no Uchi https://kunoichi-tsubaki.com/ #くノ一ツバキ @tsubaki_anime
# Machikado Mazoku: 2-choume http://www.tbs.co.jp/anime/machikado/ #まちカドまぞく #MachikadoMazoku @machikado_staff
# Mahoutsukai Reimeiki https://www.tbs.co.jp/anime/reimeiki/ #魔法使い黎明期 @reimeiki_pr
# Otome Game Sekai wa Mob ni Kibishii Sekai desu https://mobseka.com/ #モブせか #mobseka @mobseka_anime
# Paripi Koumei https://paripikoumei-anime.com/ #パリピ孔明 @paripikoumei_PR
# Rikei ga Koi ni Ochita no de Shoumei shitemita. Heart #リケ恋 #りけこい #rikekoi @rikeigakoini
# RPG Fudousan https://rpg-rs.jp/ #RPG不動産 @rpgrs_anime
# Shachiku-san wa Youjo Yuurei ni Iyasaretai. https://shachikusan.com/ #しゃちされたい @shachisaretai
# Shijou Saikyou no Daimaou, Murabito A ni Tensei suru https://murabito-a-anime.com/ #村人Aに転生 @murabitoA_anime
# Shokei Shoujo no Virgin Road http://virgin-road.com/ #処刑少女 #shokei_anime @VirginroadAnime
# Spy x Family https://spy-family.net/ #SPY_FAMILY #スパイファミリー @spyfamily_anime
# Summertime Render https://summertime-anime.com/ #サマータイムレンダ #サマレン @summertime_PR
# Tate no Yuusha S2 http://shieldhero-anime.jp/2nd/ #shieldhero #盾の勇者の成り上がり @shieldheroanime
# Yuusha, Yamemasu https://yuuyame.com/ #yuuyame #勇やめ @yuuyame_anime


# Summer 2022 Anime
class Spring2022AnimeDownload(MainDownload):
    season = "2022-2"
    season_name = "Spring 2022"
    folder_name = '2022-2'

    def __init__(self):
        super().__init__()


# Aharen-san wa Hakarenai
class AharensanDownload(Spring2022AnimeDownload, NewsTemplate):
    title = 'Aharen-san wa Hakarenai'
    keywords = [title]
    website = 'https://aharen-pr.com/1st/'
    twitter = 'aharen_pr'
    hashtags = '阿波連さん'
    folder_name = 'aharensan'

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
            a_tags = soup.select('nav.story--nav li a[href]')
            for a_tag in a_tags:
                try:
                    if len(a_tag.text.strip()) == 0:
                        continue
                    episode = str(int(a_tag.text.strip())).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                ep_soup = self.get_soup(a_tag['href'])
                if ep_soup is not None:
                    images = ep_soup.select('.story--ss__slider img[src]')
                    self.image_list = []
                    for i in range(len(images)):
                        image_url = images[i]['src']
                        image_name = episode + '_' + str(i + 1)
                        self.add_to_image_list(image_name, image_url)
                    self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.md-li__news li',
                                    date_select='time', title_select='.ttl', id_select='a', date_separator='.&nbsp;',
                                    next_page_select='ul.pagenation-list li',
                                    next_page_eval_index_class='is__current', next_page_eval_index=-1)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz', self.PAGE_PREFIX + 'wp/wp-content/themes/aharen-teaser/_assets/images/kv/kv_pc.jpg')
        # self.add_to_image_list('tz_2', self.PAGE_PREFIX + 'wp/wp-content/uploads/2021/07/阿波連さんははかれない_ティザービジュアル.jpg')
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/E7ohr6yVIAEQI6z?format=jpg&name=large')
        self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/FFqAiWPaAAA-7gz?format=jpg&name=large')
        # self.add_to_image_list('kv1', self.PAGE_PREFIX + 'wp/wp-content/uploads/2021/12/阿波連さん_第1弾KV.jpg')
        self.add_to_image_list('kv2_pc', self.PAGE_PREFIX + 'wp/wp-content/themes/aharen-teaser/_assets/images/kv/kv2_pc.jpg')
        self.add_to_image_list('kv2', self.PAGE_PREFIX + 'wp/wp-content/uploads/2022/01/阿波連さん第2弾KV_220117.jpg')
        self.download_image_list(folder)

        template = self.PAGE_PREFIX + 'wp/wp-content/themes/aharen-main/_assets/images/top/fv_%s_pc.png'
        self.download_by_template(folder, template, 3, 1)

    def download_character(self):
        folder = self.create_character_directory()
        self.image_list = []
        template = self.PAGE_PREFIX + 'wp/wp-content/themes/aharen-teaser/_assets/images/char/main/%s_pc.png'
        for chara in ['aharen', 'raido', 'oshiro', 'tobaru']:
            image_url = template % chara
            image_name = 'tz_' + chara
            self.add_to_image_list(image_name, image_url)
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            images = soup.select('div.chardata img')
            for image in images:
                if image.has_attr('src'):
                    image_url = image['src']
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
        except Exception as e:
            self.print_exception(e, 'Character')
        self.download_image_list(folder)

    def download_media(self):
        folder = self.create_media_directory()
        try:
            for i in range(1, 4, 1):
                url = self.PAGE_PREFIX + 'bd/vol' + str(i) + '/'
                image_name = 'bdvol' + str(i)
                if self.is_image_exists(image_name, folder):
                    continue
                soup = self.get_soup(url)
                if soup is not None:
                    images = soup.select('.bd--main__block img[src]')
                    if len(images) > 0:
                        image_url = images[0]['src']
                        if image_url.endswith('np_bd.png'):
                            break
                        self.download_image(image_url, folder + '/' + image_name)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


# Deaimon
class DeaimonDownload(Spring2022AnimeDownload, NewsTemplate2):
    title = 'Deaimon'
    keywords = [title]
    website = 'https://deaimon.jp/'
    twitter = 'deaimon_anime'
    hashtags = ['であいもん', 'deaimon']
    folder_name = 'deaimon'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 8

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
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            stories = soup.select('#ContentsListUnit02 a[href]')
            for story in stories:
                try:
                    episode = str(int(story['href'].split('/')[-1].split('.html')[0])).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                ep_soup = self.get_soup(self.PAGE_PREFIX + story['href'].replace('../', ''))
                if ep_soup is not None:
                    images = ep_soup.select('.img_link img[src]')
                    self.image_list = []
                    for i in range(len(images)):
                        image_url = self.PAGE_PREFIX + images[i]['src'].replace('../', '').split('?')[0]
                        image_name = episode + '_' + str(i + 1)
                        self.add_to_image_list(image_name, image_url)
                    self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_external(self):
        jp_title = 'であいもん'
        AniverseMagazineScanner(jp_title, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20220331', download_id=self.download_id).run()

    def download_episode_preview_guess(self):
        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'core_sys/images/contents/%s/block/%s/%s.jpg'
        is_successful = False
        for i in range(1, self.FINAL_EPISODE + 1, 1):
            episode = str(i).zfill(2)
            is_success = False
            if self.is_image_exists(episode + '_1'):
                continue
            first = 21 + (i - 1)
            second = 28 + 3 * (i - 1)
            third = 30 + 6 * (i - 1)
            third2 = 104 + 2 * (i - 1)
            for j in range(self.IMAGES_PER_EPISODE):
                if j < 6:
                    third_ = third + j
                elif i == 4:
                    third_ = third2 + j - 4
                elif i == 5:
                    third_ = third2 + j - 8
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
        image_prefix = self.PAGE_PREFIX + 'core_sys/images/'
        self.add_to_image_list('kv_tw', 'https://pbs.twimg.com/media/E_T2HaPUUAIwv3-?format=jpg&name=4096x4096')
        self.add_to_image_list('kv_wide', image_prefix + 'main/tz/kv.webp')
        # self.add_to_image_list('kv', image_prefix + 'news/00000002/block/00000009/00000003.jpg')
        self.add_to_image_list('kv_sp', image_prefix + 'main/tz/kv_sp.png')
        self.add_to_image_list('kv2', image_prefix + 'main/top/kv2.webp')
        self.add_to_image_list('kv2_1', image_prefix + 'news/00000016/block/00000035/00000021.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'chara/')
            chara_links = soup.select('#ContentsListUnit01 a')
            for link in chara_links:
                if link.has_attr('href') and link['href'].startswith('../') and '/chara/' in link['href']:
                    if link['href'].endswith('.html'):
                        chara_name = link['href'].split('/')[-1].split('.html')[0]
                    else:
                        continue
                    if chara_name in processed:
                        continue
                    if chara_name == 'index':
                        chara_soup = soup
                    else:
                        chara_soup = self.get_soup(self.PAGE_PREFIX + link['href'].replace('../', ''))
                    if chara_soup is not None:
                        images = chara_soup.select('.charaStand img, .charaFace img')
                        self.image_list = []
                        for image in images:
                            if image.has_attr('src'):
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
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'bd/')
            images = soup.select('#cms_block img[src]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].replace('../', '').split('?')[0].replace('sn_', '')
                split1 = image_url.split('/')
                if len(split1) > 0:
                    image_name = split1[-1].split('.')[0]
                    if self.is_image_exists(image_name, folder) or image_name == 'music_np'\
                            or self.is_matching_content_length(image_url, [94695, 73412]):
                        continue
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


# Gaikotsu Kishi-sama, Tadaima Isekai e Odekakechuu
class GaikotsuKishiDownload(Spring2022AnimeDownload, NewsTemplate):
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
        self.download_news()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story')
            a_tags = soup.select('ol.switch a[href]')
            for a_tag in reversed(a_tags):
                try:
                    episode = str(int(a_tag.text.strip().replace('第', '').replace('話', ''))).zfill(2)
                except:
                    continue
                ep_soup = self.get_soup(a_tag['href'])
                if ep_soup is not None:
                    images = ep_soup.select('#story_cont img[src]')
                    self.image_list = []
                    for i in range(len(images)):
                        image_url = self.clear_resize_in_url(images[i]['src'])
                        image_name = episode + '_' + str(i + 1)
                        self.add_to_image_list(image_name, image_url)
                    self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        news_prefix = self.PAGE_PREFIX + 'news/'
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='ol.frames_inner li',
                                    date_select='span', title_select='span:nth-child(2)', id_select='a',
                                    a_tag_prefix=news_prefix)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('kv', 'https://aniverse-mag.com/wp-content/uploads/2021/04/key_visual.jpg')
        self.add_to_image_list('kv02b', self.PAGE_PREFIX + 'img/kv02b.jpg')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('ul.slide img[src]')
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
        self.image_list = []
        self.add_to_image_list('arc', self.PAGE_PREFIX + 'img/arc.png')
        self.add_to_image_list('arian', self.PAGE_PREFIX + 'img/arian.jpg')
        self.download_image_list(folder)

        chara_prefix = self.PAGE_PREFIX + 'character/'
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        try:
            soup = self.get_soup(chara_prefix)
            a_tags = soup.select('li.anim a[href]')
            for a_tag in a_tags:
                if len(a_tag['href']) > 0:
                    href = a_tag['href']
                    if href.startswith('cc.php'):
                        images = a_tag.select('img[src]')
                        for image in images:
                            image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                            image_name = self.extract_image_name_from_url(image_url)
                            self.add_to_image_list(image_name, image_url)
                        self.download_image_list(folder)
                        continue
                    page_name = href.replace('.php', '')
                    if page_name in processed:
                        continue
                    chara_soup = self.get_soup(chara_prefix + href)
                    if chara_soup:
                        self.image_list = []
                        main_img = chara_soup.select('div.continner figure img[src]')
                        if len(main_img) > 0:
                            self.add_to_image_list(page_name, self.PAGE_PREFIX + main_img[0]['src'].replace('../', ''))
                        images = chara_soup.select('div.continner ol img[src]')
                        for image in images:
                            image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                            image_name = page_name + '_' + self.extract_image_name_from_url(image_url)
                            self.add_to_image_list(image_name, image_url)
                        if len(self.image_list) > 0:
                            processed.append(page_name)
                        self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')
        self.create_cache_file(cache_filepath, processed, num_processed)

    def download_media(self):
        folder = self.create_media_directory()
        self.download_by_template(folder, self.PAGE_PREFIX + 'img/snap%s.jpg', 1, 1, 4)


# Honzuki no Gekokujou: Shisho ni Naru Tame ni wa Shudan wo Erandeiraremasen 3rd Season
class Honzuki3Download(Spring2022AnimeDownload, NewsTemplate):
    title = "Honzuki no Gekokujou: Shisho ni Naru Tame ni wa Shudan wo Erandeiraremasen 3rd Season"
    keywords = [title, "Ascendance of a Bookworm"]
    website = 'http://booklove-anime.jp/'
    twitter = 'anime_booklove'
    hashtags = '本好きの下剋上'
    folder_name = 'honzuki3'

    PAGE_PREFIX = website
    FIRST_EPISODE = 27
    FINAL_EPISODE = 40

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_episode_preview_external()
        self.download_episode_preview_guess()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            box_stories = soup.select('#third div.box_story')
            for box_story in box_stories:
                if box_story.has_attr('class') and box_story['class'][0].startswith('storyNo'):
                    try:
                        episode = str(int(box_story['class'][0][7:].strip())).zfill(2)
                    except:
                        continue
                    if int(episode) < self.FIRST_EPISODE or self.is_image_exists(episode + '_1'):
                        continue
                    images = box_story.select('ul.img_thum img')
                    self.image_list = []
                    for i in range(len(images)):
                        if images[i].has_attr('src'):
                            image_url = self.PAGE_PREFIX + images[i]['src'].split('?')[0].replace('../', '')
                            image_name = episode + '_' + str(i + 1)
                            self.add_to_image_list(image_name, image_url)
                    self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='ol.list_news li',
                                    date_select='time', title_select='p.ttl', id_select='a')

    def download_episode_preview_guess(self):
        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'img/story/ep%s/img%s.jpg'
        try:
            for i in range(self.FIRST_EPISODE, self.FINAL_EPISODE + 1, 1):
                episode = str(i).zfill(2)
                if self.is_image_exists(episode + '_1'):
                    continue
                img_template = template % (episode, '%s')
                if not self.download_by_template(folder, img_template, 2, 1, end=6, prefix=episode + '_'):
                    break
        except Exception as e:
            self.print_exception(e, 'Guess')

    def download_episode_preview_external(self):
        jp_title = '本好きの下剋上'
        AniverseMagazineScanner(jp_title, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20220402', download_id=self.download_id).run()

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz', self.PAGE_PREFIX + 'news/wp/wp-content/uploads/2021/08/「本好きの下剋上」ティザービジュアル（ロゴ入り）軽.jpg')
        self.download_image_list(folder)


# Kaguya-sama wa Kokurasetai: Ultra Romantic
class Kaguyasama3Download(Spring2022AnimeDownload, NewsTemplate):
    title = "Kaguya-sama wa Kokurasetai: Ultra Romantic"
    keywords = [title, "Kaguya", "Kaguyasama", "Kaguya-sama: Love is War 3rd Season"]
    website = 'https://kaguya.love/3rd/'
    twitter = 'anime_kaguya'
    hashtags = 'かぐや様'
    folder_name = 'kaguya-sama3'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_media()

    def download_episode_preview(self):
        story_url = self.PAGE_PREFIX + 'story/'
        try:
            soup = self.get_soup(story_url)
            story_list = soup.select('.nav-story_list')
            if len(story_list) > 0:
                stories = story_list[0].select('li')
                for story in stories:
                    span = story.select('span')
                    try:
                        ep_num = int(span[0].text)
                        if ep_num < 1:
                            continue
                        episode = str(ep_num).zfill(2)
                    except:
                        continue
                    if self.is_image_exists(episode + '_1'):
                        continue
                    if story.has_attr('class') and 'active' in story['class']:
                        ep_soup = soup
                    else:
                        a_tags = story.select('a[href]')
                        if len(a_tags) < 1:
                            continue
                        ep_soup = self.get_soup(self.PAGE_PREFIX + a_tags[0]['href'][1:])
                    if ep_soup is not None:
                        images = ep_soup.select('.p-story__scene-item img[src]')
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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='li.c-news_list__item',
                                    title_select='div.c-news_list__ttl', date_select='div.c-news_list__date',
                                    id_select='a', a_tag_prefix=news_url, paging_type=1, stop_date='2021.10.16',
                                    date_func=lambda x: x[0:4] + '.' + x[5:].replace('/', '.'),
                                    next_page_select='div.c-pagination__nav-button.-next',
                                    next_page_eval_index_class='is-disabled', next_page_eval_index=-1)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        # self.add_to_image_list('tz', self.PAGE_PREFIX + 'assets/3rd/t/img/top/main/img_main.jpg')
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FCKDRzxVkAAIwMv?format=jpg&name=4096x4096')
        self.add_to_image_list('aprilfools', 'https://aniverse-mag.com/wp-content/uploads/2022/03/7502043a5b64c558b0144f7dfdeb289f.jpg')
        self.download_image_list(folder)

        for i in range(10):
            image_url = self.PAGE_PREFIX + 'assets/3rd/t/img/top/main/img_main'
            image_name = 'img_main'
            if i > 0:
                image_url += f'_{str(i + 1).zfill(2)}'
                image_name += f'_{str(i + 1).zfill(2)}'
            image_url += '.jpg'
            if self.is_image_exists(image_name, folder):
                self.download_image_with_different_length(image_url, image_name, 'old', folder)
            else:
                result = self.download_image(image_url, folder + '/' + image_name)
                if result == -1:
                    break

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.p-hero__visual img[src]')
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].replace('./', '')
                image_name = self.extract_image_name_from_url(image_url)
                if self.is_image_exists(image_name, folder):
                    self.download_image_with_different_length(image_url, image_name, 'old', folder)
                else:
                    result = self.download_image(image_url, folder + '/' + image_name)
                    if result == -1:
                        break
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_media(self):
        folder = self.create_media_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        try:
            bd_prefix = self.PAGE_PREFIX + 'bddvd/'
            for i in range(1, 7, 1):
                if i > 1:
                    if str(i) in processed:
                        continue
                    bd_url = bd_prefix + str(i).zfill(2) + '.html'
                else:
                    bd_url = bd_prefix
                soup = self.get_soup(bd_url)
                if soup is not None:
                    if i == 1:
                        images = soup.select('.p-bddvd img[src]')
                    else:
                        images = soup.select('.p-bddvd__info img[src]')
                    self.image_list = []
                    for image in images:
                        image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                        image_name = self.extract_image_name_from_url(image_url)
                        if image_name == 'img_np' or image_name == 'img_jk':
                            continue
                        self.add_to_image_list(image_name, image_url)
                    if i > 1:
                        if len(self.image_list) > 0:
                            processed.append(str(i))
                        else:
                            break
                    self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Kakkou no Iinazuke
class KakkounoIinazukeDownload(Spring2022AnimeDownload, NewsTemplate3):
    title = 'Kakkou no Iinazuke'
    keywords = [title, 'A Couple of Cuckoos']
    website = 'https://cuckoos-anime.com/season1/'
    twitter = 'cuckoo_anime'
    hashtags = 'カッコウの許嫁'
    folder_name = 'kakkou-no-iinazuke'

    PAGE_PREFIX = website
    FINAL_EPISODE = 24
    IMAGES_PER_EPISODE = 6

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
        # YouTube thumbnails
        yt_folder = self.create_custom_directory('yt')  # YouTube thumbnails
        yt_images = os.listdir(yt_folder)
        yt_episodes = ['01']
        for yt_image in yt_images:
            if os.path.isfile(yt_folder + '/' + yt_image) and yt_image.endswith('.jpg') \
                    and yt_image[0:2].isnumeric() and yt_image[2] == '_':
                yt_episodes.append(yt_image[0:2])
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            story_divs = soup.select('.story-data')
            for story_div in story_divs:
                ep_no_span = story_div.select('h3.ep-no span')
                if len(ep_no_span) == 0:
                    continue
                try:
                    ep_num = str(int(ep_no_span[0].text.strip())).zfill(2)
                except:
                    continue
                if ep_num in yt_episodes:
                    continue
                yt_link = story_div.select('.ep-trailer-btn a[href]')
                if len(yt_link) == 0 or 'www.youtube.com/embed/' not in yt_link[0]['href']:
                    continue
                yt_id = yt_link[0]['href'].split('?')[0].split('/')[-1].strip()
                if len(yt_id) > 0:
                    yt_image_url = f'https://img.youtube.com/vi/{yt_id}/maxresdefault.jpg'
                    self.download_image(yt_image_url, f'{yt_folder}/{ep_num}_{yt_id}')
        except Exception as e:
            self.print_exception(e, 'YouTube thumbnails')

        base_template = self.PAGE_PREFIX + 'assets/story/%s/%s.'
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1'):
                continue
            template = base_template % (str(i + 1), '%s')
            templates = [template + 'jpg', template + 'png']
            for j in range(1, self.IMAGES_PER_EPISODE + 1, 1):
                is_successful = False
                for t in templates:
                    image_url = t % str(j)
                    image_name = episode + '_' + str(j)
                    result = self.download_image(image_url, self.base_folder + '/' + image_name)
                    if result == -1:
                        continue
                    is_successful = True
                if not is_successful:
                    return

    def download_news(self):
        self.download_template_news(self.PAGE_PREFIX)

    def download_episode_preview_external(self):
        jp_title = 'カッコウの許嫁'
        AniverseMagazineScanner(jp_title, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20220414', prefix='', suffix='羽', download_id=self.download_id).run()

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        template = self.PAGE_PREFIX + 'assets/news/kv%s.jpg'
        self.download_by_template(folder, template, 1, 1)

        for i in range(20):
            image_url = self.PAGE_PREFIX + f'assets/top/main-t{i + 1}/vis.jpg'
            result = self.download_image(image_url, f'{folder}/vis{i + 1}')
            if result == -1:
                break

        self.image_list = []
        # self.add_to_image_list('2022-nenga', self.PAGE_PREFIX + 'assets/top/2022-nenga.jpg')
        self.add_to_image_list('2022-nenga_tw', 'https://pbs.twimg.com/media/FH4LR7HaAAAg0u2?format=jpg&name=4096x4096')
        self.add_to_image_list('2022-stvd', self.PAGE_PREFIX + 'assets/top/2022-stvd.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'assets/top/character/c%s.png'
        self.download_by_template(folder, template, 1)

    def download_media(self):
        folder = self.create_media_directory()
        self.image_list = []
        valentine_template = 'https://aniverse-mag.com/wp-content/uploads/2022/02/%s.jpg'
        self.add_to_image_list('valentine1', valentine_template % 'A_2-e1644765742792')
        self.add_to_image_list('valentine2', valentine_template % 'C_2-e1644765764457')
        self.add_to_image_list('valentine3', valentine_template % 'B_2-e1644765752743')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'bddvd.html')
            images = soup.select('#BdData img[src]')
            self.image_list = []
            for image in images:
                if 'bddvd' in image['src']:
                    split1 = image['src'].split('/')
                    if len(split1) > 1:
                        image_name = split1[-1].split('.')[0]
                        if image_name == 'np' or image_name == 'cp1-np':
                            continue
                        if split1[-2] != 'bddvd':
                            image_name = split1[-2] + '_' + image_name
                        image_url = self.PAGE_PREFIX + image['src'][2:]
                        self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


# Kawaii dake ja Nai Shikimori-san
class ShikimorisanDownload(Spring2022AnimeDownload, NewsTemplate2):
    title = 'Kawaii dake ja Nai Shikimori-san'
    keywords = [title]
    website = 'https://shikimori-anime.com/'
    twitter = 'anime_shikimori'
    hashtags = '式守さん'
    folder_name = 'shikimorisan'

    PAGE_PREFIX = website

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
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/introduction.html', decode=True)
            a_tags = soup.select('#ContentsListUnit02 a[href]')
            for a_tag in a_tags:
                try:
                    episode = str(int(a_tag.text.replace('第', '').replace('話', ''))).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                ep_soup = self.get_soup(self.PAGE_PREFIX + a_tag['href'].replace('../', ''))
                if ep_soup is not None:
                    images = ep_soup.select('ul.tp5 img[src]')
                    self.image_list = []
                    for i in range(len(images)):
                        image_url = self.PAGE_PREFIX + images[i]['src'].split('?')[0]
                        image_url = self.remove_string(image_url, ['../', 'sn_'])
                        image_name = episode + '_' + str(i + 1)
                        self.add_to_image_list(image_name, image_url)
                    self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(self.PAGE_PREFIX, 'news/list00010000.html')

    def download_episode_preview_external(self):
        jp_title = '可愛いだけじゃない式守さん'
        last_date = datetime.strptime('20220801', '%Y%m%d')
        today = datetime.today()
        if today < last_date:
            end_date = today
        else:
            end_date = last_date
        MocaNewsScanner(jp_title, self.base_folder, '20220409', end_date.strftime('%Y%m%d'),
                        download_id=self.download_id).run()

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz', self.PAGE_PREFIX + 'core_sys/images/main/home/kv.jpg')
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FAiftmBVIAASbjk?format=jpg&name=large')
        self.download_image_list(folder)

        template = self.PAGE_PREFIX + 'core_sys/images/main/home/kv%s.jpg'
        self.download_by_template(folder, template, 1, 2)

    def download_character(self):
        folder = self.create_character_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/shikimori.html')
            a_tags = soup.select('#ContentsListUnit01 a')
            for a_tag in a_tags:
                if a_tag.has_attr('href'):
                    chara_url = self.PAGE_PREFIX + a_tag['href'].replace('../', '')
                    chara_name = chara_url.split('/')[-1].split('.html')[0]
                    if chara_name in processed:
                        continue
                    if chara_name != 'shikimori':
                        chara_soup = self.get_soup(chara_url)
                    else:
                        chara_soup = soup
                    if chara_soup:
                        images = chara_soup.select('.charFace img, .charPh img')
                        self.image_list = []
                        for image in images:
                            if image.has_attr('src'):
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
        bd_template = self.PAGE_PREFIX + 'bd/%s.html'
        for i in range(8):
            if i == 0:
                bd_page = 'tokuten'
            else:
                bd_page = str(i).zfill(2)
                if bd_page in processed:
                    continue
            bd_url = bd_template % bd_page
            try:
                bd_soup = self.get_soup(bd_url)
                if bd_soup is not None:
                    if i == 0:
                        images = bd_soup.select('#cms_block img[src]')
                    else:
                        images = bd_soup.select('#cms_block .line_01 img[src]')
                    self.image_list = []
                    for image in images:
                        image_url = self.PAGE_PREFIX + image['src'].replace('../', '').replace('sn_', '').split('?')[0]
                        image_name = self.extract_image_name_from_url(image_url)
                        if self.is_image_exists(image_name, folder):
                            if i == 0:
                                self.download_image_with_different_length(image_url, image_name, 'old', folder)
                        elif self.is_matching_content_length(image_url, [3219, 7666]):
                            continue
                        else:
                            self.add_to_image_list(image_name, image_url)
                    if i > 0:
                        if len(self.image_list) > 0:
                            processed.append(bd_page)
                        else:
                            break
                    self.download_image_list(folder)
            except Exception as e:
                self.print_exception(e, 'Blu-ray - %s' % bd_page)
        self.create_cache_file(cache_filepath, processed, num_processed)


# Kingdom 4th Season
class Kingdom4Download(Spring2022AnimeDownload):
    title = "Kingdom 4th Season"
    keywords = [title]
    website = 'https://kingdom-anime.com/'
    twitter = 'kingdom_animePR'
    hashtags = 'キングダム'
    folder_name = 'kingdom4'

    STORY_PAGE = "https://kingdom-anime.com/story/?season=4"
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
                                end_date='20220406', download_id=self.download_id).run()


# Koi wa Sekai Seifuku no Ato de
class KoisekaDownload(Spring2022AnimeDownload, NewsTemplate):
    title = 'Koi wa Sekai Seifuku no Ato de'
    keywords = [title, 'Koiseka', 'Love After World Domination']
    website = 'https://koiseka-anime.com/'
    twitter = 'koiseka_anime'
    hashtags = ['恋せか', 'koiseka']
    folder_name = 'koiseka'

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
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            box_stories = soup.select('div.box_story')
            for story in box_stories:
                try:
                    ttl_num = story.select('.story_ttl_num span')[0].text.replace('第', '').replace('話', '')
                    episode = str(int(ttl_num)).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                images = story.select('ul.img_thum img[src]')
                self.image_list = []
                for i in range(len(images)):
                    image_url = self.PAGE_PREFIX + images[i]['src'].replace('../', '')
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_external(self):
        jp_title = '恋は世界征服のあとで'
        AniverseMagazineScanner(jp_title, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20220331', download_id=self.download_id).run()

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

        self.download_youtube_thumbnails(self.PAGE_PREFIX, folder)

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
            self.print_exception(e, 'Character')

    def download_media(self):
        folder = self.create_media_directory()
        prefix = 'https://www.toei-video.co.jp'
        try:
            soup = self.get_soup('https://www.toei-video.co.jp/special/koiseka-anime/')
            self.image_list = []
            packages = soup.select('div.package')
            for i in range(len(packages)):
                bd_images = packages[i].select('img[src]')
                for bd_image in bd_images:
                    if 'btn-buy' in bd_image['src'] or self.is_matching_content_length(bd_image['src'], [21667, 21607]):
                        continue
                    bd_image_url = bd_image['src'].split('?')[0]
                    if bd_image_url.startswith('/'):
                        bd_image_url = prefix + bd_image_url
                    bd_image_name = self.extract_image_name_from_url(bd_image_url)
                    self.add_to_image_list(bd_image_name, bd_image_url)

            images = soup.select('div.shoplist img[src]')
            for image in images:
                image_url = prefix + image['src'].split('?')[0]
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


# Komi-san wa, Comyushou desu.
class Komisan2Download(Spring2022AnimeDownload, NewsTemplate):
    title = 'Komi-san wa, Comyushou desu. 2nd Season'
    keywords = [title, 'Comyushou', "Komi Can't Communicate", 'komisan']
    website = 'https://komisan-official.com/'
    twitter = 'comisanvote'
    hashtags = ['komisan', '古見さん']
    folder_name = 'komisan2'

    PAGE_PREFIX = website
    FINAL_EPISODE = 24

    def run(self):
        self.download_episode_preview_external()
        self.download_key_visual()

    def download_episode_preview_external(self):
        jp_title = '古見さんは、コミュ症です'
        AniverseMagazineScanner(jp_title, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20220404', check_resize=True, download_id=self.download_id).run()

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/FMu8zsMVEAIE1VX?format=jpg&name=4096x4096')
        self.download_image_list(folder)


# Kono Healer, Mendokusai
class KonoHealerDownload(Spring2022AnimeDownload, NewsTemplate2):
    title = 'Kono Healer, Mendokusai'
    keywords = [title, "This Healer's a Handful"]
    website = 'https://kono-healer-anime.com/'
    twitter = 'kono_healer'
    hashtags = ['このヒーラー', 'kono_healer']
    folder_name = 'kono-healer'

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
            a_tags = soup.select('#ContentsListUnit01 a[href]')
            for a_tag in a_tags:
                if 'index' not in a_tag['href'] and a_tag['href'].endswith('.html') and '/' in a_tag['href']:
                    try:
                        episode = str(int(a_tag['href'].split('/')[-1].split('.html')[0])).zfill(2)
                    except Exception:
                        continue
                    if self.is_image_exists(episode + '_1'):
                        continue
                    ep_soup = self.get_soup(self.PAGE_PREFIX + a_tag['href'].replace('../', ''))
                    if ep_soup:
                        images = ep_soup.select('ul.tp5 img[src]')
                        self.image_list = []
                        for i in range(len(images)):
                            image_url = self.PAGE_PREFIX + images[i]['src'].replace('../', '').split('?')[0]
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
        for i in range(1, self.FINAL_EPISODE + 1, 1):
            episode = str(i).zfill(2)
            is_success = False
            if self.is_image_exists(episode + '_1'):
                continue
            first = 10 + (i - 1)
            second = 32 + 5 * (i - 1)
            third = 38 + self.IMAGES_PER_EPISODE * (i - 1)
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
        self.add_to_image_list('teaser', 'https://pbs.twimg.com/media/Ey5yDx_VgAUuHlX?format=jpg&name=large')
        self.add_to_image_list('tz_visual', self.PAGE_PREFIX + 'core_sys/images/main/tz/tz_visual.png')
        self.add_to_image_list('tz2_tw', 'https://pbs.twimg.com/media/FCG8xMCUcAEjhO3?format=jpg&name=4096x4096')
        self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/FM7Jj7rUcAANg3L?format=jpg&name=large')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'chara')
            images = soup.select('div.read img')
            self.image_list = []
            for image in images:
                if image.has_attr('src'):
                    image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')

    def download_media(self):
        folder = self.create_media_directory()

        # Blu-ray
        bd_template = self.PAGE_PREFIX + 'core_sys/images/contents/000000%s/block/000000%s/00000%s.jpg'
        self.image_list = []
        for i in range(3):
            image_name = 'bd' + str(i + 1)
            if self.is_image_exists(image_name, folder):
                continue
            image_url = bd_template % (str(i + 22).zfill(2), str(i + 90).zfill(2), str(i + 110).zfill(3))
            if self.is_matching_content_length(image_url, 34034):
                continue
            self.add_to_image_list(image_name, image_url)
        self.download_image_list(folder)

        # Music & Blu-ray Bonus
        pages = ['music/', 'bddvd/privilege.html', 'bddvd/campaign.html']
        for i in range(len(pages)):
            url = self.PAGE_PREFIX + pages[i]
            try:
                soup = self.get_soup(url)
                images = soup.select('#cms_block img')
                self.image_list = []
                for image in images:
                    image_url = self.PAGE_PREFIX + image['src'].replace('../', '').split('?')[0]
                    if 'nowrinting' in image_url or 'nowprinting' in image_url:
                        continue
                    image_name = self.extract_image_name_from_url(image_url)
                    if self.is_matching_content_length(image_url, [17128, 61159]):
                        continue
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(folder)
            except Exception as e:
                print("Error in running " + self.__class__.__name__ + " - Music/Blu-Ray %s" % url)
                print(e)


# Kunoichi Tsubaki no Mune no Uchi
class KunoichiTsubakiDownload(Spring2022AnimeDownload, NewsTemplate):
    title = 'Kunoichi Tsubaki no Mune no Uchi'
    keywords = [title, 'In the Heart of Kunoichi Tsubaki']
    website = 'https://kunoichi-tsubaki.com/'
    hashtags = 'くノ一ツバキ'
    twitter = 'tsubaki_anime'
    folder_name = 'kunoichi-tsubaki'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 5

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
            soup = self.get_soup(self.PAGE_PREFIX + 'story/', decode=True)
            li_tags = soup.select('.p-story__nav-list li')
            for li in li_tags:
                ep_soup = None
                para = li.find('p')
                if para is not None:
                    try:
                        episode = str(self.convert_kanji_to_number(para.text.replace('の巻', ''))).zfill(2)
                    except:
                        continue
                else:
                    continue
                if self.is_image_exists(episode + '_5'):
                    continue
                if li.has_attr('class') and 'current' in li['class']:
                    ep_soup = soup
                else:
                    a_tag = li.find('a[href]')
                    if a_tag is not None:
                        ep_soup = self.get_soup(self.PAGE_PREFIX + a_tag['href'][1:])
                if ep_soup is not None and episode is not None:
                    images = ep_soup.select('li.swiper-slide img[src]')
                    self.image_list = []
                    for i in range(len(images)):
                        image_url = self.PAGE_PREFIX + images[i]['src'][1:]
                        image_name = episode + '_' + str(i + 1)
                        self.add_to_image_list(image_name, image_url)
                    self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_guess(self):
        folder = self.create_custom_directory('guess')
        is_success = False
        end_num = self.IMAGES_PER_EPISODE
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            start_num = None
            for j in range(end_num):
                if self.is_image_exists(episode + '_' + str(j + 1)):
                    start_num = j + 2
                else:
                    start_num = j + 1
                    break
            if not start_num or start_num > end_num:
                continue
            template1 = self.PAGE_PREFIX + 'assets/img/story/img_ep%s-%s.jpg' % (episode, '%s')
            template2 = self.PAGE_PREFIX + 'assets/img/story/img_ep%s-%s.png' % (episode, '%s')
            if not self.download_by_template(folder, [template1, template2], 1, start=start_num, end=end_num):
                break
            print(self.__class__.__name__ + ' - Episode %s guessed correctly!' % episode)
            is_success = True
        return is_success

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news/'
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='li.c-news__item',
                                    date_select='.c-news__item-date', title_select='.c-news__item-txt',
                                    id_select='.c-news__item-link', a_tag_prefix=news_url, paging_type=1,
                                    next_page_select='.c-pagination__count-item',
                                    next_page_eval_index_class='is-current', next_page_eval_index=-1)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_main', self.PAGE_PREFIX + 'teaser/img/top/main.jpg')
        self.add_to_image_list('kv1', self.PAGE_PREFIX + 'teaser/img/top/main_2nd.jpg')
        # self.add_to_image_list('kv1', self.PAGE_PREFIX + 'assets/img/top/main.jpg')
        self.add_to_image_list('kv2', self.PAGE_PREFIX + 'assets/img/top/main-2nd.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/detail.html')
            images = soup.select('.p-inChara__whole-img img, .p-inChara__face-item img')
            self.image_list = []
            for image in images:
                if image.has_attr('data-src'):
                    image_url = self.PAGE_PREFIX + image['data-src'][1:]
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')

    def download_media(self):
        folder = self.create_media_directory()

        # Blu-ray
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        bd_template = self.PAGE_PREFIX + 'bddvd/%s.html'
        for i in range(8):
            if i == 0:
                bd_page = 'special'
            else:
                bd_page = str(i).zfill(2)
                if bd_page in processed:
                    continue
            bd_url = bd_template % bd_page
            try:
                bd_soup = self.get_soup(bd_url)
                if bd_soup is not None:
                    images = bd_soup.select('.p-bddvd img[src]')
                    self.image_list = []
                    for image in images:
                        image_url = self.PAGE_PREFIX + image['src'].replace('../', '').split('?')[0]
                        if '/bddvd/' in image_url:
                            split1 = image_url.split('/')
                            if len(split1) == 0 or 'img_np' in split1[-1] or 'jk_np' in split1[-1]:
                                continue
                            image_name = ''
                            for split_ in reversed(split1):
                                if split_ == 'bddvd':
                                    break
                                if len(split_) == 0:
                                    continue
                                if len(image_name) == 0:
                                    image_name = split_.split('.')[0]
                                else:
                                    image_name = split_ + "_" + image_name
                            if self.is_image_exists(image_name, folder):
                                if i == 0:
                                    self.download_image_with_different_length(image_url, image_name, 'old', folder)
                            else:
                                self.add_to_image_list(image_name, image_url)
                    if i > 0:
                        if len(self.image_list) > 0:
                            processed.append(bd_page)
                        else:
                            break
                    self.download_image_list(folder)
            except Exception as e:
                self.print_exception(e, 'Blu-ray - %s' % bd_page)
        self.create_cache_file(cache_filepath, processed, num_processed)

        # Digicon
        digicon_folder = folder + '/digicon'
        if not os.path.exists(digicon_folder):
            os.makedirs(digicon_folder)

        self.image_list = []
        try:
            digicon_soup = self.get_soup(self.PAGE_PREFIX + 'special/digicon/')
            digicon_imgs = digicon_soup.select('.digicon_img img')
            for digicon_img in digicon_imgs:
                if digicon_img.has_attr('src'):
                    if digicon_img['src'].startswith('../../'):
                        digicon_image_url = self.PAGE_PREFIX + digicon_img['src'][6:]
                    elif digicon_img['src'].startswith('/'):
                        digicon_image_url = self.PAGE_PREFIX + digicon_img['src'][1:]
                    else:
                        continue
                    digicon_image_name = self.extract_image_name_from_url(digicon_image_url)
                    self.add_to_image_list(digicon_image_name, digicon_image_url)
            self.download_image_list(digicon_folder)
        except Exception as e:
            self.print_exception(e, 'Media - Digicon')

        # Countdown Voice
        countdown_voice_folder = folder + '/countdown-voice'
        if not os.path.exists(countdown_voice_folder):
            os.makedirs(countdown_voice_folder)

        try:
            voice_soup = self.get_soup(self.PAGE_PREFIX + 'special/countdown-voice/')
            voices = voice_soup.select('.voice audio')
            for voice in voices:
                if voice.has_attr('src'):
                    if voice['src'].startswith('../../'):
                        audio_url = self.PAGE_PREFIX + voice['src'][6:]
                    elif voice['src'].startswith('/'):
                        audio_url = self.PAGE_PREFIX + voice['src'][1:]
                    else:
                        continue
                    audio_name = audio_url.split('/')[-1]
                    self.download_content(audio_url, countdown_voice_folder + '/' + audio_name)
        except Exception as e:
            self.print_exception(e, 'Media - Countdown Voice')


# Machikado Mazoku: 2-choume
class MachikadoMazoku2Download(Spring2022AnimeDownload, NewsTemplate):
    title = 'Machikado Mazoku: 2-choume'
    keywords = ["Machikado Mazoku", "The Demon Girl Next Door", "2nd"]
    website = 'http://www.tbs.co.jp/anime/machikado/'
    twitter = 'machikado_staff'
    hashtags = ['まちカドまぞく', 'MachikadoMazoku']
    folder_name = 'machikado-mazoku2'

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
        template = self.PAGE_PREFIX + 'story/img/story%s/%s.jpg'
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                continue
            for j in range(self.IMAGES_PER_EPISODE):
                image_url = template % (episode, str(j + 1).zfill(2))
                image_name = episode + '_' + str(j + 1)
                if self.download_image(image_url, self.base_folder + '/' + image_name) == -1:
                    return

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='ul.newslist li',
                                    date_select='time', title_select='p', id_select='a',
                                    a_tag_prefix=self.PAGE_PREFIX + 'news/')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/E__DujoVcAktN1i?format=jpg&name=large')
        self.add_to_image_list('tz', self.PAGE_PREFIX + 'img/machikado_top_pc@2x.jpg')
        self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/FMnJhjJacAIwzef?format=jpg&name=large')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('#top-visual img')
            for image in images:
                if image.has_attr('src'):
                    image_url = self.PAGE_PREFIX + image['src']
                    image_name = self.extract_image_name_from_url(image_url)
                    if self.is_image_exists(image_name, folder):
                        self.download_image_with_different_length(image_url, image_name, 'old', folder)
                    else:
                        self.download_image(image_url, folder + '/' + image_name)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        chara_prefix = self.PAGE_PREFIX + 'character/img/'
        template = [chara_prefix + 'chara_nav_%s@2x.png']
        self.download_by_template(folder, template, 2, 1)

        template2 = chara_prefix + 'charaimg_%s@2x.png'
        for i in range(1, 30, 1):
            image_url = template2 % str(i).zfill(2)
            image_name = 'charaimg_%s@2x' % str(i).zfill(2)
            if self.is_image_exists(image_name, folder):
                self.download_image_with_different_length(image_url, image_name, 'old', folder)
            else:
                self.download_image(image_url, folder + '/' + image_name)

    def download_media(self):
        folder = self.create_media_directory()
        goods_prefix = self.PAGE_PREFIX + 'goods/'

        self.image_list = []
        self.add_to_image_list('cdimg_op', goods_prefix + 'img/cdimg_op.jpg')
        self.add_to_image_list('cdimg_ed', goods_prefix + 'img/cdimg_ed.jpg')
        self.download_image_list(folder)

        # Blu-ray
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        try:
            bd_template = goods_prefix + 'disc%s.html'
            bd_pages = ['05', '01', '02', '03', '04']
            for bd_page in bd_pages:
                if bd_page != '05' and bd_page in processed:
                    continue
                if bd_page == '01':
                    bd_url = bd_template % ''
                else:
                    bd_url = bd_template % bd_page
                soup = self.get_soup(bd_url)
                if soup is not None:
                    images = soup.select('.disc-content-block img[src]')
                    self.image_list = []
                    for image in images:
                        image_url = goods_prefix + image['src']
                        image_name = self.extract_image_name_from_url(image_url)
                        if 'noimage' in image_name:
                            continue
                        self.add_to_image_list(image_name, image_url)
                    if bd_page != '05':
                        if len(self.image_list) > 0:
                            processed.append(bd_page)
                        else:
                            break
                    self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Mahoutsukai Reimeiki
class ReimeikiDownload(Spring2022AnimeDownload, NewsTemplate):
    title = 'Mahoutsukai Reimeiki'
    keywords = [title, 'The Dawn of the Witch']
    website = 'https://www.tbs.co.jp/anime/reimeiki/'
    twitter = 'reimeiki_pr'
    hashtags = '魔法使い黎明期'
    folder_name = 'reimeiki'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

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
        template = self.PAGE_PREFIX + 'story/img/story%s/%s.jpg'
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                continue
            for j in range(self.IMAGES_PER_EPISODE):
                image_url = template % (episode, str(j + 1).zfill(2))
                image_name = episode + '_' + str(j + 1)
                if self.download_image(image_url, self.base_folder + '/' + image_name) == -1:
                    return

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='dl.update-box',
                                    date_select='.update-date', title_select='a', id_select='a',
                                    a_tag_prefix=self.PAGE_PREFIX + 'news/')

    def download_episode_preview_external(self):
        jp_title = '魔法使い黎明期'
        AniverseMagazineScanner(jp_title, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20220405', download_id=self.download_id).run()

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.add_to_image_list('tz', 'https://pbs.twimg.com/media/FCy4SbFVgBETtHo?format=jpg&name=large')
        self.add_to_image_list('teaser_visual_chara', self.PAGE_PREFIX + 'img/teaser_visual_chara.png')
        self.add_to_image_list('teaser_visual_chara_bg', self.PAGE_PREFIX + 'img/teaser_visual_chara.jpg')
        self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/FMbjID_VEAUuCcr?format=jpg&name=large')
        # self.add_to_image_list('keyvisual', self.PAGE_PREFIX + 'img/keyvisual.jpg')
        self.download_image_list(folder)

        try:
            css_text = self.get_response(self.PAGE_PREFIX + 'css/common.css')
            split1 = css_text.split('.top-main-visual')
            for i in range(len(split1)):
                split2 = split1[i].split('}')[0].split('")')[0].split('url("../')
                if len(split2) > 1:
                    image_url = self.PAGE_PREFIX + split2[1].strip()
                    image_name = self.extract_image_name_from_url(image_url)
                    if self.is_image_exists(image_name, folder):
                        self.download_image_with_different_length(image_url, image_name, 'old', folder)
                        continue
                    self.download_image(image_url, folder + '/' + image_name)
                    break
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        # prefix = self.PAGE_PREFIX + 'img/chara'
        # templates = [prefix + '_%s_on.png', prefix + 'img_%s.jpg']
        template = self.PAGE_PREFIX + 'character/img/chara_img_%s@2x.png'
        self.download_by_template(folder, template, 2, 1)

    def download_media(self):
        folder = self.create_media_directory()
        self.image_list = []
        self.add_to_image_list('bdbox', 'https://moca-news.net/article/20220408/2022040802300a_/image/911-5juy9a.jpg', is_mocanews=True)
        self.add_to_image_list('bdbonus1', 'https://moca-news.net/article/20220408/2022040802300a_/image/912-5d83ro.jpg', is_mocanews=True)
        self.add_to_image_list('bdbonus2', 'https://moca-news.net/article/20220408/2022040802300a_/image/913-48m9a2.jpg', is_mocanews=True)
        self.add_to_image_list('bdbonus3', 'https://moca-news.net/article/20220408/2022040802300a_/image/914-22zesg.jpg', is_mocanews=True)
        self.add_to_image_list('bdbonus4', 'https://moca-news.net/article/20220408/2022040802300a_/image/915-0wdkbv.jpg', is_mocanews=True)
        self.download_image_list(folder)


# Otome Game Sekai wa Mob ni Kibishii Sekai desu
class MobsekaDownload(Spring2022AnimeDownload, NewsTemplate):
    title = 'Otome Game Sekai wa Mob ni Kibishii Sekai desu'
    keywords = [title, 'Trapped in a Dating Sim: The World of Otome Games is Tough for Mobs', 'Mobseka', 'Mobuseka']
    website = 'https://mobseka.com/'
    twitter = 'mobseka_anime'
    hashtags = ['モブせか', 'mobseka', 'mobuseka']
    folder_name = 'mobseka'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

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
        for i in range(self.FINAL_EPISODE):
            for j in range(self.IMAGES_PER_EPISODE):
                image_name = str(i + 1).zfill(2) + '_' + str(j + 1)
                if not self.is_image_exists(image_name):
                    image_url = image_url_template % (str(i + 1).zfill(2), str(j + 1).zfill(2))
                    result = self.download_image(image_url, self.base_folder + '/' + image_name)
                    if result == -1:
                        return

    def download_episode_preview_external(self):
        jp_title = '⼄⼥ゲー世界はモブに厳しい世界です'
        AniverseMagazineScanner(jp_title, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20220331', download_id=self.download_id).run()

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, news_prefix='news.html', article_select='#news dl',
                                    title_select='a', date_select='dt', id_select='a', a_tag_prefix=self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FFBOuWKaMAQzQbY?format=jpg&name=large')
        self.download_image_list(folder)

        template = self.PAGE_PREFIX + 'img/top_mv_%s.jpg'
        self.download_by_template(folder, template, 2, 1)

    def download_character(self):
        folder = self.create_character_directory()
        body_template = self.PAGE_PREFIX + 'img/chara/illust_%s.png'
        face_template = self.PAGE_PREFIX + 'img/chara/face_%s.png'
        self.download_by_template(folder, [body_template, face_template], 2, 1)

    def download_media(self):
        folder = self.create_media_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'bluray.html')
            images = soup.select('.news_contents img[src]')
            self.image_list = []
            for image in images:
                if image['src'].endswith('20210000_00_01cs.jpg') or image['src'].endswith('20210000_00_02cs.jpg'):
                    continue
                image_url = self.PAGE_PREFIX + image['src']
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception('e', 'Blu-ray')


# Paripi Koumei
class ParipiKoumeiDownload(Spring2022AnimeDownload, NewsTemplate):
    title = 'Paripi Koumei'
    keywords = [title, 'Ya Boy Kongming!']
    website = 'https://paripikoumei-anime.com/'
    twitter = 'paripikoumei_PR'
    hashtags = 'パリピ孔明'
    folder_name = 'paripikoumei'

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

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            divs = soup.select('.contents div[id]')
            for div in divs:
                if div['id'].isnumeric:
                    episode = str(int(div['id'])).zfill(2)
                    if self.is_image_exists(episode + '_01'):
                        continue
                    images = div.select('img[src]')
                    self.image_list = []
                    for i in range(len(images)):
                        image_url = images[i]['src']
                        image_name = episode + '_' + str(i + 1).zfill(2)
                        self.add_to_image_list(image_name, image_url)
                    self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        news_prefix = self.PAGE_PREFIX + 'news/'
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-list article',
                                    title_select='h2', date_select='time', id_select='a',
                                    date_separator='/', a_tag_prefix=news_prefix)

    def download_episode_preview_external(self):
        jp_title = 'パリピ孔明'
        AniverseMagazineScanner(jp_title, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20220330', download_id=self.download_id).run()

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('top_kv', self.PAGE_PREFIX + 'assets/images/top/kv.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            images = soup.select('.characters img[src]')
            self.image_list = []
            for image in images:
                if '/character/' in image['src']:
                    image_url = self.PAGE_PREFIX + image['src'].split('?')[0].replace('../', '')
                    split1 = image_url.split('/')
                    if len(split1) > 2 and split1[-1].startswith('pic') and split1[-3] == 'character':
                        image_name = 'chara_' + split1[-2]
                        self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Rikei ga Koi ni Ochita no de Shoumei shitemita. Heart
class Rikekoi2Download(Spring2022AnimeDownload, NewsTemplate):
    title = "Rikei ga Koi ni Ochita no de Shoumei shitemita. Heart"
    keywords = [title, "Rikekoi", "Science Fell in Love, So I Tried to Prove It", "2nd"]
    website = 'https://rikekoi.com/'
    twitter = 'rikeigakoini'
    hashtags = ['リケ恋', 'Rikekoi']
    folder_name = 'rikekoi2'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()

    def download_episode_preview(self):
        story_url = self.PAGE_PREFIX + 'story/season2-1'
        try:
            soup = self.get_soup(story_url)
            story_links = soup.select('div.story-link')
            if len(story_links) > 0:
                story_link_items = story_links[-1].select('a.story-link-item[href][class]')
                for link_item in story_link_items:
                    try:
                        episode = str(int(link_item.text)).zfill(2)
                    except:
                        continue
                    if self.is_image_exists(episode + '_1'):
                        continue
                    story_soup = None
                    if link_item.has_attr('class'):
                        if 'disabled' in link_item['class']:
                            continue
                        elif 'this-page' in link_item['class']:
                            story_soup = soup
                    if story_soup is None:
                        story_soup = self.get_soup(self.PAGE_PREFIX + link_item['href'][1:])
                    if story_soup is not None:
                        images = story_soup.select('figure.wp-block-image img')
                        for i in range(len(images)):
                            image_url = self.get_image_url_from_srcset(images[i])
                            if image_url is not None:
                                image_name = episode + '_' + str(i + 1)
                                self.add_to_image_list(image_name, image_url)
                        self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_guess(self):
        template = self.PAGE_PREFIX + 'wp-content/uploads/2022/04/vlcsnap-2022-01-29-%sh%sm%ss%s.jpg'
        folder = self.create_custom_directory('guess')
        hours = 18
        minutes = 0
        seconds = 0
        milliseconds = 0
        image_url = template % (str(hours).zfill(2), str(minutes).zfill(2), str(seconds).zfill(2), str(milliseconds).zfill(3))
        try:
            while hours < 24:
                while minutes < 60:
                    while seconds < 60:
                        while milliseconds < 1000:
                            image_url = template % (str(hours).zfill(2), str(minutes).zfill(2), str(seconds).zfill(2), str(milliseconds).zfill(3))
                            print(image_url)
                            if self.is_valid_url(image_url, is_image=True):
                                image_name = self.extract_image_name_from_url(image_url)
                                self.download_image(image_url, folder + '/' + image_name + '.jpg')
                            milliseconds += 1
                        milliseconds = 0
                        seconds += 1
                    seconds = 0
                    minutes += 1
                minutes = 0
                hours += 1
        except KeyboardInterrupt:
            print('Interrupted at: ' + image_url)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.post',
                                    title_select='a', date_select='.date', id_select='a',
                                    date_func=lambda x: x.replace('提出日：', '').replace('年', '.').replace('月', '.')
                                    .replace('日', ''), stop_date='2020.10.02')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        # self.add_to_image_list('key_pc', self.PAGE_PREFIX + 'wp-content/themes/rikekoi/assets/images/season2/key_pc.png')
        self.add_to_image_list('kv', self.PAGE_PREFIX + 'wp-content/uploads/2021/12/リケ恋2キービジュアル_A_FIX_logoあり.png')
        self.download_image_list(folder)


# RPG Fudousan
class RPGFudousanDownload(Spring2022AnimeDownload, NewsTemplate3):
    title = 'RPG Fudousan'
    keywords = [title, 'RPG Real Estate']
    website = 'https://rpg-rs.jp/'
    twitter = 'rpgrs_anime'
    hashtags = 'RPG不動産'
    folder_name = 'rpg-fudousan'

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
        try:
            soup = self.get_soup(self.PAGE_PREFIX + '/story.html')
            stories = soup.select('.story-data[id]')
            for story in stories:
                try:
                    ep_num = int(story['id'][1:])
                    if ep_num < 1:
                        continue
                    episode = str(ep_num).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                images = story.select('div.img img[src]')
                self.image_list = []
                for i in range(len(images)):
                    image_url = self.PAGE_PREFIX + images[i]['src'][2:]
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(self.PAGE_PREFIX)

    def download_episode_preview_external(self):
        jp_title = 'RPG不動産'
        AniverseMagazineScanner(jp_title, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20220404', check_resize=True, download_id=self.download_id).run()

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        # self.add_to_image_list('tz1_1', self.PAGE_PREFIX + 'core_sys/images/main/tz/kv.png')
        self.add_to_image_list('tz1_2', self.PAGE_PREFIX + 'assets/news/vis-t1.jpg')
        self.add_to_image_list('vis-k1', self.PAGE_PREFIX + 'assets/news/vis-k1.jpg')
        self.add_to_image_list('2022apr_vis', self.PAGE_PREFIX + 'assets/top/2022apr/vis.jpg')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            visual = soup.select('.vis img')
            if len(visual) > 0 and visual[0].has_attr('src'):
                image_url = self.PAGE_PREFIX + visual[0]['src'].replace('./', '')
                image_name = self.extract_image_name_from_url(image_url)
                if self.is_image_exists(image_name, folder):
                    self.download_image_with_different_length(image_url, image_name, 'old', folder)
                else:
                    self.download_image(image_url, folder + '/' + image_name)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        # template = self.PAGE_PREFIX + 'assets/character/c/%s.png'
        # self.download_by_template(folder, template, 1, 1, prefix='c')
        template = self.PAGE_PREFIX + 'assets/character/%sc.png'
        self.download_by_template(folder, template, 1, 1, prefix='chara')

    def download_media(self):
        folder = self.create_media_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'bddvd.html')
            images = soup.select('#BdData img[src]')
            self.image_list = []
            for image in images:
                if 'bddvd' in image['src']:
                    split1 = image['src'].split('/')
                    if len(split1) > 1:
                        image_name = split1[-1].split('.')[0]
                        if image_name == 'np' or image_name == 'cp1-np':
                            continue
                        if split1[-2] != 'bddvd':
                            image_name = split1[-2] + '_' + image_name
                        image_url = self.PAGE_PREFIX + image['src'][2:]
                        self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


# Shachiku-san wa Youjo Yuurei ni Iyasaretai. https://shachikusan.com/ #しゃちされたい @shachisaretai
class ShachisaretaiDownload(Spring2022AnimeDownload, NewsTemplate):
    title = 'Shachiku-san wa Youjo Yuurei ni Iyasaretai.'
    keywords = [title, 'Shachisaretai', 'Shachikusan']
    website = 'https://shachikusan.com/'
    twitter = 'shachisaretai'
    hashtags = 'しゃちされたい'
    folder_name = 'shachisaretai'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 5

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_episode_preview_external()
        self.download_episode_preview_guess()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        yt_folder = self.create_custom_directory('yt')  # YouTube thumbnails
        yt_images = os.listdir(yt_folder)
        yt_episodes = []
        for yt_image in yt_images:
            if os.path.isfile(yt_folder + '/' + yt_image) and yt_image.endswith('.jpg') \
                    and yt_image[0:2].isnumeric() and yt_image[2] == '_':
                yt_episodes.append(yt_image[0:2])

        story_url = self.PAGE_PREFIX + 'story/'
        try:
            soup = self.get_soup(story_url)
            stories = soup.select('.story_list li')
            for story in stories:
                ttl = story.select('.ttl')
                if len(ttl) > 0:
                    try:
                        episode = str(int(ttl[0].text.replace('第', '').replace('話', ''))).zfill(2)
                    except:
                        continue
                    if self.is_image_exists(episode + '_5') and episode in yt_episodes:
                        continue
                    page = story.select('a[href]')
                    if len(page) > 0:
                        page_url = story_url + page[0]['href'][2:]
                        ep_soup = self.get_soup(page_url)
                        if ep_soup is not None:
                            images = ep_soup.select('ul.img_thum img[src]')
                            self.image_list = []
                            for i in range(len(images)):
                                image_url = self.PAGE_PREFIX + images[i]['src'].replace('../../', '')
                                image_name = episode + '_' + str(i + 1)
                                self.add_to_image_list(image_name, image_url)
                            self.download_image_list(self.base_folder)

                            yt_tag = ep_soup.select('.movie_wp iframe')
                            if len(yt_tag) > 0 and yt_tag[0]['src'].lower().startswith('https://www.youtube.com/embed/'):
                                yt_id = yt_tag[0]['src'][30:].split('?')[0]
                                yt_image_url = f'https://img.youtube.com/vi/{yt_id}/maxresdefault.jpg'
                                yt_image_name = f'{episode}_{yt_id}'
                                self.download_image(yt_image_url, f'{yt_folder}/{yt_image_name}')
        except Exception as e:
            print(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='li.news_list_item',
                                    date_select='time', title_select='p.article_ttl', id_select='a')

    def download_episode_preview_external(self):
        jp_title = '社畜さんは幼女幽霊に癒されたい'
        AniverseMagazineScanner(jp_title, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20220401', check_resize=True, download_id=self.download_id).run()

    def download_episode_preview_guess(self):
        folder = self.create_custom_directory('guess')
        is_success = False
        end_num = self.IMAGES_PER_EPISODE
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            start_num = None
            for j in range(end_num):
                if self.is_image_exists(episode + '_' + str(j + 1)):
                    start_num = j + 2
                else:
                    break
            if not start_num or start_num > end_num:
                continue
            template1 = self.PAGE_PREFIX + 'img/story/ep%s/img%s.jpg' % (episode, '%s')
            template2 = self.PAGE_PREFIX + 'img/story/ep%s/img%s.png' % (episode, '%s')
            if not self.download_by_template(folder, [template1, template2], 2, start=start_num, end=end_num):
                break
            print(self.__class__.__name__ + ' - Episode %s guessed correctly!' % episode)
            is_success = True
        return is_success

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('kv1', self.PAGE_PREFIX + 'img/top/kv.jpg')
        self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/FDzAecoagAEj3PI?format=jpg&name=4096x4096')
        self.add_to_image_list('kv2_big', self.PAGE_PREFIX + 'news/wp-content/uploads/2022/01/YYanime-KV2_mojiari.jpg')
        self.download_image_list(folder)

        template = self.PAGE_PREFIX + 'img/top/kv%s.jpg'
        self.download_by_template(folder, template, 2, 2)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            images = soup.select('div.chara_media img')
            self.image_list = []
            for image in images:
                if image.has_attr('class') and 'front' in image['class']:
                    continue
                if image.has_attr('src'):
                    image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Shijou Saikyou no Daimaou, Murabito A ni Tensei suru
class MurabitoADownload(Spring2022AnimeDownload, NewsTemplate):
    title = 'Shijou Saikyou no Daimaou, Murabito A ni Tensei suru'
    keywords = [title, 'The Greatest Demon Lord Is Reborn as a Typical Nobody']
    website = 'https://murabito-a-anime.com/'
    twitter = 'murabitoA_anime'
    hashtags = '村人Aに転生'
    folder_name = 'murabito-a'

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
            stories = soup.select('.oneStory')
            for story in stories:
                try:
                    episode = str(int(story.select('.oneStory__title--num')[0].text.replace('#', ''))).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                images = story.select('.swiper-slide img[src]')
                self.image_list = []
                for i in range(len(images)):
                    image_url = story_url + images[i]['src'][2:]
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        # Need update page logic
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='ul.newsLists__list li',
                                    title_select='.newsLists__list--title', date_select='.f_roc', id_select='a')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        template = self.PAGE_PREFIX + 'assets/img/top/fv_visual%s.jpg'
        self.download_by_template(folder, template, 1, 1)

        self.image_list = []
        self.add_to_image_list('kv1_news', self.PAGE_PREFIX + 'news/wp-content/uploads/2021/12/211216_01.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        prefix = self.PAGE_PREFIX + 'assets/img/character/character%s_'
        templates = [prefix + 'main.png', prefix + 'face1.jpg', prefix + 'face2.jpg', prefix + 'thumb.jpg']
        self.download_by_template(folder, templates, 1, 1)

        old_dir = 'old'
        for i in range(20):
            image_name = f'character{str(i + 1)}_main'
            if self.is_image_exists(image_name, folder):
                image_url = (prefix % str(i + 1)) + 'main.png'
                if self.download_image_with_different_length(image_url, image_name, old_dir, folder):
                    for p in ['face1', 'face2', 'thumb']:
                        img_name = f'character{str(i + 1)}_{p}'
                        if self.is_image_exists(img_name, folder):
                            img_url = (prefix % str(i + 1)) + p + '.jpg'
                            self.download_image_with_different_length(img_url, img_name, old_dir, folder)
            else:
                break

    def download_media(self):
        folder = self.create_media_directory()
        self.image_list = []
        self.add_to_image_list('music_op', 'https://pbs.twimg.com/media/FO2xv2WVkAQDdkF?format=jpg&name=large')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'bddvd/')
            images = soup.select('.bddvdWrap img[src]')
            self.image_list = []
            for image in images:
                if 'bddvd' in image['src']:
                    split1 = image['src'].split('/')
                    if len(split1) > 1:
                        image_name = split1[-1].split('.')[0]
                        if split1[-2] != 'bddvd':
                            image_name = split1[-2] + '_' + image_name
                        image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                        self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


# Shokei Shoujo no Virgin Road
class ShokeiShoujoDownload(Spring2022AnimeDownload, NewsTemplate):
    title = 'Shokei Shoujo no Virgin Road'
    keywords = [title, 'The Executioner and Her Way of Life']
    website = 'http://virgin-road.com/'
    twitter = 'VirginroadAnime'
    hashtags = ['shokei_anime', '処刑少女']
    folder_name = 'shokeishoujo'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_episode_preview_external()
        self.download_episode_preview_guess()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        yt_folder = self.create_custom_directory('yt')  # YouTube thumbnails
        yt_images = os.listdir(yt_folder)
        yt_episodes = ['01']
        for yt_image in yt_images:
            if os.path.isfile(yt_folder + '/' + yt_image) and yt_image.endswith('.jpg') \
                    and yt_image[0:2].isnumeric() and yt_image[2] == '_':
                yt_episodes.append(yt_image[0:2])

        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            a_tags = soup.select('#ContentsListUnit02 a[href]')
            for a_tag in a_tags:
                if 'index' not in a_tag['href'] and a_tag['href'].endswith('.html') and '/' in a_tag['href']:
                    try:
                        episode = str(int(a_tag['href'].split('/')[-1].split('.html')[0])).zfill(2)
                    except Exception:
                        continue
                    if self.is_image_exists(episode + '_6') and episode in yt_episodes:
                        continue
                    ep_soup = self.get_soup(self.PAGE_PREFIX + a_tag['href'].replace('../', ''))
                    if ep_soup:
                        images = ep_soup.select('ul.tp5 img')
                        self.image_list = []
                        for i in range(len(images)):
                            image_url = self.PAGE_PREFIX + images[i]['src'].replace('../', '').split('?')[0]
                            image_name = episode + '_' + str(i + 1)
                            self.add_to_image_list(image_name, image_url)
                        self.download_image_list(self.base_folder)

                        yt_tag = ep_soup.select('#cms_block iframe[src]')
                        if len(yt_tag) > 0 and yt_tag[0]['src'].lower().startswith('https://www.youtube.com/embed/'):
                            yt_id = yt_tag[0]['src'][30:].split('?')[0]
                            yt_image_url = f'https://img.youtube.com/vi/{yt_id}/maxresdefault.jpg'
                            yt_image_name = f'{episode}_{yt_id}'
                            self.download_image(yt_image_url, f'{yt_folder}/{yt_image_name}')
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_external(self):
        jp_title = '処刑少女の生きる道'
        AniverseMagazineScanner(jp_title, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20220402', download_id=self.download_id, prefix='').run()

    def download_episode_preview_guess(self):
        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'core_sys/images/contents/%s/block/%s/%s.jpg'
        is_successful = False
        for i in range(2, self.FINAL_EPISODE + 1, 1):
            episode = str(i).zfill(2)
            is_success = False
            if self.is_image_exists(episode + '_1'):
                continue
            first = 16 + (i - 1)
            second = 42 + 4 * (i - 1)
            third = 41 + self.IMAGES_PER_EPISODE * (i - 1)
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

    def download_news(self):
        # Paging logic need update
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='#list_07 dd',
                                    title_select='.title', date_select='.day', id_select='a', date_separator='/',
                                    a_tag_replace_from='../', a_tag_replace_to=self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('teaser', self.PAGE_PREFIX + 'core_sys/images/main/tz/kv.png')
        self.add_to_image_list('teaser_tw', 'https://pbs.twimg.com/media/EtDn9lYU0AAKje-?format=jpg&name=4096x4096')
        self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/E6Ur9dWVIAEE3Ee?format=jpg&name=4096x4096')
        self.add_to_image_list('main_kv', 'https://pbs.twimg.com/media/FIP1l-HaMEAKxOE?format=jpg&name=4096x4096')
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

        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'chara/')
            a_tags = soup.select('#ContentsListUnit01 a')
            for a_tag in a_tags:
                if a_tag.has_attr('href'):
                    get_chara_soup = False
                    if a_tag['href'].endswith('.html'):
                        chara_name = a_tag['href'].split('/')[-1][:-5]
                        if chara_name != 'index':
                            get_chara_soup = True
                    else:
                        chara_name = 'index'
                    if chara_name in processed:
                        continue
                    if get_chara_soup:
                        chara_soup = self.get_soup(self.PAGE_PREFIX + a_tag['href'].replace('../', ''))
                    else:
                        chara_soup = soup
                    if chara_soup is not None:
                        images = chara_soup.select('.charWrap img')
                        self.image_list = []
                        for image in images:
                            if image.has_attr('src'):
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
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'bd/')
            images = soup.select('#cms_block img[src]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                if 'nowprinting' in image_url.lower():
                    continue
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


# Spy x Family
class SpyFamilyDownload(Spring2022AnimeDownload, NewsTemplate):
    title = 'Spy x Family'
    keywords = [title]
    website = 'https://spy-family.net/'
    twitter = 'spyfamily_anime'
    hashtags = ['SPY_FAMILY', 'スパイファミリー']
    folder_name = 'spy-family'

    PAGE_PREFIX = website
    FINAL_EPISODE = 25
    IMAGES_PER_EPISODE = 6

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        soup = self.get_soup(self.PAGE_PREFIX)
        self.download_character(soup)
        self.download_media(soup)

    def download_episode_preview(self):
        image_url_template = self.PAGE_PREFIX + 'assets/img/episodes/episode%s_%s.jpg'
        for i in range(self.FINAL_EPISODE):
            for j in range(self.IMAGES_PER_EPISODE):
                image_name = str(i + 1).zfill(2) + '_' + str(j + 1)
                if not self.is_image_exists(image_name):
                    image_url = image_url_template % (str(i + 1), str(j + 1))
                    result = self.download_image(image_url, self.base_folder + '/' + image_name)
                    if result == -1:
                        return

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='li.newsLists__item',
                                    date_select='time', title_select='.newsLists--title', id_select='a',
                                    paging_type=3, paging_suffix='?paged=%s', next_page_select='.wp-pagenavi *',
                                    next_page_eval_index_class='current', next_page_eval_index=-1)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz1', 'https://pbs.twimg.com/media/FDCUAXsagAArKcA?format=jpg&name=4096x4096')
        self.add_to_image_list('tz2', 'https://pbs.twimg.com/media/FDCUBF7akAEMcUM?format=jpg&name=4096x4096')
        self.download_image_list(folder)

    def download_character(self, soup=None):
        folder = self.create_character_directory()
        try:
            if soup is None:
                soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.charaImgLists__imgWrap img[src]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].replace('./', '')
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')

    def download_media(self, soup=None):
        folder = self.create_media_directory()
        try:
            if soup is None:
                soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.bddvdLists__item img[src]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].replace('./', '')
                image_name = self.extract_image_name_from_url(image_url)
                if 'nowprinting' in image_name:
                    continue
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')

        # Blu-ray Bonus
        try:
            if soup is None:
                soup = self.get_soup(self.PAGE_PREFIX + 'bddvd/bddvd_tokuten.php')
            images = soup.select('.bddvdDetailWrap img[src]')
            self.image_list = []
            for image in images:
                image_src = image['src']
                if image_src.startswith('./'):
                    image_url = self.PAGE_PREFIX + image_src.replace('./', '')
                elif image_src.startswith('../'):
                    image_url = self.PAGE_PREFIX + image_src.replace('../', '')
                else:
                    image_url = image_src
                image_name = self.extract_image_name_from_url(image_url)
                if 'nowprinting' in image_name:
                    continue
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


# Summertime Render
class SummertimeRenderDownload(Spring2022AnimeDownload, NewsTemplate):
    title = 'Summertime Render'
    keywords = [title, 'Summer Time Rendering']
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
                if self.is_image_exists(episode + '_1'):
                    continue
                ep_soup = self.get_soup(a_tag['href'])
                if ep_soup is not None:
                    images = ep_soup.select('.story--main__slider img[src]')
                    self.image_list = []
                    for i in range(len(images)):
                        image_url = images[i]['src'].split('?')[0]
                        image_name = episode + '_' + str(i + 1)
                        self.add_to_image_list(image_name, image_url)
                    self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.md-news__li',
                                    date_select='.date', title_select='.ttl', id_select='a',
                                    next_page_select='ul.pagenation-list li',
                                    next_page_eval_index_class='is__current', next_page_eval_index=-1)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        # self.add_to_image_list('tz', self.PAGE_PREFIX + 'wp/wp-content/themes/summertime-teaser/_assets/images/kv/kv_pc.jpg')
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/E63h3z-VEAMtJYy?format=jpg&name=medium')
        self.add_to_image_list('kv1', self.PAGE_PREFIX + 'wp/wp-content/uploads/2021/11/サマータイムレンダ_KV1_logomini.jpg')
        self.add_to_image_list('kv2', self.PAGE_PREFIX + 'wp/wp-content/uploads/2022/02/STR_KV2_logomini.jpg')
        self.add_to_image_list('kv_004_pc2', self.PAGE_PREFIX + 'wp/wp-content/themes/summertime-main/_assets/images/top/kv/kv_004_pc2.png')
        # self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/FG8lGwpaMAc7Aj3?format=jpg&name=large')
        self.download_image_list(folder)

        template = self.PAGE_PREFIX + 'wp/wp-content/themes/summertime-main/_assets/images/top/kv/kv_%s_pc.png'
        self.download_by_template(folder, template, 3, 1)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            images = soup.select('.chardata--v--img img')
            self.image_list = []
            for image in images:
                if image.has_attr('src'):
                    image_url = image['src']
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Tate no Yuusha no Nariagari S2
class TateNoYuusha2Download(Spring2022AnimeDownload):
    title = "Tate no Yuusha no Nariagari Season 2"
    keywords = [title, "The Rising of the Shield Hero", "2nd"]
    website = "http://shieldhero-anime.jp"
    twitter = 'shieldheroanime'
    hashtags = ['shieldhero', '盾の勇者の成り上がり']
    folder_name = 'tate-no-yuusha2'

    PAGE_PREFIX = website + '/2nd'
    FINAL_EPISODE = 13
    IMAGES_PER_EPISODE = 6

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
            soup = self.get_soup(self.PAGE_PREFIX)
            stories = soup.select('.p-story_contents')
            for story in stories:
                try:
                    episode = str(int(story.select('p.no')[0].text)).zfill(2)
                except:
                    continue
                images = story.select('div.images.is-lg div.main img[src]')
                self.image_list = []
                for i in range(len(images)):
                    image_url = self.PAGE_PREFIX + images[i]['src'].split('?')[0]
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_guess(self):
        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + '/assets/img/2nd/story/%s/img_%s.jpg'
        is_success = False
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1'):
                continue
            stop = False
            for j in range(self.IMAGES_PER_EPISODE):
                image_url = template % (str(i + 1), str(j))
                image_name = episode + '_' + str(j + 1)
                result = self.download_image(image_url, folder + '/' + image_name)
                if result == -1:
                    stop = True
                    break
                elif result == 0:
                    is_success = True
            if is_success:
                print(self.__class__.__name__ + ' - Episode %s guessed correctly!' % episode)
            if stop:
                break
        return is_success

    def download_news(self):
        news_url = self.website + '/news/'
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
                    if date.startswith('2019.08') or (news_obj
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

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('announce', 'https://pbs.twimg.com/media/EDag4MkUwAAQnf0?format=jpg&name=medium')
        self.add_to_image_list('kv1', 'https://pbs.twimg.com/media/EhHFvyVU4AA7cUw?format=jpg&name=large')
        self.add_to_image_list('mv_lg', self.PAGE_PREFIX + '/assets/img/2nd/mv_lg.jpg')
        self.add_to_image_list('kv2', 'https://pbs.twimg.com/media/FLKADbeaMAMa18f?format=jpg&name=4096x4096')
        self.add_to_image_list('mv_lg_3', self.PAGE_PREFIX + '/assets/img/2nd/mv_lg_3.jpg')
        self.add_to_image_list('kv3_tw', 'https://pbs.twimg.com/media/FOwQJqBaAAIvrpw?format=jpg&name=large')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + '/assets/img/2nd/chara/char_%s.png'
        self.download_by_template(folder, template, 3, 0)


# Yuusha, Yamemasu
class YuuyameDownload(Spring2022AnimeDownload, NewsTemplate):
    title = 'Yuusha, Yamemasu'
    keywords = [title, "I'm Quitting Heroing", 'yuuyame']
    website = 'https://yuuyame.com/'
    twitter = 'yuuyame_anime'
    hashtags = ['yuuyame', '勇やめ']
    folder_name = 'yuuyame'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

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
        template = self.PAGE_PREFIX + 'images/story/%s/p_%s.jpg'
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
        # Need update for paging
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='div.newsPaging article',
                                    title_select='div.news_list_title', date_select='div.news_list_day',
                                    id_select='a', a_tag_prefix=self.PAGE_PREFIX, date_separator='/',
                                    news_prefix='news.html')

    def download_episode_preview_external(self):
        jp_title = '勇者、辞めます'
        AniverseMagazineScanner(jp_title, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20220407', download_id=self.download_id).run()

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/FCEakgUXMAYyVuC?format=jpg&name=large')
        self.add_to_image_list('kv1_1', self.PAGE_PREFIX + 'images/news/p_001.jpg')
        self.add_to_image_list('kv1_2', self.PAGE_PREFIX + 'images/top/v_001.jpg')
        self.add_to_image_list('kv2_tw', 'https://pbs.twimg.com/media/FL3ta3HUUAQm59j?format=jpg&name=medium')
        self.add_to_image_list('kv2_2', self.PAGE_PREFIX + 'images/top/v_002_02.jpg')
        self.add_to_image_list('kv2_2', self.PAGE_PREFIX + 'images/top/v_002_tab.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        prefix = self.PAGE_PREFIX + 'images/chara/'
        templates = [prefix + 'p_%s.png', prefix + 'f_%s_01.png', prefix + 'f_%s_02.png']
        self.download_by_template(folder, templates, 3, 1)

    def download_media(self):
        folder = self.create_media_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'package.html')
            images = soup.select('div.element img[src]')
            self.image_list = []
            for image in images:
                split1 = image['src'].split('/')
                if len(split1) > 1:
                    if 'nowpri' in split1[-1]:
                        continue
                    image_url = self.PAGE_PREFIX + image['src']
                    image_name = split1[-2] + '_' + split1[-1].split('.')[0]
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e)
