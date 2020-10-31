import os
import re
import anime.constants as constants
from anime.main_download import MainDownload
from anime.external_download import MocaNewsDownload
from datetime import datetime
from scan import AniverseMagazineScanner, MocaNewsScanner, WebNewtypeScanner

# Arte http://arte-anime.com/ #アルテ @arte_animation [SUN]
# BNA https://bna-anime.com/story/ #ビーエヌエー @bna_anime [THU]
# Gleipnir http://gleipnir-anime.com/ #グレイプニル @gleipnir_anime [MON]
# Hachi-nan tte http://hachinan-anime.com/story/ #八男 #hachinan @Hachinan_PR [WED]
# Honzuki S2 http://booklove-anime.jp/story/ #本好きの下剋上 @anime_booklove [MON]
# Houkago Teibou Nisshi https://teibotv.com/ #teibo @teibo_bu [FRI]
# Kaguya-sama S2 https://kaguya.love/ #かぐや様 @anime_kaguya [SAT]
# Kakushigoto https://kakushigoto-anime.com/ #かくしごと @kakushigoto_pr [TUE]
# Kingdom S3 https://kingdom-anime.com/story/ #キングダム @kingdom_animePR [THU]
# Otome Game https://hamehura-anime.com/story/ #はめふら #hamehura @hamehura [WED]
# Namiyo https://namiyo-anime.com/story/ #波よ聞いてくれ #namiyo [WED]
# Princess Connect https://anime.priconne-redive.jp/story/ #アニメプリコネ #プリコネR #プリコネ @priconne_anime [FRI]
# Shachibato https://shachibato-anime.com/story.html #シャチバト #shachibato @schbt_anime [TUE]
# Tamayomi https://tamayomi.com/story/ #tamayomi @tamayomi_PR [WED]
# Tsugumomo S2 http://tsugumomo.com/story/ #つぐもも @tsugumomo_anime [FRI]
# Yesterday wo Utatte https://singyesterday.com/ #イエスタデイをうたって @anime_yesterday [FRI]


# Spring 2020 Anime
class Spring2020AnimeDownload(MainDownload):
    season = "2020-2"
    season_name = "Spring 2020"

    def __init__(self):
        super().__init__()
        self.init_base_folder('2020-2')


# Arte
class ArteDownload(Spring2020AnimeDownload):
    title = "Arte"
    keywords = [title]
    folder_name = 'arte'

    PAGE_PREFIX = "http://arte-anime.com/"
    IMAGE_TEMPLATE = 'http://arte-anime.com/U1y9gMfZ/wp-content/themes/arte/images/story/img%s_%s.jpg'
    FINAL_EPISODE = 13
    IMAGES_PER_EPISODE = 5

    def __init__(self):
        super().__init__()
        self.init_base_folder()

    def run(self):
        try:
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(
                        self.base_folder + "/" + episode + "_1.png"):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = self.IMAGE_TEMPLATE % (episode, str(j + 1).zfill(2))
                    file_path_without_extension = self.base_folder + '/' + episode + '_' + str(j + 1)
                    result = self.download_image(image_url, file_path_without_extension)
                    if result == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

        '''
        soup = self.get_soup(self.PAGE_PREFIX)
        story_mob = soup.find_all('div', class_='story_mob')
        regex = '#[０|１|２|３|４|５|６|７|８|９|0-9]+'
        prog = re.compile(regex)
        for story in story_mob:
            h4_tag_text = story.find('h4', class_='st_ntit').text.strip()
            result = prog.match(h4_tag_text)
            if result is None:
                continue
            episode = str(int(result.group(0).split('#')[1])).zfill(2)
            if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(
                    self.base_folder + "/" + episode + "_1.png"):
                continue
            st_smlist = story.find_all('div', class_='st_smlist')
            for j in range(len(st_smlist)):
                image_url = st_smlist[j].find('img')['src']
                file_path_without_extension = self.base_folder + '/' + episode + '_' + str(j + 1)
                self.download_image(image_url, file_path_without_extension)
        '''


