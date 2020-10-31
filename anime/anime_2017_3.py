import os
from anime.main_download import MainDownload


# Summer 2017 Anime
class Summer2017AnimeDownload(MainDownload):
    season = "2017-3"
    season_name = "Summer 2017"
    folder_name = '2017-3'
    
    def __init__(self):
        super().__init__()


# Gamers!
class GamersDownload(Summer2017AnimeDownload):
    title = "Gamers!"
    keywords = ["Gamers!"]
    folder_name = 'gamers'

    PAGE_URL = 'https://www.gamers-anime.com/story/%s.html'
    IMAGE_PREFIX = 'https://www.gamers-anime.com/'
    FINAL_EPISODE = 12
    
    def __init__(self):
        super().__init__()
    
    def run(self):
        try:
            for i in range(self.FINAL_EPISODE):
                episode = str(i+1).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                    continue
                page_url = self.PAGE_URL % episode
                story_li = self.get_soup(page_url).find_all('div', class_='ph')
                for j in range(len(story_li)):
                    image_url = story_li[j].find('a')['href'].replace('../', self.IMAGE_PREFIX)
                    filepath_without_extension = self.base_folder + "/" + episode + '_' + str(j+1)
                    self.download_image(image_url, filepath_without_extension)

        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Isekai wa Smartphone to Tomo ni
class IsesumaDownload(Summer2017AnimeDownload):
    title = "Isekai wa Smartphone to Tomo ni"
    keywords = ["Isekai wa Smartphone to Tomo ni", "Isesuma", "In Another World With My Smartphone"]
    folder_name = 'isesuma'

    IMAGE_URL = "http://isesuma-anime.jp/img/story/ep%s/scene%s.png"
    FINAL_EPISODE = 12
    NUM_OF_PICTURES_PER_PAGE = 4

    def __init__(self):
        super().__init__()

    def run(self):
        for i in range(self.FINAL_EPISODE):
            episode = str(i+1).zfill(2)
            if self.is_file_exists(self.base_folder + "/" + episode + "_1.png"):
                continue
            for j in range(self.NUM_OF_PICTURES_PER_PAGE):
                pic_num = str(j+1).zfill(2)
                image_url = self.IMAGE_URL % (episode, pic_num)
                filepath_without_extension = self.base_folder + "/" + episode + '_' + str(j+1)
                self.download_image(image_url, filepath_without_extension)


# New Game!!
class NewGame2Download(Summer2017AnimeDownload):
    title = "New Game!!"
    keywords = ["New Game!!"]
    folder_name = 'new-game2'

    IMAGE_URL = 'http://newgame-anime.com/assets/outline/s2/%s_%s.jpg'
    FINAL_EPISODE = 12
    NUM_OF_PICTURES_PER_PAGE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        for i in range(self.FINAL_EPISODE):
            episode = str(i+1).zfill(2)
            if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                continue
            for j in range(self.NUM_OF_PICTURES_PER_PAGE):
                pic_num = str(j+1)
                image_url = self.IMAGE_URL % (str(i+1), pic_num)
                filepath_without_extension = self.base_folder + "/" + episode + '_' + str(j+1)
                self.download_image(image_url, filepath_without_extension)


# Tenshi no 3P
class TenshiNo3PDownload(Summer2017AnimeDownload):
    title = "Tenshi no 3P!"
    keywords = ["Tenshi no 3P!", "Angel's 3Piece!"]
    folder_name = 'tenshi-no-3p'

    IMAGE_URL = 'http://www.tenshi-no-3p.com/img/story/ep%s/story%s_%s.jpg'
    FINAL_EPISODE = 12
    NUM_OF_PICTURES_PER_PAGE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                continue
            for j in range(self.NUM_OF_PICTURES_PER_PAGE):
                pic_num = str(j + 1).zfill(2)
                num = episode
                # Handle episode 9 image link
                if (i+1) == 9:
                    num = str(i+1)
                image_url = self.IMAGE_URL % (num, episode, pic_num)
                filepath_without_extension = self.base_folder + "/" + episode + '_' + str(j + 1)
                self.download_image(image_url, filepath_without_extension)


# Tsurezure Children
class TsurezureChildrenDownload(Summer2017AnimeDownload):
    title = "Tsurezure Children"
    keywords = ["Tsurezure Children", "Tsuredure"]
    folder_name = 'tsurezure-children'

    PAGE_URL = 'http://tsuredure-project.jp/story'

    def __init__(self):
        super().__init__()

    def run(self):
        try:
            story_divs = self.get_soup(self.PAGE_URL).find_all('div', class_='thumbnail')
            episode_num = 0
            for story_div in reversed(story_divs):
                episode_num += 1
                episode = str(episode_num).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                    continue
                image_urls = story_div.find_all('img')
                for j in range(len(image_urls)):
                    image_url = image_urls[j]['src']
                    filepath_without_extension = self.base_folder + "/" + episode + '_' + str(j + 1)
                    self.download_image(image_url, filepath_without_extension)

        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Youkoso Jitsuryoku Shijou Shugi no Kyoushitsu e
class YouzitsuDownload(Summer2017AnimeDownload):
    title = "Youkoso Jitsuryoku Shijou Shugi no Kyoushitsu e"
    keywords = ["Youkoso Jitsuryoku Shijou Shugi no Kyoushitsu e", "Youzitsu", "Youjitsu",
                "Classroom of the Elite"]
    folder_name = 'youzitsu'

    IMAGE_URL = 'http://you-zitsu.com/assets/story/%s_%s.jpg'
    FINAL_EPISODE = 12
    NUM_OF_PICTURES_PER_PAGE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                continue
            for j in range(self.NUM_OF_PICTURES_PER_PAGE):
                image_url = self.IMAGE_URL % (str(i + 1), str(j + 1))
                filepath_without_extension = self.base_folder + "/" + episode + '_' + str(j + 1)
                self.download_image(image_url, filepath_without_extension)
