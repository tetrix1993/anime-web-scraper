import os
import anime.constants as constants
from anime.main_download import MainDownload

# Assassins Pride https://assassinspride-anime.com/ #アサプラ @assassins_anime [TUE/THU]
# Bokuben 2nd https://boku-ben.com/story/ #ぼくたちは勉強ができない #ぼく勉 @bokuben_anime [SUN]
# Choyoyu http://choyoyu.com/story/ #超余裕 @choyoyu_PR [THU/FRI]
# Hataage! Kemonomichi http://hataage-kemonomichi.com/story/ #けものみち @hatakemoanime [MON]
# High Score Girl II http://hi-score-girl.com/story/ #ハイスコ @hi_score_girl [FRI]
# Honzuki http://booklove-anime.jp/story/ #本好きの下剋上 @anime_booklove [WED]
# Houkago Saikoro Club http://saikoro-club.com/story/index.html #放課後さいころ倶楽部 #さいころくらぶ @saikoro_club [FRI]
# Mairimashita! Iruma-kun https://www6.nhk.or.jp/anime/program/detail.html?i=iruma #魔入りました入間くん @wc_mairuma
# Null Peta https://nullpeta.com/ #nullpeta #ぬるぺた @nullpeta [FRI]
# Oresuki https://ore.ski/story/ #俺好き @oresuki_anime [MON]
# Rifle is Beautiful https://chidori-high-school.com/story/?page=00 #RIFL @rib_anime
# Shinchou Yuusha http://shincho-yusha.jp/ #慎重勇者 @shincho_yusha [MON/TUE 6pm]
# Shin Chuuka Ichiban! http://cookingmaster-anime.jp/story #cookingmaster #真・中華一番 @shin_chuichi [FRI]
# Val x Love https://val-love.com/episode/ #ヴァルラヴ #戦恋 @val_love_pr [MON]
# Noukin https://noukin-anime.com/story/ #のうきん @noukin_anime [FRI]


# Fall 2019 Anime
class Fall2019AnimeDownload(MainDownload):
    season = "2019-4"
    season_name = "Fall 2019"
    folder_name = '2019-4'
    
    def __init__(self):
        super().__init__()


# Assassins Pride
class AssassinsPrideDownload(Fall2019AnimeDownload):
    title = "Assassins Pride"
    keywords = ["Assassins Pride"]
    folder_name = 'assassins-pride'

    PAGE_LINK = "https://assassinspride-anime.com/"
    FINAL_EPISODE = 12
    NUM_OF_PICTURES_PER_PAGE = 3
    
    def __init__(self):
        super().__init__()
    
    def run(self):
        self.download_episode_preview()
        self.download_keyvisual()
        self.download_bluray()

    def download_episode_preview(self):
        try:
            response = self.get_response(self.PAGE_LINK)
            split1 = response.split('<h3 class="top-story-box-ttl">')
            if len(split1) < 2:
                return
            for i in range(1, self.FINAL_EPISODE + 1, 1):
                episode = str(i).zfill(2)
                split2 = split1[i].split('<ul>')
                if len(split2) < 2:
                    continue
                split3 = split2[1].split('</ul>')[0].split('<li><img src="')
                for j in range(1, len(split3), 1):
                    imageUrl = split3[j].split('"')[0]
                    if len(imageUrl) == 0:
                        continue
                    if "sample" in imageUrl:
                        break
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    if not os.path.exists(filepathWithoutExtension + '.jpg'):
                        self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_keyvisual(self):
        filepath = self.create_key_visual_directory()
        image_url_template = 'https://assassinspride-anime.com/assets/img/top/main/visual/%s.jpg'
        image_objs = []
        for i in range(0, 6, 1):
            image_url = image_url_template % str(i)
            image_objs.append({'name': 'kv_' + str(i), 'url': image_url})
        self.download_image_objects(image_objs, filepath)

    def download_bluray(self):
        filepath = self.create_bluray_directory()
        image_objs = [
            {'name': 'music_ost', 'url': 'https://img.imageimg.net/artist/assassinspride-anime/img/product_1030791.jpg'},
            {'name': 'music_op', 'url': 'https://img.imageimg.net/artist/assassinspride-anime/img/product_1030685.jpg'},
            {'name': 'music_ed', 'url': 'https://img.imageimg.net/artist/assassinspride-anime/img/product_1030686.jpg'},
            {'name': 'bd_1_1', 'url': 'https://m.imageimg.net/upload/artist_img/ASSSP/0be0ba5eeff1ecb7ff05a3aac0ca2772b54eb0f5_5dc3b42657914.jpg'},
            {'name': 'bd_1_2', 'url': 'https://m.imageimg.net/upload/artist_img/ASSSP/bf34841f5725f2ed7098caf53c305d630711247a_5dc3b426c5b49.jpg'},
            {'name': 'bd_1_3', 'url': 'https://m.imageimg.net/upload/artist_img/ASSSP/c41e2864f2e0f4c4012b8f273d49b5eb7a5aa6f0_5dd68534e94eb.jpg'},
            {'name': 'bd_2_1', 'url': 'https://m.imageimg.net/upload/artist_img/ASSSP/54607137c3e8b5224e4c6a5d7a2eb83f96270d2c_5e0554b0c92a4.jpg'},
            {'name': 'bd_2_2', 'url': 'https://m.imageimg.net/upload/artist_img/ASSSP/5f779c6126936ab5cafab1c535425dcbf0546bc2_5e0554b16a0d7.jpg'},
            {'name': 'bd_2_3', 'url': 'https://m.imageimg.net/upload/artist_img/ASSSP/8a3331ed49c5c86b0d18f189318fcae0ebeb29fd_5e0554b2044c6.jpg'},
            {'name': 'bd_3_1', 'url': 'https://m.imageimg.net/upload/artist_img/ASSSP/254d9210a0a37afa7100f11e7e7b64ad9d1df583_5e60eb7e219a8.jpg'},
            {'name': 'bd_3_2', 'url': 'https://m.imageimg.net/upload/artist_img/ASSSP/114e87dec4c9808edac7e278dc7848bb69fadd28_5e60eb861207c.jpg'},
            {'name': 'bd_3_3', 'url': 'https://m.imageimg.net/upload/artist_img/ASSSP/e6fbabc8bd63767e6e11487c9b2ab9f703e8b8d3_5e60eb8c9e08a.jpg'},
            {'name': 'bd_bonus_1', 'url': 'https://pbs.twimg.com/media/EaAA-9SUcAEFoM9?format=jpg&name=medium'},
            {'name': 'bd_bonus_2', 'url': 'https://pbs.twimg.com/media/EaAA-9gU8AAI3Bb?format=jpg&name=medium'},
            {'name': 'bd_bonus_3', 'url': 'https://pbs.twimg.com/media/EaAA-9eU8AASuRF?format=jpg&name=medium'},
            {'name': 'bd_bonus_4', 'url': 'https://pbs.twimg.com/media/EaAA-9fUMAAJYBL?format=jpg&name=medium'},
            {'name': 'bd_bonus_5', 'url': 'https://pbs.twimg.com/media/EaABDs4VAAEw14r?format=jpg&name=medium'},
            {'name': 'bd_bonus_6', 'url': 'https://pbs.twimg.com/media/EaABDtWUEAAiL2G?format=jpg&name=medium'}]
        self.download_image_objects(image_objs, filepath)