# Brand New Animal
class BrandNewAnimalDownload(Spring2020AnimeDownload):
    title = "Brand New Animal"
    keywords = [title, "BNA"]
    folder_name = 'bna'

    STORY_PAGE = "https://bna-anime.com/story/"
    IMAGE_TEMPLATE = 'https://bna-anime.com/story/images/%s_%s.jpg'
    TOTAL_EPISODES = 24
    TOTAL_IMAGES_PER_EPISODE = 8

    def __init__(self):
        super().__init__()
        self.init_base_folder()

    def run(self):
        try:
            soup = self.get_soup(self.STORY_PAGE)
            ep_list = soup.find('ul', id='storyList').find_all('li')
            for ep in ep_list:
                try:
                    episode = self.get_episode_number(ep.find('span', class_='cn').text)
                    if episode is None:
                        continue
                    if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(
                            self.base_folder + "/" + episode + "_1.png"):
                        continue
                    ep_url = self.STORY_PAGE + ep.find('a')['href']
                    ep_soup = self.get_soup(ep_url)
                    images = ep_soup.find('ul', {'class': ['imgClick', 'cf']}).find_all('img')
                    for j in range(len(images)):
                        image_url = self.STORY_PAGE + images[j]['src']
                        file_path_without_extension = self.base_folder + '/' + episode + '_' + str(j + 1)
                        self.download_image(image_url, file_path_without_extension)
                except:
                    continue

            for i in range(self.TOTAL_EPISODES):
                episode = str(i + 1).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(
                        self.base_folder + "/" + episode + "_1.png"):
                    continue
                for j in range(self.TOTAL_IMAGES_PER_EPISODE):
                    image_url = self.IMAGE_TEMPLATE % (str(i + 1), str(j + 1))
                    file_path_without_extension = self.base_folder + '/' + episode + '_' + str(j + 1)
                    result = self.download_image(image_url, file_path_without_extension)
                    if result == -1:
                        return
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Gleipnir
class GleipnirDownload(Spring2020AnimeDownload):
    title = "Gleipnir"
    keywords = [title]
    folder_name = 'gleipnir'
    
    PAGE_PREFIX = "http://gleipnir-anime.com"
    STORY_PAGE = 'http://gleipnir-anime.com/story/'

    def __init__(self):
        super().__init__()
        self.init_base_folder()
    
    def run(self):
        try:
            soup = self.get_soup(self.STORY_PAGE)
            stories = soup.find('section', class_='storyNavi').find_all('li')
            for story in stories:
                story_url_tag = story.find('a')
                episode = self.get_episode_number(story_url_tag.text)
                if episode is None:
                    continue
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(
                        self.base_folder + "/" + episode + "_1.png"):
                    continue
                story_url = self.PAGE_PREFIX + story_url_tag['href']
                story_soup = self.get_soup(story_url)
                images = story_soup.find('section', class_='story_slider').find_all('img')
                for j in range(len(images)):
                    image_url = images[j]['src'].replace('-1024x576', '')
                    file_path_without_extension = self.base_folder + '/' + episode + '_' + str(j + 1)
                    self.download_image(image_url, file_path_without_extension)
            WebNewtypeScanner('グレイプニル', self.base_folder, 13).run()
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Hachi-nan tte, Sore wa Nai deshou!
class HachinanDownload(Spring2020AnimeDownload):
    title = "Hachi-nan tte, Sore wa Nai deshou!"
    keywords = [title, "Hachinan", "The 8th Son? Are You Kidding Me?"]
    folder_name = 'hachinan'
    
    PAGE_PREFIX = "http://hachinan-anime.com"
    STORY_PAGE = "http://hachinan-anime.com/story/"
    TOTAL_EPISODES = 13
    IMAGES_PER_EPISODE = 6
    IMAGE_TEMPLATE = 'http://hachinan-anime.com/wp-content/themes/hachinan-anime/images/story/%s-%s.jpg'
    
    def __init__(self):
        super().__init__()
        self.init_base_folder()

    def run(self):
        self.download_episode_preview()
        self.download_bluray()
        self.download_key_visual()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.STORY_PAGE)
            a_tags = soup.find('nav', class_='l-nav').find_all('a')
            for a_tag in a_tags:
                episode = self.get_episode_number(a_tag.text)
                if episode is None:
                    continue
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(
                        self.base_folder + "/" + episode + "_1.png"):
                    continue
                story_soup = self.get_soup(self.PAGE_PREFIX + a_tag['href'])
                images = story_soup.find('ul', class_='capture').find_all('img')
                for j in range(len(images)):
                    image_url = images[j]['src']
                    if self.PAGE_PREFIX not in image_url:
                        image_url = self.PAGE_PREFIX + image_url
                    file_path_without_extension = self.base_folder + '/' + episode + '_' + str(j + 1)
                    self.download_image(image_url, file_path_without_extension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_bluray(self):
        filepath = self.create_bluray_directory()
        image_objs = [
            {'name': 'bd_packege_sample', 'url': 'http://hachinan-anime.com/wp-content/themes/hachinan-anime/images/bddvd/packege_sample.jpg'},
            {'name': 'bd_package', 'url': 'http://hachinan-anime.com/wp-content/uploads/2020/05/bd_package.jpg'},
            {'name': 'bd_onsen_sample', 'url': 'http://hachinan-anime.com/wp-content/themes/hachinan-anime/images/bddvd/onsen_sample.jpg'},
            {'name': 'bd_onsen_sample_2', 'url': 'http://hachinan-anime.com/wp-content/uploads/2020/04/onsen_sample.jpg'},
            {'name': 'bd_onsen', 'url': 'http://hachinan-anime.com/wp-content/uploads/2020/05/hachiman_A3_poster.jpg'},
            #{'name': 'music_op', 'url': 'http://hachinan-anime.com/wp-content/themes/hachinan-anime/images/music/op-jacket.jpg'},
            {'name': 'music_ed', 'url': 'http://hachinan-anime.com/wp-content/themes/hachinan-anime/images/music/ed-jacket.jpg'},
            {'name': 'bd_tokuten_sample_1_1', 'url': 'http://hachinan-anime.com/wp-content/uploads/2020/04/animate_sample.jpg'},
            {'name': 'bd_tokuten_sample_1_2', 'url': 'http://hachinan-anime.com/wp-content/uploads/2020/04/amazon_sample.jpg'},
            {'name': 'bd_tokuten_sample_1_3', 'url': 'http://hachinan-anime.com/wp-content/uploads/2020/04/gamers_sample.jpg'},
            {'name': 'bd_tokuten_sample_1_4', 'url': 'http://hachinan-anime.com/wp-content/uploads/2020/04/toranoana_sample.jpg'},
            {'name': 'bd_tokuten_sample_1_5', 'url': 'http://hachinan-anime.com/wp-content/uploads/2020/04/sofmap_sample.jpg'},
            {'name': 'bd_tokuten_sample_2_1', 'url': 'http://hachinan-anime.com/wp-content/uploads/2020/05/animate_sample.png'},
            {'name': 'bd_tokuten_sample_2_2', 'url': 'http://hachinan-anime.com/wp-content/uploads/2020/05/amazon_sample.png'},
            {'name': 'bd_tokuten_sample_2_3', 'url': 'http://hachinan-anime.com/wp-content/uploads/2020/05/gamers_sample.png'},
            {'name': 'bd_tokuten_sample_2_4', 'url': 'http://hachinan-anime.com/wp-content/uploads/2020/05/toranoana_sample.png'},
            {'name': 'bd_tokuten_sample_2_5', 'url': 'http://hachinan-anime.com/wp-content/uploads/2020/05/sofmap_sample.png'},
            {'name': 'bd_tokuten_1', 'url': 'http://hachinan-anime.com/wp-content/uploads/2020/05/animate.jpg'},
            {'name': 'bd_tokuten_2', 'url': 'http://hachinan-anime.com/wp-content/uploads/2020/05/amazon.jpg'},
            {'name': 'bd_tokuten_3', 'url': 'http://hachinan-anime.com/wp-content/uploads/2020/05/gamers.jpg'},
            {'name': 'bd_tokuten_4', 'url': 'http://hachinan-anime.com/wp-content/uploads/2020/05/toranoana.jpg'},
            {'name': 'bd_tokuten_5', 'url': 'http://hachinan-anime.com/wp-content/uploads/2020/05/sofmap.jpg'}]
        self.download_image_objects(image_objs, filepath)

        '''
        image_urls = []
        other_filepath = self.base_folder + '/' + constants.FOLDER_BLURAY
        if not os.path.exists(other_filepath):
            os.makedirs(other_filepath)
        url_list = ["http://hachinan-anime.com/bd/",
                    "http://hachinan-anime.com/bd/bd-special/",
                    "http://hachinan-anime.com/bd/campaign/"]
        for url in url_list:
            bd_soup = self.get_soup(url)
            try:
                images = bd_soup.find('section', class_='bdvdArea').find_all('img')
                for image in images:
                    image_urls.append(self.PAGE_PREFIX + image['src'])
            except:
                pass

        music_soup = self.get_soup("http://hachinan-anime.com/music/")
        try:
            music_sections = music_soup.find_all('section', class_='musicArea')
            for music_section in music_sections:
                images = music_section.find_all('img')
                for image in images:
                    image_url = image['src']
                    if 'http://' not in image_url and 'https://' not in image_url:
                        image_url = self.PAGE_PREFIX + image_url
                    image_urls.append(image_url)
        except:
            pass

        for image_url in image_urls:
            try:
                image_filename = image_url.split('/')[-1]
                file_path_without_extension = other_filepath + '/' + image_filename.split('.jpg')[0].split('.jpeg')[0].split('.png')[0]
                if os.path.exists(other_filepath + '/' + image_filename):
                    #self.download_image_if_exists(image_url, file_path_without_extension, other_filepath + '/' + image_filename)
                    continue
                self.download_image(image_url, file_path_without_extension)
            except Exception as e:
                print(e)
                pass
        '''

    def download_key_visual(self):
        filepath = self.create_key_visual_directory()
        image_objs = [
            {'name': 'kv1', 'url': 'http://hachinan-anime.com/wp-content/uploads/2019/07/（確認用）Hachinan-keyvisual-completeのコピー.jpg'},
            {'name': 'kv2', 'url': 'http://hachinan-anime.com/wp-content/uploads/2019/12/アニメ「八男って、それはないでしょう！」キービジュアル第2弾.png'},
            {'name': 'kv3', 'url': 'http://hachinan-anime.com/wp-content/uploads/2020/02/【八男】キービジュアル第3弾.jpg'},
            {'name': 'kv4', 'url': 'http://hachinan-anime.com/wp-content/themes/hachinan-anime/images/home/img_main.jpg'}]
        self.download_image_objects(image_objs, filepath)


# Honzuki no Gekokujou: Shisho ni Naru Tame ni wa Shudan wo Erandeiraremasen 2nd Season
class Honzuki2Download(Spring2020AnimeDownload):
    title = "Honzuki no Gekokujou: Shisho ni Naru Tame ni wa Shudan wo Erandeiraremasen 2nd Season"
    keywords = [title, "Ascendance of a Bookworm"]
    folder_name = 'honzuki2'
    
    PAGE_PREFIX = "http://booklove-anime.jp/story/"
    IMAGE_PREFIX = "http://booklove-anime.jp/"
    FIRST_EPISODE = 15
    FINAL_EPISODE = 26
    
    def __init__(self):
        super().__init__()
        self.init_base_folder()
    
    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_external()
        self.download_key_visual()

    def download_episode_preview(self):
        try:
            ep_num = self.FIRST_EPISODE - 1
            box_story_divs = self.get_soup(self.PAGE_PREFIX).find('section', id='second').find_all('div',
                                                                                                   class_='box_story')
            for box_story_div in box_story_divs:
                if 'intro02' in box_story_div['class']:
                    continue
                ep_num += 1
                episode = str(ep_num)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(
                        self.base_folder + "/" + episode + "_1.png"):
                    continue
                lis = box_story_div.find_all('li')
                for j in range(len(lis)):
                    img = lis[j].find('img')
                    image_url = self.IMAGE_PREFIX + img['src'].replace('../', '')
                    file_path_without_extension = self.base_folder + '/' + episode + '_' + str(j + 1)
                    self.download_image(image_url, file_path_without_extension)

            template = 'http://booklove-anime.jp/img/story/ep%s/img%s.jpg'
            episode = 14
            result = 0
            while episode <= self.FINAL_EPISODE:
                episode += 1
                if self.is_file_exists(self.base_folder + "/" + str(episode) + "_1.jpg") or self.is_file_exists(
                        self.base_folder + "/" + str(episode) + "_1.png"):
                    continue
                for j in range(6):
                    image_url = template % (str(episode), str(j + 1).zfill(2))
                    file_path_without_extension = self.base_folder + '/' + str(episode) + '_' + str(j + 1)
                    result = self.download_image(image_url, file_path_without_extension)
                    if result == -1 or result is None:
                        break
                if result == -1 or result is None:
                    break
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_episode_preview_external(self):
        try:
            last_date = datetime.strptime('20200630', '%Y%m%d')
            today = datetime.today()
            if today < last_date:
                end_date = today
            else:
                end_date = last_date
            MocaNewsScanner('本好きの下剋上', self.base_folder, '20200401', end_date.strftime('%Y%m%d')).run()
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - MocaNews')
            print(e)

    def download_key_visual(self):
        filepath = self.create_key_visual_directory()
        image_objs = [
            {'name': 'kv', 'url': 'http://booklove-anime.jp/img/index/mainvisual02.jpg'}]
        self.download_image_objects(image_objs, filepath)


# Nami yo Kiitekure
class NamiyoDownload(Spring2020AnimeDownload):
    title = "Nami yo Kiitekure"
    keywords = [title, "Namiyo", "Wave, Listen to Me!"]
    folder_name = 'namiyo'

    STORY_PAGE = 'https://namiyo-anime.com/story/'

    def __init__(self):
        super().__init__()
        self.init_base_folder()

    def run(self):
        try:
            soup = self.get_soup(self.STORY_PAGE)
            stories = soup.find('ul', class_='l-episode-list').find_all('li', class_='l-episode-item')
            ep_num = 0
            for story in stories:
                ep_num += 1
                episode = str(ep_num).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + str(episode) + "_1.jpg") or self.is_file_exists(
                        self.base_folder + "/" + str(episode) + "_1.png"):
                    continue
                images = story.find_all('div', class_='swiper-slide')
                for j in range(len(images)):
                    image_url = images[j].find('img')['src']
                    file_path_without_extension = self.base_folder + '/' + str(episode) + '_' + str(j + 1)
                    self.download_image(image_url, file_path_without_extension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Houkago Teibou Nisshi
class TeiboDownload(Spring2020AnimeDownload):
    title = "Houkago Teibou Nisshi"
    keywords = [title, "Teibo", "Diary of Our Days at the Breakwater"]
    folder_name = 'teibo'

    PAGE_PREFIX = "https://teibotv.com/"
    STORY_PAGE = 'https://teibotv.com/story.html'
    IMAGE_TEMPLATE = 'https://teibotv.com/images/story/%s/p_%s.jpg'

    TOTAL_EPISODES = 13
    TOTAL_IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()
        self.init_base_folder()
    
    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_external()
        self.download_key_visual()
        self.download_bluray()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.STORY_PAGE)
            story_thumb_boxes = soup.find_all('div', class_='story_thumb_box')
            for story_thumb_box in story_thumb_boxes:
                try:
                    content = str(story_thumb_box.find('div', class_='title'))
                    split1 = content.split('<span')[0].split('"title">')[1].split('れぽーと')[1]
                    episode = str(int(split1)).zfill(2)
                except:
                    continue
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(self.base_folder + "/" + episode + "_1.png"):
                    continue
                story_url = story_thumb_box.find('a')['href']
                story_soup = self.get_soup(self.PAGE_PREFIX + story_url)
                images = story_soup.find('ol', class_='main').find_all('img')
                for j in range(len(images)):
                    image_url = self.PAGE_PREFIX + images[j]['src']
                    file_path_without_extension = self.base_folder + '/' + str(episode) + '_' + str(j + 1)
                    self.download_image(image_url, file_path_without_extension)

            for i in range(self.TOTAL_EPISODES):
                episode = str(i + 1).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(
                        self.base_folder + "/" + episode + "_1.png"):
                    continue
                for j in range(self.TOTAL_IMAGES_PER_EPISODE):
                    image_url = self.IMAGE_TEMPLATE % (str(i + 1).zfill(3), str(j).zfill(3))
                    file_path_without_extension = self.base_folder + '/' + str(episode) + '_' + str(j + 1)
                    result = self.download_image(image_url, file_path_without_extension)
                    if result == -1 or result is None:
                        return
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_episode_preview_external(self):
        AniverseMagazineScanner('放課後ていぼう日誌', self.base_folder, 12).run()

    def download_key_visual(self):
        filepath = self.create_key_visual_directory()
        image_objs = [
            {'name': 'kv', 'url': 'https://teibotv.com/images/top/v_003.jpg'}]
        self.download_image_objects(image_objs, filepath)

    def download_bluray(self):
        folder = self.create_bluray_directory()
        if not os.path.exists(self.base_folder + '/bd_bonus_01.jpg'):
            MocaNewsDownload("20200729/2020072912000a_", self.base_folder.replace('download/', ''), 'bd_bonus').run()
        image_objs = [
            {'name': 'bd_vol2', 'url': 'https://pbs.twimg.com/media/Ei-p86vUYAIC245?format=jpg&name=large'}
        ]
        try:
            soup = self.get_soup('https://teibotv.com/package.html')
            for i in range(3):
                volume_class = 'vol' + str(i + 1).zfill(2)
                elem = soup.find('div', class_=volume_class)
                if elem is not None:
                    images = elem.find_all('img')
                    if images is not None and len(images) > 0:
                        for image in images:
                            image_url = self.PAGE_PREFIX + image['src']
                            image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                            image_objs.append({'name': image_name, 'url': image_url})
            bonus_elem = soup.find('div', class_='tokuten')
            if bonus_elem is not None:
                images = bonus_elem.find_all('img')
                if images is not None and len(images) > 0:
                    for image in images:
                        image_url = self.PAGE_PREFIX + image['src']
                        image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                        image_objs.append({'name': image_name, 'url': image_url})
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Blu-Ray')
            print(e)
        self.download_image_objects(image_objs, folder)


