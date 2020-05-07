import os
from anime.main_download import MainDownload

# Maou Gakuin no Futekigousha https://maohgakuin.com/ #魔王学院 @maohgakuin
# Re:Zero S2 http://re-zero-anime.jp/tv/story/ #rezero #リゼロ @Rezero_official


# Summer 2020 Anime
class Summer2020AnimeDownload(MainDownload):

    # season = "2020-3"
    # season_name = "Summer 2020"

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/2020-3"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
