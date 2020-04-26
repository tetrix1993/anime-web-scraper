import os
from anime.main_download import MainDownload


# Spring 2017 Anime
class Spring2017AnimeDownload(MainDownload):
    season = "2017-2"
    season_name = "Spring 2017"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/2017-2"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)


# Alice to Zouroku
class AliceToZourokuDownload(Spring2017AnimeDownload):
    title = "Alice to Zouroku"
    keywords = ["Alice to Zouroku", "Alice & Zoroku", "and"]

    PAGE_URL = 'https://www.alicetozouroku.com/story/story_%s.html'
    IMAGE_PREFIX = 'https://www.alicetozouroku.com'
    FINAL_EPISODE = 12
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/alice-to-zouroku"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            for i in range(self.FINAL_EPISODE):
                episode = str(i+1).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + ".jpg"):
                    continue
                page_url = self.PAGE_URL % episode
                image_url = self.IMAGE_PREFIX + self.get_soup(page_url).find('ul', class_='story-slider').find('img')['src']
                filepath_without_extension = self.base_folder + "/" + episode
                self.download_image(image_url, filepath_without_extension)

        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Busou Shoujo Machiavellianism
class BusouShoujoMachiavellismDownload(Spring2017AnimeDownload):
    title = "Busou Shoujo Machiavellianism"
    keywords = ["Busou Shoujo Machiavellianism", "Armed Girl's Machiavellism"]

    IMAGE_URL = 'http://machiavellism-anime.jp/story/img/%s/%s.jpg'

    FINAL_EPISODE = 12
    NUM_OF_PICTURES_PER_PAGE = 6

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/busou-shoujo"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                continue
            for j in range(self.NUM_OF_PICTURES_PER_PAGE):
                image_url = self.IMAGE_URL % (str(i + 1), str(j + 1))
                filepath_without_extension = self.base_folder + "/" + episode + '_' + str(j + 1)
                self.download_image(image_url, filepath_without_extension)


# Clockwork Planet
class ClockworkPlanetDownload(Spring2017AnimeDownload):
    title = "Clockwork Planet"
    keywords = ["Clockwork Planet"]

    IMAGE_URL = 'http://www.tbs.co.jp/anime/cp/story/img/story%s/%s.png'
    FINAL_EPISODE = 12
    NUM_OF_PICTURES_PER_PAGE = 5

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/clockwork-planet"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_file_exists(self.base_folder + "/" + episode + "_1.png"):
                continue
            for j in range(self.NUM_OF_PICTURES_PER_PAGE):
                image_url = self.IMAGE_URL % (str(i + 1).zfill(2), str(j + 1).zfill(2))
                filepath_without_extension = self.base_folder + "/" + episode + '_' + str(j + 1)
                self.download_image(image_url, filepath_without_extension)


# Dungeon ni Deai wo Motomeru no wa Machigatteiru Darou ka Gaiden: Sword Oratoria
class SwordOratoriaDownload(Spring2017AnimeDownload):
    title = "Dungeon ni Deai wo Motomeru no wa Machigatteiru Darou ka Gaiden: Sword Oratoria"
    keywords = ["Dungeon ni Deai wo Motomeru no wa Machigatteiru Darou ka Gaiden: Sword Oratoria", "Danmachi",
                "Sword Oratoria: Is it Wrong to Try to Pick Up Girls in a Dungeon? On the Side"]

    STORY_PAGE = 'http://danmachi.com/sword_oratoria/story/'

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/sword-oratoria"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        image_div = self.get_soup(self.STORY_PAGE).find_all('div', class_='vol-img')
        for i in range(len(image_div)):
            episode = str(i + 1).zfill(2)
            if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                continue
            images = image_div[i].find_all('img')
            for j in range(len(images)):
                image_url = self.STORY_PAGE + images[j]['src']
                filepath_without_extension = self.base_folder + "/" + episode + '_' + str(j + 1)
                self.download_image(image_url, filepath_without_extension)