# Kaguya-sama wa Kokurasetai? Tensai-tachi no Renai Zunousen
class Kaguyasama2Download(Spring2020AnimeDownload):
    title = "Kaguya-sama wa Kokurasetai?: Tensai-tachi no Renai Zunousen"
    keywords = [title, "Kaguya", "Kaguyasama", "Kaguya-sama: Love is War 2nd Season"]
    folder_name = 'kaguya-sama2'

    STORY_PAGE = "https://kaguya.love/story/"
    PAGE_PREFIX = 'https://kaguya.love'
    
    def __init__(self):
        super().__init__()
        self.init_base_folder()
    
    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_bluray()
        self.download_character()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.STORY_PAGE)
            story_nav = soup.find('div', class_='p-story_nav').find_all('a')
            for story_tag in story_nav:
                try:
                    page_url = self.PAGE_PREFIX + story_tag['href']
                    episode = str(int(story_tag.text)).zfill(2)
                    if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(
                            self.base_folder + "/" + episode + "_1.png"):
                        continue
                    page_soup = self.get_soup(page_url)
                    story_div = page_soup.find('div', class_='p-story__main')
                    li_tags = story_div.find_all('li', class_='scene_item')
                    for j in range(len(li_tags)):
                        image_url = self.STORY_PAGE + li_tags[j].find('img')['src']
                        file_path_without_extension = self.base_folder + '/' + episode + '_' + str(j + 1)
                        self.download_image(image_url, file_path_without_extension)
                except:
                    continue
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_key_visual(self):
        filepath = self.create_key_visual_directory()
        template = 'https://kaguya.love/assets/img/top/img_main%s.jpg'
        image_objs = []
        for i in range(1, 4, 1):
            image_url = template % str(i).zfill(2)
            image_objs.append({'name': 'kv' + str(i), 'url': image_url})
        self.download_image_objects(image_objs, filepath)

    def download_bluray(self):
        self.has_website_updated('https://kaguya.love/bddvd/', 'bd_bonus')
        try:
            image_urls = []
            other_filepath = self.base_folder + '/' + constants.FOLDER_BLURAY
            if not os.path.exists(other_filepath):
                os.makedirs(other_filepath)
            image_objs = [
                {'name': 'bd_1', 'url': 'https://pbs.twimg.com/media/EYsi1b-UMAAyPDK?format=jpg&name=900x900'},
                {'name': 'bd_2', 'url': 'https://pbs.twimg.com/media/EcUL42TUYAAfElR?format=jpg&name=900x900'},
                {'name': 'bd_3', 'url': 'https://pbs.twimg.com/media/EeQoG9GVAAANa_C?format=jpg&name=900x900'},
                {'name': 'bd_4', 'url': 'https://pbs.twimg.com/media/EguZjVqUcAEuusP?format=jpg&name=900x900'},
                {'name': 'bd_5', 'url': 'https://pbs.twimg.com/media/EjG8xLHU4AAW_DY?format=jpg&name=900x900'},
            ]
            self.download_image_objects(image_objs, other_filepath)
            url_list = ["https://kaguya.love/bddvd/"]
            for i in range(2, 7, 1):
                url_list.append('https://kaguya.love/bddvd/%s.html' % str(i).zfill(2))
            for url in url_list:
                bd_soup = self.get_soup(url)
                try:
                    package_tag = bd_soup.find('figure', class_='jk')
                    if package_tag is not None:
                        package_image = package_tag.find('img')
                        if package_image is not None:
                            image_url = self.PAGE_PREFIX + package_image['src'].replace('../', '/')
                            image_urls.append(image_url)
                    novelty_tags = bd_soup.find_all('figure', class_='novelty_img')
                    if novelty_tags is not None and len(novelty_tags) > 0:
                        for novelty_tag in novelty_tags:
                            image_tag = novelty_tag.find('img')
                            if image_tag is not None:
                                image_url = self.PAGE_PREFIX + image_tag['src'].replace('..', '')
                                image_urls.append(image_url)
                except:
                    pass

            url_list = ["https://kaguya.love/music/opening/",
                        "https://kaguya.love/music/ending/",
                        "https://kaguya.love/music/charasong/"]
            for url in url_list:
                music_soup = self.get_soup(url)
                try:
                    images = music_soup.find('div', class_='p-music').find_all('img')
                    for image in images:
                        image_url = image['src'].replace('../..', '')
                        if 'http://' not in image_url and 'https://' not in image_url:
                            image_url = self.PAGE_PREFIX + image_url
                        image_urls.append(image_url)
                except:
                    pass

            for image_url in image_urls:
                try:
                    image_filename = image_url.split('/')[-1]
                    if os.path.exists(other_filepath + '/' + image_filename):
                        continue
                    file_path_without_extension = other_filepath + '/' + \
                                                  image_filename.split('.jpg')[0].split('.jpeg')[0].split('.png')[0]
                    self.download_image(image_url, file_path_without_extension)
                except:
                    pass
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Blu-Ray')
            print(e)

    def download_character(self):
        try:
            chara_filepath = self.base_folder + '/' + constants.FOLDER_CHARACTER
            if not os.path.exists(chara_filepath):
                os.makedirs(chara_filepath)
            chara_image_templates = [self.PAGE_PREFIX + '/assets/img/chara/img_chara%s.png',
                                     self.PAGE_PREFIX + '/assets/img/chara/img_face%s-1.png',
                                     self.PAGE_PREFIX + '/assets/img/chara/img_face%s-2.png']
            num_of_characters = 10
            for i in range(len(chara_image_templates)):
                for j in range(num_of_characters):
                    image_url = chara_image_templates[i] % str(j + 1).zfill(2)
                    filename = image_url.split('/')[-1].replace('.jpg', '').replace('.png', '')
                    filepath = chara_filepath + '/' + filename
                    if not os.path.exists(filepath + '.jpg') and not os.path.exists(filepath + '.png'):
                        self.download_image(image_url, filepath)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Character')
            print(e)


