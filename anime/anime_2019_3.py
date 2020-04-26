import os
from anime.main_download import MainDownload


# Summer 2019 Anime
class Summer2019AnimeDownload(MainDownload):
    season = "2019-3"
    season_name = "Summer 2019"

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/2019-3"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)


# Arifureta
class ArifuretaDownload(Summer2019AnimeDownload):
    title = "Arifureta Shokugyou de Sekai Saikyou"
    keywords = ["Arifureta Shokugyou de Sekai Saikyou", "Arifureta: From Commonplace to World's Strongest"]

    MAIN_PAGE = "https://arifureta.com/storys/"

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/arifureta"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
        
    def run(self):
        try:
            response = self.get_response(self.MAIN_PAGE)
            if len(response) == 0:
                return
            textBlocks = response.split("<h2 class=\"rdwh\">")[1] \
                .split("</ul>")[0] \
                .split("<li><a href=\"")
            
            for i in range(len(textBlocks)):
                if i == 0:
                    continue
                pageUrl = textBlocks[i].split("\"")[0]
                if "introduction" in pageUrl:
                    continue
                episode = str(i-1).zfill(2)
                response2 = self.get_response(pageUrl)
                if len(response2) == 0:
                    break
                textBlocks2 = response2.split("<ul class=\"slider-for\">")[1] \
                            .split("</ul>")[0] \
                            .split("src=\"")
                for j in range(len(textBlocks2)):
                    if j == 0:
                        continue
                    imageUrl = textBlocks2[j].split("\"")[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Dumbbell
class DumbbellDownload(Summer2019AnimeDownload):
    title = "Dumbbell Nan Kilo Moteru?"
    keywords = ["Dumbbell Nan Kilo Moteru?", "How heavy are the dumbbells you lift?"]

    PAGE_LINK = "https://dumbbell-anime.jp/story/"
    IMAGE_PREFIX = "https://dumbbell-anime.jp/"
    FINAL_EPISODE = 13
    NUM_OF_PICTURES_PER_PAGE = 6

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/dumbbell"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
            
    def run(self):
        try:
            response = self.get_response(self.PAGE_LINK)
            if len(response) == 0:
                return
            for i in range(self.FINAL_EPISODE):
                episode = str(i+1).zfill(2)
                first_split = response.split("<div id=\"S_" + str(i+1) + "\">")
                if len(first_split) < 2:
                    break
                second_split = first_split[1].split("<div class=\"ep-slider-sceneImage\">")
                if len(second_split) < 2:
                    break
                textBlocks = second_split[1].split("src=\"../")
                for j in range(self.NUM_OF_PICTURES_PER_PAGE + 1):
                    if j == 0:
                        continue
                    imageUrl = self.IMAGE_PREFIX + textBlocks[j].split("\"")[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Granbelm
class GranbelmDownload(Summer2019AnimeDownload):
    title = "Granbelm"
    keywords = ["Granbelm"]
    
    PAGE_LINK = "http://granbelm.com/story/"
    FINAL_EPISODE = 13
    NUM_OF_PICTURES_PER_PAGE = 6
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/granbelm"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            response = self.get_response(self.PAGE_LINK)
            if len(response) == 0:
                return
            for i in range(self.FINAL_EPISODE):
                episode = str(i+1).zfill(2)
                first_split = response.split("<strong>" + episode + "</strong>")
                if len(first_split) < 2:
                    break
                textBlocks = first_split[1].split("src=\"")
                for j in range(self.NUM_OF_PICTURES_PER_PAGE + 1):
                    if j == 0:
                        continue
                    imageUrl = textBlocks[j].split("\"")[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
                
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Hensuki
class HensukiDownload(Summer2019AnimeDownload):
    title = "Kawaikereba Hentai demo Suki ni Natte Kuremasu ka?"
    keywords = ["Kawaikereba Hentai demo Suki ni Natte Kuremasu ka?",
                "Hensuki: Are you willing to fall in love with a pervert, as long as she's a cutie?"]

    PAGE_PREFIX = "https://hensuki.com/story/?mode=story"
    IMAGE_PREFIX = "https://hensuki.com/story/"
    FINAL_EPISODE = 13
    NUM_OF_PICTURES_PER_PAGE = 6
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/hensuki"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            for i in range(self.FINAL_EPISODE):
                link = self.PAGE_PREFIX + str(i+1)
                response = self.get_response(link)
                if len(response) == 0:
                    break
                episode = str(i+1).zfill(2)
                first_split = response.split("<div class=\"story_img_wrap\">")
                if len(first_split) < 2:
                    break
                textBlocks = first_split[1].split("<img src=\"")
                for j in range(self.NUM_OF_PICTURES_PER_PAGE + 1):
                    if j == 0:
                        continue
                    imageUrl = self.IMAGE_PREFIX + textBlocks[j].split("\"")[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
                
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Isekai Cheat Magician
class IsekaiCheatDownload(Summer2019AnimeDownload):
    title = "Isekai Cheat Magician"
    keywords = ["Isekai Cheat Magician"]

    PAGE_LINK = "http://isekai-cheat-magician.com/story/"
    FINAL_EPISODE = 13
    NUM_OF_PICTURES_PER_PAGE = 6

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/isekai-cheat"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            response = self.get_response(self.PAGE_LINK)
            if len(response) == 0:
                return
            for i in range(self.FINAL_EPISODE):
                episode = str(i+1).zfill(2)
                first_split = response.split("id=\"s" + str(i+1) + "\"")
                if len(first_split) < 2:
                    continue
                textBlocks = first_split[1].split("<li><img src=\"")
                for j in range(self.NUM_OF_PICTURES_PER_PAGE + 1):
                    if j == 0:
                        continue
                    imageUrl = self.PAGE_LINK + textBlocks[j].split("\"")[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
                
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Joshikousei no Mudazukai
class JyoshimudaDownload(Summer2019AnimeDownload):
    title = "Joshikousei no Mudazukai"
    keywords = ["Joshikousei no Mudazukai", "Wasteful Days of High School Girl"]

    PAGE_PREFIX = "http://jyoshimuda.com/story"
    PAGE_SUFFIX = ".html"
    IMAGE_PREFIX = "http://jyoshimuda.com/"
    FINAL_EPISODE = 13
    NUM_OF_PICTURES_PER_PAGE = 5

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/jyoshimuda"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            for i in range(self.FINAL_EPISODE):
                episode = str(i+1).zfill(2)
                link = self.PAGE_PREFIX + episode + self.PAGE_SUFFIX
                response = self.get_response(link)
                if len(response) == 0:
                    break
                first_split = response.split("<div class=\"story_box\">")
                if len(first_split) < 2:
                    return
                textBlocks = first_split[1].split("<img src=\"")
                if len(textBlocks) < 2:
                    return
                for j in range(self.NUM_OF_PICTURES_PER_PAGE + 1):
                    if j == 0:
                        continue
                    imageUrl = self.IMAGE_PREFIX + textBlocks[j].split("\"")[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
                
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Kanata no Astra
class KanataNoAstraDownload(Summer2019AnimeDownload):
    title = "Kanata no Astra"
    keywords = ["Astra Lost in Space"]

    IMAGE_PREFIX = "http://astra-anime.com/"
    PAGE_LINK = "http://astra-anime.com/story/"
    FINAL_EPISODE = 13
    NUM_OF_PICTURES_PER_PAGE = 6
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/kanata-no-astra"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            response = self.get_response(self.PAGE_LINK)
            if len(response) == 0:
                return
            for i in range(self.FINAL_EPISODE):
                episode = str(i+1).zfill(2)
                first_split = response.split("<div id=\"S_" + str(i+1) + "\">")
                if len(first_split) < 2:
                    break
                textBlocks = first_split[1].split("src=\"../")
                for j in range(self.NUM_OF_PICTURES_PER_PAGE + 1):
                    if j == 0:
                        continue
                    imageUrl = self.IMAGE_PREFIX + textBlocks[j].split("\"")[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
                
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Machikado Mazoku
class MachikadoMazokuDownload(Summer2019AnimeDownload):
    title = "Machikado Mazoku"
    keywords = ["Machikado Mazoku", "The Demon Girl Next Door"]

    PAGE_PREFIX = "http://www.tbs.co.jp/anime/machikado/story/"
    # PAGE_SUFFIX = ".html"
    # IMAGE_PREFIX = "http://www.tbs.co.jp/anime/machikado/story/"
    # FINAL_EPISODE = 13
    NUM_OF_PICTURES_PER_PAGE = 4

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/machikado-mazoku"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            page_response = self.get_response(self.PAGE_PREFIX)
            if (len(page_response) == 0):
                return
            main_page_split = page_response.split("<ul class=\"story-list-block\">")
            if (len(main_page_split) < 2):
                return
            main_page_split2 = main_page_split[1].split("</ul>")
            page_split = main_page_split2[0].split("<li><a href=\"")
            if len(page_split) < 2:
                return
            for i in range(len(page_split)):
                if i == 0:
                    continue
                episode = str(i).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                    continue
                page_url = page_split[i].split("\"")[0]
                link = self.PAGE_PREFIX + page_url
                response = self.get_response(link)
                if len(response) == 0:
                    break
                first_split = response.split("<ul class=\"slides\">")
                if len(first_split) < 2:
                    break
                textBlocks = first_split[1].split("<img src=\"")
                for j in range(self.NUM_OF_PICTURES_PER_PAGE + 1):
                    if j == 0:
                        continue
                    imageUrl = self.PAGE_PREFIX + textBlocks[j].split("\"")[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Maou-sama, Retry!
class MaousamaRetryDownload(Summer2019AnimeDownload):
    title = "Maou-sama, Retry!"
    keywords = ["Maou-sama, Retry!", "Maousama", "Demon Lord, Retry!"]

    PAGE_PREFIX = "http://maousama-anime.com/story/"
    FINAL_EPISODE = 13
    NUM_OF_PICTURES_PER_PAGE = 6

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/maousama-retry"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            for i in range(self.FINAL_EPISODE):
                episode = str(i+1).zfill(2)
                link = self.PAGE_PREFIX + episode
                response = self.get_response(link)
                if len(response) == 0:
                    break
                first_split = response.split("<div class=\"top_slider swiper-container gallery-top\">")
                if len(first_split) < 2:
                    return
                textBlocks = first_split[1].split("<img src=\"")
                if len(textBlocks) < 2:
                    return
                for j in range(self.NUM_OF_PICTURES_PER_PAGE + 1):
                    if j == 0:
                        continue
                    imageUrl = textBlocks[j].split("\"")[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Okaasan Online
class OkaasanOnlineDownload(Summer2019AnimeDownload):
    title = "Maou-sama, Retry!"
    keywords = ["Tsuujou Kougeki ga Zentai Kougeki de Ni-kai Kougeki no Okaasan wa Suki Desu ka?",
                "Do You Like Your Mom? Her Normal Attack is Two Attacks at Full Power",
                "Okaasan online"]

    PAGE_PREFIX = "https://okaasan-online.com/story/"
    IMAGE_PREFIX = "https://okaasan-online.com"
    FINAL_EPISODE = 13
    NUM_OF_PICTURES_PER_PAGE = 4

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/okaasan-online"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            for i in range(self.FINAL_EPISODE):
                episode = str(i+1).zfill(2)
                link = self.PAGE_PREFIX + episode
                response = self.get_response(link)
                if len(response) == 0:
                    break
                textBlocks = response.split("<div class=\"p-story_slide__img\">")
                if len(textBlocks) < 2:
                    return
                for j in range(self.NUM_OF_PICTURES_PER_PAGE + 1):
                    if j == 0:
                        continue
                    imageUrl = self.IMAGE_PREFIX + textBlocks[j].split("style=\"background: url('")[1] \
                        .split("'")[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Sounan desu ka?
class SounanDesukaDownload(Summer2019AnimeDownload):
    title = "Sounan Desu ka?"
    keywords = ["Sounan Desu ka?", "Are You Lost?"]

    PAGE_LINK = "http://sounandesuka.jp/"
    FINAL_EPISODE = 13
    NUM_OF_PICTURES_PER_PAGE = 4

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/sounan-desu-ka"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            response = self.get_response(self.PAGE_LINK)
            if len(response) == 0:
                return
            for i in range(self.FINAL_EPISODE):
                episode = str(i+1).zfill(2)
                first_split = response.split("<h2>Case." + str(i+1))
                if len(first_split) < 2:
                    break
                textBlocks = first_split[1].split("<li><img src=\"")
                for j in range(self.NUM_OF_PICTURES_PER_PAGE + 1):
                    if j == 0:
                        continue
                    imageUrl = self.PAGE_LINK + textBlocks[j].split("\"")[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Tejina-senpai
class TejinaDownload(Summer2019AnimeDownload):
    title = "Tejina-senpai"
    keywords = ["Tejina-senpai", "Magical Sempai"]

    PAGE_LINK = "http://www.tejina-senpai.jp/story.html"
    IMAGE_PREFIX = "http://www.tejina-senpai.jp/"
    FINAL_EPISODE = 13
    NUM_OF_PICTURES_PER_PAGE = 4

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/tejina"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            response = self.get_response(self.PAGE_LINK)
            if len(response) == 0:
                return
            for i in range(self.FINAL_EPISODE):
                episode = str(i+1).zfill(2)
                first_split = response.split("<div class=\"story_detail\" id=\"story" + episode + "\">")
                if len(first_split) < 2 or "images/story/sample.png" in first_split[1]:
                    return
                textBlocks = first_split[1].split("<img src=\"")
                if len(textBlocks) < 2:
                    return
                for j in range(self.NUM_OF_PICTURES_PER_PAGE + 1):
                    if j == 0:
                        continue
                    imageUrl = self.IMAGE_PREFIX + textBlocks[j].split("\"")[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Uchinoko
class UchinokoDownload(Summer2019AnimeDownload):
    title = "Uchi no Ko no Tame naraba, Ore wa Moshikashitara Maou mo Taoseru kamo Shirenai."
    keywords = ["Uchi no Ko no Tame naraba, Ore wa Moshikashitara Maou mo Taoseru kamo Shirenai.",
                "Uchinoko", "Uchimusume", "If It's for My Daughter, I'd Even Defeat a Demon Lord"]

    PAGE_PREFIX = "http://uchinoko-anime.com/story/"
    FINAL_EPISODE = 13
    NUM_OF_PICTURES_PER_PAGE = 6

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/uchinoko"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            for i in range(self.FINAL_EPISODE):
                episode = str(i+1).zfill(2)
                link = self.PAGE_PREFIX + episode
                response = self.get_response(link)
                if len(response) == 0:
                    break
                first_split = response.split("<div class=\"slider_box\">")
                if len(first_split) < 2:
                    return
                textBlocks = first_split[1].split("<img src=\"")
                if len(textBlocks) < 2:
                    return
                for j in range(self.NUM_OF_PICTURES_PER_PAGE + 1):
                    if j == 0:
                        continue
                    imageUrl = textBlocks[j].split("\"")[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)