# Bokuben 2 (Sunday)
class Bokuben2Download(Fall2019AnimeDownload):
    title = "Bokutachi wa Benkyou ga Dekinai!"
    keywords = ["Bokuben", "Bokutachi wa Benkyou ga Dekinai!", "We Never Learn" "2", "2nd"]
    folder_name = 'bokuben2'

    PAGE_PREFIX = "https://boku-ben.com/story/2nd/"
    PAGE_SUFFIX = ".html"
    IMAGE_PREFIX = "https://boku-ben.com"
    FINAL_EPISODE = 13
    NUM_OF_PICTURES_PER_PAGE = 3

    def __init__(self):
        super().__init__()
    
    def run(self):
        try:
            for i in range(self.FINAL_EPISODE):
                episode = str(i+1).zfill(2)
                if (self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg")):
                    continue
                link = self.PAGE_PREFIX + episode + self.PAGE_SUFFIX
                response = self.get_response(link)
                if len(response) == 0:
                    break
                first_split = response.split('<ul class="story_slide">')
                if len(first_split) < 2:
                    return
                textBlocks = first_split[1].split('<img src="../..')
                if len(textBlocks) < 2:
                    return
                for j in range(self.NUM_OF_PICTURES_PER_PAGE + 1):
                    if j == 0:
                        continue
                    imageUrl = self.IMAGE_PREFIX + textBlocks[j].split('"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
                
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Choujin Koukousei-tachi wa Isekai demo Yoyuu de Ikinuku you desu!
class ChoyoyuDownload(Fall2019AnimeDownload):
    title = "Choujin Koukousei-tachi wa Isekai demo Yoyuu de Ikinuku you desu!"
    keywords = ["Choujin Koukousei-tachi wa Isekai demo Yoyuu de Ikinuku you desu!",
                "CHOYOYU!: High School Prodigies Have It Easy Even in Another World!"]
    folder_name = 'choyoyu'
    
    PAGE_LINK = "http://choyoyu.com/story/"
    PAGE_PREFIX = "http://choyoyu.com"
    FINAL_EPISODE = 13
    NUM_OF_PICTURES_PER_PAGE = 6
    
    def __init__(self):
        super().__init__()
    
    def run(self):
        self.download_episode_preview()
        self.download_bluray()
        self.download_character()

    def download_episode_preview(self):
        try:
            response = self.get_response(self.PAGE_LINK)
            if len(response) == 0:
                return
            first_split = response.split('<h3><span class="story-storybox__title__number">')
            for i in range(len(first_split)):
                if i == 0:
                    continue
                episode = str(i).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                    continue
                second_split = first_split[i].split('<div class="story-storybox__thumbs__image"><img src="..')
                for j in range(len(second_split)):
                    if j == 0:
                        continue
                    imageUrl = self.PAGE_PREFIX + second_split[j].split('"')[0]
                    imageFileName = episode + '_' + str(j)
                    filepathWithoutExtension = self.base_folder + "/" + imageFileName
                    self.download_image(imageUrl, filepathWithoutExtension)

        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_bluray(self):
        filepath = self.create_bluray_directory()
        image_objs = [
            {'name': 'music_ost', 'url': 'http://choyoyu.com/assets/img/products/cd/cd03_image01.jpg'}]
        image_url_template = 'http://choyoyu.com/assets/img/products/bluray/bluray0%s_image01.jpg'
        for i in range(1, 5, 1):
            image_url = image_url_template % str(i)
            image_objs.append({'name': 'bd_' + str(i), 'url': image_url})
        self.download_image_objects(image_objs, filepath)

    def download_character(self):
        filepath = self.create_character_directory()
        try:
            soup = self.get_soup('http://choyoyu.com/character/')
            image_objs = []
            sections = soup.find_all('section')
            for section in sections:
                image_div = section.find('div', class_='chara-slide__image')
                if image_div is not None:
                    image_url = self.PAGE_PREFIX + image_div.find('img')['src'].replace('..', '')
                    image_name = image_url.split('/')[-1].split('.png')[0]
                    image_objs.append({'name': image_name, 'url': image_url})
                face_div = section.find('div', class_='chara-slide__face')
                if face_div is not None:
                    image_url = self.PAGE_PREFIX + face_div.find('img')['src'].replace('..', '')
                    image_name = image_url.split('/')[-1].split('.png')[0]
                    image_objs.append({'name': image_name, 'url': image_url})
            self.download_image_objects(image_objs, filepath)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Character')
            print(e)


# Hataage! Kemonomichi (Monday)
class KemonomichiDownload(Fall2019AnimeDownload):
    title = "Hataage! Kemonomichi"
    keywords = ["Hataage! Kemonomichi", "Kemono Michi: Rise Up"]
    folder_name = 'kemonomichi'

    PAGE_LINK = "http://hataage-kemonomichi.com/story/"
    PAGE_PREFIX = "http://hataage-kemonomichi.com"
    
    def __init__(self):
        super().__init__()
    
    def run(self):
        self.download_episode_preview()
        self.download_bluray()

    def download_episode_preview(self):
        try:
            response = self.get_response(self.PAGE_LINK)
            if len(response) == 0:
                return
            first_split = response.split('<div class="ep-slider-sceneImage">')
            for i in range(len(first_split), 2, -1):
                episode = str(len(first_split) - i + 1).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_01.jpg"):
                    continue
                second_split = first_split[i - 1].split('<div class="ep-slider-thumb">')[0]
                third_split = second_split.split('<img src="..')
                for j in range(len(third_split)):
                    if j == 0:
                        continue
                    imageUrl = self.PAGE_PREFIX + third_split[j].split('"')[0]
                    imageFileName = episode + '_' + str(j).zfill(2)
                    filepathWithoutExtension = self.base_folder + "/" + imageFileName
                    self.download_image(imageUrl, filepathWithoutExtension)

        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_bluray(self):
        filepath = self.create_bluray_directory()
        image_objs = [
            {'name': 'music_ost', 'url': 'http://hataage-kemonomichi.com/assets/music/cs.png'},
            {'name': 'music_op_1', 'url': 'http://hataage-kemonomichi.com/assets/music/op-a.png'},
            {'name': 'music_op_2', 'url': 'http://hataage-kemonomichi.com/assets/music/op-b.png'},
            {'name': 'bd_1', 'url': 'http://hataage-kemonomichi.com/assets/bddvd/1-boxil.png'},
            {'name': 'bd_2', 'url': 'http://hataage-kemonomichi.com/assets/bddvd/2-boxil.png'},
            {'name': 'bd_3', 'url': 'http://hataage-kemonomichi.com/assets/bddvd/3-boxil.png'},
            {'name': 'bd_bonus_1', 'url': 'http://hataage-kemonomichi.com/assets/bddvd/cmp1.png'}]
        image_url_template = 'http://hataage-kemonomichi.com/assets/bddvd/bnf/%s.jpg'
        for i in range(1, 7, 1):
            image_url = image_url_template % str(i)
            image_objs.append({'name': 'bd_bonus_' + str(i + 1), 'url': image_url})
        self.download_image_objects(image_objs, filepath)


# High Score Girl II
class HiScoreGirl2Download(Fall2019AnimeDownload):
    title = "High Score Girl II"
    keywords = ["High Score Girl II", "Hi Score Girl", "2", "2nd"]
    folder_name = 'hi-score-girl2'

    PAGE_LINK = "http://hi-score-girl.com/story/"
    PAGE_PREFIX = "http://hi-score-girl.com"
    FIRST_EPISODE = 16
    FINAL_EPISODE = 25
    NUM_OF_PICTURES_PER_PAGE = 3
    
    def __init__(self):
        super().__init__()
    
    def run(self):
        try:
            response = self.get_response(self.PAGE_LINK)
            split1 = response.split('INTRODUCTION II')
            if len(split1) < 2:
                return
            split2 = split1[1].split('<div class="sm">')
            for i in range(1, len(split2), 1):
                episode = str(self.FIRST_EPISODE + i - 1).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                    continue
                split3 = split2[i].split('<a href="..')
                if len(split3) < 2:
                    continue
                pageLink = self.PAGE_PREFIX + split3[1].split('"')[0]
                pageResponse = self.get_response(pageLink)
                split4 = pageResponse.split('<div class="img_u wdxmax">')
                if len(split4) < 2:
                    continue
                split5 = split4[1].split('<div class="block line_04">')[0]
                split6 = split5.split('<div class="ph"><a href="..')
                for j in range(1, len(split6), 1):
                    imageUrl = self.PAGE_PREFIX + split6[j].split('?')[0]
                    imageFileName = episode + '_' + str(j)
                    filepathWithoutExtension = self.base_folder + "/" + imageFileName
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    
# Honzuki no Gekokujou: Shisho ni Naru Tame ni wa Shudan wo Erandeiraremasen
class HonzukiDownload(Fall2019AnimeDownload):
    title = "Honzuki no Gekokujou: Shisho ni Naru Tame ni wa Shudan wo Erandeiraremasen"
    keywords = ["Honzuki no Gekokujou: Shisho ni Naru Tame ni wa Shudan wo Erandeiraremasen",
                "Ascendance of a Bookworm"]
    folder_name = 'honzuki'

    PAGE_LINK = "http://booklove-anime.jp/story/"
    IMAGE_PREFIX = "http://booklove-anime.jp"
    FINAL_EPISODE = 14
    NUM_OF_PICTURES_PER_PAGE = 6
    
    def __init__(self):
        super().__init__()
    
    def run(self):
        try:
            response = self.get_response(self.PAGE_LINK)
            split1 = response.split('box_story')
            for i in range(len(split1)):
                if i < 2:
                    continue
                episode = str(i-1).zfill(2)
                if (self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg")):
                    continue
                split2 = split1[i].split('<ul class="img_thum">')
                if len(split2) < 2:
                    break
                split3 = split2[1].split('</ul>')[0]
                split4 = split3.split('<img src="..')
                for j in range(len(split4)):
                    if j == 0:
                        continue
                    imageUrl = self.IMAGE_PREFIX + split4[j].split('"')[0]
                    imageFileName = episode + '_' + str(j)
                    filepathWithoutExtension = self.base_folder + "/" + imageFileName
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Kandagawa Jet Girls
class KandagawaJetGirlsDownload(Fall2019AnimeDownload):
    title = "Kandagawa Jet Girls"
    keywords = ["Kandagawa Jet Girls"]
    folder_name = 'kandagawa-jet-girls'
    
    PAGE_PREFIX = "http://kjganime.com/story.html"
    IMAGE_PREFIX = "http://kjganime.com/"
    
    def __init__(self):
        super().__init__()
            
    def run(self):
        try:
            response = self.get_response(self.PAGE_PREFIX)
            split1 = response.split('<div id="StoryData">')
            if len(split1) < 2:
                return
            split2 = split1[1].split('<div id="S_itl1">')[0].split('<div class="ep-slider-sceneImage">')
            for i in range(len(split2) - 1, 0, -1):
                episode = str(len(split2) - i).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                    continue
                split3 = split2[i].split('<div class="ep-slider-thumb">')[0].split('<img src=".')
                for j in range(1, len(split3), 1):
                    imageUrl = self.IMAGE_PREFIX + split3[j].split('"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)           


# Houkago Saikoro Club
# Wednesday? Friday?
class SaikoroDownload(Fall2019AnimeDownload):
    title = "Houkago Saikoro Club"
    keywords = ["Houkago Saikoro Club", "Afterschool Dice Club"]
    folder_name = 'saikoro'

    PAGE_LINK = "http://saikoro-club.com/story/index.html"
    PAGE_PREFIX = "http://saikoro-club.com/story/"
    IMAGE_PREFIX = "http://saikoro-club.com"
    FINAL_EPISODE = 13
    NUM_OF_PICTURES_PER_PAGE = 3
    
    def __init__(self):
        super().__init__()
    
    def run(self):
        try:
            response = self.get_response(self.PAGE_LINK)
            split1 = response.split('<ul id="storyIndex">')
            if len(split1) < 2:
                return
            split2 = split1[1].split('</ul>')[0]
            split3 = split2.split('<a href="')
            i = len(split3)
            while (i > 1):
                i = i - 1
                episode = str(len(split3) - i).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                    continue
                pageUrl = self.PAGE_PREFIX + split3[i].split('"')[0]
                pageResponse = self.get_response(pageUrl)
                split4 = pageResponse.split('<ul id="photogallery">')
                if len(split4) < 2:
                    continue
                split5 = split4[1].split('</ul>')[0]
                split6 = split5.split('<img src="..')
                for j in range(1, len(split6), 1):
                    imageUrl = self.IMAGE_PREFIX + split6[j].split('"')[0]
                    imageFileName = episode + "_" + str(j)
                    filepathWithoutExtension = self.base_folder + "/" + imageFileName
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)
        

# Mairimashita! Iruma-kun
class IrumaKunDownload(Fall2019AnimeDownload):
    title = "Mairimashita! Iruma-kun"
    keywords = ["Mairimashita! Iruma-kun", "Welcome to Demon School! Iruma-kun", "Irumakun"]
    folder_name = 'iruma-kun'

    IMAGE_PREFIX = 'https://www6.nhk.or.jp/anime/program/common/images/iruma/'
    FINAL_EPISODE = 23
    
    def __init__(self):
        super().__init__()
    
    def run(self):
        self.download_episode_preview()

    def download_episode_preview(self):
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1'):
                continue
            image_url = self.IMAGE_PREFIX + 'story_' + episode + '.jpg'
            if self.is_valid_url(image_url):
                self.download_image(image_url, self.base_folder + '/' + episode + '_1')
            else:
                break
        

# Null Peta
class NullPetaDownload(Fall2019AnimeDownload):
    title = "Null Peta"
    keywords = ["Null Peta", "Nullpeta"]
    folder_name = 'null-peta'

    PAGE_LINK = "https://nullpeta.com/story/"
    FINAL_EPISODE = 12
    NUM_OF_PICTURES_PER_PAGE = 4
    
    def __init__(self):
        super().__init__()
    
    def run(self):
        try:
            response = self.get_response(self.PAGE_LINK)
            split1 = response.split('<div class="str-Pagenation_Inner">')
            if len(split1) < 2:
                return
            split2 = split1[1].split('</div>')[0].split('<li>')
            if len(split2) < 2:
                return
            for i in range(1, len(split2), 1):
                if "isDisabled" in split2[i]:
                    return
                episode = str(i).zfill(2)
                if (self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg")):
                    continue
                split3 = split2[i].split('href="')
                if len(split3) < 2:
                    continue
                pageUrl = split3[1].split('"')[0]
                pageResponse = self.get_response(pageUrl)
                split4 = pageResponse.split('<div class="slider-main">')
                if len(split4) < 2:
                    return
                split5 = split4[1].split('<div class="str-Text">')[0].split('<img src="')
                for j in range(1, len(split5), 1):
                    imageUrl = split5[j].split('"')[0]
                    imageFileName = episode + "_" + str(j)
                    filepathWithoutExtension = self.base_folder + "/" + imageFileName
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)
        

# Ore wo Suki nano wa Omae dake ka yo (Tuesday)
class OresukiDownload(Fall2019AnimeDownload):
    title = "Ore wo Suki nano wa Omae dake ka yo"
    keywords = ["Ore wo Suki nano wa Omae dake ka yo", "ORESUKI Are you the only one who loves me?"]
    folder_name = 'oresuki'

    PAGE_PREFIX = "https://ore.ski/story/?id=ep"
    IMAGE_PREFIX = "https://ore.ski/story/"
    FINAL_EPISODE = 13
    NUM_OF_PICTURES_PER_PAGE = 4
    
    def __init__(self):
        super().__init__()
    
    def run(self):
        self.download_bluray()
        self.download_episode_preview()

    def download_bluray(self):
        bluray_filepath = self.base_folder + '/' + constants.FOLDER_BLURAY
        if not os.path.exists(bluray_filepath):
            os.makedirs(bluray_filepath)

        bluray_template = 'https://ore.ski/_assets/img/blu-ray_dvd/%s/jacket_%s.%s'
        for i in range(1, 7, 1):
            for j in range(1, 5, 1):
                pic_type = 'png'
                if i == 6:
                    pic_type = 'jpg'
                bluray_url = bluray_template % (str(i).zfill(2), str(j).zfill(2), pic_type)
                filepath_without_extension = bluray_filepath + '/bd_' + str(i) + '_' + str(j)
                self.download_image(bluray_url, filepath_without_extension)

        image_objs = [
            {'name': 'bd_bonus_1', 'url': 'https://ore.ski/_assets/img/blu-ray_dvd/ph_all.jpg'},
            {'name': 'bd_bonus_2', 'url': 'https://ore.ski/_assets/img/blu-ray_dvd/ph_animate.jpg'},
            {'name': 'bd_bonus_3', 'url': 'https://ore.ski/_assets/img/blu-ray_dvd/ph_amazon.jpg'},
            {'name': 'bd_bonus_4', 'url': 'https://ore.ski/_assets/img/blu-ray_dvd/ph_gamers.jpg'},
            {'name': 'bd_bonus_5', 'url': 'https://ore.ski/_assets/img/blu-ray_dvd/ph_sofmap.jpg'},
            {'name': 'bd_bonus_6', 'url': 'https://ore.ski/_assets/img/blu-ray_dvd/ph_toranoana.jpg'}]
        for image_obj in image_objs:
            if os.path.exists(bluray_filepath + '/' + image_obj['name'] + '.png') or \
                    os.path.exists(bluray_filepath + '/' + image_obj['name'] + '.jpg'):
                continue
            filepath_without_extension = bluray_filepath + '/' + image_obj['name']
            self.download_image(image_obj['url'], filepath_without_extension)

    def download_episode_preview(self):
        try:
            for i in range(1, self.FINAL_EPISODE + 1, 1):
                episode = str(i).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                    continue
                response = self.get_response(self.PAGE_PREFIX + str(i))
                if len(response) == 0:
                    return
                first_split = response.split('<div class="story__ph js-slick">')
                if len(first_split) < 2:
                    return
                second_split = first_split[1].split('<div><img src="')
                for j in range(len(second_split)):
                    if j == 0:
                        continue
                    imageUrl = self.IMAGE_PREFIX + second_split[j].split('"')[0]
                    imageFileName = episode + '_' + str(j)
                    filepathWithoutExtension = self.base_folder + "/" + imageFileName
                    self.download_image(imageUrl, filepathWithoutExtension)

        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)
        

# Rifle is Beautiful
class RifleIsBeautifulDownload(Fall2019AnimeDownload):
    title = "Rifle is Beautiful"
    keywords = ["Rifle is Beautiful", "Chidori RSC"]
    folder_name = 'rifle-is-beautiful'

    PAGE_PREFIX = "https://chidori-high-school.com/story/"
    IMAGE_PREFIX = PAGE_PREFIX
    INITIAL_PAGE_LINK = 'https://chidori-high-school.com/story/?page=00'
    
    def __init__(self):
        super().__init__()
    
    def run(self):
        self.download_episode_preview()
        self.download_goods()

    def download_episode_preview(self):
        try:
            response = self.get_response(self.INITIAL_PAGE_LINK)
            split1 = response.split('<div class="nav_num flex">')
            if len(split1) < 2:
                return
            split2 = split1[1].split('<a href="?page=00"')[0].split('<a href="')
            for i in range(1, len(split2), 1):
                relative_page_link = split2[i].split('"')[0]
                page_link = self.PAGE_PREFIX + relative_page_link
                episode = relative_page_link[-2:]
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                    continue
                page_response = self.get_response(page_link)
                split3 = page_response.split('<div class="swiper-slide">')
                for j in range(1, len(split3), 1):
                    split4 = split3[j].split('</div>')[0]
                    split5 = split4.split('<img src="')
                    if len(split5) < 2:
                        continue
                    imageUrl = self.IMAGE_PREFIX + split5[1].split('"')[0]
                    imageFileName = episode + '_' + str(j)
                    filepathWithoutExtension = self.base_folder + "/" + imageFileName
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_goods(self):
        filepath = self.create_custom_directory(constants.FOLDER_GOODS)
        image_objs = [
            {'name': 'dakimakura_hikari', 'url': 'https://chidori-high-school.com/news/wp-content/uploads/2019/12/hikari_dakimakura_cmyk.jpg'},
            {'name': 'dakimakura_erika', 'url': 'https://chidori-high-school.com/news/wp-content/uploads/2019/12/erika_dakimakura_cmyk.jpg'},
            {'name': 'dakimakura_izumi', 'url': 'https://chidori-high-school.com/news/wp-content/uploads/2019/12/izumi_dakimakura_cmyk.jpg'},
            {'name': 'dakimakura_yukio', 'url': 'https://chidori-high-school.com/news/wp-content/uploads/2019/12/yukio_dakimakura_cmyk.jpg'}]
        self.download_image_objects(image_objs, filepath)
        

# Shinchou Yuusha: Kono Yuusha ga Ore Tueee Kuse ni Shinchou Sugiru (Tuesday)
class ShinchouYuushaDownload(Fall2019AnimeDownload):
    title = "Shinchou Yuusha: Kono Yuusha ga Ore Tueee Kuse ni Shinchou Sugiru"
    keywords = ["Shinchou Yuusha: Kono Yuusha ga Ore Tueee Kuse ni Shinchou Sugiru",
                "Cautious Hero: The Hero Is Overpowered but Overly Cautious"]
    folder_name = 'shinchou-yuusha'

    PAGE_LINK = "http://shincho-yusha.jp"
    
    def __init__(self):
        super().__init__()
    
    def run(self):
        try:
            response = self.get_response(self.PAGE_LINK)
            if len(response) == 0:
                return
            first_split = response.split('<ul class="ep-slider">')
            for i in range(len(first_split)):
                if i == 0:
                    continue
                episode = str(i).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_01.jpg"):
                    continue
                second_split = first_split[i].split('</ul>')[0].split('<li><img src="')
                for j in range(len(second_split)):
                    if j == 0:
                        continue
                    imageUrl = self.PAGE_LINK + second_split[j].split('"')[0]
                    imageFileName = episode + '_' + str(j).zfill(2)
                    filepathWithoutExtension = self.base_folder + "/" + imageFileName
                    self.download_image(imageUrl, filepathWithoutExtension)
        
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)
        

# Val x Love (Fri)
class ValLoveDownload(Fall2019AnimeDownload):
    title = "Val x Love"
    keywords = ["Val x Love", "Vallove", "Ikusa x Koi"]
    folder_name = 'val-love'

    PAGE_LINK = "https://val-love.com/episode/"
    
    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_goods()
    
    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_LINK)
            a_tags = soup.select('#episodeList a')
            for i in range(len(a_tags)):
                index = len(a_tags) - i - 1
                episode = str(i + 1).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                    continue
                pageLink = self.PAGE_LINK + a_tags[index]['href']
                pageResponse = self.get_response(pageLink)
                split4 = pageResponse.split('<div id="episodeCont">')
                if len(split4) < 2:
                    continue
                split5 = split4[1].split("</div>")[0]
                split6 = split5.split('<img src="')
                for j in range(len(split6)):
                    if j == 0:
                        continue
                    imageUrl = split6[j].split('"')[0]
                    imageFileName = episode + '_' + str(j)
                    filepathWithoutExtension = self.base_folder + "/" + imageFileName
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_goods(self):
        folder = self.create_custom_directory('goods')
        try:
            prefix = 'https://val-love.com/goods/?page='
            soup = self.get_soup(prefix + '1')
            pages_tag = soup.select('div.pagingBox a')
            daki_count = 0
            daki_ids = ['1012801', '1012802']
            if len(pages_tag) > 0:
                try:
                    last_page = int(pages_tag[-1].text)
                    for i in range(last_page):
                        page = i + 1
                        if page > 1:
                            soup = self.get_soup(prefix + str(page))
                        if soup:
                            a_tags = soup.select('#goodsList a')
                            for a_tag in a_tags:
                                try:
                                    id_ = a_tag['href'].split('?id=')[1]
                                except:
                                    continue
                                self.image_list = []
                                is_daki = False
                                if id_ in daki_ids:
                                    daki_count += 1
                                    is_daki = True
                                    thumb = a_tag.find('p', class_='goodsThumb')
                                    if thumb and thumb.has_attr('style') and 'background-image:url(' in thumb['style']:
                                        thumb_url = thumb['style'].replace('background-image:url(', '').replace(')', '')
                                        thumb_name = 'daki' + str(daki_count) + '_1'
                                        self.add_to_image_list(thumb_name, thumb_url)
                                goods_url = 'https://val-love.com/goods/' + a_tag['href']
                                goods_soup = self.get_soup(goods_url)
                                if goods_soup:
                                    image = goods_soup.select('#item_0 img')
                                    if len(image) > 0:
                                        image_url = image[0]['src']
                                        if is_daki:
                                            image_name = 'daki' + str(daki_count) + '_2'
                                        else:
                                            image_name = self.extract_image_name_from_url(image_url)
                                        self.add_to_image_list(image_name, image_url)
                                self.download_image_list(folder)
                except Exception:
                    pass
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Goods')
            print(e)