# Kakushigoto
class KakushigotoDownload(Spring2020AnimeDownload):
    title = "Kakushigoto"
    keywords = [title]
    folder_name = 'kakushigoto'

    STORY_PAGE = "https://kakushigoto-anime.com/story/"
    
    def __init__(self):
        super().__init__()
        self.init_base_folder()
    
    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_bluray()
            
    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.STORY_PAGE)
            contents = soup.find_all('div', class_='story_tab_content')
            for content in contents:
                episode = ''
                try:
                    episode = str(int(content['id'])).zfill(2)
                    if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(
                            self.base_folder + "/" + episode + "_1.png"):
                        continue
                    image_divs = content.find_all('div', class_='swiper-slide')
                    for j in range(len(image_divs)):
                        image_url = image_divs[j].find('img')['src']
                        file_path_without_extension = self.base_folder + '/' + episode + '_' + str(j + 1)
                        self.download_image(image_url, file_path_without_extension)
                except:
                    continue
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_key_visual(self):
        filepath = self.create_key_visual_directory()
        template = 'https://kakushigoto-anime.com/wp/wp-content/themes/kakushigoto_common/assets/img/top/kv0%s_pc.jpg'
        image_objs = []
        for i in range(1, 5, 1):
            image_objs.append({'name': 'kv' + str(i), 'url': template % str(i)})
        self.download_image_objects(image_objs, filepath)

    def download_bluray(self):
        filepath = self.create_bluray_directory()
        image_objs = [
            {'name': 'collab_cd', 'url': 'https://pbs.twimg.com/media/EUbrX69UcAA0qMr?format=jpg&name=medium'},
            {'name': 'bd_1', 'url': 'https://pbs.twimg.com/media/EUmnFbkU8AUE-1Y?format=jpg&name=large'},
            {'name': 'bd_2', 'url': 'https://pbs.twimg.com/media/EaTmvQ3UYAE2JIf?format=jpg&name=4096x4096'},
            {'name': 'bd_3', 'url': 'https://pbs.twimg.com/media/EczEXSWVAAALRl1?format=jpg&name=4096x4096'},
            {'name': 'bd_bonus_1', 'url': 'https://pbs.twimg.com/media/EXZ763qU8AEVa7j?format=jpg&name=900x900'},
            {'name': 'bd_bonus_2', 'url': 'https://pbs.twimg.com/media/EaymgYTU0AE6VeG?format=jpg&name=900x900'}]
        self.download_image_objects(image_objs, filepath)