# Eromanga Sensei
class EromangaSenseiDownload(Spring2017AnimeDownload):
    title = "Eromanga Sensei"
    keywords = ["Eromanga Sensei", "Eromanga-Sensei"]

    IMAGE_URL = 'https://eromanga-sensei.com/assets/img/story/%s/%s.jpg'
    FINAL_EPISODE = 12
    NUM_OF_PICTURES_PER_PAGE = 6

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/eromanga-sensei"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                continue
            for j in range(self.NUM_OF_PICTURES_PER_PAGE):
                image_url = self.IMAGE_URL % (str(i + 1).zfill(2), str(j + 1).zfill(2))
                filepath_without_extension = self.base_folder + "/" + episode + '_' + str(j + 1)
                self.download_image(image_url, filepath_without_extension)


# Hinako Note
class HinakoNoteDownload(Spring2017AnimeDownload):
    title = "Hinako Note"
    keywords = ["Hinako Note"]

    IMAGE_URL = 'http://hinakonote.jp/assets/story/%s_%s.jpg'

    FINAL_EPISODE = 12
    NUM_OF_PICTURES_PER_PAGE = 6

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/hinako-note"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                continue
            for j in range(self.NUM_OF_PICTURES_PER_PAGE):
                image_url = self.IMAGE_URL % (str(i + 1), str(j + 1))
                filepath_without_extension = self.base_folder + "/" + episode + '_' + str(j + 1)
                self.download_image(image_url, filepath_without_extension)


# Re:Creators
class ReCreatorsDownload(Spring2017AnimeDownload):
    title = "Re:Creators"
    keywords = ["Re:Creators"]

    IMAGE_URL = 'https://recreators.tv/img/story/story_%s_%s.jpg'
    FINAL_EPISODE = 22
    NUM_OF_PICTURES_PER_PAGE = 3

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/re-creators"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                continue
            for j in range(self.NUM_OF_PICTURES_PER_PAGE):
                image_url = self.IMAGE_URL % (str(i + 1).zfill(2), str(j + 1).zfill(2))
                filepath_without_extension = self.base_folder + "/" + episode + '_' + str(j + 1)
                self.download_image(image_url, filepath_without_extension)


# Renai Boukun
class RenaiBoukunDownload(Spring2017AnimeDownload):
    title = "Renai Boukun"
    keywords = ["Renai Boukun", "Love Tyrant"]

    STORY_PAGE = 'https://renaiboukun.com/story/'
    NUM_OF_PICTURES_PER_PAGE = 6

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/renai-boukun"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        try:
            page_divs = self.get_soup(self.STORY_PAGE).find_all('div', class_='newsBox')
            for i in range(len(page_divs)):
                episode = str(i + 1).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                    continue
                page_url = self.STORY_PAGE + page_divs[i].find('a')['href']
                images = self.get_soup(page_url).find('div', class_='txtBody').find_all('img')
                max_len = min(len(images), self.NUM_OF_PICTURES_PER_PAGE)
                # Skip Episode 1's 6th image
                if (i + 1) == 1:
                    max_len = min(max_len, 5)
                for j in range(max_len):
                    image_url = images[j]['src']
                    filepath_without_extension = self.base_folder + "/" + episode + '_' + str(j + 1)
                    self.download_image(image_url, filepath_without_extension)

        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Rokudenashi Majutsu Koushi to Akashic Records
class RokuakaDownload(Spring2017AnimeDownload):
    title = "Rokudenashi Majutsu Koushi to Akashic Records"
    keywords = ["Rokudenashi Majutsu Koushi to Akashic Records", "Rokuaka",
                "Akashic Records of Bastard Magic Instructor"]

    STORY_PAGE = 'http://rokuaka.jp/story/'
    IMAGE_PREFIX = 'http://rokuaka.jp'

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/rokuaka"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        try:
            page_divs = self.get_soup(self.STORY_PAGE).find_all('div', class_='main-carousel')
            num = 0
            for page_div in reversed(page_divs):
                num += 1
                episode = str(num).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                    continue
                images = page_div.find_all('img')
                for j in range(len(images)):
                    image_url = self.IMAGE_PREFIX + images[j]['src']
                    filepath_without_extension = self.base_folder + "/" + episode + '_' + str(j + 1)
                    self.download_image(image_url, filepath_without_extension)

        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Saenai Heroine no Sodatekata Flat
