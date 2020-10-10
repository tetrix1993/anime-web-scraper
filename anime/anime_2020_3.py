import os
import anime.constants as constants
from anime.main_download import MainDownload
from datetime import datetime
from scan import AniverseMagazineScanner, MocaNewsScanner, WebNewtypeScanner

# Deca-Dence http://decadence-anime.com/ #デカダンス #DECA_DENCE @decadence_anime
# Dokyuu Hentai HxEros https://hxeros.com/ #エグゼロス #hxeros @hxeros_anime [WED]
# Kanojo, Okarishimasu https://kanokari-official.com/ #かのかり #kanokari @kanokari_anime [WED]
# Maou Gakuin no Futekigousha https://maohgakuin.com/ #魔王学院 @maohgakuin [MON]
# Monster Musume no Oishasan https://mon-isha-anime.com/character/ #モン医者 #m_doctor @mon_isha_anime [FRI]
# Peter Grill to Kenja no Jikan http://petergrill-anime.jp/ #賢者タイムアニメ #petergrill @petergrillanime [FRI]
# Re:Zero S2 http://re-zero-anime.jp/tv/story/ #rezero #リゼロ @Rezero_official [MON]
# Uzaki-chan wa Asobitai! https://uzakichan.com/ #宇崎ちゃん @uzakichan_asobi [MON]
# Yahari Ore no Seishun http://www.tbs.co.jp/anime/oregairu/story/ #俺ガイル #oregairu @anime_oregairu [THU]


# Summer 2020 Anime
class Summer2020AnimeDownload(MainDownload):
    season = "2020-3"
    season_name = "Summer 2020"

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/2020-3"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)


