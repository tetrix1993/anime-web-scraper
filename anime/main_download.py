import requests
import random
import datetime
import anime.constants as constants
import urllib.request
import os
import re
from bs4 import BeautifulSoup as bs
from search import *
import shutil
from PIL import Image


class MainDownload:
    title = ""
    keywords = []
    season = None
    season_name = ""

    def __init__(self):
        self.base_folder = "download"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
            
    def init_base_folder(self, name):
        self.base_folder = self.base_folder + "/" + name
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        pass

    @staticmethod
    def get_response(url, headers=None, decode=False):
        response = ""
        if headers is None:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        try:
            result = requests.get(url, headers=headers)
            if decode:
                response = str(result.content.decode())
            else:
                response = str(result.content)
        except Exception as e:
            print(e)
        return response

    def has_website_updated(self, url, cache_name='story', headers=None, charset=None):
        if headers is None:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        if charset is None:
            charset = 'utf-8'
        try:
            response = requests.get(url, headers=headers)
            if response.status_code >= 400:
                print("Error %s for %s" % (str(response.status_code), url))
            content = str(response.content.decode(charset))
            try:
                content_length = str(len(content))
            except:
                print('Error in reading content length for ' + url)
                return False
            log_folder = self.base_folder + '/log'
            if not os.path.exists(log_folder):
                os.makedirs(log_folder)

            # Compatibility
            old_cache_file = self.base_folder + '/' + cache_name + '.log'
            cache_file = log_folder + '/' + cache_name + '.log'
            if os.path.exists(old_cache_file):
                if not os.path.exists(cache_file):
                    shutil.move(old_cache_file, cache_file)

            old_content_length = '0'
            if os.path.exists(cache_file):
                try:
                    with open(cache_file, 'r') as f:
                        old_content_length = f.read()
                except:
                    pass

            if content_length != old_content_length:
                print('The website ' + url + ' has been updated.')
                with open(cache_file, 'w+') as f:
                    f.write(content_length)
                webpage = log_folder + '/' + cache_name + '_' + datetime.datetime.today().strftime('%Y%m%d%H%M%S') \
                          + '.html'
                with open(webpage, 'w', encoding='utf-8') as f:
                    f.write(content)
                return True
        except Exception as e:
            print(e)
        return False

    @staticmethod
    def get_soup(url, headers=None, decode=False):
        if headers == None:
            headers = {}
            headers[
                'User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        try:
            result = requests.get(url, headers=headers)
            if decode:
                return bs(result.content.decode(), 'html.parser')
            else:
                return bs(result.text, 'html.parser')
        except Exception as e:
            print(e)
        return ""

    @staticmethod
    def get_json(url, headers=None):
        response = ""
        if headers == None:
            headers = {}
            headers[
                'User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        try:
            response = requests.get(url, headers=headers).json()
        except Exception as e:
            print(e)
        return response

    @staticmethod
    def post_response(url, headers=None, data=None):
        response = ""
        if headers == None:
            headers = {}
            headers[
                'User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        try:
            result = requests.post('https://moca-news.net/pd.php', headers=headers, data=data)
            response = str(result.content.decode())
        except Exception as e:
            print(e)
        return response

    def download_image(self, url, filepath_without_extension, headers=None, file_type=None):
        """
        Download image to the filepath
        :param url:
        :param filepath_without_extension:
        :param headers:
        :return: 0 - Success, 1 - File Exists, -1 - Error
        """

        if headers == None:
            headers = {}
            headers[
                'User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'

        # Download image:
        extension = ''
        try:
            with requests.get(url, stream=True, headers=headers) as r:
                # File not found or redirected to main page
                if r.status_code == 404:
                    return -1
                content_type = r.headers['Content-Type']
                if 'image/png' in content_type:
                    filepath = filepath_without_extension + ".png"
                elif 'image/jpeg' in content_type:
                    filepath = filepath_without_extension + ".jpg"
                elif 'image/gif' in content_type:
                    filepath = filepath_without_extension + ".gif"
                else:
                    extension = url.split('.')[-1]
                    if extension == 'jpg' or extension == 'jpeg':
                        filepath = filepath_without_extension + ".jpg"
                    elif extension == 'png':
                        filepath = filepath_without_extension + ".png"
                    elif extension == 'gif':
                        filepath = filepath_without_extension + ".gif"
                    elif extension == 'webp':
                        filepath = filepath_without_extension + ".webp"
                    else:
                        return -1

                if MainDownload.is_file_exists(filepath):
                    return 1

                if 'image/webp' in content_type and len(extension) > 0:
                    r.raise_for_status()
                    with open(filepath + '_temp', 'wb') as f:
                        for chunk in r.iter_content(chunk_size=8192):
                            if chunk:
                                f.write(chunk)
                    if extension == 'jpg':
                        im = Image.open(filepath + '_temp').convert('RGB')
                        im.save(filepath, 'jpeg')
                        os.remove(filepath + '_temp')
                    elif extension == 'png':
                        im = Image.open(filepath + '_temp').convert('RGB')
                        im.save(filepath, 'png')
                        os.remove(filepath + '_temp')
                    elif extension == 'gif':
                        im = Image.open(filepath + '_temp')
                        im.info.pop('background', None)
                        im.save(filepath, 'gif', save_all=True)
                        os.remove(filepath + '_temp')
                    else: #webp
                        os.rename(filepath + '_temp', filepath)
                else:
                    r.raise_for_status()
                    with open(filepath, 'wb') as f:
                        for chunk in r.iter_content(chunk_size=8192):
                            if chunk:
                                f.write(chunk)
            print("Downloaded " + url)

            # Create download log:
            timenow = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            filename = filepath.replace(self.base_folder, '')
            log_folder = self.base_folder + '/log'
            if not os.path.exists(log_folder):
                os.makedirs(log_folder)
            logpath = log_folder + '/download.log'
            with open(logpath, 'a+', encoding='utf-8') as f:
                f.write(timenow + '\t' + filename + '\t' + url + '\n')
            return 0
        except Exception as e:
            print("Failed to download " + url + ' - ' + str(e))
            return -1

    def download_image_if_exists(self, url, filepath_without_extension, old_filepath, headers=None):
        if headers == None:
            headers = {}
            headers[
                'User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'

        temp_filepath = self.base_folder + "/%032x" % random.getrandbits(128)
        # Download image:
        try:
            is_identical = True
            with requests.get(url, stream=True, headers=headers) as r:
                # File not found or redirected to main page
                if r.status_code == 404:
                    return -1
                r.raise_for_status()
                with open(temp_filepath, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
            with open(temp_filepath, 'rb') as f1:
                with open(old_filepath, 'rb') as f2:
                    if f1.read() == f2.read():
                        is_identical = True
                    else:
                        is_identical = False
            if is_identical:
                os.remove(temp_filepath)
            else:
                i = 1
                while True:
                    if ".png" in url:
                        filepath = filepath_without_extension + '_' + str(i) + ".png"
                    elif ".jpeg" in url:
                        filepath = filepath_without_extension + '_' + str(i) + ".jpeg"
                    elif ".gif" in url:
                        filepath = filepath_without_extension + '_' + str(i) + ".gif"
                    else:
                        filepath = filepath_without_extension + '_' + str(i) + ".jpg"
                    # To handle multiple files with same name
                    if os.path.exists(filepath):
                        with open(filepath, 'rb') as f1:
                            with open(temp_filepath, 'rb') as f2:
                                if f1.read() == f2.read():
                                    is_identical = True
                        if is_identical:
                            os.remove(temp_filepath)
                            return 1
                    else:
                        os.replace(temp_filepath, filepath)
                        break
                    i += 1

                # Create download log:
                timenow = str(datetime.datetime.now())
                split1 = filepath_without_extension.split('/')
                if len(split1) > 2:
                    filepath = ''
                    for j in range(len(split1) - 1):
                        filepath += split1[j] + '/'
                    filename = split1[len(split1) - 1]
                    logpath = filepath + 'log.txt'
                    with open(logpath, 'a+', encoding='utf-8') as f:
                        f.write(timenow + '\t' + filename + '\t' + url + '\n')
                print("Downloaded " + url)
            return 0
        except Exception as e:
            if os.path.exists(temp_filepath):
                os.remove(temp_filepath)
            print("Failed to download " + url)
            print(e)
            return -1

    @staticmethod
    def create_directory(filepath):
        # If directory exists
        if not os.path.exists(filepath):
            os.makedirs(filepath)

    @staticmethod
    def is_file_exists(filepath):
        return os.path.isfile(filepath)

    @staticmethod
    def get_episode_number(text, prefix=None, suffix=None):
        if prefix is None:
            prefix = '第'
        if suffix is None:
            suffix = '話'
        regex = prefix + '[０|１|２|３|４|５|６|７|８|９|0-9]+' + suffix
        prog = re.compile(regex)
        result = prog.match(text)
        if result is not None:
            return str(int(result.group(0).split(suffix)[0].split(prefix)[1])).zfill(2)
        else:
            return None

    @staticmethod
    def extract_image_name_from_url(text, with_extension=True):
        split1 = text.split('/')[-1]

        # Expected input with extension e.g. image.jpg or http://website.com/image.jpg
        if not with_extension:
            split2 = split1.split('.')
            if len(split2) == 1:
                raise ValueError("Unexpected url: " + split2[0])
            if len(split2) == 2:
                return split2[0]

            str = ''
            for i in range(len(split2) - 1):
                if i == len(split2) - 2:
                    str += split2[i]
                else:
                    str += split2[i] + '.'
            return str
        else:
            return split1

    @staticmethod
    def extract_image_name_from_twitter(text, with_extension=True):
        # Example url: https://pbs.twimg.com/media/ESLTIUOVAAAWQ5L?format=jpg&name=4096x4096
        name = text.split('/')[-1].split('?')[0]
        if with_extension:
            if "format=jpg" in text:
                return name + '.jpg'
            elif "format=png" in text:
                return name + '.png'
            else:
                return name + '.jpg'
        else:
            return name

    def create_bluray_directory(self):
        filepath = self.base_folder + '/' + constants.FOLDER_BLURAY
        if not os.path.exists(filepath):
            os.makedirs(filepath)
        return filepath

    def create_character_directory(self):
        filepath = self.base_folder + '/' + constants.FOLDER_CHARACTER
        if not os.path.exists(filepath):
            os.makedirs(filepath)
        return filepath

    def create_key_visual_directory(self):
        filepath = self.base_folder + '/' + constants.FOLDER_KEY_VISUAL
        if not os.path.exists(filepath):
            os.makedirs(filepath)
        return filepath

    def create_custom_directory(self, dir_name):
        filepath = self.base_folder + '/' + dir_name
        if not os.path.exists(filepath):
            os.makedirs(filepath)
        return filepath

    def download_image_objects(self, image_objs, filepath):
        for image_obj in image_objs:
            filename = filepath + '/' + image_obj['name']
            if os.path.exists(filename + '.jpg') or os.path.exists(filename + '.png') or \
                    os.path.exists(filename + '.gif') or os.path.exists(filename + '.webp'):
                continue
            self.download_image(image_obj['url'], filename)

    def is_image_exists(self, name, filepath=None):
        if filepath is None:
            filepath = self.base_folder
        filename = filepath + '/' + name
        return os.path.exists(filename + '.jpg') \
            or os.path.exists(filename + '.png') \
            or os.path.exists(filename + '.gif') \
            or os.path.exists(filename + '.webp')

    # Match filter
    def match(self, s_filter):
        if not isinstance(s_filter, SearchFilter):
            return False
        if s_filter.season is not None:
            if self.season is not None and self.season.lower() not in s_filter.season:
                return False
            elif self.season is None:
                return False
        matched_keywords = 0
        for filter_keyword in s_filter.keywords:
            for keyword in self.keywords:
                if filter_keyword.lower() in keyword.lower():
                    matched_keywords += 1
                    break
        return matched_keywords == len(s_filter.keywords)
