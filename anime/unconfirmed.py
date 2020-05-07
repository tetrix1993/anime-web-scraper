import os
from anime.main_download import MainDownload

# Maou Gakuin no Futekigousha https://maohgakuin.com/ #魔王学院 @maohgakuin
# Re:Zero S2 http://re-zero-anime.jp/tv/story/ #rezero #リゼロ @Rezero_official
# Yahari Ore no Seishun http://www.tbs.co.jp/anime/oregairu/story/ #俺ガイル #oregairu @anime_oregairu


# Unconfirmed Season Anime
class UnconfirmedDownload(MainDownload):

    season = "9999-9"
    season_name = "Unconfirmed"

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/unconfirmed"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)


# Maou Gakuin no Futekigousha: Shijou Saikyou no Maou no Shiso, Tensei shite Shison-tachi no Gakkou e
class MaohgakuinDownload(UnconfirmedDownload):
    title = "Maou Gakuin no Futekigousha: Shijou Saikyou no Maou no Shiso, Tensei shite Shison-tachi no Gakkou e"
    keywords = ["Maou Gakuin no Futekigousha: Shijou Saikyou no Maou no Shiso, Tensei shite Shison-tachi no Gakkou e"]

    PAGE_PREFIX = "https://maohgakuin.com/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/maohgakuin"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        pass


# Re:Zero kara Hajimeru Isekai Seikatsu 2nd Season
class ReZero2Download(UnconfirmedDownload):
    title = "Re:Zero kara Hajimeru Isekai Seikatsu 2nd Season"
    keywords = ["Re:Zero kara Hajimeru Isekai Seikatsu 2nd Season",
                "Re:Zero - Starting Life in Another World"]

    PAGE_PREFIX = "http://re-zero-anime.jp/tv/story/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/rezero2"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        pass


# Yahari Ore no Seishun Love Comedy wa Machigatteiru. Kan
class Oregairu3Download(UnconfirmedDownload):
    title = "Yahari Ore no Seishun Love Comedy wa Machigatteiru. Kan"
    keywords = ["Oregairu", "Yahari Ore no Seishun Love Comedy wa Machigatteiru. Kan",
                "My Teen Romantic Comedy SNAFU 3", "My youth romantic comedy is wrong as I expected 3"]

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
