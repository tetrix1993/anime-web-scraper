import os
from anime.main_download import MainDownload


# Fall 2018 Anime
class Fall2018AnimeDownload(MainDownload):
    season = "2018-4"
    season_name = "Fall 2018"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/2018-4"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)


# Akanesasu Shoujo
class AkanesasuShoujoDownload(Fall2018AnimeDownload):
    title = "Akanesasu Shoujo"
    keywords = ["Akanesasu Shoujo", "The Girl in Twilight"]
    
    PAGE_PREFIX = "http://akanesasushojo.com/"
    STORY_PAGE = "http://akanesasushojo.com/story/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/akanesasu-shoujo"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
            
    def run(self):
        try:
            response = self.get_response(self.STORY_PAGE)
            split1 = response.split('<table summary="List_Type01">')
            if len(split1) < 2:
                return
            split2 = split1[1].split('</table>')[0].split('<a href="../')
            for i in range(2, len(split2), 1):
                episode = str(i-1).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(self.base_folder + "/" + episode + "_1.png"):
                    continue
                page_url = self.PAGE_PREFIX + split2[i].split('"')[0]
                page_response = self.get_response(page_url)
                split4 = page_response.split('<div class="block line_02">')
                if len(split4) < 2:
                    continue
                split5 = split4[1].split('<div id="ext_area_02">')[0].split('<img src="../')
                for j in range(1, len(split5), 1):
                    imageUrl = self.PAGE_PREFIX + split5[j].split('"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Anima Yell!
class AnimaYellDownload(Fall2018AnimeDownload):
    title = "Anima Yell!"
    keywords = ["Anima Yell!"]
    
    PAGE_PREFIX = "http://www.animayell.com/"
    STORY_PAGE = "http://www.animayell.com/story/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/anima-yell"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
            
    def run(self):
        try:
            response = self.get_response(self.STORY_PAGE)
            split1 = response.split('<table summary="List_Type01">')
            if len(split1) < 2:
                return
            split2 = split1[1].split('</table>')[0].split('<a href="../')
            for i in range(2, len(split2), 1):
                episode = str(i-1).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(self.base_folder + "/" + episode + "_1.png"):
                    continue
                page_url = self.PAGE_PREFIX + split2[i].split('"')[0]
                page_response = self.get_response(page_url)
                split4 = page_response.split('<div class="block line_03">')
                if len(split4) < 2:
                    continue
                split5 = split4[1].split('<div class="cate_bottom_tag">')[0].split('<img src="../')
                for j in range(1, len(split5), 1):
                    imageUrl = self.PAGE_PREFIX + split5[j].split('"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Beelzebub-jou no Okinimesu mama.
class BeelmamaDownload(Fall2018AnimeDownload):
    title = "Beelzebub-jou no Okinimesu mama."
    keywords = ["Beelzebub-jou no Okinimesu mama.", "Beelmama", "As Miss Beelzebub Likes."]
    
    PAGE_PREFIX = "https://beelmama.com/"
    STORY_PAGE = "https://beelmama.com/story/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/beelmama"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            response = self.get_response(self.STORY_PAGE)
            split1 = response.split('<nav class="story_tab">')
            if len(split1) < 2:
                return
            split2 = split1[1].split('</nav>')[0].split('<a href="./')
            for i in range(2, len(split2), 1):
                episode = str(i-1).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(self.base_folder + "/" + episode + "_1.png"):
                    continue
                page_url = self.STORY_PAGE + split2[i].split('"')[0]
                page_response = self.get_response(page_url)
                split4 = page_response.split('<div class="wrap clearfix">')
                if len(split4) < 2:
                    continue
                split5 = split4[1].split('</div>')[0].split('<img src="../')
                for j in range(1, len(split5), 1):
                    imageUrl = self.PAGE_PREFIX + split5[j].split('"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Conception
class ConceptionDownload(Fall2018AnimeDownload):
    title = "Conception"
    keywords = ["Conception"]

    PAGE_LINK = "http://conception-anime.com/story/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/conception"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
            
    def run(self):
        try:
            response = self.get_response(self.PAGE_LINK)
            split1 = response.split('<div id="slideshow')
            for i in range(1, len(split1), 1):
                episode_temp = split1[i].split('"')[0]
                try:
                    temp = int(episode_temp)
                except:
                    continue
                episode = episode_temp.zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(self.base_folder + "/" + episode + "_1.png"):
                    continue
                split2 = split1[i].split('<ul class="clearfix">')[0].split('<img src="')
                for j in range(1, len(split2), 1):
                    imageUrl = split2[j].split('"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Goblin Slayer
class GoblinSlayerDownload(Fall2018AnimeDownload):
    title = "Goblin Slayer"
    keywords = ["Goblin Slayer"]

    PAGE_PREFIX = "http://goblinslayer.jp/"
    STORY_PAGE = "http://goblinslayer.jp/story/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/goblin-slayer"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
            
    def run(self):
        try:
            response = self.get_response(self.STORY_PAGE)
            split1 = response.split('<h3>')
            if len(split1) < 2:
                return
            split2 = split1[1].split('</ul>')[0].split('<a href="')
            for i in range(len(split2) - 1, 0, -1):
                page_url = split2[i].split('"')[0]
                split3 = page_url.split('/')
                if len(split3) < 2:
                    continue
                episode = ""
                temp1 = split3[len(split3) - 1].split('episode')
                if len(temp1) < 2:
                    continue
                temp2 = temp1[1]
                if temp2 == '_special':
                    episode = 'sp'
                else:
                    try:
                        temp3 = int(temp2)
                    except:
                        continue
                    episode = temp2
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(self.base_folder + "/" + episode + "_1.png"):
                    continue
                page_response = self.get_response(page_url)
                split4 = page_response.split('<ul class="bxslider">')
                if len(split4) < 2:
                    continue
                split5 = split4[1].split('</ul>')[0].split('<img src="')
                for j in range(1, len(split5), 1):
                    imageUrl = split5[j].split('"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Golden Kamuy 2nd Season
class GoldenKamuy2Download(Fall2018AnimeDownload):
    title = "Golden Kamuy 2nd Season"
    keywords = ["Golden Kamuy 2nd Season", "Kamui"]

    PAGE_URL = "https://kamuy-anime.com/story/%s.html"
    PAGE_PREFIX = "https://kamuy-anime.com/"
    FIRST_EPISODE = 13
    FINAL_EPISODE = 24
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/golden-kamuy2"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            for i in range(self.FIRST_EPISODE, self.FINAL_EPISODE + 1, 1):
                episode = str(i).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                    continue
                response = self.get_response(self.PAGE_URL % episode)
                split1 = response.split('<div class="ph"><a href="../')
                for j in range(1, len(split1), 1):
                    imageUrl = self.PAGE_PREFIX + split1[j].split('"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + '_' + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Hangyakusei Million Arthur
class HangyakuseiMillionArthurDownload(Fall2018AnimeDownload):
    title = "Hangyakusei Million Arthur"
    keywords = ["Hangyakusei Million Arthur", "Operation Han-Gyaku-Sei Million Arthur"]
    
    PAGE_PREFIX = "http://hangyakusei-anime.com/"
    STORY_PAGE = "http://hangyakusei-anime.com/story/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/hangyakusei"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
            
    def run(self):
        try:
            response = self.get_response(self.STORY_PAGE)
            split1 = response.split('<table summary="List_Type01">')
            if len(split1) < 2:
                return
            split2 = split1[1].split('</table>')[0].split('<a href="../')
            for i in range(1, len(split2), 1):
                if i > 10:
                    continue
                episode = str(i).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(self.base_folder + "/" + episode + "_1.png"):
                    continue
                page_url = self.PAGE_PREFIX + split2[i].split('"')[0]
                page_response = self.get_response(page_url)
                split4 = page_response.split('<div class="block line_01">')
                if len(split4) < 2:
                    continue
                split5 = split4[1].split('<div class="block line_02">')[0].split('<img src="../')
                for j in range(1, len(split5), 1):
                    imageUrl = self.PAGE_PREFIX + split5[j].split('"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Irozuku Sekai no Ashita kara
class IrodukuDownload(Fall2018AnimeDownload):
    title = "Irozuku Sekai no Ashita kara"
    keywords = ["Irozuku Sekai no Ashita kara", "Iroduku: The World in Colors"]

    PAGE_PREFIX = "http://www.iroduku.jp/"
    STORY_PAGE = "http://iroduku.jp/story/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/iroduku"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            response = self.get_response(self.STORY_PAGE)
            split1 = response.split('<ul class="img_thum">')
            for i in range(1, len(split1), 1):
                episode = str(i).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(self.base_folder + "/" + episode + "_1.png"):
                    continue
                split2 = split1[i].split('</ul>')[0].split('<img src="../')
                for j in range(1, len(split2), 1):
                    imageUrl = self.PAGE_PREFIX + split2[j].split('"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Kishuku Gakkou no Juliet
class KishukuJulietDownload(Fall2018AnimeDownload):
    title = "Kishuku Gakkou no Juliet"
    keywords = ["Kishuku Gakkou no Juliet", "Boarding School Juliet"]
    
    PAGE_PREFIX = "https://www.juliet-anime.com/"
    STORY_PAGE = "https://www.juliet-anime.com/story/index.html"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/kishuku-juliet"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
            
    def run(self):
        try:
            response = self.get_response(self.STORY_PAGE)
            split1 = response.split('<div id="cms_block">')
            if len(split1) < 2:
                return
            split2 = split1[1].split('<div class="main_sa08">')[0].split('<div class="nwu_box">')
            for i in range(len(split2) - 1, 0, -1):
                episode = str(len(split2) - i).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(self.base_folder + "/" + episode + "_1.png"):
                    continue
                split3 = split2[i].split('<a href="../')
                if len(split3) < 2:
                    continue
                page_url = self.PAGE_PREFIX + split3[1].split('"')[0]
                page_response = self.get_response(page_url)
                split4 = page_response.split('<div class="block line_01">')
                if len(split4) < 2:
                    continue
                split5 = split4[1].split('<div class="block line_02">')[0].split('<img src="../')
                for j in range(1, len(split5), 1):
                    imageUrl = self.PAGE_PREFIX + split5[j].split('"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Merc Storia: Mukiryoku no Shounen to Bin no Naka no Shoujo
class MercStoriaDownload(Fall2018AnimeDownload):
    title = "Merc Storia: Mukiryoku no Shounen to Bin no Naka no Shoujo"
    keywords = ["Merc Storia: Mukiryoku no Shounen to Bin no Naka no Shoujo"]
    
    PAGE_PREFIX = "http://www.mercstoria.jp/"
    STORY_PAGE = "http://www.mercstoria.jp/story/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/merc-storia"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
            
    def run(self):
        try:
            response = self.get_response(self.STORY_PAGE)
            split1 = response.split('<h3>')
            if len(split1) < 2:
                return
            split2 = split1[1].split('</ul>')[0].split('<a href="')
            for i in range(len(split2) - 1, 0, -1):
                page_url = split2[i].split('"')[0]
                split3 = page_url.split('episode')
                if len(split3) < 2:
                    continue
                episode = ""
                temp1 = split3[1].split('.html')[0]
                try:
                    temp2 = int(temp1)
                except:
                    continue
                episode = temp1
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(self.base_folder + "/" + episode + "_1.png"):
                    continue
                page_url = self.STORY_PAGE + page_url
                page_response = self.get_response(page_url)
                split4 = page_response.split('<ul class="bxslider">')
                if len(split4) < 2:
                    continue
                split5 = split4[1].split('</ul>')[0].split('<img src="')
                for j in range(1, len(split5), 1):
                    imageUrl = self.STORY_PAGE + split5[j].split('"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Ore ga Suki nano wa Imouto dakedo Imouto ja Nai
class ImoimoDownload(Fall2018AnimeDownload):
    title = "Ore ga Suki nano wa Imouto dakedo Imouto ja Nai"
    keywords = ["Ore ga Suki nano wa Imouto dakedo Imouto ja Nai", "Imoimo", "My Sister, My Writer"]

    STORY_PAGE = "http://imo-imo.jp/story/"
    IMAGE_PREFIX = "http://imo-imo.jp/assets/story/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/imoimo"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            response = self.get_response(self.STORY_PAGE)
            split1 = response.split('<div class="mg5r cs"')
            for i in range(1, len(split1), 1):
                episode = str(i).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                    continue
                for j in range(6):
                    imageUrl = self.IMAGE_PREFIX + str(i) + "_" + str(j+1) + ".jpg"
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j+1)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Release the Spyce
class ReleaseTheSpyceDownload(Fall2018AnimeDownload):
    title = "Release the Spyce"
    keywords = ["Release the Spyce"]

    IMAGE_PREFIX = "https://releasethespyce.jp/story/img/"
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 4
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/release-the-spyce"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            for i in range(self.FINAL_EPISODE):
                episode = str(i+1).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    imageNum = str(j+1).zfill(2)
                    imageUrl = self.IMAGE_PREFIX + episode + "/" + episode + "_" + imageNum + ".jpg"
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j+1)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Sora to Umi no Aida
class SoraumiDownload(Fall2018AnimeDownload):
    title = "Sora to Umi no Aida"
    keywords = ["Sora to Umi no Aida", "Between the Sky and Sea", "Soraumi"]
    
    PAGE_PREFIX = "http://soraumi-anime.com/story/"
    PAGE_SUFFIX = "/"
    FINAL_EPISODE = 12
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/soraumi"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        for i in range(self.FINAL_EPISODE):
            episode = str(i+1).zfill(2)
            if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                    continue
            try:
                page_url = self.PAGE_PREFIX + episode + self.PAGE_SUFFIX
                response = self.get_response(page_url)
                split1 = response.split('<div class="story_img">')
                if len(split1) < 2:
                    continue
                split2 = split1[1].split('</ul>')[0].split('<img src="')
                for j in range(1, len(split2), 1):
                    imageUrl = split2[j].split('"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
            except Exception as e:
                print("Error in running " + self.__class__.__name__)
                print(e)


# SSSS.Gridman
class SsssGridmanDownload(Fall2018AnimeDownload):
    title = "SSSS.Gridman"
    keywords = ["SSSS.Gridman"]

    IMAGE_PREFIX = "https://gridman.net/story/img/"
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 5
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/ssss-gridman"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            for i in range(self.FINAL_EPISODE):
                episode = str(i+1).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    imageNum = str(j+1).zfill(2)
                    imageUrl = self.IMAGE_PREFIX + episode + "/" + episode + "_" + imageNum + ".jpg"
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j+1)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Seishun Buta Yarou wa Bunny Girl Senpai no Yume wo Minai
class AobutaDownload(Fall2018AnimeDownload):
    title = "Seishun Buta Yarou wa Bunny Girl Senpai no Yume wo Minai"
    keywords = ["Seishun Buta Yarou wa Bunny Girl Senpai no Yume wo Minai", "Aobuta",
                "Rascal Does Not Dream of Bunny Girl Senpai"]
    
    PAGE_PREFIX = "https://ao-buta.com/"
    STORY_PAGE = "https://ao-buta.com/story/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/aobuta"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            response = self.get_response(self.STORY_PAGE)
            split1 = response.split('<nav class="page_tab">')
            if len(split1) < 2:
                return
            split2 = split1[1].split('</nav>')[0].split('<a href="./')
            for i in range(1, len(split2), 1):
                episode = str(i).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                    continue
                page_url = self.STORY_PAGE + split2[i].split('"')[0]
                page_response = self.get_response(page_url)
                split3 = page_response.split('<div class="img_list">')
                if len(split3) < 2:
                    continue
                split4 = split3[1].split('</ul>')[0].split('<img src="../')
                for j in range(1, len(split4), 1):
                    imageUrl = self.PAGE_PREFIX + split4[j].split('"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Tensei shitara Slime Datta Ken
# Tonari no Kyuuketsuki-san
class TensuraDownload(Fall2018AnimeDownload):
    title = "Tensei shitara Slime Datta Ken"
    keywords = ["Tensei shitara Slime Datta Ken", "Tensura", "That Time I Got Reincarnated as a Slime"]
    
    STORY_PAGE = "http://www.ten-sura.com/story/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/tensura"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
            
    def run(self):
        try:
            response = self.get_response(self.STORY_PAGE)
            split1 = response.split('<ul class="storyTemp-nav-list">')
            if len(split1) < 2:
                return
            split2 = split1[1].split('</ul>')[0].split('<a href="')
            for i in range(1, len(split2), 1):
                episode = str(i).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                    continue
                page_url = split2[i].split('"')[0]
                page_response = self.get_response(page_url)
                split3 = page_response.split('<div class="swiper-slide"><img src="')
                for j in range(1, len(split3), 1):
                    imageUrl = split3[j].split('"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Tonari no Kyuuketsuki-san
class TonariNoKyuuketsukiSanDownload(Fall2018AnimeDownload):
    title = "Tonari no Kyuuketsuki-san"
    keywords = ["Tonari no Kyuuketsuki-san", "Kyuketsukisan", "Ms. vampire who lives in my neighborhood."]
    
    STORY_PAGE = "http://kyuketsukisan-anime.com/story/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/tonari-no-kyuuketsuki-san"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
            
    def run(self):
        try:
            response = self.get_response(self.STORY_PAGE)
            split1 = response.split('<section class="storyNavi">')
            if len(split1) < 2:
                return
            split2 = split1[1].split('</ul>')[0].split('<a href="')
            for i in range(1, len(split2), 1):
                episode = str(i).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                    continue
                page_url = split2[i].split('"')[0]
                page_response = self.get_response(page_url)
                split3 = page_response.split('data-src="')
                for j in range(1, len(split3), 1):
                    imageUrl = split3[j].split('"')[0].replace('-810x456.jpg','.jpg')
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Uchi no Maid ga Uzasugiru!
class UzamaidDownload(Fall2018AnimeDownload):
    title = "Uchi no Maid ga Uzasugiru!"
    keywords = ["Uchi no Maid ga Uzasugiru!", "Uzamaid!"]

    PAGE_PREFIX = "http://uzamaid.com/"
    STORY_PAGE = "http://uzamaid.com/story.html"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/uzamaid"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            response = self.get_response(self.STORY_PAGE)
            split1 = response.split('<article>')
            if len(split1) < 2:
                return
            split2 = split1[1].split('</article>')[0].split('<a href="')
            for i in range(1, len(split2), 1):
                episode = str(i).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                    continue
                page_url = self.PAGE_PREFIX + split2[i].split('"')[0]
                page_response = self.get_response(page_url)
                split3 = page_response.split('<ol class="main">')
                if len(split3) < 2:
                    continue
                split4 = split3[1].split('</ol>')[0].split('<img src="')
                for j in range(1, len(split4), 1):
                    imageUrl = self.PAGE_PREFIX + split4[j].split('"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Ulysses: Jehanne Darc to Renkin no Kishi
class UlyssesDownload(Fall2018AnimeDownload):
    title = "Ulysses: Jehanne Darc to Renkin no Kishi"
    keywords = ["Ulysses: Jeanne d'Arc and the Alchemist Knight"]

    PAGE_PREFIX = "https://ulysses-anime.jp/story/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/ulysses"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            response = self.get_response(self.PAGE_PREFIX)
            split1 = response.split('<ul class="cf">')
            if len(split1) < 2:
                return
            split2 = split1[1].split('</ul>')[0].split('<a href="')
            for i in range(1, len(split2), 1):
                episode = str(i).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                    continue
                page_url = self.PAGE_PREFIX + split2[i].split('"')[0]
                page_response = self.get_response(page_url)
                split3 = page_response.split('<ul class="imgClick">')
                if len(split3) < 2:
                    continue
                split4 = split3[1].split('</ul>')[0].split('<img src="')
                for j in range(1, len(split4), 1):
                    imageUrl = self.PAGE_PREFIX + split4[j].split('"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)
