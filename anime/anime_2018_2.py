import os
from anime.main_download import MainDownload


# Spring 2018 Anime
class Spring2018AnimeDownload(MainDownload):
    season = "2018-2"
    season_name = "Spring 2018"
    folder_name = '2018-2'
    
    def __init__(self):
        super().__init__()


# Alice or Alice: Siscon Niisan to Futago no Imouto
class AliceOrAliceDownload(Spring2018AnimeDownload):
    title = "Alice or Alice"
    keywords = ["Alice or Alice: Siscon Niisan to Futago no Imouto"]
    folder_name = 'alice-or-alice'

    IMAGE_URL = "http://alice-or-alice.com/images/story/story%s/%s.jpg"
    FINAL_EPISODE = 12
    NUM_OF_PICTURES_PER_PAGE = 6
    
    def __init__(self):
        super().__init__()
    
    def run(self):
        try:
            for i in range(1, self.FINAL_EPISODE + 1, 1):
                episode = str(i).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                    continue
                for j in range(self.NUM_OF_PICTURES_PER_PAGE):
                    imageNum = str(j+1).zfill(2)
                    imageUrl = self.IMAGE_URL % (episode, imageNum)
                    filepathWithoutExtension = self.base_folder + "/" + episode + '_' + str(j+1)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Amanchu! Advance
class Amanchu2Download(Spring2018AnimeDownload):
    title = "Amanchu! Advance"
    keywords = ["Amanchu! Advance"]
    folder_name = 'amanchu2'

    IMAGE_URL = "http://amanchu-anime.com/img/story2%s_1%s.jpg"
    FINAL_EPISODE = 12
    NUM_OF_PICTURES_PER_PAGE = 3
    
    def __init__(self):
        super().__init__()
    
    def run(self):
        try:
            for i in range(1, self.FINAL_EPISODE + 1, 1):
                episode = str(i).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                    continue
                for j in range(self.NUM_OF_PICTURES_PER_PAGE):
                    imageNum = str(j+1)
                    imageUrl = self.IMAGE_URL % (episode, imageNum)
                    filepathWithoutExtension = self.base_folder + "/" + episode + '_' + imageNum
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Comic Girls
class ComicGirlsDownload(Spring2018AnimeDownload):
    title = "Comic Girls"
    keywords = ["Comic Girls"]
    folder_name = 'comic-girls'

    IMAGE_URL = "http://comic-girls.com/story/img/story%s.png"
    FINAL_EPISODE = 12
    
    def __init__(self):
        super().__init__()
    
    def run(self):
        try:
            for i in range(1, self.FINAL_EPISODE + 1, 1):
                episode = str(i).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + ".png"):
                    continue
                imageUrl = self.IMAGE_URL % str(i)
                filepathWithoutExtension = self.base_folder + "/" + episode
                self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Golden Kamuy