class Saekano2Download(Spring2017AnimeDownload):
    title = "Saenai Heroine no Sodatekata Flat"
    keywords = ["Saenai Heroine no Sodatekata Flat", "Saekano: How to Raise a Boring Girlfriend"]

    IMAGE_URL = 'https://www.saenai.tv/images/story/%s/%s.jpg'
    FINAL_EPISODE = 12 # including Episode 0
    NUM_OF_PICTURES_PER_PAGE = 4

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/saekano2"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        for i in range(self.FINAL_EPISODE):
            episode = str(i).zfill(2)
            if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                continue
            for j in range(self.NUM_OF_PICTURES_PER_PAGE):
                image_url = self.IMAGE_URL % (str(i).zfill(2), str(j + 1).zfill(2))
                filepath_without_extension = self.base_folder + "/" + episode + '_' + str(j + 1)
                self.download_image(image_url, filepath_without_extension)


# Sakura Quest
class SakuraQuestDownload(Spring2017AnimeDownload):
    title = "Sakura Quest"
    keywords = ["Sakura Quest"]

    IMAGE_URL = 'http://sakura-quest.com/story/images/%s_%s.jpg'
    FINAL_EPISODE = 25
    NUM_OF_PICTURES_PER_PAGE = 6

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/sakura-quest"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                continue
            for j in range(self.NUM_OF_PICTURES_PER_PAGE):
                image_url = self.IMAGE_URL % (str(i + 1).zfill(2), str(j + 1))
                filepath_without_extension = self.base_folder + "/" + episode + '_' + str(j + 1)
                self.download_image(image_url, filepath_without_extension)


# Sakurada Reset
class SakuradaResetDownload(Spring2017AnimeDownload):
    title = "Sakurada Reset"
    keywords = ["Sakurada Reset", "Sagrada Reset"]

    IMAGE_URL = 'http://wwwsp.sagrada-anime.com/img/story/ep%s/img%s.jpg'
    FINAL_EPISODE = 24
    NUM_OF_PICTURES_PER_PAGE = 4

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/sakurada-reset"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                continue
            for j in range(self.NUM_OF_PICTURES_PER_PAGE):
                image_url = self.IMAGE_URL % (str(i + 1).zfill(2), str(j + 1).zfill(2))
                filepath_without_extension = self.base_folder + "/" + episode + '_' + str(j + 1)
                self.download_image(image_url, filepath_without_extension)


# Shuumatsu Nani Shitemasu ka? Isogashii Desu ka? Sukutte Moratte Ii Desu ka?
class SukasukaDownload(Spring2017AnimeDownload):
    title = "Shuumatsu Nani Shitemasu ka? Isogashii Desu ka? Sukutte Moratte Ii Desu ka?"
    keywords = ["Shuumatsu Nani Shitemasu ka? Isogashii Desu ka? Sukutte Moratte Ii Desu ka?", "Sukasuka",
                "WorldEnd: What do you do at the end of the world? Are you busy? Will you save us?"]

    STORY_PAGE = 'http://sukasuka-anime.com/story/%s.html'
    PAGE_PREFIX = 'http://sukasuka-anime.com/'
    FINAL_EPISODE = 12

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/sukasuka"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                continue
            image_divs = self.get_soup(self.STORY_PAGE % episode).find_all('div', class_='ph')
            for j in range(len(image_divs)):
                image_url = image_divs[j].find('img')['src'].replace('../', self.PAGE_PREFIX)
                filepath_without_extension = self.base_folder + "/" + episode + '_' + str(j + 1)
                self.download_image(image_url, filepath_without_extension)


# Zero kara Hajimeru Mahou no Sho
class ZeronosyoDownload(Spring2017AnimeDownload):
    title = "Zero kara Hajimeru Mahou no Sho"
    keywords = ["Zero kara Hajimeru Mahou no Sho", "Zeronosyo", "Grimoire of Zero"]

    IMAGE_URL = 'http://zeronosyo.com/img/story/ep%s/img%s.jpg'
    FINAL_EPISODE = 12
    NUM_OF_PICTURES_PER_PAGE = 6

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/zeronosyo"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                continue
            for j in range(self.NUM_OF_PICTURES_PER_PAGE):
                image_url = self.IMAGE_URL % (str(i + 1).zfill(2), str(j + 1).zfill(2))
                filepath_without_extension = self.base_folder + "/" + episode + '_' + str(j + 1)
                self.download_image(image_url, filepath_without_extension)
