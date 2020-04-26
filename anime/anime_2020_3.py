import os
from anime.main_download import MainDownload

# Maou Gakuin no Futekigousha https://maohgakuin.com/ #魔王学院 @maohgakuin
# Re:Zero S2 http://re-zero-anime.jp/tv/story/ #rezero #リゼロ @Rezero_official


# Summer 2020 Anime
class Summer2020AnimeDownload(MainDownload):

    season = "2020-3"
    season_name = "Summer 2020"

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/2020-3"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)


# Maou Gakuin no Futekigousha: Shijou Saikyou no Maou no Shiso, Tensei shite Shison-tachi no Gakkou e
class MaohgakuinDownload(Summer2020AnimeDownload):
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
class ReZero2Download(Summer2020AnimeDownload):
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
