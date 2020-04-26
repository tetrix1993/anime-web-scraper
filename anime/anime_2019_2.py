import os
from anime.main_download import MainDownload

# Spring 2019 Anime
class Spring2019AnimeDownload(MainDownload):
    season = "2019-2"
    season_name = "Spring 2019"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/2019-2"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)


# Bokutachi wa Benkyou ga Dekinai
class BokubenDownload(Spring2019AnimeDownload):
    title = "Bokutachi wa Benkyou ga Dekinai"
    keywords = ["Bokuben", "Bokutachi wa Benkyou ga Dekinai", "We Never Learn"]

    PAGE_PREFIX = "https://boku-ben.com/story/"
    PAGE_SUFFIX = ".html"
    IMAGE_PREFIX = "https://boku-ben.com"
    FINAL_EPISODE = 13
    NUM_OF_PICTURES_PER_PAGE = 3

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/bokuben"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            for i in range(self.FINAL_EPISODE):
                episode = str(i+1).zfill(2)
                link = self.PAGE_PREFIX + episode + self.PAGE_SUFFIX
                response = self.get_response(link)
                if len(response) == 0:
                    break
                first_split = response.split("<ul class=\"story_slide\">")
                if len(first_split) < 2:
                    return
                textBlocks = first_split[1].split("<img src=\"..")
                if len(textBlocks) < 2:
                    return
                for j in range(self.NUM_OF_PICTURES_PER_PAGE + 1):
                    if j == 0:
                        continue
                    imageUrl = self.IMAGE_PREFIX + textBlocks[j].split("\"")[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
                
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Choukadou Girl 1/6
class ChoukadouGirlDownload(Spring2019AnimeDownload):
    title = "Choukadou Girl 1/6"
    keywords = ["Choukadou Girl 1/6", "Amazing Stranger"]
    
    PAGE_LINK = "http://choukadou-anime.com/story/"
    FINAL_EPISODE = 12
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/choukadou"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            response = self.get_response(self.PAGE_LINK)
            if len(response) == 0:
                return
            for i in range(self.FINAL_EPISODE):
                episode = str(i+1).zfill(2)
                first_split = response.split("id=\"story" + str(i+1) + "\"")
                if len(first_split) < 2:
                    return
                textBlocks = first_split[1].split("src=\"")
                if len(textBlocks) < 2:
                    return
                imageUrl = textBlocks[1].split("\"")[0]
                filepathWithoutExtension = self.base_folder + "/" + episode
                self.download_image(imageUrl, filepathWithoutExtension)
                
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Hachigatsu no Cinderella Nine
class HachinaiDownload(Spring2019AnimeDownload):
    title = "Hachigatsu no Cinderella Nine"
    keywords = ["Hachigatsu no Cinderella Nine", "Amazing Stranger"]
    
    PAGE_LINK = "https://anime-hachinai.com"
    FINAL_EPISODE = 12
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/hachinai"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            response = self.get_response(self.PAGE_LINK)
            if len(response) == 0:
                return
            first_split = response.split("<section id=\"story\">")
            if len(first_split) < 2:
                return
            second_split = first_split[1].split("<div class=\"image\">")
            for i in range(self.FINAL_EPISODE + 1):
                if i == 0:
                    continue
                episode = str(i).zfill(2)
                third_split = second_split[i].split("<img src=\"")
                if len(third_split) < 2:
                    continue
                imageUrl = self.PAGE_LINK + third_split[1].split("\"")[0]
                filepathWithoutExtension = self.base_folder + "/" + episode
                self.download_image(imageUrl, filepathWithoutExtension)
                
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Hangyakusei Million Arthur 2nd Season
class HangyakuseiMillionArthur2Download(Spring2019AnimeDownload):
    title = "Hangyakusei Million Arthur 2nd Season"
    keywords = ["Hangyakusei Million Arthur 2nd Season", "Operation Han-Gyaku-Sei Million Arthur 2nd Season"]
    
    PAGE_PREFIX = "http://hangyakusei-anime.com/"
    STORY_PAGE = "http://hangyakusei-anime.com/story/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/hangyakusei2"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
            
    def run(self):
        try:
            response = self.get_response(self.STORY_PAGE)
            split1 = response.split('<table summary="List_Type01">')
            if len(split1) < 2:
                return
            split2 = split1[1].split('</table>')[0].split('<a href="../')
            for i in range(1, len(split2), 1):
                if i < 11 or i > 23:
                    continue
                episode = str(i).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(self.base_folder + "/" + episode + "_1.png"):
                    continue
                page_url = self.PAGE_PREFIX + split2[i].split('"')[0]
                page_response = self.get_response(page_url)
                split4 = page_response.split('<div class="block line_01">')
                if len(split4) < 2:
                    continue
                split5 = split4[1].split('<div class="block line_02">')[0].split('<img src="../')
                for j in range(1, len(split5), 1):
                    imageUrl = self.PAGE_PREFIX + split5[j].split('"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Hitoribocchi no Marumaru Seikatsu
class HitoribocchiDownload(Spring2019AnimeDownload):
    title = "Hitoribocchi no Marumaru Seikatsu"
    keywords = ["Hitoribocchi no Marumaru Seikatsu"]
    
    IMAGE_PREFIX = "http://hitoribocchi.jp/"
    PAGE_LINK = "http://hitoribocchi.jp/story/"
    FINAL_EPISODE = 12
    NUM_OF_PICTURES_PER_PAGE = 6
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/hitoribocchi"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            response = self.get_response(self.PAGE_LINK)
            if len(response) == 0:
                return
            for i in range(self.FINAL_EPISODE):
                episode = str(i+1).zfill(2)
                first_split = response.split("<div id=\"S_" + str(i+1) + "\">")
                if len(first_split) < 2:
                    break
                textBlocks = first_split[1].split("src=\"../")
                for j in range(self.NUM_OF_PICTURES_PER_PAGE + 1):
                    if j == 0:
                        continue
                    imageUrl = self.IMAGE_PREFIX + textBlocks[j].split("\"")[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
                
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Isekai Quartet
class IsekaiQuartetDownload(Spring2019AnimeDownload):
    title = "Isekai Quartet"
    keywords = ["Isekai Quartet"]
    
    IMAGE_PREFIX = "http://isekai-quartet.com/"
    PAGE_LINK = "http://isekai-quartet.com/story/index_s1.html"
    FINAL_EPISODE = 12
    NUM_OF_PICTURES_PER_PAGE = 6
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/isekai-quartet"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            response = self.get_response(self.PAGE_LINK)
            if len(response) == 0:
                return
            for i in range(self.FINAL_EPISODE):
                episode = str(i+1).zfill(2)
                first_split = response.split("<div id=\"S_" + str(i+1) + "\">")
                if len(first_split) < 2:
                    break
                second_split = first_split[1].split("<div class=\"slider-sceneImage\">")
                if len(second_split) < 2:
                    break
                textBlocks = second_split[1].split("src=\"../")
                for j in range(self.NUM_OF_PICTURES_PER_PAGE + 1):
                    if j == 0:
                        continue
                    imageUrl = self.IMAGE_PREFIX + textBlocks[j].split("\"")[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
                
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Kenja no Mago
class KenjaNoMagoDownload(Spring2019AnimeDownload):
    title = "Kenja no Mago"
    keywords = ["Kenja no Mago", "Wise Man's Grandchild"]

    IMAGE_PREFIX = "http://kenja-no-mago.jp/story/img/story/"
    IMAGE_SUFFIX = ".gif"
    FINAL_EPISODE = 12
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/kenja-no-mago"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            for i in range(self.FINAL_EPISODE):
                episode = str(i+1).zfill(2)
                imageUrl = self.IMAGE_PREFIX + str(i+1) + self.IMAGE_SUFFIX
                filepathWithoutExtension = self.base_folder + "/" + episode
                self.download_image(imageUrl, filepathWithoutExtension)
                
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Midara na Ao-chan wa Benkyou ga Dekinai
class MidaraNaAochanDownload(Spring2019AnimeDownload):
    title = "Midara na Ao-chan wa Benkyou ga Dekinai"
    keywords = ["Midara na Ao-chan wa Benkyou ga Dekinai", "Ao-chan Can't Study!", "Aochan"]
    
    PAGE_LINK = "http://aochan-anime.com/story"
    FINAL_EPISODE = 12
    NUM_OF_PICTURES_PER_PAGE = 6
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/midara-na-aochan"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            response = self.get_response(self.PAGE_LINK)
            if len(response) == 0:
                return
            for i in range(self.FINAL_EPISODE):
                episode = str(i+1).zfill(2)
                first_split = response.split("<div id=\"slideshow" + str(i+1).zfill(2) + "\">")
                if len(first_split) < 2:
                    break
                textBlocks = first_split[1].split("src=\"")
                for j in range(self.NUM_OF_PICTURES_PER_PAGE + 1):
                    if j == 0:
                        continue
                    imageUrl = textBlocks[j].split("\"")[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
                
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Nande Koko ni Sensei ga!?
class NankokoDownload(Spring2019AnimeDownload):
    title = "Nande Koko ni Sensei ga!?"
    keywords = ["Nande Koko ni Sensei ga!?", "Nankoko", "Why the hell are you here, Teacher!?"]
    
    PAGE_LINK = "http://nankoko-anime.com/"
    # FINAL_EPISODE = 12
    NUM_OF_PICTURES_PER_PAGE = 4
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/nankoko"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            response = self.get_response(self.PAGE_LINK)
            if len(response) == 0:
                return
            first_split = response.split("<p class=\"temp_red_title slider\">")
            if len(first_split) < 2:
                return
            for i in range(len(first_split)):
                if i == 0:
                    continue
                episode = str(i).zfill(2)
                second_split = first_split[i].split("</ul>")
                if len(second_split) < 2:
                    continue
                textBlocks = second_split[1].split("src=\"")
                for j in range(self.NUM_OF_PICTURES_PER_PAGE + 1):
                    if j == 0:
                        continue
                    imageUrl = textBlocks[j].split("\"")[0].replace("-1024x576","")
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
                
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Nobunaga-sensei no Osanazuma
class NobutsumaDownload(Spring2019AnimeDownload):
    title = "Nobunaga-sensei no Osanazuma"
    keywords = ["Nobunaga-sensei no Osanazuma", "Nobutsuma"]
    
    PAGE_LINK = "http://nobutsuma-anime.com/story/"
    FINAL_EPISODE = 12
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/nobutsuma"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            response = self.get_response(self.PAGE_LINK)
            if len(response) == 0:
                return
            for i in range(self.FINAL_EPISODE):
                episode = str(i+1).zfill(2)
                first_split = response.split("id=\"story" + str(i+1) + "\"")
                if len(first_split) < 2:
                    return
                textBlocks = first_split[1].split("src=\"")
                if len(textBlocks) < 2:
                    return
                imageUrl = textBlocks[1].split("\"")[0]
                filepathWithoutExtension = self.base_folder + "/" + episode
                self.download_image(imageUrl, filepathWithoutExtension)
                
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Senryuu Shoujo
class SenryuuShoujoDownload(Spring2019AnimeDownload):
    title = "Senryuu Shoujo"
    keywords = ["Senryuu Shoujo", "Senryuu Girl"]
    
    PAGE_LINK = "http://senryu-girl-official.com/story"
    FINAL_EPISODE = 12
    NUM_OF_PICTURES_PER_PAGE = 6
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/senryuu-shoujo"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            response = self.get_response(self.PAGE_LINK)
            if len(response) == 0:
                return
            for i in range(self.FINAL_EPISODE):
                episode = str(i+1).zfill(2)
                first_split = response.split("<div id=\"slideshow" + str(i+1).zfill(2) + "\"")
                if len(first_split) < 2:
                    break
                textBlocks = first_split[1].split("src=\"")
                for j in range(self.NUM_OF_PICTURES_PER_PAGE + 1):
                    if j == 0:
                        continue
                    imageUrl = textBlocks[j].split("\"")[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
                
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Sewayaki Kitsune no Senko-san
class SenkosanDownload(Spring2019AnimeDownload):
    title = "Sewayaki Kitsune no Senko-san"
    keywords = ["Sewayaki Kitsune no Senko-san", "Senkosan", "The Helpful Fox Senko-san"]
    
    IMAGE_PREFIX = "http://senkosan.com/"
    PAGE_LINK = "http://senkosan.com/story/"
    FINAL_EPISODE = 12
    NUM_OF_PICTURES_PER_PAGE = 6
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/senkosan"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            response = self.get_response(self.PAGE_LINK)
            if len(response) == 0:
                return
            for i in range(self.FINAL_EPISODE):
                episode = str(i+1).zfill(2)
                first_split = response.split("<div id=\"S_" + str(i+1) + "\">")
                if len(first_split) < 2:
                    break
                second_split = first_split[1].split("<div class=\"slider-sceneImage\">")
                if len(second_split) < 2:
                    break
                textBlocks = second_split[1].split("src=\"../")
                for j in range(self.NUM_OF_PICTURES_PER_PAGE + 1):
                    if j == 0:
                        continue
                    imageUrl = self.IMAGE_PREFIX + textBlocks[j].split("\"")[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
                
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Yatogame-chan Kansatsu Nikki
class YatogameDownload(Spring2019AnimeDownload):
    title = "Yatogame-chan Kansatsu Nikki"
    keywords = ["Yatogame-chan Kansatsu Nikki", "Yatogamechan"]
    
    PAGE_LINK = "https://yatogame.nagoya/story/"
    FINAL_EPISODE = 12
    NUM_OF_PICTURES_PER_PAGE = 4
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/yatogame"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            response = self.get_response(self.PAGE_LINK)
            if len(response) == 0:
                return
            for i in range(self.FINAL_EPISODE):
                episode = str(i+1).zfill(2)
                first_split = response.split("<div id=\"chapter" + str(i+1).zfill(2) + "\"")
                if len(first_split) < 2:
                    break
                second_split = first_split[1].split("<div id=\"story-sumbnail\">")
                if len(second_split) < 2:
                    break
                textBlocks = second_split[1].split("src=\"")
                for j in range(self.NUM_OF_PICTURES_PER_PAGE + 1):
                    if j == 0:
                        continue
                    imageUrl = textBlocks[j].split("\"")[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
                
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Kono Yo no Hate de Koi wo Utau Shoujo YU-NO
class YunoDownload(Spring2019AnimeDownload):
    title = "Kono Yo no Hate de Koi wo Utau Shoujo YU-NO"
    keywords = ["Kono Yo no Hate de Koi wo Utau Shoujo YU-NO", "Yuno",
                "YU-NO: A girl who chants love at the bound of this world."]

    PAGE_PREFIX = "http://yuno-anime.com/episode/"
    FINAL_EPISODE = 26
    NUM_OF_PICTURES_PER_PAGE = 8

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/yuno"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            for i in range(self.FINAL_EPISODE):
                episode = str(i+1).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                    continue
                link = self.PAGE_PREFIX + str(i+1)
                response = self.get_response(link)
                if len(response) == 0:
                    break
                first_split = response.split("id=\"episode_swiper\">")
                if len(first_split) < 2:
                    return
                textBlocks = first_split[1].split("data-src=\"")
                if len(textBlocks) < 2:
                    return
                for j in range(self.NUM_OF_PICTURES_PER_PAGE + 1):
                    if j == 0:
                        continue
                    imageUrl = textBlocks[j].split("\"")[0].replace("-1024x576", "")
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
                
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)
    