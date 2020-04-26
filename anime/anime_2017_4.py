import os
from anime.main_download import MainDownload


# Fall 2017 Anime
class Fall2017AnimeDownload(MainDownload):
    season = "2017-4"
    season_name = "Fall 2017"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/2017-4"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)


# Animegataris
class AnimegatarisDownload(Fall2017AnimeDownload):
    title = "Animegataris"
    keywords = ["Animegataris"]

    STORY_URL = 'http://animegataris.com/story'
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/animegataris"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            story_li = self.get_soup(self.STORY_URL).find_all('li', class_='contentsMenu__item')
            for i in range(1, len(story_li), 1):
                page_url = story_li[i].find('a')['href']
                episode = str(i).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(
                        self.base_folder + "/" + episode + "_1.png"):
                    continue
                page_soup = self.get_soup(page_url)
                image_urls = []
                slider_items = page_soup.find_all('li', class_='article__sliderItem')

                for slider_item in slider_items:
                    image_urls.append(slider_item.find('img')['src'])

                next_image_main = page_soup.find('figure', class_='article__nextImageMain')
                image_urls.append(next_image_main.find('img')['src'])

                next_thumbs = page_soup.find_all('li', class_='article__nextThumb')
                for next_thumb in next_thumbs:
                    image_urls.append(next_thumb.find('img')['src'])

                for j in range(len(image_urls)):
                    image_url = image_urls[j]
                    filepath_without_extension = self.base_folder + "/" + episode + '_' + str(j+1)
                    self.download_image(image_url, filepath_without_extension)

        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Blend S
class BlendSDownload(Fall2017AnimeDownload):
    title = "Blend S"
    keywords = ["Blend S"]

    IMAGE_URL = "https://blend-s.jp/assets/img/story/%s/img%s.jpg"
    FINAL_EPISODE = 12
    NUM_OF_PICTURES_PER_PAGE = 4

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/blend-s"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        for i in range(self.FINAL_EPISODE):
            episode = str(i+1).zfill(2)
            if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(
                    self.base_folder + "/" + episode + "_1.png"):
                continue
            for j in range(self.NUM_OF_PICTURES_PER_PAGE):
                pic_num = str(j+1)
                image_url = self.IMAGE_URL % (episode, pic_num)
                filepath_without_extension = self.base_folder + "/" + episode + '_' + pic_num
                self.download_image(image_url, filepath_without_extension)


# Imouto sae Ireba Ii.
class ImotosaeDownload(Fall2017AnimeDownload):
    title = "Imouto sae Ireba Ii."
    keywords = ["Imouto sae Ireba Ii.", "Imotosae", "A Sister's All You Need"]

    IMAGE_URL = "http://imotosae.com/story/img/%s/%s_%s.jpg"
    FINAL_EPISODE = 12
    NUM_OF_PICTURES_PER_PAGE = 3

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/imotosae"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        for i in range(self.FINAL_EPISODE):
            episode = str(i+1).zfill(2)
            if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(
                    self.base_folder + "/" + episode + "_1.png"):
                continue
            for j in range(self.NUM_OF_PICTURES_PER_PAGE):
                pic_num = str(j+1).zfill(2)
                image_url = self.IMAGE_URL % (episode, episode, pic_num)
                filepath_without_extension = self.base_folder + "/" + episode + '_' + str(j+1)
                self.download_image(image_url, filepath_without_extension)


# Konohana Kitan
class KonohanaKitanDownload(Fall2017AnimeDownload):
    title = "Konohana Kitan"
    keywords = ["Konohana Kitan"]

    IMAGE_URL = "http://konohanatei.jp/story/img/vol_%s/pic_%s.jpg"
    FINAL_EPISODE = 12
    NUM_OF_PICTURES_PER_PAGE = 7

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/konohana-kitan"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(
                    self.base_folder + "/" + episode + "_1.png"):
                continue
            for j in range(self.NUM_OF_PICTURES_PER_PAGE):
                pic_num = str(j + 1).zfill(2)
                image_url = self.IMAGE_URL % (episode, pic_num)
                filepath_without_extension = self.base_folder + "/" + episode + '_' + str(j+1)
                self.download_image(image_url, filepath_without_extension)


# Shoujo Shuumatsu Ryokou
class ShoujoShuumatsuRyokouDownload(Fall2017AnimeDownload):
    title = "Shoujo Shuumatsu Ryokou"
    keywords = ["Shoujo Shuumatsu Ryokou", "Girls' Last Tour"]

    IMAGE_URL = "http://girls-last-tour.com/assets/story/%s_%s.jpg"
    FINAL_EPISODE = 12
    NUM_OF_PICTURES_PER_PAGE = 6

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/shoujo-shuumatsu"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1)
            if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(
                    self.base_folder + "/" + episode + "_1.png"):
                continue
            for j in range(self.NUM_OF_PICTURES_PER_PAGE):
                pic_num = str(j + 1)
                image_url = self.IMAGE_URL % (episode, pic_num)
                filepath_without_extension = self.base_folder + "/" + episode + '_' + pic_num
                self.download_image(image_url, filepath_without_extension)