class GoldenKamuyDownload(Spring2018AnimeDownload):
    title = "Golden Kamuy"
    keywords = ["Golden Kamuy", "Kamui"]
    folder_name = 'golden-kamuy'

    PAGE_URL = "https://kamuy-anime.com/story/%s.html"
    PAGE_PREFIX = "https://kamuy-anime.com/"
    FINAL_EPISODE = 12
    
    def __init__(self):
        super().__init__()
    
    def run(self):
        try:
            for i in range(1, self.FINAL_EPISODE + 1, 1):
                episode = str(i).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                    continue
                response = self.get_response(self.PAGE_URL % episode)
                split1 = response.split('<div class="ph"><a href="../')
                for j in range(1, len(split1), 1):
                    imageUrl = self.PAGE_PREFIX + split1[j].split('"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + '_' + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Hinamatsuri
class HinamatsuriDownload(Spring2018AnimeDownload):
    title = "Hinamatsuri"
    keywords = ["Hinamatsuri"]
    folder_name = 'hinamatsuri'

    IMAGE_URL = "http://hina-matsuri.net/assets/story/%s_%s.jpg"
    FINAL_EPISODE = 12
    NUM_OF_PICTURES_PER_PAGE = 6
    
    def __init__(self):
        super().__init__()
    
    def run(self):
        try:
            for i in range(1, self.FINAL_EPISODE + 1, 1):
                episode = str(i).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                    continue
                for j in range(self.NUM_OF_PICTURES_PER_PAGE):
                    imageNum = str(j+1)
                    imageUrl = self.IMAGE_URL % (str(i), imageNum)
                    filepathWithoutExtension = self.base_folder + "/" + episode + '_' + imageNum
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Hisone to Maso-tan
class HisomasoDownload(Spring2018AnimeDownload):
    title = "Hisone to Maso-tan"
    keywords = ["Hisone to Maso-tan", "Dragon Pilot: Hisone and Masotan"]
    folder_name = 'hisomaso'

    IMAGE_URL = "http://hisomaso.com/core_sys/images/main/cont/story/ep%s_story_img%s.jpg"
    MAX_PAGES = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 6]
    
    def __init__(self):
        super().__init__()
    
    def run(self):
        try:
            for i in range(len(self.MAX_PAGES)):
                episode = str(i+1).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                    continue
                for j in range(self.MAX_PAGES[i]):
                    imageNum = str(j+1)
                    imageUrl = self.IMAGE_URL % (str(i+1), imageNum)
                    filepathWithoutExtension = self.base_folder + "/" + episode + '_' + imageNum
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Last Period: Owarinaki Rasen no Monogatari
class LastPeriodDownload(Spring2018AnimeDownload):
    title = "Last Period: Owarinaki Rasen no Monogatari"
    keywords = ["Last Period: Owarinaki Rasen no Monogatari", "Last Period: The Journey to the End of the Despair"]
    folder_name = 'last-period'

    PAGE_PREFIX = "https://www.lastperiod.jp/"
    STORY_PAGE_URL = "https://www.lastperiod.jp/story/%s.html"
    FINAL_EPISODE = 12
    
    def __init__(self):
        super().__init__()
    
    def run(self):
        try:
            for i in range(self.FINAL_EPISODE):
                episode = str(i+1).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(self.base_folder + "/" + episode + "_1.png"):
                    continue
                page_url = self.STORY_PAGE_URL % episode
                response = self.get_response(page_url)
                split1 = response.split('<div class="ph"><a href="../')
                for j in range(1, len(split1), 1):
                    imageUrl = self.PAGE_PREFIX + split1[j].split('"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + '_' + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Lostorage Conflated WIXOSS
class LostorageConflatedWixossDownload(Spring2018AnimeDownload):
    title = "Lostorage Conflated WIXOSS"
    keywords = ["Lostorage Conflated WIXOSS"]
    folder_name = 'lostorage-conflated-wixoss'

    IMAGE_URL = "http://lostorage-wixoss.com/story/images/story%s_%s.jpg"
    FINAL_EPISODE = 12
    NUM_OF_PICTURES_PER_PAGE = 6
    
    def __init__(self):
        super().__init__()
    
    def run(self):
        try:
            for i in range(1, self.FINAL_EPISODE + 1, 1):
                episode = str(i).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                    continue
                for j in range(self.NUM_OF_PICTURES_PER_PAGE):
                    imageNum = str(j+1)
                    imageUrl = self.IMAGE_URL % (episode, imageNum)
                    filepathWithoutExtension = self.base_folder + "/" + episode + '_' + imageNum
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Sword Art Online Alternative: Gun Gale Online
class GunGaleOnlineDownload(Spring2018AnimeDownload):
    title = "Sword Art Online Alternative: Gun Gale Online"
    keywords = [title, 'ggo']
    folder_name = 'gungale-online'

    IMAGE_URL = "https://gungale-online.net/1st/assets/images/story/img_ep%s_%s.jpg"
    FINAL_EPISODE = 12
    NUM_OF_PICTURES_PER_PAGE = 2
    
    def __init__(self):
        super().__init__()
    
    def run(self):
        try:
            for i in range(1, self.FINAL_EPISODE + 1, 1):
                episode = str(i).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                    continue
                for j in range(self.NUM_OF_PICTURES_PER_PAGE):
                    imageNum = str(j+1)
                    imageUrl = self.IMAGE_URL % (episode, imageNum.zfill(2))
                    filepathWithoutExtension = self.base_folder + "/" + episode + '_' + imageNum
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Tada-kun wa Koi wo Shinai
class TadakoiDownload(Spring2018AnimeDownload):
    title = "Tada-kun wa Koi wo Shinai"
    keywords = ["Tada-kun wa Koi wo Shinai", "Tada Never Falls in Love", "Tadakun"]
    folder_name = 'tadakoi'

    IMAGE_URL = "http://tadakoi.tv/images/story/%s/p_%s.jpg"
    FINAL_EPISODE = 13
    NUM_OF_PICTURES_PER_PAGE = 6
    
    def __init__(self):
        super().__init__()
    
    def run(self):
        try:
            for i in range(1, self.FINAL_EPISODE + 1, 1):
                episode = str(i).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                    continue
                for j in range(self.NUM_OF_PICTURES_PER_PAGE):
                    imageNum = str(j+1)
                    imageUrl = self.IMAGE_URL % (episode.zfill(3), imageNum.zfill(3))
                    filepathWithoutExtension = self.base_folder + "/" + episode + '_' + imageNum
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Wotaku ni Koi wa Muzukashii
class WotakoiDownload(Spring2018AnimeDownload):
    title = "Wotaku ni Koi wa Muzukashii"
    keywords = ["Wotaku ni Koi wa Muzukashii", "Wotakoi: Love is Hard for Otaku"]
    folder_name = 'wotakoi'

    IMAGE_URL = "https://wotakoi-anime.com/assets/img/story/%s/ph_slide%s.jpg"
    FINAL_EPISODE = 11
    NUM_OF_PICTURES_PER_PAGE = 4
    
    def __init__(self):
        super().__init__()
    
    def run(self):
        try:
            for i in range(1, self.FINAL_EPISODE + 1, 1):
                episode = str(i).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                    continue
                for j in range(self.NUM_OF_PICTURES_PER_PAGE):
                    imageNum = str(j+1)
                    imageUrl = self.IMAGE_URL % (episode, imageNum.zfill(2))
                    filepathWithoutExtension = self.base_folder + "/" + episode + '_' + imageNum
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)