# Deca-Dence
class DecaDenceDownload(Summer2020AnimeDownload):
    title = 'Deca-Dence'
    keywords = [title]

    LAST_EPISODE = 12

    def __init__(self):
        super().__init__()
        self.init_base_folder('decadence')

    def run(self):
        self.download_episode_preview()

    def download_episode_preview(self):
        if self.is_image_exists(str(self.LAST_EPISODE) + '_6'):
            return

        image_url_template = 'http://decadence-anime.com/assets/story/%s_%s.jpg'
        for i in range(self.LAST_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1'):
                continue
            for j in range(1, 7, 1):
                image_name = episode + '_' + str(j)
                image_url = image_url_template % (str(i + 1), str(j))
                result = self.download_image(image_url, self.base_folder + '/' + image_name)
                if result == -1:
                    return


# Dokyuu Hentai HxEros
class HxErosDownload(Summer2020AnimeDownload):
    title = "Dokyuu Hentai HxEros"
    keywords = [title]

    PAGE_PREFIX = 'https://hxeros.com'
    STORY_PAGE = 'https://hxeros.com/story/'

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/hxeros"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_character()
        self.download_bluray()

    def download_episode_preview(self):
        #self.has_website_updated(self.STORY_PAGE)
        try:
            soup = self.get_soup(self.STORY_PAGE)
            episode_tags = soup.find('ul', class_='storynav').find_all('a')
            for episode_tag in episode_tags:
                try:
                    episode = str(int(episode_tag.text)).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                episode_url = self.PAGE_PREFIX + episode_tag['href']
                episode_soup = self.get_soup(episode_url)
                story_slider = episode_soup.find('div', class_='story__slider')
                if story_slider is not None:
                    images = story_slider.find_all('img')
                    image_objs = []
                    for i in range(len(images)):
                        image_name = episode + '_' + str(i + 1)
                        image_url = self.STORY_PAGE + images[i]['src']
                        image_objs.append({'name': image_name, 'url': image_url})
                    self.download_image_objects(image_objs, self.base_folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_key_visual(self):
        filepath = self.create_key_visual_directory()
        image_objs = [
            {'name': 'teaser', 'url': 'https://pbs.twimg.com/media/EIRucj0XkAUJTsE?format=jpg&name=medium'},
            {'name': 'kv', 'url': 'https://pbs.twimg.com/media/ESLTIUOVAAAWQ5L?format=jpg&name=4096x4096'},
            {'name': 'kv_web', 'url': 'https://hxeros.com/assets/img/top/ph_main.jpg'},
            {'name': 'kv2', 'url': 'https://pbs.twimg.com/media/EZo3lpqUEAEH3Xp?format=jpg&name=4096x4096'},
            {'name': 'kv2_web', 'url': 'https://hxeros.com/assets/img/top/ph_main_2.jpg'},
            {'name': 'ph_main_kirara', 'url': 'https://hxeros.com/assets/img/top/ph_main_kirara.jpg'},
            {'name': 'ph_main_kirara_twitter', 'url': 'https://pbs.twimg.com/media/EeVou8SU8AAQ3CO?format=jpg&name=900x900'}
        ]
        self.download_image_objects(image_objs, filepath)

    def download_character(self):
        character_folder = self.create_character_directory()
        try:
            # Main Characters
            image_objs = [
                {'name': 'retto', 'url': 'https://hxeros.com/assets/img/character/single/retto/ph_character.png'},
                {'name': 'kirara', 'url': 'https://hxeros.com/assets/img/character/single/kirara/ph_character.png'},
                {'name': 'momoka', 'url': 'https://hxeros.com/assets/img/character/single/momoka/ph_character.png'},
                {'name': 'sora', 'url': 'https://hxeros.com/assets/img/character/single/sora/ph_character.png'},
                {'name': 'maihime', 'url': 'https://hxeros.com/assets/img/character/single/maihime/ph_character.png'}]
            for image_obj in image_objs:
                if os.path.exists(character_folder + '/' + image_obj['name'] + '.png'):
                    continue
                filepath_without_extension = character_folder + '/' + image_obj['name']
                self.download_image(image_obj['url'], filepath_without_extension)
        except Exception as e:
                print("Error in running " + self.__class__.__name__ + ' - Character')
                print(e)

        # Other characters
        try:
            soup = self.get_soup('https://hxeros.com/character/')
            other_urls = soup.find_all('ul', class_='character__thumblist')[1].find_all('a')
            for other_url in other_urls:
                url = self.PAGE_PREFIX + other_url['href']
                try:
                    other_soup = self.get_soup(url)
                    pictures = other_soup.find_all('picture')
                    image_objs = []
                    for picture in pictures:
                        if picture is not None:
                            image = picture.find('img')
                            if image is not None:
                                image_url = self.PAGE_PREFIX + image['src']
                                image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                                image_objs.append({'name': image_name, 'url': image_url})
                    self.download_image_objects(image_objs, character_folder)
                except:
                    pass
        except:
            pass

    def download_bluray(self):
        bd_url = 'https://hxeros.com/bddvd/%s.html'
        self.has_website_updated(bd_url % str(1))
        folder = self.create_bluray_directory()
        image_objs = [
            {'name': 'bd_1_big', 'url': 'https://pbs.twimg.com/media/EeQ8-JEU8AIPA8t?format=jpg&name=4096x4096'}
        ]
        try:
            first_page_image_count = 0
            for i in range(1, 7, 1):
                url = bd_url % str(i)
                soup = self.get_soup(url)
                image_count = 0
                bddvd_item = 'bddvd__item'
                bddvd_shop = 'bddvd__shop'
                classes = [bddvd_item, bddvd_shop]
                for class_ in classes:
                    if i != 1 and class_ == bddvd_shop:
                        continue
                    article_tag = soup.find('article', class_=class_)
                    if article_tag is not None:
                        images = article_tag.find_all('img')
                        if images is not None and len(images) > 0:
                            if class_ == bddvd_item:
                                if i == 1:
                                    first_page_image_count = len(images)
                                else:
                                    image_count = len(images)
                            bd_image_count = 0
                            for image in images:
                                image_url = self.PAGE_PREFIX + image['src']
                                if 'ico_aniplexplus.svg' in image_url:
                                    continue
                                if class_ == bddvd_item:
                                    bd_image_count += 1
                                    if bd_image_count > 1:
                                        image_name = 'bd_' + str(i) + '_' + str(bd_image_count)
                                    else:
                                        image_name = 'bd_' + str(i)
                                else:
                                    image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                                image_objs.append({'name': image_name, 'url': image_url})
                self.download_image_objects(image_objs, folder)
                if (i > 1 and image_count != first_page_image_count) or first_page_image_count == 1:
                    break
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Blu-Ray')
            print(e)


# Kanojo, Okarishimasu
class KanokariDownload(Summer2020AnimeDownload):
    title = "Kanojo, Okarishimasu"
    keywords = [title, "Kanokari", "Rent-a-Girlfriend"]

    STORY_PAGE = 'https://kanokari-official.com/story/'

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/kanokari"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_character()
        self.download_bluray()
        self.download_other()

    def download_episode_preview(self):
        self.has_website_updated(self.STORY_PAGE)
        image_objs = []
        try:
            soup = self.get_soup(self.STORY_PAGE)
            chapters = soup.find_all('div', class_='story-main__detail__block')
            for chapter in chapters:
                episode_tag = chapter.find('span', class_='num')
                if episode_tag is None:
                    continue
                try:
                    episode = str(episode_tag.text).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                slides = chapter.find_all('div', class_='swiper-slide')
                if slides is not None and len(slides) > 0:
                    for i in range(len(slides)):
                        image = slides[i].find('img')
                        if image is not None:
                            image_url = image['src']
                            image_name = episode + '_' + str(i + 1)
                            image_objs.append({'name': image_name, 'url': image_url})
                    self.download_image_objects(image_objs, self.base_folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_key_visual(self):
        keyvisual_folder = self.create_key_visual_directory()
        image_objs = [
            {'name': 'chara_new_kv1', 'url': 'https://kanokari-official.com/wp/wp-content/themes/kanokari_main/_assets/images/slider/kv_chizuru.jpg'},
            {'name': 'chara_new_kv2', 'url': 'https://kanokari-official.com/wp/wp-content/themes/kanokari_main/_assets/images/slider/kv_mami.jpg'},
            {'name': 'chara_new_kv3', 'url': 'https://kanokari-official.com/wp/wp-content/themes/kanokari_main/_assets/images/slider/kv_ruka.jpg'},
            {'name': 'chara_new_kv4', 'url': 'https://kanokari-official.com/wp/wp-content/themes/kanokari_main/_assets/images/slider/kv_sumi.jpg'},
            {'name': 'chara_kv1', 'url': 'https://kanokari-official.com/wp/wp-content/uploads/2020/03/mv01.jpg'},
            {'name': 'chara_kv2', 'url': 'https://kanokari-official.com/wp/wp-content/uploads/2020/03/mv02.jpg'},
            {'name': 'chara_kv3', 'url': 'https://kanokari-official.com/wp/wp-content/uploads/2020/03/ruka_KV.jpg'},
            {'name': 'chara_kv4', 'url': 'https://kanokari-official.com/wp/wp-content/uploads/2020/03/sumi_KV0322.jpg'},
            {'name': 'kv_web', 'url': 'https://kanokari-official.com/wp/wp-content/themes/kanokari_main/_assets/images/slider/kv_main.jpg'},
            {'name': 'kv', 'url': 'https://pbs.twimg.com/media/EYwr-OVU8AANFm4?format=jpg&name=large'},
            {'name': 's2_announce', 'url': 'https://kanokari-official.com/wp/wp-content/themes/kanokari_main/_assets/images/top/newsvisual_season2.jpg'},
        ]
        self.download_image_objects(image_objs, keyvisual_folder)

    def download_character(self):
        character_folder = self.create_character_directory()
        image_objs = [
            {'name': 'chara_body01', 'url': 'https://kanokari-official.com/wp/wp-content/themes/kanokari_teaser/assets/img/top/chara/chara_body01.png'},
            {'name': 'chara_body02', 'url': 'https://kanokari-official.com/wp/wp-content/themes/kanokari_teaser/assets/img/top/chara/chara_body02.png'},
            {'name': 'chara_body03', 'url': 'https://kanokari-official.com/wp/wp-content/themes/kanokari_teaser/assets/img/top/chara/chara_body03.png'},
            {'name': 'chara_body04', 'url': 'https://kanokari-official.com/wp/wp-content/themes/kanokari_teaser/assets/img/top/chara/chara_body04.png'},
            {'name': 'chara_body05', 'url': 'https://kanokari-official.com/wp/wp-content/themes/kanokari_teaser/assets/img/top/chara/chara_body05.png'},
            {'name': 'chara_yt01', 'url': 'https://kanokari-official.com/wp/wp-content/uploads/2020/03/かのかり_千鶴PV-06.jpg'},
            {'name': 'chara_yt02', 'url': 'https://kanokari-official.com/wp/wp-content/uploads/2020/03/かのかり_麻美PV-01.jpg'},
            {'name': 'chara_yt03', 'url': 'https://kanokari-official.com/wp/wp-content/uploads/2020/03/かのかり_瑠夏PV-06.jpg'},
            {'name': 'chara_yt04', 'url': 'https://kanokari-official.com/wp/wp-content/uploads/2020/03/かのかり_墨PV-06.jpg'}]
        try:
            soup = self.get_soup("https://kanokari-official.com/character/")
            chara_details = soup.find_all('div', class_='visual-chara')
            for chara_detail in chara_details:
                image = chara_detail.find('img')
                image_url = image['src']
                image_with_extension = self.extract_image_name_from_url(image_url, with_extension=True)
                if os.path.exists(character_folder + '/' + image_with_extension):
                    continue
                image_without_extension = self.extract_image_name_from_url(image_url, with_extension=False)
                image_objs.append({'name': image_without_extension, 'url': image_url})
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Character')
            print(e)
        self.download_image_objects(image_objs, character_folder)

    def download_bluray(self):
        bluray_folder = self.create_bluray_directory()
        url_template = 'https://kanokari-official.com/bluray/vol%s/'

        image_objs = [
            {'name': 'ゲーマーズ1巻特典_c', 'url': 'https://kanokari-official.com/wp/wp-content/uploads/2020/08/ゲーマーズ1巻特典_c.jpg'},
            {'name': 'ゲーマーズ_描き下ろし_c', 'url': 'https://kanokari-official.com/wp/wp-content/uploads/2020/08/ゲーマーズ_描き下ろし_c.jpg'},
            {'name': 'アニメイト_描き下ろし_c', 'url': 'https://kanokari-official.com/wp/wp-content/uploads/2020/08/アニメイト_描き下ろし_c.jpg'},
            {'name': 'とらのあな_描き下ろし_c', 'url': 'https://kanokari-official.com/wp/wp-content/uploads/2020/08/とらのあな_描き下ろし_c.jpg'},
            {'name': 'ソフマップ_描き下ろし_c', 'url': 'https://kanokari-official.com/wp/wp-content/uploads/2020/08/ソフマップ_描き下ろし_c.jpg'},
            {'name': 'Amazon_描き下ろし_c', 'url': 'https://kanokari-official.com/wp/wp-content/uploads/2020/08/Amazon_描き下ろし_c.jpg'},
            {'name': 'kanokari_gamers_kokai_s', 'url': 'http://kanokari-official.com/wp/wp-content/uploads/2020/08/kanokari_gamers_kokai_s.jpg'}
        ]
        self.download_image_objects(image_objs, bluray_folder)

        try:
            stop = False
            for i in range(1, 5, 1):
                image_objs = []
                bluray_url = url_template % str(i)
                soup = self.get_soup(bluray_url)
                bluray_div = soup.find('div', class_='bluray-main')
                if bluray_div is None:
                    break
                images = bluray_div.find_all('img')
                if images is None or len(images) == 0:
                    break
                for image in images:
                    image_url = image['src']
                    if 'nowprinting' in image_url:
                        stop = True
                        break
                    image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                    image_objs.append({'name': image_name, 'url': image_url})
                if stop:
                    break
                self.download_image_objects(image_objs, bluray_folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Blu-Ray')
            print(e)

        image_objs = [
            {'name': 'music_ed', 'url': 'https://kanokari-official.com/wp/wp-content/uploads/2020/05/halca_H1_kikan_c.jpg'}
        ]
        bd_bonus_page_url = 'https://kanokari-official.com/bluray/store/'
        self.has_website_updated(url=bd_bonus_page_url, cache_name='bd_bonus')
        try:
            soup = self.get_soup(bd_bonus_page_url)
            bonus_blocks = soup.find_all('li')
            if bonus_blocks is not None and len(bonus_blocks) > 0:
                for bonus_block in bonus_blocks:
                    images = bonus_block.find_all('div', class_='slider__img')
                    if images is not None and len(images) > 0:
                        for image in images:
                            try:
                                image_url = image['style'].split('url(')[1].split(');')[0]
                                image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                                image_objs.append({'name': image_name, 'url': image_url})
                            except:
                                pass
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Blu-Ray Bonus')
            print(e)
        self.download_image_objects(image_objs, bluray_folder)

    def download_other(self):
        folder = self.create_custom_directory(constants.FOLDER_OTHER)
        image_objs = [
            {'name': 'mygirl_vol30', 'url': 'https://images-na.ssl-images-amazon.com/images/I/716PmdvklHL.jpg'},
            {'name': 'daki_dmm_main', 'url': 'https://pbs.twimg.com/media/EfNKzGQVAAA224h?format=jpg&name=medium'},
            {'name': 'daki_dmm1', 'url': 'https://pics.dmm.com/mono/hobby/cha_202008ddmpza863/cha_202008ddmpza863pl.jpg'},
            {'name': 'daki_dmm2', 'url': 'https://pics.dmm.com/mono/hobby/cha_202008ddmpza864/cha_202008ddmpza864pl.jpg'},
            {'name': 'daki_dmm3', 'url': 'https://pics.dmm.com/mono/hobby/cha_202008ddmpza865/cha_202008ddmpza865pl.jpg'},
            {'name': 'daki_dmm4', 'url': 'https://pics.dmm.com/mono/hobby/cha_202008ddmpza866/cha_202008ddmpza866pl.jpg'}
        ]
        self.download_image_objects(image_objs, folder)


# Maou Gakuin no Futekigousha: Shijou Saikyou no Maou no Shiso, Tensei shite Shison-tachi no Gakkou e
class MaohgakuinDownload(Summer2020AnimeDownload):
    title = "Maou Gakuin no Futekigousha: Shijou Saikyou no Maou no Shiso, Tensei shite Shison-tachi no Gakkou e"
    keywords = [title, 'Maohgakuin']

    PAGE_PREFIX = "https://maohgakuin.com/"
    CHARACTER_PREFIX = 'https://maohgakuin.com/character/'
    STORY_PAGE = 'https://maohgakuin.com/story/'

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/maohgakuin"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_character()
        self.download_bluray()
        self.download_other()

    def download_episode_preview(self):
        #self.has_website_updated(self.STORY_PAGE)
        try:
            soup = self.get_soup(self.STORY_PAGE)
            episodes = soup.find('nav', class_='page_nav').find_all('a')
            for episode_tag in episodes:
                episode_num = ''
                try:
                    episode_num = str(int(episode_tag.text)).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode_num + '_1'):
                    continue
                episode_url = self.STORY_PAGE + episode_tag['href'].replace('./', '')
                episode_soup = self.get_soup(episode_url)
                image_container = episode_soup.find('div', class_='main_image')
                if image_container is not None:
                    images = image_container.find_all('img')
                    if images is not None and len(images) > 0:
                        image_objs = []
                        for i in range(len(images)):
                            image_url = self.STORY_PAGE + images[i]['src']
                            image_name = episode_num + '_' + str(i + 1)
                            image_objs.append({'name': image_name, 'url': image_url})
                        self.download_image_objects(image_objs, self.base_folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)
        WebNewtypeScanner('魔王学院の不適合者', self.base_folder, 13).run()

    def download_key_visual(self):
        keyvisual_folder = self.create_key_visual_directory()
        image_objs = [
            #{'name': 'kv', 'url': 'https://maohgakuin.com/assets/img/top/kv.jpg'}
            {'name': 'kv', 'url': 'https://pbs.twimg.com/media/EZbC3ljUMAEAkei?format=jpg&name=4096x4096'},
            {'name': 'kv2', 'url': 'https://pbs.twimg.com/media/EZaMb5WUEAAxxIg?format=jpg&name=4096x4096'}]
        self.download_image_objects(image_objs, keyvisual_folder)

    def download_character(self):
        character_folder = self.create_character_directory()
        try:
            soup = self.get_soup("https://maohgakuin.com/character/")
            chara_details = soup.find('div', class_='chara_list').find_all('li')
            for chara_detail in chara_details:
                thumb_image_url = self.PAGE_PREFIX + chara_detail.find('img')['src'].replace('../', '')
                image_with_extension = self.extract_image_name_from_url(thumb_image_url, with_extension=True)
                if os.path.exists(character_folder + '/' + image_with_extension):
                    continue
                image_urls = [thumb_image_url]
                chara_url = self.CHARACTER_PREFIX + chara_detail.find('a')['href'].replace('./', '')
                chara_soup = self.get_soup(chara_url)
                chara_detail = chara_soup.find('div', class_='chara_detail')
                image_urls.append(self.PAGE_PREFIX + chara_detail.find('p', class_='stand_image')
                                  .find('img')['src'].replace('../', ''))
                image_urls.append(self.PAGE_PREFIX + chara_detail.find('div', class_='face_image')
                                  .find('img')['src'].replace('../', ''))

                for image_url in image_urls:
                    image_with_extension = self.extract_image_name_from_url(image_url, with_extension=True)
                    if os.path.exists(character_folder + '/' + image_with_extension):
                        continue
                    image_without_extension = self.extract_image_name_from_url(image_url, with_extension=False)
                    filepath_without_extension = character_folder + '/' + image_without_extension
                    self.download_image(image_url, filepath_without_extension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Character')
            print(e)

    def download_bluray(self):
        folder = self.create_bluray_directory()
        image_objs = [
            {'name': 'music_ed', 'url': 'https://pbs.twimg.com/media/Eb6ctYuU8AEVilj?format=jpg&name=large'},
            {'name': 'bd_1_big', 'url': 'https://pbs.twimg.com/media/EfdVYazU0AcE6VM?format=jpg&name=4096x4096'},
            {'name': 'bd_2_big', 'url': 'https://pbs.twimg.com/media/EjTvsaZUcAAnOHS?format=jpg&name=medium'},
            {'name': 'bd_bonus_1', 'url': 'https://pbs.twimg.com/media/Ei1XmM2UcAA8Ha4?format=jpg&name=medium'},
        ]
        self.download_image_objects(image_objs, folder)
        
        try:
            bd_url = 'https://maohgakuin.com/products/'
            stop = False
            for i in range(1, 7, 1):
                url = bd_url
                if i > 1:
                    url = bd_url + '?no=' + str(i)
                soup = self.get_soup(url)
                products_main = 'products_main'
                products_novelty = 'products_novelty'
                classes = [products_main, products_novelty]
                for class_ in classes:
                    image_objs = []
                    divs = soup.find_all('div', class_=class_)
                    if divs is not None and len(divs) > 0:
                        for div in divs:
                            images = div.find_all('img')
                            if images is not None and len(images) > 0:
                                bd_count = 0
                                for image in images:
                                    image_url = image['src']
                                    if len(image_url) < 2 or 'nowprinting' in image_url:
                                        if class_ == products_main:
                                            stop = True
                                        if i == 1:
                                            continue
                                        else:
                                            break
                                    if image_url[0] == '/':
                                        image_url = image_url[1:len(image_url)]
                                    image_url = self.PAGE_PREFIX + image_url
                                    if class_ == products_main:
                                        bd_count += 1
                                        image_name = 'bd_' + str(i)
                                        if bd_count > 1:
                                            image_name + '_' + str(bd_count)
                                    else:
                                        image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                                    image_objs.append({'name': image_name, 'url': image_url})
                    self.download_image_objects(image_objs, folder)
                if stop:
                    break
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Blu-Ray')
            print(e)

    def download_other(self):
        folder = self.create_custom_directory(constants.FOLDER_OTHER)
        image_objs = [
            {'name': 'radio', 'url': 'http://www.onsen.ag/program/maoh/image/781_pgi01_l.jpg'},
            {'name': 'radio_big', 'url': 'https://pbs.twimg.com/media/Edcd905UYAEphRb?format=jpg&name=large'},
            {'name': 'bs11_guide', 'url': 'https://pbs.twimg.com/media/EbZlqboUwAYVvCu?format=jpg&name=4096x4096'},
            {'name': 'ep_visual_1', 'url': 'https://pbs.twimg.com/media/EcFiPBSU0AADZI9?format=jpg&name=large'},
            {'name': 'image_ep1', 'url': 'https://maohgakuin.com/assets/img/image_ep1.jpg'},
            {'name': 'image_ep2', 'url': 'https://maohgakuin.com/assets/img/image_ep2.jpg'},
            {'name': 'image_ep3', 'url': 'https://maohgakuin.com/assets/img/image_ep3.jpg'},
            {'name': 'ep01_kinen', 'url': 'https://pbs.twimg.com/media/EcFzWEEUcAM0bOT?format=jpg&name=large'},
            {'name': 'ep01_kinen_2', 'url': 'https://pbs.twimg.com/media/EcoPPXsVAAEPdSf?format=jpg&name=4096x4096'},
            {'name': 'ep01_kinen_3', 'url': 'https://pbs.twimg.com/media/EdMlINcUcAASho3?format=jpg&name=large'},
            {'name': 'ep01_kinen_4', 'url': 'https://pbs.twimg.com/media/EdwjQJKU4AAJSBL?format=jpg&name=4096x4096'}
        ]
        self.download_image_objects(image_objs, folder)


# Monster Musume no Oishasan
class MonIshaDownload(Summer2020AnimeDownload):
    title = "Monster Musume no Oishasan"
    keywords = [title, "Monisha", "Mon-Isha"]

    PAGE_PREFIX = 'https://mon-isha-anime.com/'
    STORY_PAGE = 'https://mon-isha-anime.com/story/'

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/mon-isha"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_external()
        self.download_intro()
        self.download_key_visual()
        self.download_character()
        self.download_bluray()

    def download_episode_preview(self):
        #self.has_website_updated(self.STORY_PAGE)
        template_url = 'https://mon-isha-anime.com/images/story/introdution/st_ph%s_a%s.jpg'
        for i in range(13):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_01'):
                continue
            for j in range(10):
                image_name = episode + '_' + str(j + 1).zfill(2)
                image_url = template_url % (episode, str(j + 1).zfill(2))
                result = self.download_image(image_url, self.base_folder + '/' + image_name)
                if result == -1:
                    return

    def download_episode_preview_external(self):
        jp_title = 'モンスター娘のお医者さん'
        AniverseMagazineScanner(jp_title, self.base_folder, 12).run()
        #last_date = datetime.strptime('20200930', '%Y%m%d')
        #today = datetime.today()
        #if today < last_date:
        #    end_date = today
        #else:
        #    end_date = last_date
        #MocaNewsScanner(jp_title, self.base_folder, '20200710', end_date.strftime('%Y%m%d')).run()

    def download_intro(self):
        intro_folder = self.create_custom_directory(constants.FOLDER_INTRO)
        image_objs = []
        intro_image_url_template = 'https://mon-isha-anime.com/images/story/st_ph_a%s.jpg'
        for i in range(26):
            image_url = intro_image_url_template % str(i + 1).zfill(2)
            image_name = self.extract_image_name_from_url(image_url, with_extension=False)
            image_objs.append({'name': image_name, 'url': image_url})
        self.download_image_objects(image_objs, intro_folder)

    def download_key_visual(self):
        keyvisual_folder = self.base_folder + '/' + constants.FOLDER_KEY_VISUAL
        if not os.path.exists(keyvisual_folder):
            os.makedirs(keyvisual_folder)

        image_objs = [
            {'name': 'teaser', 'url': 'https://pbs.twimg.com/media/EJTToJMU0AEgpMK?format=jpg&name=medium'},
            {'name': 'kv', 'url': 'https://pbs.twimg.com/media/ETrymlxU0AA0Oep?format=jpg&name=medium'}]
        for image_obj in image_objs:
            if os.path.exists(keyvisual_folder + '/' + image_obj['name'] + '.png') or \
                    os.path.exists(keyvisual_folder + '/' + image_obj['name'] + '.jpg'):
                continue
            filepath_without_extension = keyvisual_folder + '/' + image_obj['name']
            self.download_image(image_obj['url'], filepath_without_extension)

    def download_character(self):
        character_folder = self.create_character_directory()
        try:
            soup = self.get_soup("https://mon-isha-anime.com/character/")
            chara_details = soup.find_all('div', class_='swinmob')
            for chara_detail in chara_details:
                images = chara_detail.find_all('img')
                for image in images:
                    image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                    image_with_extension = self.extract_image_name_from_url(image_url, with_extension=True)
                    if os.path.exists(character_folder + '/' + image_with_extension):
                        continue
                    image_without_extension = self.extract_image_name_from_url(image_url, with_extension=False)
                    filepath_without_extension = character_folder + '/' + image_without_extension
                    self.download_image(image_url, filepath_without_extension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Character')
            print(e)

    def download_bluray(self):
        folder = self.create_bluray_directory()
        image_objs = []
        try:
            bd_urls = ['index', 'tokuten']
            for bd_url in bd_urls:
                url = 'https://mon-isha-anime.com/products/bd/%s.html' % bd_url
                soup = self.get_soup(url)
                innertx = soup.find('div', class_='mu_innertx')
                if innertx is None:
                    continue
                images = innertx.find_all('img')
                for image in images:
                    image_url = self.PAGE_PREFIX + image['src'].replace('../../', '')
                    image_name = self.extract_image_name_from_url(image_url)
                    image_objs.append({'name': image_name, 'url': image_url})
                self.download_image_objects(image_objs, folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Bluray')
            print(e)


# Peter Grill to Kenja no Jikan
class PeterGrillDownload(Summer2020AnimeDownload):
    title = "Peter Grill to Kenja no Jikan"
    keywords = [title, "Peter Grill and the Philosopher's Time"]

    PAGE_PREFIX = 'http://petergrill-anime.jp/'

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/petergrill"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        self.download_episode_preview()
        #self.download_episode_preview_external()
        self.download_key_visual()
        self.download_character()
        self.download_bluray()
        self.download_other()

    def download_episode_preview(self):
        #self.has_website_updated(self.PAGE_PREFIX)
        try:
            soup = self.get_soup('http://petergrill-anime.jp/works.php')
            episode_list_items = soup.find_all('li', class_='episode_list_item')
            for episode_list_item in episode_list_items:
                para = episode_list_item.find('p', class_='episode_list_honbun')
                if para is not None:
                    para_text = para.text
                    if '第' in para_text and '話' in para_text:
                        try:
                            episode = str(int(para_text.split('第')[1].split('話')[0])).zfill(2)
                        except:
                            continue
                        if self.is_image_exists(episode + '_1'):
                            continue
                        episode_link_tag = episode_list_item.find('a')
                        if episode_link_tag is not None and episode_link_tag.has_attr('href'):
                            episode_url = self.PAGE_PREFIX + episode_link_tag['href']
                            episode_soup = self.get_soup(episode_url)
                            episode_images = episode_soup.find('div', class_='episode_images')
                            if episode_images is not None:
                                slider = episode_images.find('ul', class_='slider')
                                if slider is not None:
                                    images = slider.find_all('img')
                                    image_objs = []
                                    for i in range(len(images)):
                                        image_url = images[i]['src'].replace('../', self.PAGE_PREFIX)
                                        image_name = episode + '_' + str(i + 1)
                                        image_objs.append({'name': image_name, 'url': image_url})
                                    self.download_image_objects(image_objs, self.base_folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

        template_url = 'http://petergrill-anime.jp/images/upload/pg%s_still_%s.png'
        for i in range(13):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1'):
                continue
            for j in range(6):
                image_name = episode + '_' + str(j + 1)
                image_url = template_url % (episode, str(j + 1).zfill(2))
                result = self.download_image(image_url, self.base_folder + '/' + image_name)
                if result == -1:
                    return

    def download_episode_preview_external(self):
        try:
            jp_title = 'ピーター・グリルと賢者の時間'
            AniverseMagazineScanner(jp_title, self.base_folder, 12).run()
            last_date = datetime.strptime('20200930', '%Y%m%d')
            today = datetime.today()
            if today < last_date:
                end_date = today
            else:
                end_date = last_date
            MocaNewsScanner(jp_title, self.base_folder, '20200709', end_date.strftime('%Y%m%d')).run()
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Aniverse')
            print(e)

    def download_key_visual(self):
        keyvisual_folder = self.create_key_visual_directory()
        image_objs = [
            {'name': 'kv', 'url': 'http://petergrill-anime.jp/images/key_v_202003.png'}]
        self.download_image_objects(image_objs, keyvisual_folder)

    def download_character(self):
        character_folder = self.create_character_directory()
        try:
            soup = self.get_soup("http://petergrill-anime.jp/character.php")
            chara_details = soup.find_all('li', class_='character_item')
            for chara_detail in chara_details:
                images = chara_detail.find_all('img')
                for image in images:
                    if 'upload' not in image['src']:
                        continue
                    image_url = self.PAGE_PREFIX + image['src']
                    image_with_extension = self.extract_image_name_from_url(image_url, with_extension=True)
                    if os.path.exists(character_folder + '/' + image_with_extension):
                        continue
                    image_without_extension = self.extract_image_name_from_url(image_url, with_extension=False)
                    filepath_without_extension = character_folder + '/' + image_without_extension
                    self.download_image(image_url, filepath_without_extension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Character')
            print(e)

    def download_bluray(self):
        folder = self.create_bluray_directory()
        image_objs = [
            {'name': 'bd_1_1', 'url': 'https://aniverse-mag.com/wp-content/uploads/2020/07/200702_01.jpg'},
            {'name': 'bd_1_2', 'url': 'https://aniverse-mag.com/wp-content/uploads/2020/07/200702_02.jpg'},
            {'name': 'bd_2_1', 'url': 'http://petergrill-anime.jp/images/upload/pg_dvd2.png'},
            {'name': 'bd_3_1', 'url': 'http://petergrill-anime.jp/images/upload/pg_dvd3.png'},
            {'name': 'bd_bonus_1', 'url': 'https://ecdnimg.toranoana.jp/ec/img/21/0006/61/50/210006615043-1p.jpg'},
            {'name': 'bd_bonus_2', 'url': 'https://www.gamers.co.jp/resize_image.php?image=08181030_5f3b2f360cd25.jpg'},
        ]
        self.download_image_objects(image_objs, folder)

    def download_other(self):
        folder = self.create_custom_directory('other')
        image_objs = [{'name': 'daki_dmm1', 'url': 'https://scratch.dmm.com/s3/prize/TPasD0NgnkpbYKeCf29Kq3vPX0Ylm4HPRLihP4G5.jpeg'}]
        self.download_image_objects(image_objs, folder)


# Re:Zero kara Hajimeru Isekai Seikatsu 2nd Season
class ReZero2Download(Summer2020AnimeDownload):
    title = "Re:Zero kara Hajimeru Isekai Seikatsu 2nd Season"
    keywords = [title, "rezero", "Re:Zero - Starting Life in Another World"]

    STORY_PAGE = "http://re-zero-anime.jp/tv/story/"
    PAGE_PREFIX = 'http://re-zero-anime.jp/tv/'

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/rezero2"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_bluray()

    def download_episode_preview(self):
        #self.has_website_updated(self.STORY_PAGE)
        image_url_template = 'http://re-zero-anime.jp/tv/assets/episode/%s/%s.jpg'
        episode = 25
        while True:
            episode += 1
            if self.is_image_exists(str(episode) + '_1'):
                continue
            for j in range(6):
                image_url = image_url_template % (str(episode), str(j + 1))
                image_name = str(episode) + '_' + str(j + 1)
                result = self.download_image(image_url, self.base_folder + '/' + image_name)
                if result == -1:
                    return

    def download_key_visual(self):
        keyvisual_folder = self.create_key_visual_directory()
        image_objs = [
            #{'name': 'kv_old', 'url': 'http://re-zero-anime.jp/tv/assets/top/main-tv1r.jpg'},
            {'name': 'kv', 'url': 'http://re-zero-anime.jp/tv/assets/top/main-tv2.jpg'},
            {'name': 'kv2', 'url': 'http://re-zero-anime.jp/tv/assets/top/main-tv2b.jpg'}]
        self.download_image_objects(image_objs, keyvisual_folder)

    def download_bluray(self):
        bluray_url = 'http://re-zero-anime.jp/tv/bluray/'
        self.has_website_updated(bluray_url, 'bluray')
        folder = self.create_bluray_directory()
        image_objs = []
        try:
            soup = self.get_soup(bluray_url)
            sections = soup.find_all('section')
            if sections is None or len(sections) == 0:
                return
            for section in sections:
                if not section.has_attr('id'):
                    continue
                section_id = section['id']
                bd_prefix = ''
                if len(section_id) == 3 and section_id[0:2] == 'Bd' and section_id[2].isnumeric():
                    bd_prefix = 'bd' + section_id[2]
                images = section.find_all('img')
                if images is None or len(images) == 0:
                    continue
                for i in range(len(images)):
                    image = images[i]
                    image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                    if 'assets/bluray/np.png' in image_url:
                        continue
                    if len(bd_prefix) > 0:
                        if i == 0:
                            image_name = bd_prefix
                        else:
                            image_name = bd_prefix + '_' + str(i + 1)
                    else:
                        image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                    image_objs.append({'name': image_name, 'url': image_url})
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Blu-ray')
            print(e)
        self.download_image_objects(image_objs, folder)


# Uzaki-chan wa Asobitai!
class UzakiChanDownload(Summer2020AnimeDownload):
    title = "Uzaki-chan wa Asobitai!"
    keywords = [title, "Uzakichan"]

    PAGE_PREFIX = 'https://uzakichan.com/'

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/uzakichan"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_external()
        self.download_key_visual()
        self.download_bluray()

    def download_episode_preview(self):
        try:
            template = 'https://uzakichan.com/story/story%s_%s.png'
            for i in range(13):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_1'):
                    continue
                for j in range(6):
                    image_url = template % (episode, str(j + 1).zfill(2))
                    image_name = episode + '_' + str(j + 1)
                    result = self.download_image(image_url, self.base_folder + '/' + image_name)
                    if result == -1:
                        return
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_episode_preview_external(self):
        try:
            AniverseMagazineScanner('宇崎ちゃんは遊びたい', self.base_folder, 12).run()
            #last_date = datetime.strptime('20200930', '%Y%m%d')
            #today = datetime.today()
            #if today < last_date:
            #    end_date = today
            #else:
            #    end_date = last_date
            #MocaNewsScanner('宇崎ちゃんは遊びたい', self.base_folder, '20200703', end_date.strftime('%Y%m%d')).run()
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Aniverse')
            print(e)

    def download_key_visual(self):
        keyvisual_folder = self.create_key_visual_directory()
        image_objs = [
            {'name': 'kv', 'url': 'https://pbs.twimg.com/media/EP1u35XUEAAvg4f?format=jpg&name=large'},
            {'name': 'kv2', 'url': 'https://pbs.twimg.com/media/EXi1RaHUYAAVJPM?format=jpg&name=medium'}]
        self.download_image_objects(image_objs, keyvisual_folder)

    def download_bluray(self):
        bd_url = 'https://uzakichan.com/package.html'
        self.has_website_updated(bd_url, 'bd')
        folder = self.create_bluray_directory()
        image_objs = []
        try:
            soup = self.get_soup(bd_url)
            specialboxes = soup.find_all('div', class_='specialbox')
            for specialbox in specialboxes:
                images = specialbox.find_all('img')
                for image in images:
                    image_url = self.PAGE_PREFIX + image['src']
                    image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                    image_objs.append({'name': image_name, 'url': image_url})
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Blu-Ray')
            print(e)
        self.download_image_objects(image_objs, folder)


# Yahari Ore no Seishun Love Comedy wa Machigatteiru. Kan
class Oregairu3Download(Summer2020AnimeDownload):
    title = "Yahari Ore no Seishun Love Comedy wa Machigatteiru. Kan"
    keywords = [title, "Oregairu", "My Teen Romantic Comedy SNAFU 3",
                "My youth romantic comedy is wrong as I expected 3"]

    PAGE_PREFIX = "http://www.tbs.co.jp/anime/oregairu/"
    STORY_PAGE = "http://www.tbs.co.jp/anime/oregairu/story/"
    IMAGE_TEMPLATE = 'http://www.tbs.co.jp/anime/oregairu/story/img/story%s/%s.jpg'
    TOTAL_EPISODES = 25
    TOTAL_IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/oregairu3"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_bluray()

    def download_episode_preview(self):
        try:
            self.has_website_updated(self.STORY_PAGE)
            try:
                soup = self.get_soup(self.STORY_PAGE, decode=True)
                story_nav = soup.find('ul', class_='story-nav')
                chapters = story_nav.find_all('li')
                for chapter in chapters:
                    try:
                        link_tag = chapter.find('a')
                        link_text = link_tag.text
                        if '第' in link_text and '話' in link_text:
                            episode = link_text.split('話')[0].split('第')[1].zfill(2)
                            if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(
                                    self.base_folder + "/" + episode + "_1.png"):
                                continue
                            episode_link = self.STORY_PAGE + link_tag['href']
                            episode_soup = self.get_soup(episode_link)
                            image_tags = episode_soup.find('ul', class_='slides').find_all('img')
                            j = 0
                            for image_tag in image_tags:
                                j += 1
                                image_url = self.STORY_PAGE + image_tag['src']
                                file_path_without_extension = self.base_folder + '/' + episode + '_' + str(j)
                                self.download_image(image_url, file_path_without_extension)
                    except:
                        continue
            except:
                pass

            for i in range(self.TOTAL_EPISODES):
                episode = str(i + 1).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(
                        self.base_folder + "/" + episode + "_1.png"):
                    continue
                for j in range(self.TOTAL_IMAGES_PER_EPISODE):
                    image_url = self.IMAGE_TEMPLATE % (episode, str(j + 1).zfill(2))
                    file_path_without_extension = self.base_folder + '/' + episode + '_' + str(j + 1)
                    result = self.download_image(image_url, file_path_without_extension)
                    if result == -1:
                        return
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_key_visual(self):
        keyvisual_folder = self.create_key_visual_directory()
        image_objs = [{'name': 'kv', 'url': 'http://www.tbs.co.jp/anime/oregairu/img/keyvisual_pc_2.jpg'},
            {'name': 'kv2', 'url': 'http://www.tbs.co.jp/anime/oregairu/special/img/special02_01.png'}]
        self.download_image_objects(image_objs, keyvisual_folder)

    def download_bluray(self):
        folder = self.create_bluray_directory()
        image_objs = [
            {'name': 'music_ed', 'url': 'https://pbs.twimg.com/media/Ec7bHveUwAEpB8X?format=jpg&name=large'},
            {'name': 'album_1', 'url': 'https://tc-animate.techorus-cdn.com/resize_image/resize_image.php?image=07091514_5f06b5ad6bf56.jpg'},
            {'name': 'album_2', 'url': 'https://tc-animate.techorus-cdn.com/resize_image/resize_image.php?image=07091512_5f06b558505c8.jpg'},
            #{'name': 'bd_1', 'url': 'https://tc-animate.techorus-cdn.com/resize_image/resize_image.php?image=07091503_5f06b33680c68.jpg'},
            {'name': 'bd_1_1', 'url': 'https://pbs.twimg.com/media/EflqqRCVoAAQRSa?format=jpg&name=4096x4096'},
            {'name': 'bd_1_2', 'url': 'https://pbs.twimg.com/media/Efq6Z9bUwAMUGMB?format=jpg&name=4096x4096'},
            {'name': 'bd_2_1', 'url': 'https://pbs.twimg.com/media/EgaTUXsUwAA5vJ-?format=jpg&name=large'},
            {'name': 'bd_2_2', 'url': 'https://pbs.twimg.com/media/EivEo6NUcAYVOkx?format=jpg&name=large'},
            {'name': 'bd_3_1', 'url': 'https://pbs.twimg.com/media/Eg_h8JsVkAEmg2p?format=jpg&name=large'},
            {'name': 'bd_4_1', 'url': 'https://pbs.twimg.com/media/EhjLbFyVoAEbZtn?format=jpg&name=large'},
            {'name': 'bd_5_1', 'url': 'https://pbs.twimg.com/media/EiHMiubVgAAKyVV?format=jpg&name=large'},
            {'name': 'bd_6_1', 'url': 'https://pbs.twimg.com/media/Eiu3gMJVkAAAO2Q?format=jpg&name=large'},
        ]
        disc_prefix = 'http://www.tbs.co.jp/anime/oregairu/disc/'
        try:
            soup = self.get_soup('http://www.tbs.co.jp/anime/oregairu/disc/')
            bd_vol_images = soup.find_all('div', class_='disc-img')
            for bd_vol_image in bd_vol_images:
                image = bd_vol_image.find('img')
                if image is not None:
                    image_url = disc_prefix + image['src']
                    image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                    image_objs.append({'name': image_name, 'url': image_url})

            bd_bonus_images = soup.find_all('td', class_='td_img_disc')
            for bd_bonus_image in bd_bonus_images:
                image = bd_bonus_image.find('a', class_='md-image')
                if image is not None and image.has_attr('data-image'):
                    image_url = disc_prefix + image['data-image']
                    image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                    image_objs.append({'name': image_name, 'url': image_url})
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Blu-ray')
            print(e)
        self.download_image_objects(image_objs, folder)
