import os
import math
import json
from anime.constants import HTTP_HEADER_USER_AGENT
from anime.main_download import MainDownload


class ExternalDownload(MainDownload):
    folder_name = None

    def __init__(self, download_id):
        super().__init__()
        self.download_id = download_id


class AnimeRecorderDownload(ExternalDownload):
    folder_name = None
    PAGE_PREFIX = 'https://www.anime-recorder.com/tvanime/'

    def __init__(self, article_id, save_folder, episode, download_id=None):
        super().__init__(download_id)
        self.base_folder = self.base_folder + "/" + save_folder
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
        self.article_id = str(article_id)
        if episode:
            self.episode = str(episode).zfill(2)
        else:
            self.episode = None

    def process_article(self):
        try:
            article_url = self.PAGE_PREFIX + self.article_id
            soup = self.get_soup(article_url)
            images = soup.select('section.entry-content img, header figure.eyecatch img')
            self.image_list = []
            for i in range(len(images)):
                if images[i].has_attr('src'):
                    image_url = images[i]['src']
                    if self.episode is None:
                        image_name = str(i + 1).zfill(2)
                    else:
                        image_name = self.episode + '_' + str(i + 1).zfill(2)
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(self.base_folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def run(self):
        self.process_article()
        if len(os.listdir(self.base_folder)) == 0:
            print('No content is downloaded for article ID: %s' % self.article_id)
            os.removedirs(self.base_folder)


class AniverseMagazineDownload(ExternalDownload):
    folder_name = None
    PAGE_PREFIX = "https://aniverse-mag.com/archives/"
    
    def __init__(self, article_id, save_folder, episode, num_of_pictures=0, min_width=None, check_resize=False, download_id=None):
        super().__init__(download_id)
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
        self.check_resize = check_resize

    def process_article(self):
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
                    imageUrl = self.clear_resize_in_url(textBlocks[i].split("\"")[0])
                    filepathWithoutExtension = self.base_folder + "/" + self.episode + "_" + str(i)
                    self.download_image(imageUrl, filepathWithoutExtension, min_width=self.min_width)
            else:
                soup = self.get_soup(article_url)
                gallery = soup.select('.jetpack-slideshow-window[data-gallery]')
                if len(gallery) == 0:
                    return
                imgs = json.loads(gallery[0]['data-gallery'])
                i = 1
                image_objs = []
                for img in imgs:
                    if 'src' in img:
                        if self.check_resize:
                            image_url_temp = self.check_resize_in_url_custom(img['src'])
                            if not self.is_valid_url(image_url_temp, is_image=True):
                                image_url = self.clear_resize_in_url(img['src'])
                            else:
                                image_url = image_url_temp
                        else:
                            image_url = self.clear_resize_in_url(img['src'])
                        image_name = str(i).zfill(2)
                        if self.episode is not None:
                            image_name = self.episode + '_' + image_name
                        image_objs.append({'name': image_name, 'url': image_url})
                        i += 1
                self.download_image_objects(image_objs, self.base_folder, min_width=self.min_width)

                # old logic
                '''
                soup = self.get_soup(article_url)
                image_objs = []
                i = 0
                windows = soup.select('div.slideshow-window')
                if len(windows) > 0 and windows[0].has_attr('data-gallery'):
                    try:
                        json_objs = json.loads(windows[0]['data-gallery'])
                        for json_obj in json_objs:
                            if 'src' in json_obj:
                                if self.check_resize:
                                    image_url = self.check_resize_in_url_custom(json_obj['src'])
                                    if not self.is_valid_url(image_url, is_image=True):
                                        image_url = self.clear_resize_in_url(json_obj['src'])
                                else:
                                    image_url = self.clear_resize_in_url(json_obj['src'])
                                i += 1
                                if self.episode is None:
                                    image_name = str(i).zfill(2)
                                else:
                                    image_name = self.episode + '_' + str(i).zfill(2)
                                image_objs.append({'name': image_name, 'url': image_url})
                    except:
                        print(f'Error processing gallery {article_url}')

                items = soup.find_all('dl', class_='gallery-item')
                for item in items:
                    image_url = 'https://' + item.find('img')['data-lazy-src'].split('https://')[-1]
                    if '300' in image_url[-12:]: # Skip unwanted images that are resized to 300px
                        continue
                    if self.check_resize:
                        image_url_temp = self.check_resize_in_url_custom(image_url)
                        if not self.is_valid_url(image_url_temp, is_image=True):
                            image_url = self.clear_resize_in_url(image_url)
                        else:
                            image_url = image_url_temp
                    else:
                        image_url = self.clear_resize_in_url(image_url)
                    i += 1
                    if self.episode is None:
                        image_name = str(i).zfill(2)
                    else:
                        image_name = self.episode + '_' + str(i).zfill(2)
                    image_objs.append({'name': image_name, 'url': image_url})
                self.download_image_objects(image_objs, self.base_folder, min_width=self.min_width)
                '''
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    @staticmethod
    def check_resize_in_url_custom(url):
        first_pos = url.rfind('-')
        second_pos = url.rfind('.')
        if 0 < first_pos < second_pos < len(url) - 1 and second_pos - first_pos > 3:
            return url[0:first_pos] + url[second_pos:]
        return url
        
    def run(self):
        self.process_article()
        if len(os.listdir(self.base_folder)) == 0:
            print('No content is downloaded for article ID: %s' % self.article_id)
            os.removedirs(self.base_folder)


class MocaNewsDownload(ExternalDownload):
    folder_name = None
    PAGE_PREFIX = "https://moca-news.net/article/"
    COOKIE_URL = "https://moca-news.net/pd.php"
    
    def __init__(self, article_id, save_folder, episode, download_id=None):
        super().__init__(download_id)
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

    def process_article(self):
        page_url = self.PAGE_PREFIX + self.article_id + "/01/"
        headers = HTTP_HEADER_USER_AGENT
        try:
            response = self.get_response(page_url, headers)
            article_id_split = self.article_id.split("/")
            if len(article_id_split) < 2:
                return
            art_id = article_id_split[1]
            data = {'art_id': art_id}
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
                image_url = self.PAGE_PREFIX + self.article_id + "/image/" + img_id + self.check_str(art_id,
                                                                                                     img_id) + ".jpg"
                headers['Cookie'] = 'imgkey' + img_id + '=' + str(cookie)
                filepathWithoutExtension = image_filepath
                self.download_image(image_url, filepathWithoutExtension, headers, is_mocanews=True)
        except Exception as e:
            print(e)
    
    def run(self):
        self.process_article()
        if len(os.listdir(self.base_folder)) == 0:
            art_id = self.article_id[9:24] if len(self.article_id) == 24 else self.article_id
            print('No content is downloaded for article ID: %s' % art_id)
            os.removedirs(self.base_folder)


class NatalieDownload(ExternalDownload):
    folder_name = None
    PAGE_PREFIX = 'https://natalie.mu/comic/news/'

    def __init__(self, article_id, save_folder, episode, title=None, download_id=None):
        super().__init__(download_id)
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

    def process_article(self):
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

    def run(self):
        self.process_article()
        if len(os.listdir(self.base_folder)) == 0:
            print('No content is downloaded for article ID: %s' % self.article_id)
            os.removedirs(self.base_folder)


class WebNewtypeDownload(ExternalDownload):
    folder_name = None
    PAGE_PREFIX = "https://webnewtype.com/news/article/"
    
    def __init__(self, article_id, save_folder, episode, download_id=None):
        super().__init__(download_id)
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

    def process_article(self):
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
        
    def run(self):
        self.process_article()
        if len(os.listdir(self.base_folder)) == 0:
            print('No content is downloaded for article ID: %s' % self.article_id)
            os.removedirs(self.base_folder)