# Watashi, Nouryoku wa Heikinchi de tte Itta yo ne!
class NoukinDownload(Fall2019AnimeDownload):
    title = "Watashi, Nouryoku wa Heikinchi de tte Itta yo ne!"
    keywords = ["Noukin", "Watashi, Nouryoku wa Heikinchi de tte Itta yo ne!",
                "Didn't I Say to Make My Abilities Average in the Next Life?!"]
    folder_name = 'noukin'

    PAGE_LINK = "https://noukin-anime.com/story/"
    
    def __init__(self):
        super().__init__()
    
    def run(self):
        self.download_episode_preview()
        self.download_bluray()
        self.download_character()

    def download_episode_preview(self):
        try:
            response = self.get_response(self.PAGE_LINK)
            split1 = response.split('<ul class="c-news_list">')
            if len(split1) < 2:
                return
            split2 = split1[1].split("</ul>")[0]
            split3 = split2.split('<a href="')
            for i in range(len(split3)-2, 0, -1):
                episode = str(len(split3) - i - 1).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                    continue
                pageLink = self.PAGE_LINK + split3[i].split('"')[0]
                pageResponse = self.get_response(pageLink)
                split4 = pageResponse.split('<div class="p-news__detail_article">')
                if len(split4) < 2:
                    continue
                split5 = split4[1].split("</div>")[0]
                split6 = split5.split('<img src="')
                for j in range(len(split6)):
                    if j == 0:
                        continue
                    imageUrl = split6[j].split('"')[0]
                    imageFileName = episode + '_' + str(j)
                    filepathWithoutExtension = self.base_folder + "/" + imageFileName
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_bluray(self):
        filepath = self.create_bluray_directory()
        image_objs = [
            {'name': 'music_op', 'url': 'https://pbs.twimg.com/media/EF9AeyIVUAAvU8i?format=jpg&name=small'},
            {'name': 'music_ed', 'url': 'https://pbs.twimg.com/media/EH8jYnwU8AAPq0D?format=jpg&name=small'},
            {'name': 'bd_1_1', 'url': 'https://pbs.twimg.com/media/EJoJ9YuU8AIH-TY?format=jpg&name=900x900'},
            {'name': 'bd_1_2', 'url': 'https://pbs.twimg.com/media/EJoKAQaUEAAGkFb?format=jpg&name=900x900'},
            {'name': 'bd_2_1', 'url': 'https://pbs.twimg.com/media/EMcEweWUYAE8wJh?format=jpg&name=900x900'},
            {'name': 'bd_2_2', 'url': 'https://pbs.twimg.com/media/EMcE1NKUYAAmuJ6?format=jpg&name=900x900'},
            {'name': 'bd_3_1', 'url': 'https://pbs.twimg.com/media/EP3O4mQUUAIFFRh?format=jpg&name=900x900'},
            {'name': 'bd_3_2', 'url': 'https://pbs.twimg.com/media/EP3O4mZU0AE4pnI?format=jpg&name=900x900'},
            {'name': 'bd_bonus_1', 'url': 'https://m.imageimg.net/upload/artist_img/NOUKN/c5f143690ecb1cf10797e46e43b061397ab61672_5ded9ad3c9543.jpg'},
            {'name': 'bd_bonus_2', 'url': 'https://m.imageimg.net/upload/artist_img/NOUKN/a0e237a7b078ec0d289ae95d1f74ae72d100328d_5ded9afea75c1.jpg'},
            {'name': 'bd_bonus_2_1', 'url': 'https://www.gamers.co.jp/resize_image.php?image=12171428_5df867862e4de.jpg'},
            {'name': 'bd_bonus_3', 'url': 'https://m.imageimg.net/upload/artist_img/NOUKN/67ab91a841c5684e734298af68009cafa645698f_5df82a3043663.jpg'},
            {'name': 'bd_bonus_4', 'url': 'https://m.imageimg.net/upload/artist_img/NOUKN/55a784882229b7c45887f1db577156506a252a8d_5ded9b253412e.jpg'},
            {'name': 'bd_bonus_4_1', 'url': 'https://pbs.twimg.com/media/ES--_fzU0AAemUS.jpg'},
            #{'name': 'bd_bonus_4_1', 'url': 'https://a.sofmap.com/ec/topics/3000/19916699_toku_01.jpg'},
            {'name': 'bd_bonus_5', 'url': 'https://m.imageimg.net/upload/artist_img/NOUKN/43ce4af9ac52d6a7353b4731472b4df9bdaf306f_5ded9b4c54d9d.jpg'},
            {'name': 'bd_bonus_5_1', 'url': 'https://img.amiami.jp/images/product/review/194/MED-DVD2-44857_01.jpg'}]
        self.download_image_objects(image_objs, filepath)

    def download_character(self):
        filepath = self.create_character_directory()
        image_objs = []
        image_url_template = 'https://noukin-anime.com/assets/img_201910/chara/img_main%s-%s.png'
        for i in range(1, 10, 1):
            image_url = image_url_template % (str(i).zfill(2), '1')
            image_objs.append({'name': 'chara_' + str(i).zfill(2), 'url': image_url})
            if i == 1:
                image_url = image_url_template % (str(i).zfill(2), '2')
                image_objs.append({'name': 'chara_' + str(i).zfill(2) + '_2', 'url': image_url})
        self.download_image_objects(image_objs, filepath)
