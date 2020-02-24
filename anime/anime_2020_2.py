import os
from anime.main_download import MainDownload

# Gleipnir http://gleipnir-anime.com/ #グレイプニル @gleipnir_anime
# Hachi-nan tte http://hachinan-anime.com/ #八男 @Hachinan_PR
# Honzuki S2 http://booklove-anime.jp/story/ #本好きの下剋上 @anime_booklove
# Houkago Teibou Nisshi https://teibotv.com/ #teibo @teibo_bu
# Kaguya-sama S2 https://kaguya.love/ #かぐや様 @anime_kaguya
# Kakushigoto https://kakushigoto-anime.com/ #かくしごと @kakushigoto_pr
# Kingdom S3 https://kingdom-anime.com/story/ #キングダム @kingdom_animePR
# Maou Gakuin no Futekigousha https://maohgakuin.com/ #魔王学院 @maohgakuin
# Otome Game https://hamehura-anime.com/ #はめふら #hamehura @hamehura
# Princess Connect https://anime.priconne-redive.jp/ #アニメプリコネ #プリコネR #プリコネ @priconne_anime
# Re:Zero S2 http://re-zero-anime.jp/tv/story/ #rezero #リゼロ @Rezero_official
# Tamayomi https://tamayomi.com/ #tamayomi @tamayomi_PR
# Tsugumomo S2 http://tsugumomo.com/story/ #つぐもも @tsugumomo_anime
# Yahari Ore no Seishun http://www.tbs.co.jp/anime/oregairu/ #俺ガイル #oregairu @anime_oregairu
# Yesterday wo Utatte https://singyesterday.com/ #イエスタデイをうたって @anime_yesterday


# Spring 2020 Anime
class Spring2020AnimeDownload(MainDownload):
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/2020-2"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)


# Gleipnir
class GleipnirDownload(Spring2020AnimeDownload):
    
    PAGE_PREFIX = "http://gleipnir-anime.com/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/gleipnir"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        pass


# Hachi-nan tte, Sore wa Nai deshou!
class HachinanDownload(Spring2020AnimeDownload):
    
    PAGE_PREFIX = "http://hachinan-anime.com/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/hachinan"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        pass


# Honzuki no Gekokujou: Shisho ni Naru Tame ni wa Shudan wo Erandeiraremasen 2nd Season
class Honzuki2Download(Spring2020AnimeDownload):
    
    PAGE_PREFIX = "http://booklove-anime.jp/story/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/honzuki2"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        pass


# Houkago Teibou Nisshi
class TeiboDownload(Spring2020AnimeDownload):

    PAGE_PREFIX = "https://teibotv.com/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/teibo"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        pass


# Kaguya-sama wa Kokurasetai? Tensai-tachi no Renai Zunousen
class Kaguyasama2Download(Spring2020AnimeDownload):

    PAGE_PREFIX = "https://teibotv.com/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/kaguya-sama2"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        pass


# Kakushigoto
class KakushigotoDownload(Spring2020AnimeDownload):

    PAGE_PREFIX = "https://kakushigoto-anime.com/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/kakushigoto"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        pass


# Kingdom 3rd Season
class Kingdom3Download(Spring2020AnimeDownload):

    PAGE_PREFIX = "https://kingdom-anime.com/story/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/kingdom3"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        pass


# Maou Gakuin no Futekigousha: Shijou Saikyou no Maou no Shiso, Tensei shite Shison-tachi no Gakkou e
class MaohgakuinDownload(Spring2020AnimeDownload):

    PAGE_PREFIX = "https://maohgakuin.com/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/maohgakuin"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        pass


# Otome Game no Hametsu Flag shika Nai Akuyaku Reijou ni Tensei shiteshimatta...
class HamehuraDownload(Spring2020AnimeDownload):

    PAGE_PREFIX = "https://hamehura-anime.com/story"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/hamehura"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        pass


# Princess Connect! Re:Dive
class PriconneDownload(Spring2020AnimeDownload):
    
    PAGE_PREFIX = "https://anime.priconne-redive.jp/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/priconne"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        pass


# Re:Zero kara Hajimeru Isekai Seikatsu 2nd Season
class ReZero2Download(Spring2020AnimeDownload):

    PAGE_PREFIX = "http://re-zero-anime.jp/tv/story/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/rezero2"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        pass


# Tamayomi
class TamayomiDownload(Spring2020AnimeDownload):

    PAGE_PREFIX = "https://tamayomi.com/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/tamayomi"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        pass


# Tsugu Tsugumomo
class Tsugumomo2Download(Spring2020AnimeDownload):

    PAGE_PREFIX = "http://tsugumomo.com/story/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/tsugumomo2"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        pass


# Yahari Ore no Seishun Love Comedy wa Machigatteiru. Kan
class Oregairu3Download(Spring2020AnimeDownload):

    PAGE_PREFIX = "http://www.tbs.co.jp/anime/oregairu/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/oregairu3"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        pass


# Yesterday wo Utatte
class YesterdayDownload(Spring2020AnimeDownload):

    PAGE_PREFIX = "https://singyesterday.com/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/yesterday"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        pass