# Kingdom 3rd Season
class Kingdom3Download(Spring2020AnimeDownload):
    title = "Kingdom 3rd Season"
    keywords = [title]
    folder_name = 'kingdom3'

    STORY_PAGE = "https://kingdom-anime.com/story/"
    
    def __init__(self):
        super().__init__()
        self.init_base_folder()
    
    def run(self):
        try:
            soup = self.get_soup(self.STORY_PAGE)
            ep_list = soup.find('ul', id='ep_list').find_all('li')
            for ep in ep_list:
                try:
                    episode = self.get_episode_number(ep.find('span', class_='hd').text)
                    if episode is None:
                        continue
                    if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(
                            self.base_folder + "/" + episode + "_1.png"):
                        continue
                    ep_url = self.STORY_PAGE + ep.find('a')['href']
                    ep_soup = self.get_soup(ep_url)
                    images = ep_soup.find('div', id='episodeCont').find_all('img')
                    for j in range(len(images)):
                        image_url = images[j]['src']
                        file_path_without_extension = self.base_folder + '/' + episode + '_' + str(j + 1)
                        self.download_image(image_url, file_path_without_extension)
                except:
                    continue
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Otome Game no Hametsu Flag shika Nai Akuyaku Reijou ni Tensei shiteshimatta...
class HamehuraDownload(Spring2020AnimeDownload):
    title = "Otome Game no Hametsu Flag shika Nai Akuyaku Reijou ni Tensei shiteshimatta..."
    keywords = [title, "Hamehura", "My Next Life as a Villainess: All Routes Lead to Doom!"]
    folder_name = 'hamehura'

    STORY_PAGE = "https://hamehura-anime.com/story"
    
    def __init__(self):
        super().__init__()
        self.init_base_folder()

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.STORY_PAGE)
            story_content = soup.find_all('div', class_='story_content')
            for story in story_content:
                title = story.find('p', class_='orn_ttl').text
                episode = self.get_episode_number(title)
                if episode is None:
                    continue
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(
                        self.base_folder + "/" + episode + "_1.png"):
                    continue
                swiper_slide = story.find_all('div', class_='swiper-slide')
                for j in range(len(swiper_slide)):
                    image_url = swiper_slide[j].find('img')['src']
                    file_path_without_extension = self.base_folder + '/' + episode + '_' + str(j + 1)
                    self.download_image(image_url, file_path_without_extension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

        '''
        self.base_folder += "_hidden"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
        image_template = "https://hamehura-anime.com/wp/wp-content/uploads/2020/%s/%s.jpg"
        for i in range(3, 7):
            month = str(i).zfill(2)
            for j in range(6):
                image_num = str(j + 1).zfill(2)
                for k in range(12):
                    if k == 0:
                        image_url = image_template % (month, image_num)
                    else:
                        image_url = image_template % (month, image_num + '-' + str(k))
                    file_path_without_extension = self.base_folder + '/' + month + '_' + image_num + '_' + str(k)
                    self.download_image(image_url, file_path_without_extension)
        '''

    def download_key_visual(self):
        filepath = self.create_key_visual_directory()
        image_objs = [
            {'name': 'kv4', 'url': 'https://hamehura-anime.com/wp/wp-content/uploads/2020/02/4thKV_FIX.jpg'},
            {'name': 'kv5', 'url': 'https://hamehura-anime.com/wp/wp-content/uploads/2020/03/第5弾キービジュアル.jpg'}]
        self.download_image_objects(image_objs, filepath)


# Princess Connect! Re:Dive
class PriconneDownload(Spring2020AnimeDownload):
    title = "Princess Connect! Re:Dive"
    keywords = [title, "Priconne"]
    folder_name = 'priconne'
    
    PAGE_PREFIX = "https://anime.priconne-redive.jp"
    STORY_PREFIX = "https://anime.priconne-redive.jp/story/"
    STORY_TEMPLATE = "https://anime.priconne-redive.jp/story/?id=%s"
    
    def __init__(self):
        super().__init__()
        self.init_base_folder()
    
    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_bluray()
        self.download_character()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.STORY_PREFIX)
            latest_episode_text = soup.find('ul', class_='story-num').find('li', class_='active').text
            prog = re.compile('[0-9]+')
            result = prog.findall(latest_episode_text)
            max_episode = int(result[0])
            for i in range(max_episode):
                episode = str(i + 1).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_01.jpg") or self.is_file_exists(
                        self.base_folder + "/" + episode + "_01.png"):
                    continue
                try:
                    story_soup = self.get_soup(self.STORY_TEMPLATE % episode)
                    img_list = story_soup.find('ul', class_='img-list')
                    images = img_list.find_all('img')
                    for j in range(len(images)):
                        image_url = self.PAGE_PREFIX + images[j]['src'].replace('-840x472', '')
                        file_path_without_extension = self.base_folder + '/' + episode + '_' + str(j + 1).zfill(2)
                        self.download_image(image_url, file_path_without_extension)
                except:
                    continue
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_key_visual(self):
        filepath = self.create_key_visual_directory()
        image_objs = [
            #{'name': 'kv', 'url': 'https://anime.priconne-redive.jp/assets/images/top_kv.png'} # replaced in S2
            {'name': 'kv', 'url': 'https://pbs.twimg.com/media/EfTtfRwUwAUt67l?format=jpg&name=large'}
        ]
        self.download_image_objects(image_objs, filepath)

    def download_bluray(self):
        bluray_filepath = self.create_bluray_directory()
        image_objs = [
            {'name': 'bd_1_1', 'url': 'https://anime.priconne-redive.jp/assets/data/82a6345d72fd68036496915319c326f0.png'},
            {'name': 'bd_1_1s', 'url': 'https://pbs.twimg.com/media/EYTkbHcXQAQsR0A?format=jpg&name=900x900'},
            {'name': 'bd_1_2', 'url': 'https://anime.priconne-redive.jp/assets/data/11323f9ee9ffc83c3151a0e18cb9b07b.png'},
            {'name': 'bd_1_2s', 'url': 'https://pbs.twimg.com/media/EYTkbHeXQAMc7YR?format=jpg&name=900x900'},
            {'name': 'bd_2_1', 'url': 'https://anime.priconne-redive.jp/assets/data/e7ea4524bba61f75f2dcb6a256a8b83b.png'},
            {'name': 'bd_2_1s', 'url': 'https://pbs.twimg.com/media/Ebrro9AUYAIUDHy?format=png&name=900x900'},
            {'name': 'bd_2_2', 'url': 'https://anime.priconne-redive.jp/assets/data/aaa7409d1f2c64ff3025e61576115a9a.png'},
            {'name': 'bd_2_2s', 'url': 'https://pbs.twimg.com/media/Ebr7kB6U0AEMNBK?format=png&name=900x900'},
            {'name': 'bd_3_1', 'url': 'https://anime.priconne-redive.jp/assets/data/c9224cfde16f25a941a6cc46e3779f93.jpg'},
            {'name': 'bd_3_1s', 'url': 'https://pbs.twimg.com/media/EfTYv2aUYAABOhK?format=png&name=900x900'},
            {'name': 'bd_3_2', 'url': 'https://anime.priconne-redive.jp/assets/data/2b6a06cdd66432d9e2541fbad3c97b97.jpg'},
            {'name': 'bd_3_2s', 'url': 'https://pbs.twimg.com/media/EfTYzgSUEAIZOK_?format=png&name=900x900'},
            {'name': 'bd_4_1', 'url': 'https://anime.priconne-redive.jp/assets/data/28431f86423342f51c2b2fc0fdf810f3.jpg'},
            {'name': 'bd_4_1s', 'url': 'https://pbs.twimg.com/media/EjiJrg1VcAAc5fX?format=png&name=900x900'},
            {'name': 'bd_4_2', 'url': 'https://anime.priconne-redive.jp/assets/data/9ad0b1ee801f23d0abdcdcea33a7d45a.png'},
            {'name': 'bd_4_2s', 'url': 'https://pbs.twimg.com/media/EjiJrrMU0AEvHIX?format=png&name=900x900'},
        ]
        self.download_image_objects(image_objs, bluray_filepath)

    def download_character(self):
        try:
            # Download characters
            chara_filepath = self.base_folder + '/' + constants.FOLDER_CHARACTER
            if not os.path.exists(chara_filepath):
                os.makedirs(chara_filepath)
            chara_soup = self.get_soup('https://anime.priconne-redive.jp/character/')
            full_image_urls = []
            thumb_image_urls = []
            chara_names = []
            try:
                main_lis = chara_soup.find('ul', class_='main-list').find_all('li')
                for li in main_lis:
                    chara_names.append(li.find('p', class_='name').text)
                    full_image_urls.append(self.PAGE_PREFIX + li.find('a')['href'])
                    thumb_image_urls.append(self.PAGE_PREFIX + li.find('img')['src'])
                sub_lis = chara_soup.find('ul', class_='sub-list').find_all('li')
                for li in sub_lis:
                    chara_names.append(li.find('p', class_='name').text)
                    full_image_urls.append(self.PAGE_PREFIX + li.find('a')['href'])
                    thumb_image_urls.append(self.PAGE_PREFIX + li.find('img')['src'])
            except:
                pass
            if len(full_image_urls) == len(thumb_image_urls) == len(chara_names):
                for i in range(len(full_image_urls)):
                    full_image_filepath = chara_filepath + '/f_' + chara_names[i]
                    thumb_image_filepath = chara_filepath + '/t_' + chara_names[i]
                    self.download_image(full_image_urls[i], full_image_filepath)
                    self.download_image(thumb_image_urls[i], thumb_image_filepath)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Character')
            print(e)


