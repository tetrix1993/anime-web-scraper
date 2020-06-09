import os
import anime.constants as constants
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
        self.download_episode_preview()
        self.download_bluray()
        self.download_goods()

    def download_episode_preview(self):
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
                episode = str(i - 1).zfill(2)
                if os.path.exists(self.base_folder + "/" + episode + "_1.jpg"):
                    continue
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

    def download_bluray(self):
        filepath = self.create_bluray_directory()
        image_objs = [
            {'name': 'music_ed', 'url': 'https://arifureta.com/wp-content/uploads/2019/06/DracoVirgo_%E3%83%8F%E3%82%B8%E3%83%A1%E3%83%8E%E3%82%A6%E3%82%BF_%E5%88%9D%E5%9B%9E%E9%99%90%E5%AE%9A%E3%80%8C%E3%81%82%E3%82%8A%E3%81%B5%E3%82%8C%E3%81%9F%E8%81%B7%E6%A5%AD%E3%81%A7%E4%B8%96%E7%95%8C%E6%9C%80%E5%BC%B7%E3%80%8D%E7%9B%A4.jpg'},
            {'name': 'charasong_mini_album', 'url': 'https://arifureta.com/wp-content/uploads/2019/11/LACA15802_H1.jpg'},
            {'name': 'bd_1_1', 'url': 'https://arifureta.com/wp-content/uploads/2019/08/ARFR_BD01_BOX_SAMPLE.jpg'},
            {'name': 'bd_1_2', 'url': 'https://arifureta.com/wp-content/uploads/2019/07/ARFR_BD01_DIGI_SAMPLE.jpg'},
            {'name': 'bd_2_1', 'url': 'https://arifureta.com/wp-content/uploads/2019/11/ARFR_BD02_BOX_FIX_sample.jpg'},
            {'name': 'bd_2_2', 'url': 'https://arifureta.com/wp-content/uploads/2019/11/ARFR_BD02_DIGI_FIX_sample.jpg'},
            {'name': 'bd_3_1', 'url': 'https://arifureta.com/wp-content/uploads/2019/12/ARFR_BD03_BD_BOX-sample.jpg'},
            {'name': 'bd_3_2', 'url': 'https://arifureta.com/wp-content/uploads/2019/12/ARFR_BD03_DIGI_191226-sample.jpg'},
            {'name': 'bd_bonus_1', 'url': 'https://arifureta.com/wp-content/uploads/2019/06/OVL_sample.jpg'},
            {'name': 'bd_bonus_2', 'url': 'https://arifureta.com/wp-content/uploads/2019/06/animate_sample.jpg'},
            {'name': 'bd_bonus_3', 'url': 'https://arifureta.com/wp-content/uploads/2019/06/%E3%81%A8%E3%82%89%E3%83%AD%E3%83%B3%E3%82%B0%E3%82%BF%E3%83%9A.jpg'},
            {'name': 'bd_bonus_4', 'url': 'https://arifureta.com/wp-content/uploads/2019/06/gamers_sample.jpg'},
            {'name': 'bd_bonus_5', 'url': 'https://arifureta.com/wp-content/uploads/2019/06/Amazon_191202OK_sample.jpg'},
            {'name': 'bd_bonus_6', 'url': 'https://arifureta.com/wp-content/uploads/2019/06/sofmap_sample.jpg'},
            {'name': 'bd_bonus_7', 'url': 'https://arifureta.com/wp-content/uploads/2019/06/HMV%E5%8F%8E%E7%B4%8DBOX.jpg'},
            {'name': 'unaired_ep_1', 'url': 'https://arifureta.com/wp-content/uploads/2020/01/asex02_003_H1.jpg'},
            {'name': 'unaired_ep_2', 'url': 'https://arifureta.com/wp-content/uploads/2020/01/asex02_008_H1.mov.jpg'},
            {'name': 'unaired_ep_3', 'url': 'https://arifureta.com/wp-content/uploads/2020/01/asex02_010_H1.mov-2.jpg'},
            {'name': 'unaired_ep_4', 'url': 'https://arifureta.com/wp-content/uploads/2020/01/asex02_011_H1.mov.jpg'},
            {'name': 'unaired_ep_5', 'url': 'https://arifureta.com/wp-content/uploads/2020/01/asex02_023_H1.jpg'},
            {'name': 'unaired_ep_6', 'url': 'https://arifureta.com/wp-content/uploads/2020/01/asex02_043_H2.mov.jpg'}]
        self.download_image_objects(image_objs, filepath)

    def download_goods(self):
        filepath = self.create_custom_directory(constants.FOLDER_GOODS)
        image_objs = [
            {'name': 'online_kuji', 'url': 'https://arifureta.com/wp-content/uploads/2019/09/main700-500-2.jpg'},
            {'name': 'online_kuji_1', 'url': 'https://arifureta.com/wp-content/uploads/2019/09/tape_sample.png'},
            {'name': 'online_kuji_2', 'url': 'https://arifureta.com/wp-content/uploads/2019/09/cu_sample.png'}]
        self.download_image_objects(image_objs, filepath)


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
        self.download_episode_preview()
        self.download_bluray()

    def download_episode_preview(self):
        try:
            for i in range(self.FINAL_EPISODE):
                link = self.PAGE_PREFIX + str(i + 1)
                response = self.get_response(link)
                if len(response) == 0:
                    break
                episode = str(i + 1).zfill(2)
                if os.path.exists(self.base_folder + '/' + episode + '_1.jpg'):
                    continue
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

    def download_bluray(self):
        filepath = self.create_bluray_directory()
        image_objs = [
            {'name': 'bd_1_1', 'url': 'https://pbs.twimg.com/media/EFTAiqGU8AIEWcV?format=jpg&name=large'},
            {'name': 'bd_1_2', 'url': 'https://hensuki.com/bd/img/bd-1-open.jpg'},
            {'name': 'bd_2_1', 'url': 'https://pbs.twimg.com/media/EGBVudvVAAAgyPx?format=jpg&name=medium'},
            {'name': 'bd_2_2', 'url': 'https://pbs.twimg.com/media/EGBVvSnU8AAukM9?format=jpg&name=medium'},
            {'name': 'bd_2_3', 'url': 'https://pbs.twimg.com/media/EGBVv7OVUAEfUQl?format=jpg&name=medium'},
            {'name': 'bd_3_1', 'url': 'https://pbs.twimg.com/media/EIvt5c-U4AATYbV?format=jpg&name=4096x4096'},
            {'name': 'bd_3_2', 'url': 'https://hensuki.com/bd/img/bd-3-dp.jpg'},
            {'name': 'bd_3_2_1', 'url': 'https://pbs.twimg.com/media/EIvt-tdU0AEjJUn?format=jpg&name=4096x4096'},
            {'name': 'bd_3_3', 'url': 'https://pbs.twimg.com/media/EIvt_12U8AAYeXj?format=jpg&name=4096x4096'},
            {'name': 'bd_bonus_1', 'url': 'https://hensuki.com/bd/img/img_souki_tokuten.jpg'},
            {'name': 'bd_bonus_2', 'url': 'https://hensuki.com/bd/img/amazon.jpg'},
            {'name': 'bd_bonus_3', 'url': 'https://hensuki.com/bd/img/animeite.jpg'},
            {'name': 'bd_bonus_4', 'url': 'https://hensuki.com/bd/img/gamers2.jpg'},
            {'name': 'bd_bonus_5', 'url': 'https://hensuki.com/bd/img/sofmap.jpg'},
            {'name': 'bd_bonus_6', 'url': 'https://hensuki.com/bd/img/toranoana2.jpg'},
            {'name': 'bd_bonus_7', 'url': 'https://hensuki.com/bd/img/charaani.jpg'}]
        self.download_image_objects(image_objs, filepath)


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
        self.download_episode_preview()
        self.download_bluray()

    def download_episode_preview(self):
        try:
            response = self.get_response(self.PAGE_LINK)
            if len(response) == 0:
                return
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if os.path.exists(self.base_folder + '/' + episode + '_1.jpg'):
                    continue
                first_split = response.split("id=\"s" + str(i + 1) + "\"")
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

    def download_bluray(self):
        filepath = self.create_bluray_directory()
        image_objs = [
            {'name': 'music_ed', 'url': 'https://pbs.twimg.com/media/D_FWx9DUcAA7E8r?format=jpg&name=4096x4096'},
            {'name': 'bd_1_1', 'url': 'https://pbs.twimg.com/media/EF8S_KBU0AAJ6f1?format=jpg&name=900x900'},
            {'name': 'bd_1_2', 'url': 'https://pbs.twimg.com/media/EFzKDxlU8AIurM8?format=jpg&name=large'},
            {'name': 'bd_2_1', 'url': 'https://pbs.twimg.com/media/EImTHsxU0AEF9Um?format=jpg&name=large'},
            {'name': 'bd_2_2', 'url': 'https://pbs.twimg.com/media/EImTHsvU8AAxrX9?format=jpg&name=large'},
            {'name': 'bd_3_1', 'url': 'https://pbs.twimg.com/media/EKXpYVIUYAEmZmY?format=jpg&name=large'},
            {'name': 'bd_3_2', 'url': 'https://pbs.twimg.com/media/EKXpYVHVUAAwPvO?format=jpg&name=large'},
            {'name': 'bd_bonus_1', 'url': 'http://isekai-cheat-magician.com/bd/img/toku_souki.jpg'},
            {'name': 'bd_bonus_2', 'url': 'https://pbs.twimg.com/media/ECfB7QgVUAEZsV6?format=jpg&name=large'},
            {'name': 'bd_bonus_3', 'url': 'https://pbs.twimg.com/media/ECfB7QhUcAEohZ0?format=jpg&name=large'},
            {'name': 'bd_bonus_4', 'url': 'https://pbs.twimg.com/media/ECj5F2fUwAAoWb-?format=jpg&name=large'},
            {'name': 'bd_bonus_5', 'url': 'https://pbs.twimg.com/media/ECfB7QiUcAMNF-W?format=jpg&name=large'},
            {'name': 'bd_bonus_6', 'url': 'https://pbs.twimg.com/media/ECfB7RDU4Ag77Ri?format=jpg&name=large'}]
        self.download_image_objects(image_objs, filepath)


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
