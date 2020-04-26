import os
from anime.main_download import MainDownload


# Fall 2015 Anime
class Fall2015AnimeDownload(MainDownload):
    season = "2015-4"
    season_name = "Fall 2015"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/2015-4"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)


# Gakusen Toshi Asterisk
class GakusenToshiAsteriskDownload(Fall2015AnimeDownload):
    title = "Gakusen Toshi Asterisk"
    keywords = ["Gakusen Toshi Asterisk", "The Asterisk War"]

    IMAGE_URL = 'https://asterisk-war.com/assets/img/story/%s/ep_slide%s.jpg'
    FINAL_EPISODE = 12
    NUM_OF_PICTURES_PER_PAGE = 4

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/gakusen-toshi-asterisk"
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


# Rakudai Kishi no Cavalry
class RakudaiKishiDownload(Fall2015AnimeDownload):
    title = "Rakudai Kishi no Cavalry"
    keywords = ["Rakudai Kishi no Cavalry", "Chivalry of a Failed Knight"]

    IMAGE_URL = 'http://ittoshura.com/story/img/onair_p%s_%s.jpg'
    FINAL_EPISODE = 12
    NUM_OF_PICTURES_PER_PAGE = 6

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/rakudai-kishi"
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
