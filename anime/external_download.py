import os
import math
from anime.main_download import MainDownload


class ExternalDownload(MainDownload):
    def __init__(self):
        super().__init__()


class AniverseMagazineDownload(ExternalDownload):

    PAGE_PREFIX = "https://aniverse-mag.com/archives/"
    
    def __init__(self, article_id, save_folder, episode, num_of_pictures=0):
        super().__init__()
        self.base_folder = self.base_folder + "/" + save_folder
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
        self.article_id = str(article_id)
        self.episode = str(episode).zfill(2)
        self.num_of_pictures = num_of_pictures
        
    def run(self):
        try:
            article_url = self.PAGE_PREFIX + self.article_id
            if self.num_of_pictures > 0: # Old Logic
                response = self.get_response(article_url)
                if len(response) == 0:
                    return
                textBlocks = response.split("data-lazy-src=\"")
                if len(textBlocks) < 2:
                    return
                for i in range(self.num_of_pictures + 1):
                    if i == 0:
                        continue
                    imageUrl = textBlocks[i].split("\"")[0]
                    filepathWithoutExtension = self.base_folder + "/" + self.episode + "_" + str(i)
                    self.download_image(imageUrl, filepathWithoutExtension)
            else:
                soup = self.get_soup(article_url)
                items = soup.find_all('dl', class_='gallery-item')
                image_objs = []
                for i in range(len(items)):
                    image_url = items[i].find('img')['data-lazy-src']
                    image_name = self.episode + '_' + str(i + 1).zfill(2)
                    image_objs.append({'name': image_name, 'url': image_url})
                self.download_image_objects(image_objs, self.base_folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


class MocaNewsDownload(ExternalDownload):

    PAGE_PREFIX = "https://moca-news.net/article/"
    COOKIE_URL = "https://moca-news.net/pd.php"
    
    def __init__(self, article_id, save_folder, episode):
        super().__init__()
        self.base_folder = self.base_folder + "/" + save_folder
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
        self.article_id = str(article_id)
        if isinstance(episode, int):
            self.episode = str(episode).zfill(2)
        else:
            self.episode = str(episode)
        
    def check_str(self, art_id, img_id):
        check_chr = "abcdefghijklmnopqrstuvwxyz0123456789"
        root_chr = "020305071113"
        wk_check_str = "-"
        
        for i in range(0, 11, 2):
            temp = math.floor(( \
                pow(int(art_id[0:4]),(1 / int(root_chr[i:i+2])) \
                ) + pow(int(art_id[4:8]),(1 / int(root_chr[i:i+2])) \
                ) + pow(int(art_id[8:12]),(1 / int(root_chr[i:i+2])) \
                ) + pow(int(img_id),(1 / int(root_chr[i:i+2])))) * 100000) % 36
            wk_check_str += check_chr[temp:temp+1]
        return wk_check_str
    
    def run(self):
        page_url = self.PAGE_PREFIX + self.article_id + "/01/"
        headers = {}
        headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        try:
            response = self.get_response(page_url, headers)
            article_id_split = self.article_id.split("/")
            if len(article_id_split) < 2:
                return
            art_id = article_id_split[1]
            data = {}
            data['art_id'] = art_id
            split1 = response.split('<img src="../image/!')
            for i in range(1, len(split1), 1):
                split2 = split1[i].split('.jpg')[0]
                try:
                    img_num = int(split2)
                except Exception as e:
                    continue
                pic_num = str(i).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + self.episode + "_" + pic_num + ".jpg"):
                    continue
                cookie = self.post_response(self.COOKIE_URL, headers, data)
                img_id = str(img_num).zfill(3)
                image_page_url = self.PAGE_PREFIX + self.article_id + "/image" + img_id + ".html"
                image_url = self.PAGE_PREFIX + self.article_id + "/image/" + img_id + self.check_str(art_id, img_id) + ".jpg"
                headers['Cookie'] = 'imgkey' + img_id + '=' + str(cookie)
                filepathWithoutExtension = self.base_folder + "/" + self.episode + "_" + pic_num
                self.download_image(image_url, filepathWithoutExtension, headers)
        except Exception as e:
            print(e)


class WebNewtypeDownload(ExternalDownload):
    
    PAGE_PREFIX = "https://webnewtype.com/news/article/"
    
    def __init__(self, article_id, save_folder, episode):
        super().__init__()
        self.base_folder = self.base_folder + "/" + save_folder
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
        self.article_id = str(article_id)
        if isinstance(episode, int):
            self.episode = str(episode).zfill(2)
        else:
            self.episode = str(episode)
        
    def run(self):
        try:
            if self.is_file_exists(self.base_folder + "/" + self.episode.zfill(2) + "_01.jpg"):
                return
            response = self.get_response(self.PAGE_PREFIX + self.article_id)
            if len(response) == 0:
                return
            split1 = response.split('<div class="related_imgArea">')
            if len(split1) < 2:
                return
            split2 = split1[1].split('<div class="related_tagArea">')[0]
            split3 = split2.split('<div class="imgBox"><img src="')
            for i in range(1, len(split3), 1):
                pic_num = str(i).zfill(2)
                imageUrl = split3[i].split(".jpg")[0] + ".jpg"
                filepathWithoutExtension = self.base_folder + "/" + self.episode + "_" + pic_num
                self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)
    
