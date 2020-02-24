import os
from anime.main_download import MainDownload


# Spring 2016 Anime
class Spring2016AnimeDownload(MainDownload):
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/2016-2"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)


# Gakusen Toshi Asterisk 2nd Season
class GakusenToshiAsterisk2Download(Spring2016AnimeDownload):

    IMAGE_URL = 'https://asterisk-war.com/assets/img/story/%s/ep_slide%s.jpg'
    FIRST_EPISODE = 13
    FINAL_EPISODE = 24
    NUM_OF_PICTURES_PER_PAGE = 4

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/gakusen-toshi-asterisk2"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        for i in range(self.FIRST_EPISODE, self.FINAL_EPISODE + 1, 1):
            episode = str(i).zfill(2)
            #if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
            #    continue
            for j in range(self.NUM_OF_PICTURES_PER_PAGE):
                image_url = self.IMAGE_URL % (str(i).zfill(2), str(j + 1).zfill(2))
                filepath_without_extension = self.base_folder + "/" + episode + '_' + str(j + 1)
                self.download_image(image_url, filepath_without_extension)
