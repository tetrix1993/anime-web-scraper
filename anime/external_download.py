import os
import math
from anime.main_download import MainDownload


class ExternalDownload(MainDownload):
    folder_name = None

    def __init__(self):
        super().__init__()


class AniverseMagazineDownload(ExternalDownload):
    folder_name = None
    PAGE_PREFIX = "https://aniverse-mag.com/archives/"
    
    def __init__(self, article_id, save_folder, episode, num_of_pictures=0, min_width=None):
        super().__init__()
        self.base_folder = self.base_folder + "/" + save_folder
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
        self.article_id = str(article_id)
        if episode:
            self.episode = str(episode).zfill(2)
        else:
            self.episode = None
        self.num_of_pictures = num_of_pictures
        self.min_width = min_width
        
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
                    self.download_image(imageUrl, filepathWithoutExtension, min_width=self.min_width)
            else:
                soup = self.get_soup(article_url)
                items = soup.find_all('dl', class_='gallery-item')
                image_objs = []
                i = 0
                for item in items:
                    image_url = 'https://' + item.find('img')['data-lazy-src'].split('https://')[-1]
                    if '300' in image_url[-12:]: # Skip unwanted images that are resized to 300px
                        continue
                    i += 1
                    if self.episode is None:
                        image_name = str(i).zfill(2)
                    else:
                        image_name = self.episode + '_' + str(i).zfill(2)
                    image_objs.append({'name': image_name, 'url': image_url})
                self.download_image_objects(image_objs, self.base_folder, min_width=self.min_width)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


class MocaNewsDownload(ExternalDownload):
    folder_name = None
    PAGE_PREFIX = "https://moca-news.net/article/"
    COOKIE_URL = "https://moca-news.net/pd.php"
    
    def __init__(self, article_id, save_folder, episode):
        super().__init__()
        self.base_folder = self.base_folder + "/" + save_folder
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
        self.article_id = str(article_id)
        if episode is None:
            self.episode = None
        elif isinstance(episode, int):
            self.episode = str(episode).zfill(2)
        else:
            self.episode = str(episode)

    @staticmethod
    def check_str(art_id, img_id):
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

    @staticmethod
    def generate_image_url(art_id, img_id):
        if len(art_id) == 15:
            image_id = str(img_id).zfill(3) + MocaNewsDownload.check_str(art_id, str(img_id).zfill(3))
            return 'https://moca-news.net/article/%s/%s/image/%s.jpg' % (art_id[0:8], art_id, image_id)
        return None
    
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
                if self.episode is None:
                    image_filepath = self.base_folder + "/" + pic_num
                else:
                    image_filepath = self.base_folder + "/" + self.episode + "_" + pic_num
                if self.is_file_exists(image_filepath + ".jpg"):
                    continue
                cookie = self.post_response(self.COOKIE_URL, headers, data)
                img_id = str(img_num).zfill(3)
                image_url = self.PAGE_PREFIX + self.article_id + "/image/" + img_id + self.check_str(art_id, img_id) + ".jpg"
                headers['Cookie'] = 'imgkey' + img_id + '=' + str(cookie)
                filepathWithoutExtension = image_filepath
                self.download_image(image_url, filepathWithoutExtension, headers, is_mocanews=True)
        except Exception as e:
            print(e)


class NatalieDownload(ExternalDownload):
    folder_name = None
    PAGE_PREFIX = 'https://natalie.mu/comic/news/'

    def __init__(self, article_id, save_folder, episode, title=None):
        super().__init__()
        self.base_folder = self.base_folder + "/" + save_folder
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
        self.article_id = str(article_id)
        if episode is None:
            self.episode = None
        elif isinstance(episode, int):
            self.episode = str(episode).zfill(2)
        else:
            self.episode = str(episode)
        self.title = title

    def run(self):
        if self.episode is None:
            if self.is_file_exists(self.base_folder + "/01.jpg"):
                return
        elif self.is_file_exists(self.base_folder + "/" + self.episode.zfill(2) + "_01.jpg"):
            return
        try:
            soup = self.get_soup(self.PAGE_PREFIX + self.article_id)
            gallery_div = soup.find('div', class_='NA_article_gallery')
            if not gallery_div:
                return
            na_imglist = gallery_div.find('ul', class_='NA_imglist')
            if not na_imglist:
                return
            a_tags = na_imglist.find_all('a')
            self.image_list = []
            for i in range(len(a_tags)):
                if self.title is not None and a_tags[i].has_attr('title') and self.title not in a_tags[i]['title']:
                    continue
                image = a_tags[i].find('img')
                if image and image.has_attr('data-src'):
                    image_url = image['data-src'].split('?')[0]
                    if self.episode is None:
                        image_name = str(i + 1).zfill(2)
                    else:
                        image_name = self.episode + '_' + str(i + 1).zfill(2)
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(self.base_folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


class WebNewtypeDownload(ExternalDownload):
    folder_name = None
    PAGE_PREFIX = "https://webnewtype.com/news/article/"
    
    def __init__(self, article_id, save_folder, episode):
        super().__init__()
        self.base_folder = self.base_folder + "/" + save_folder
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
        self.article_id = str(article_id)
        if episode is None:
            self.episode = None
        elif isinstance(episode, int):
            self.episode = str(episode).zfill(2)
        else:
            self.episode = str(episode)
        
    def run(self):
        try:
            if self.episode is None:
                if self.is_file_exists(self.base_folder + "/01.jpg"):
                    return
            elif self.is_file_exists(self.base_folder + "/" + self.episode.zfill(2) + "_01.jpg"):
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
                if self.episode is None:
                    filepathWithoutExtension = self.base_folder + "/" + pic_num
                else:
                    filepathWithoutExtension = self.base_folder + "/" + self.episode.zfill(2) + "_" + pic_num
                self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)