# Shachou, Battle no Jikan Desu!
class ShachibatoDownload(Spring2020AnimeDownload):
    title = "Shachou, Battle no Jikan Desu!"
    keywords = [title, "Shachibato! President, It's Time for Battle!"]
    folder_name = 'shachibato'

    PAGE_PREFIX = "https://shachibato-anime.com/"
    STORY_PAGE = "https://shachibato-anime.com/story.html"
    IMAGE_TEMPLATE = 'https://shachibato-anime.com/img/story/story-episode%s-img-%s.jpg'
    TOTAL_EPISODES = 25
    TOTAL_IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()
        self.init_base_folder()

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_bluray()
        self.download_character()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.STORY_PAGE)
            story_list = soup.find('ul', class_='story_navi').find_all('a')
            for story in story_list:
                episode = self.get_episode_number(story.text)
                if episode is None:
                    continue
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(
                        self.base_folder + "/" + episode + "_1.png"):
                    continue
                story_url = self.PAGE_PREFIX + story['href']
                story_soup = self.get_soup(story_url)
                images = story_soup.find('div', class_='slider-for').find_all('img')
                for j in range(len(images)):
                    image_url = self.PAGE_PREFIX + images[j]['src'].replace('../', '')
                    file_path_without_extension = self.base_folder + '/' + episode + '_' + str(j + 1)
                    self.download_image(image_url, file_path_without_extension)

            result = 0
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
                        break
                if result == -1:
                    break
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_bluray(self):
        filepath = self.create_bluray_directory()
        image_urls = []
        url_list = ["https://shachibato-anime.com/bluray.html",
                    "https://shachibato-anime.com/music.html"]
        for url in url_list:
            bd_soup = self.get_soup(url)
            try:
                images = bd_soup.find('div', class_='container1').find_all('img')
                for image in images:
                    image_url = image['src']
                    if 'http://' not in image_url and 'https://' not in image_url:
                        image_url = self.PAGE_PREFIX + image_url
                    image_urls.append(image_url)
            except:
                pass

        for image_url in image_urls:
            try:
                image_filename = image_url.split('/')[-1]
                if os.path.exists(filepath + '/' + image_filename):
                    continue
                file_path_without_extension = filepath + '/' + \
                    image_filename.split('.jpg')[0].split('.jpeg')[0].split('.png')[0]
                self.download_image(image_url, file_path_without_extension)
            except:
                pass

    def download_character(self):
        try:
            chara_filepath = self.base_folder + '/' + constants.FOLDER_CHARACTER
            if not os.path.exists(chara_filepath):
                os.makedirs(chara_filepath)
            chara_soup = self.get_soup('https://shachibato-anime.com/character.html')
            image_urls = []
            try:
                lis = chara_soup.find('ul', class_='panel').find_all()
                for li in lis:
                    visual_div = li.find('div', class_='visual')
                    if visual_div is not None:
                        image_urls.append(self.PAGE_PREFIX + visual_div.find('img')['src'])
                    face_div = li.find('div', class_='face')
                    if face_div is not None:
                        face_images = face_div.find_all('img')
                        for face_img in face_images:
                            image_urls.append(self.PAGE_PREFIX + face_img['src'])
                    visual2_div = li.find('div', class_='visual2')
                    if visual2_div is not None:
                        image_urls.append(self.PAGE_PREFIX + visual2_div.find('img')['src'])
            except:
                pass
            for image_url in image_urls:
                filename = image_url.split('/')[-1].replace('.jpg', '').replace('.png', '')
                file_path_without_extension = chara_filepath + '/' + filename
                self.download_image(image_url, file_path_without_extension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Character')
            print(e)

    def download_key_visual(self):
        filepath = self.create_key_visual_directory()
        image_objs = [
            {'name': 'kv1', 'url': 'https://pbs.twimg.com/media/EPBl4JZUUAQc52k?format=jpg&name=medium'},
            {'name': 'kv2', 'url': 'https://pbs.twimg.com/media/ERnjhKQUwAIKUEq?format=jpg&name=large'}]
        self.download_image_objects(image_objs, filepath)


# Tamayomi
class TamayomiDownload(Spring2020AnimeDownload):
    title = "Tamayomi"
    keywords = [title]
    folder_name = 'tamayomi'

    PAGE_PREFIX = "https://tamayomi.com"
    STORY_PREFIX = "https://tamayomi.com/story/"
    
    def __init__(self):
        super().__init__()
        self.init_base_folder()
    
    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_bluray()
        self.download_character()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.STORY_PREFIX)
            stories = soup.find('ul', class_='story-storybox_thumbs').find_all('li', class_='story-storybox_thumbs_item')
            for story in stories:
                story_title = story.find('p', class_='story-storybox_thumbs_title').text
                episode = self.get_episode_number(story_title, prefix='第', suffix='球')
                if episode is None:
                    continue
                if self.is_file_exists(self.base_folder + "/" + episode + "_01.jpg") or self.is_file_exists(self.base_folder + "/" + episode + "_01.png"):
                    continue
                story_url = self.STORY_PREFIX + story.find('a')['href']
                story_soup = self.get_soup(story_url)
                images = story_soup.find('div', class_='story-detbox_main').find_all('img')
                for j in range(len(images)):
                    image_url = images[j]['src']
                    file_path_without_extension = self.base_folder + '/' + episode + '_' + str(j + 1).zfill(2)
                    self.download_image(image_url, file_path_without_extension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_bluray(self):
        filepath = self.create_bluray_directory()
        image_objs = [
            {'name': 'music', 'url': 'https://img.imageimg.net/artist/tamayomi/img/product_1031383.jpg'},
            {'name': 'music_bonus', 'url': 'https://m.imageimg.net/upload/artist_img/TMYMX/9d8e75e1e572dc299319aad7bc8c46e97dc75816_5ea64d7728b35.jpg'},
            {'name': 'bd_1_1', 'url': 'https://pbs.twimg.com/media/EYBcL7KUMAAzETM?format=jpg&name=small'},
            {'name': 'bd_1_2', 'url': 'https://pbs.twimg.com/media/EYBcOPCU0AASO2c?format=jpg&name=small'},
            {'name': 'bd_2_1', 'url': 'https://pbs.twimg.com/media/EYBcSZDU8AAV3oc?format=jpg&name=small'},
            {'name': 'bd_2_2', 'url': 'https://pbs.twimg.com/media/EYBcVieXkAATCH5?format=jpg&name=small'},
            {'name': 'bd_3_1', 'url': 'https://pbs.twimg.com/media/EZK2fXMU0AIVWun?format=jpg&name=small'},
            {'name': 'bd_3_2', 'url': 'https://pbs.twimg.com/media/EZK2g17VcAUpMfE?format=jpg&name=small'},
            {'name': 'bd_4_1', 'url': 'https://pbs.twimg.com/media/EZK2iQQUwAADyPY?format=jpg&name=small'},
            {'name': 'bd_4_2', 'url': 'https://pbs.twimg.com/media/EZK2jzcU0AIm_Uy?format=jpg&name=small'},
            {'name': 'bd_bonus_1', 'url': 'https://m.imageimg.net/upload/artist_img/TMYMX/79336eca283b54c872bff032c87f6ad8763b12ee_5eaa4755dd468.png'},
            {'name': 'bd_bonus_2', 'url': 'https://m.imageimg.net/upload/artist_img/TMYMX/ab0571bc7edc6a7d8f4ba0475bdfa907f0783c2b_5eaa476e8b18f.png'},
            {'name': 'bd_bonus_3', 'url': 'https://m.imageimg.net/upload/artist_img/TMYMX/ee3cd344bd8a6f65beccf534a1a99b959bbbb12c_5eaa4795eb601.png'},
            {'name': 'bd_bonus_4', 'url': 'https://m.imageimg.net/upload/artist_img/TMYMX/551c0094a71c5d237d6479081f23bb95a1c9a6bc_5ec79a608587b.png'},
            {'name': 'bd_bonus_sample_4', 'url': 'https://m.imageimg.net/upload/artist_img/TMYMX/c86e2fe0f6263b75c4c4200a0783fd6226701eae_5eb8f11b125ae.png'},
            {'name': 'bd_bonus_new_1', 'url': 'https://m.imageimg.net/upload/artist_img/TMYMX/3644ddf00baa3127b122cd99b1e230915c9fcd5a_5edda6a703138.png'},
            {'name': 'bd_bonus_new_2', 'url': 'https://m.imageimg.net/upload/artist_img/TMYMX/1abfa15a0442f36d1d065f11b76e20f35994ecb2_5edda77c63dd7.png'},
            {'name': 'bd_bonus_new_3', 'url': 'https://m.imageimg.net/upload/artist_img/TMYMX/a8fcbc5dc390b3cb92f1496e22b4d34b2baaf3a1_5edda79c322bc.png'},
            {'name': 'bd_bonus_new_4', 'url': 'https://m.imageimg.net/upload/artist_img/TMYMX/6d86c0e4eaeb448714f12880178b84b9d50aa9b9_5edda969b26f1.png'}]
        self.download_image_objects(image_objs, filepath)

    def download_bluray_old(self):
        image_urls = []
        other_filepath = self.base_folder + '/' + constants.FOLDER_BLURAY
        if not os.path.exists(other_filepath):
            os.makedirs(other_filepath)

        url_list = ["https://tamayomi.com/discography/detail.php?id=1017453",
                    "https://tamayomi.com/discography/detail.php?id=1017468",
                    "https://tamayomi.com/discography/detail.php?id=1017553",
                    "https://tamayomi.com/discography/detail.php?id=1017554",
                    "https://tamayomi.com/discography/detail.php?id=1017555",
                    "https://tamayomi.com/discography/detail.php?id=1017556"]
        for url in url_list:
            bd_soup = self.get_soup(url)
            try:
                images = bd_soup.find('div', class_='disc-single').find_all('img')
                for image in images:
                    image_url = image['src']
                    if 'http://' not in image_url and 'https://' not in image_url:
                        image_url = self.PAGE_PREFIX + image_url
                    image_urls.append(image_url)
            except:
                pass

        for image_url in image_urls:
            try:
                image_filename = image_url.split('/')[-1]
                if os.path.exists(other_filepath + '/' + image_filename):
                    continue
                file_path_without_extension = other_filepath + '/' + \
                    image_filename.split('.jpg')[0].split('.jpeg')[0].split('.png')[0]
                self.download_image(image_url, file_path_without_extension)
            except:
                pass

    def download_character(self):
        try:
            chara_filepath = self.base_folder + '/' + constants.FOLDER_CHARACTER
            if not os.path.exists(chara_filepath):
                os.makedirs(chara_filepath)

            image_urls = []
            chara_soup = self.get_soup("https://tamayomi.com/character/")
            class_names = ['character-thumbs_imageArea', 'character-modal_item_headerFace',
                           'character-modal_item_imagebox']
            for class_name in class_names:
                try:
                    div_tags = chara_soup.find_all('div', class_=class_name)
                    for div_tag in div_tags:
                        image_url = div_tag.find('img')['src']
                        if image_url[0:3] == "../":
                            image_url = self.PAGE_PREFIX + image_url[2:]
                        image_urls.append(image_url)
                except:
                    pass

            for image_url in image_urls:
                filename = image_url.split('/')[-1].replace('.jpg', '').replace('.png', '')
                file_path_without_extension = chara_filepath + '/' + filename
                self.download_image(image_url, file_path_without_extension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Character')
            print(e)

    def download_key_visual(self):
        filepath = self.create_key_visual_directory()
        image_objs = [
            {'name': 'teaser', 'url': 'https://m.imageimg.net/upload/artist_img/TMYMX/176c07d906a0ff6f7fc0d2e9795dccaeb34cf6d0_5d47d5f463bee.jpg'},
            {'name': 'kv', 'url': 'https://pbs.twimg.com/media/EPmR6ltUUAAGkSa?format=jpg&name=4096x4096'}]
        self.download_image_objects(image_objs, filepath)


# Tsugu Tsugumomo
class Tsugumomo2Download(Spring2020AnimeDownload):
    title = "Tsugu Tsugumomo"
    keywords = [title]
    folder_name = 'tsugumomo2'

    STORY_PAGE = "http://tsugumomo.com/story/"
    
    def __init__(self):
        super().__init__()
        self.init_base_folder()
    
    def run(self):
        self.download_episode_preview()
        self.download_bluray()
        self.download_key_visual()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.STORY_PAGE)
            ep_li = soup.find_all('div', class_='l-sub-title')
            ep_num = 0
            for ep in ep_li:
                ep_num += 1
                episode = str(ep_num).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(
                        self.base_folder + "/" + episode + "_1.png"):
                    continue
                images = ep.find('div', class_='inner').find_all('img')
                for j in range(len(images)):
                    image_url = images[j]['src']
                    file_path_without_extension = self.base_folder + '/' + episode + '_' + str(j + 1).zfill(2)
                    self.download_image(image_url, file_path_without_extension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_bluray(self):
        filepath = self.create_bluray_directory()
        image_objs = [
            {'name': 'bd_1_1', 'url': 'http://tsugumomo.com/wp/wp-content/uploads/2020/04/ss_DSZD08246-01.jpg'},
            {'name': 'bd_1_2', 'url': 'https://pbs.twimg.com/media/EWlDBBTUYAIelWQ?format=jpg&name=4096x4096'},
            {'name': 'bd_2_1', 'url': 'http://tsugumomo.com/wp/wp-content/uploads/2020/06/DSZD08247-01.jpg'},
            {'name': 'bd_2_2', 'url': 'https://pbs.twimg.com/media/EZ-gw2NUEAAi3G6?format=jpg&name=4096x4096'},
            {'name': 'bd_3_1', 'url': 'http://tsugumomo.com/wp/wp-content/uploads/2020/06/DSZD08248-01.jpg'},
            {'name': 'bd_3_2', 'url': 'https://pbs.twimg.com/media/EeoD3obUEAAvcvd?format=jpg&name=4096x4096'},
            {'name': 'bd_4_1', 'url': 'http://tsugumomo.com/wp/wp-content/uploads/2020/08/継つぐももJK_vo4_11koap_DVD_s_h1.jpg'},
            {'name': 'bd_4_2', 'url': 'https://pbs.twimg.com/media/EfNJR_9UMAEDgrf?format=jpg&name=4096x4096'}
        ]
        self.download_image_objects(image_objs, filepath)

    def download_key_visual(self):
        filepath = self.create_key_visual_directory()
        image_objs = [
            {'name': 'kv', 'url': 'http://tsugumomo.com/wp/wp-content/themes/tsugumomo/assets/img/top/kv_pc.jpg'}]
        self.download_image_objects(image_objs, filepath)


# Yesterday wo Utatte
class YesterdayDownload(Spring2020AnimeDownload):
    title = "Yesterday wo Utatte"
    keywords = [title, "Sing Yesterday For Me"]
    folder_name = 'yesterday'

    STORY_PAGE = "https://singyesterday.com/story/"
    PAGE_PREFIX = 'https://singyesterday.com/'
    IMAGE_TEMPLATE = 'https://singyesterday.com/cmn/images/story/%s/yd_%s_%s.jpg'
    TOTAL_EPISODES = 18
    TOTAL_IMAGES_PER_EPISODE = 10
    
    def __init__(self):
        super().__init__()
        self.init_base_folder()
    
    def run(self):
        try:
            for i in range(self.TOTAL_EPISODES):
                episode = str(i + 1).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                    continue
                is_first_image = True
                result = 0
                for j in range(self.TOTAL_IMAGES_PER_EPISODE):
                    if j == 1:
                        is_first_image = False
                    image_url = self.IMAGE_TEMPLATE % (episode, episode, str(j + 1).zfill(2))
                    file_path_without_extension = self.base_folder + '/' + episode + '_' + str(j + 1)
                    result = self.download_image(image_url, file_path_without_extension)
                    if result == -1:
                        break
                if result == -1 and is_first_image:
                    break
            WebNewtypeScanner('イエスタデイをうたって', self.base_folder, 12).run()
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)
