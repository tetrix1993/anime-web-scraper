import requests
import random
import datetime
import json
import anime.constants as constants
import os
import re
from bs4 import BeautifulSoup as bs
from search import *
import shutil
import time
import traceback
import portalocker
from PIL import Image
from io import BytesIO
from html import unescape

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class MainDownload:
    title = ""
    keywords = []
    website = ""
    twitter = []  # Twitter Account Names
    hashtags = []
    season = None
    season_name = ""
    image_list = []
    folder_name = constants.FOLDER_DOWNLOAD
    enabled = True
    refresh_meta_tag = False
    download_id = None  # For printing global logs
    download_media_only = False  # Used in main.py
    guess_only = False  # Run download_episode_preview_guess method only

    def __init__(self):
        path = self.get_full_path()
        self.base_folder = path
        if not os.path.exists(path):
            os.makedirs(path)
        self.create_meta_data(refresh=True)

    def download_episode_preview(self):
        pass

    def download_episode_preview_guess(self):
        pass

    def download_episode_preview_external(self):
        pass

    def download_news(self):
        pass

    def download_key_visual(self):
        pass

    def download_character(self):
        pass

    def download_media(self):
        pass

    @classmethod
    def get_full_path(cls):
        if cls is MainDownload:
            return cls.folder_name
        else:
            path = ''
            if cls.folder_name is not None:
                path = cls.folder_name
            dl = cls
            while dl is not MainDownload:
                if len(dl.__bases__) > 0:
                    dl = dl.__bases__[0]
                    if issubclass(dl, MainDownload):
                        if dl.folder_name is not None:
                            if len(path) > 0:
                                path = dl.folder_name + '/' + path
                            else:
                                path = dl.folder_name
                    else:
                        break
                else:
                    break
            return path

    # def init_base_folder(self):
    #     self.base_folder = self.base_folder + "/" + self.folder_name
    #     if not os.path.exists(self.base_folder):
    #         os.makedirs(self.base_folder)

    def run(self):
        pass

    def create_meta_data(self, refresh):
        logpath = self.get_full_path() + '/log'
        filepath = logpath + '/' + constants.FILE_METADATA
        split1 = filepath.split('/')
        if len(split1) == 5 and 'log' == split1[3] and (refresh or not os.path.exists(filepath)):
            if not os.path.exists(logpath):
                os.makedirs(logpath)

            twitter_names = []
            if isinstance(self.twitter, str) and len(self.twitter) > 0:
                twitter_names = [self.twitter]
            elif isinstance(self.twitter, list):
                twitter_names = self.twitter

            hash_tags = []
            if isinstance(self.hashtags, str) and len(self.hashtags) > 0:
                hash_tags = [self.hashtags]
            elif isinstance(self.hashtags, list):
                hash_tags = self.hashtags

            last_run = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            data = {'title': self.title, 'website': self.website, 'twitter': twitter_names, 'hashtags': hash_tags,
                    'lastRun': last_run}
            with open(filepath, 'w+', encoding='utf-8') as f:
                json.dump(data, f)

    @staticmethod
    def get_response(url, headers=None, decode=False):
        response = ""
        if headers is None:
            headers = constants.HTTP_HEADER_USER_AGENT
        try:
            result = requests.get(url, headers=headers)
            if decode:
                response = str(result.content.decode())
            else:
                response = str(result.content)
        except Exception as e:
            print(e)
        return response

    def has_website_updated(self, url, cache_name='index', headers=None, charset=None, diff=0):
        """
        Checks if the given url is updated based on the size of the response by comparing its size with
        previously saved size in cache. Returns true if it is updated and the contents is saved as log.
        :param url: URL to check for updates.
        :param cache_name: Name of the log.
        :param headers: Headers for HTTP GET request
        :param charset: Charset used for the website.
        :param diff: If the difference in sizes are bigger than diff, returns True.
        :return:
        """
        if headers is None:
            headers = constants.HTTP_HEADER_USER_AGENT
        if charset is None:
            charset = 'utf-8'
        try:
            response = requests.get(url, headers=headers)
            if response.status_code >= 400:
                print("Error %s for %s" % (str(response.status_code), url))
                return False
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

            if content_length != old_content_length and abs(int(content_length) - int(old_content_length)) > diff:
                print('The website ' + url + ' has been updated.')
                with open(cache_file, 'w+') as f:
                    f.write(content_length)
                webpage = log_folder + '/' + cache_name + '_' + datetime.datetime.today().strftime('%Y%m%d%H%M%S') \
                          + '.html'
                with open(webpage, 'w', encoding='utf-8') as f:
                    f.write(content)

                timenow = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                global_save_success = False
                for k in range(10):
                    try:
                        with open(constants.GLOBAL_WEBSITE_LOG_FILE, 'a+', encoding='utf-8') as f:
                            portalocker.lock(f, portalocker.LOCK_EX)
                            f.write('%s\t%s\t%s\t%s\n' % (timenow, cache_name, content_length, url))
                            portalocker.unlock(f)
                            global_save_success = True
                            break
                    except Exception as e:
                        time.sleep(0.1)
                if not global_save_success:
                    print('Unable to save global website log for url: %s' % url)
                return True
        except Exception as e:
            print(e)
        return False

    @staticmethod
    def get_soup(url, headers=None, decode=False, verify=True):
        if headers is None:
            headers = constants.HTTP_HEADER_USER_AGENT
        try:
            result = requests.get(url, headers=headers, verify=verify)
            if decode:
                return bs(result.content.decode(), 'html.parser')
            else:
                return bs(result.text, 'html.parser')
        except Exception as e:
            print(e)
        return ""

    @staticmethod
    def get_json(url, headers=None, verify=True):
        if headers is None:
            headers = constants.HTTP_HEADER_USER_AGENT
        r = requests.get(url, headers=headers, verify=verify)
        r.raise_for_status()
        return r.json()

    @staticmethod
    def post_response(url, headers=None, data=None):
        response = ""
        if headers is None:
            headers = constants.HTTP_HEADER_USER_AGENT
        try:
            result = requests.post(url, headers=headers, data=data)
            response = str(result.content.decode())
        except Exception as e:
            print(e)
        return response

    def download_image(self, url, filepath_without_extension, headers=None, to_jpg=False, is_mocanews=False,
                       min_width=None, verify=True):
        """
        Download image to the filepath
        :param url:
        :param filepath_without_extension:
        :param headers:
        :return: 0 - Success, 1 - File Exists, -1 - Error
        """

        if headers is None:
            headers = constants.HTTP_HEADER_USER_AGENT

        max_try_count = 3
        try_count = 0

        # Download image:
        try:
            while try_count < max_try_count:
                try:
                    extension = ''
                    if is_mocanews:
                        url_split = url.split('/')
                        if len(url_split) != 8:
                            print('Invalid MocaNews URL')
                            return -1
                        art_id = url_split[5]
                        img_id = url_split[7].split('-')[0]
                        try:
                            int(img_id)
                        except:
                            print('Invalid MocaNews URL')
                            return -1
                        headers = constants.HTTP_HEADER_USER_AGENT
                        data = {'art_id': art_id}
                        cookie = self.post_response('https://moca-news.net/pd.php', headers, data)
                        headers['Cookie'] = 'imgkey' + img_id + '=' + cookie

                    filepath = ''
                    with requests.get(url, stream=True, headers=headers, verify=verify, ) as r:
                        # File not found or redirected to main page
                        if r.status_code >= 400:
                            return -1
                        content_type = r.headers['Content-Type']
                        if 'text' in content_type:
                            return -1
                        if 'image/png' in content_type:
                            if to_jpg:
                                filepath = filepath_without_extension + ".jpg"
                            else:
                                filepath = filepath_without_extension + ".png"
                        elif 'image/jpeg' in content_type:
                            filepath = filepath_without_extension + ".jpg"
                        elif 'image/gif' in content_type:
                            filepath = filepath_without_extension + ".gif"
                        elif 'image/webp' in content_type and to_jpg:
                            filepath = filepath_without_extension + ".jpg"
                        elif 'image/tiff' in content_type:
                            filepath = filepath_without_extension + ".tif"
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
                            elif extension == 'tif':
                                filepath = filepath_without_extension + ".tif"
                            else:
                                return -1

                        if MainDownload.is_file_exists(filepath):
                            return 1

                        temp_filepath = filepath + '_temp'
                        if MainDownload.is_file_exists(temp_filepath):
                            os.remove(temp_filepath)

                        r.raise_for_status()
                        if 'image/webp' in content_type:
                            with open(temp_filepath, 'wb') as f:
                                for chunk in r.iter_content(chunk_size=8192):
                                    if chunk:
                                        f.write(chunk)
                            if len(extension) > 0:
                                if extension == 'jpg':
                                    im = Image.open(temp_filepath).convert('RGB')
                                    im.save(filepath, 'jpeg')
                                    im.close()
                                    os.remove(temp_filepath)
                                elif extension == 'png':
                                    im = Image.open(temp_filepath).convert('RGB')
                                    im.save(filepath, 'png')
                                    im.close()
                                    os.remove(temp_filepath)
                                elif extension == 'gif':
                                    im = Image.open(temp_filepath)
                                    im.info.pop('background', None)
                                    im.save(filepath, 'gif', save_all=True)
                                    im.close()
                                    os.remove(temp_filepath)
                                else:  #webp
                                    os.rename(temp_filepath, filepath)
                            elif to_jpg:
                                im = Image.open(temp_filepath).convert('RGB')
                                im.save(filepath, 'jpeg')
                                im.close()
                                if os.path.exists(filepath) and os.path.exists(temp_filepath):
                                    os.remove(temp_filepath)
                                # Keep a copy
                                # os.rename(temp_filepath, filepath[0:len(filepath) - 3] + 'webp')
                        elif 'image/tiff' in content_type:
                            with open(temp_filepath, 'wb') as f:
                                for chunk in r.iter_content(chunk_size=8192):
                                    if chunk:
                                        f.write(chunk)
                            if to_jpg:
                                im = Image.open(temp_filepath).convert('RGB')
                                im.save(filepath, 'jpeg')
                                im.close()
                                os.rename(filepath, filepath[0:len(filepath) - 3] + 'jpg')
                                os.remove(temp_filepath)
                            else:
                                os.rename(temp_filepath, filepath)
                        elif 'image/png' in content_type and to_jpg:
                            im = Image.open(BytesIO(r.content)).convert('RGB')
                            im.save(filepath, 'jpeg')
                            im.close()
                        else:
                            with open(filepath, 'wb') as f:
                                for chunk in r.iter_content(chunk_size=8192):
                                    if chunk:
                                        f.write(chunk)
                    if os.path.exists(filepath) and min_width is not None:
                        with Image.open(filepath) as im:
                            width, height = im.size
                        if width < min_width:
                            os.remove(filepath)
                            raise InvalidImageSizeError('Width is smaller than %s px' % str(min_width))
                    if is_mocanews:
                        if len(filepath) > 0 and os.path.exists(filepath):
                            image = Image.open(filepath)
                            width, height = image.size
                            image.close()
                            if max(width, height) < 100:
                                os.remove(filepath)
                                raise Exception('Image dimensions downloaded from MocaNews is too small')
                    print("Downloaded " + url)
                    break
                except InvalidImageSizeError as e:
                    return -1
                except Exception as e:
                    try_count += 1
                    print('Download failed: %s (Attempt: %s)' % (url, str(try_count)))
                    if try_count >= max_try_count:
                        raise e

            # Create download log:
            timenow = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            filename = filepath.replace(self.base_folder, '')
            log_folder = self.base_folder + '/log'
            if not os.path.exists(log_folder):
                os.makedirs(log_folder)
            logpath = log_folder + '/download.log'
            with open(logpath, 'a+', encoding='utf-8') as f:
                f.write('%s\t%s\t%s\n' % (timenow, filename, url))

            # Global log path
            if self.download_id is None:
                global_save_success = False
                for k in range(10):
                    try:
                        with open(constants.GLOBAL_DOWNLOAD_LOG_FILE, 'a+', encoding='utf-8') as f:
                            portalocker.lock(f, portalocker.LOCK_EX)
                            f.write('%s\t%s\t%s\t%s\n' % (timenow, self.base_folder, filename, url))
                            portalocker.unlock(f)
                            global_save_success = True
                            break
                    except Exception as e:
                        time.sleep(0.1)
                if not global_save_success:
                    print('Unable to save global download log for file: %s' % filepath)
            else:
                if not os.path.exists(constants.GLOBAL_TEMP_FOLDER):
                    os.makedirs(constants.GLOBAL_TEMP_FOLDER)
                try:
                    temp_logpath = constants.GLOBAL_TEMP_FOLDER + '/download_' + self.download_id
                    with open(temp_logpath, 'a+', encoding='utf-8') as f:
                        f.write('%s\t%s\t%s\t%s\n' % (timenow, self.base_folder, filename, url))
                except Exception as e:
                    print('Unable to save temp global download log for file: %s' % filepath)
            return 0
        except Exception as e:
            print("Failed to download " + url + ' - ' + str(e))
            return -1

    def download_image_if_exists(self, url, filepath_without_extension, old_filepath, headers=None):
        if headers is None:
            headers = constants.HTTP_HEADER_USER_AGENT

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

    def download_content(self, url, filepath, headers=None):
        if MainDownload.is_file_exists(filepath):
            return 1

        if headers is None:
            headers = constants.HTTP_HEADER_USER_AGENT
        try:
            with requests.get(url, stream=True, headers=headers) as r:
                if r.status_code >= 400:
                    return -1
                with open(filepath, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
            print('Downloaded %s' % url)

            # Create download log:
            timenow = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            filename = filepath.replace(self.base_folder, '')
            log_folder = self.base_folder + '/log'
            if not os.path.exists(log_folder):
                os.makedirs(log_folder)
            logpath = log_folder + '/download.log'
            with open(logpath, 'a+', encoding='utf-8') as f:
                f.write('%s\t%s\t%s\n' % (timenow, filename, url))

            # Global log path
            global_save_success = False
            for k in range(10):
                try:
                    with open(constants.GLOBAL_DOWNLOAD_LOG_FILE, 'a+', encoding='utf-8') as f:
                        portalocker.lock(f, portalocker.LOCK_EX)
                        f.write('%s\t%s\t%s\t%s\n' % (timenow, self.base_folder, filename, url))
                        portalocker.unlock(f)
                        global_save_success = True
                        break
                except Exception as e:
                    time.sleep(0.1)
            if not global_save_success:
                print('Unable to save global download log for file: %s' % filepath)
            return 0
        except:
            return -1

    @staticmethod
    def convert_image_to_jpg(filepath, temp_folder_name='temp', delete_temp_file=False):
        if not os.path.isfile(filepath):
            raise Exception('Filepath is not a file.')
        filepath_slash_index = filepath.rfind('/')
        filename = filepath[filepath_slash_index + 1:]
        folder = filepath[0: filepath_slash_index]
        period_index = filename.rfind('.')
        extension = ''
        if period_index > 0:
            filename_without_extension = filename[0: period_index]
            extension = filename[period_index + 1:]
        else:
            filename_without_extension = filename
        temp_folder_path = folder + '/' + temp_folder_name
        if not os.path.exists(temp_folder_path):
            os.makedirs(temp_folder_path)
        temp_filepath = temp_folder_path + '/' + filename
        new_filepath = folder + '/' + filename_without_extension + '.jpg'
        i = 0
        while os.path.exists(temp_filepath):
            i += 1
            temp_filepath = temp_folder_path + '/' + filename_without_extension + ' (' + str(i) + ')'
            if len(extension) > 0:
                temp_filepath += '.' + extension
        os.rename(filepath, temp_filepath)
        im = Image.open(temp_filepath).convert('RGB')
        im.save(new_filepath, 'jpeg')
        im.close()
        if delete_temp_file:
            os.remove(temp_filepath)

    def create_news_log(self, date='', title='', _id=''):
        if date is None:
            date = ''
        if title is None:
            title = ''
        if _id is None:
            _id = ''
        try:
            timenow = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            log_folder = self.base_folder + '/log'
            if not os.path.exists(log_folder):
                os.makedirs(log_folder)
            logpath = log_folder + '/news.log'
            with open(logpath, 'a+', encoding='utf-8') as f:
                f.write('%s\t%s\t%s\t%s\n' % (timenow, date, title, _id))

            # Global log path
            folder_name = self.base_folder.replace(constants.FOLDER_DOWNLOAD + '/', '')
            if self.download_id is None:
                global_save_success = False
                for k in range(10):
                    try:
                        with open(constants.GLOBAL_NEWS_LOG_FILE, 'a+', encoding='utf-8') as f:
                            portalocker.lock(f, portalocker.LOCK_EX)
                            f.write('%s\t%s\t%s\t%s\t%s\n' % (timenow, folder_name, date, title, _id))
                            portalocker.unlock(f)
                            global_save_success = True
                            break
                    except Exception as e:
                        time.sleep(0.1)
                if not global_save_success:
                    print('Unable to save global news log for %s' % self.title)
            else:
                if not os.path.exists(constants.GLOBAL_TEMP_FOLDER):
                    os.makedirs(constants.GLOBAL_TEMP_FOLDER)
                try:
                    temp_logpath = constants.GLOBAL_TEMP_FOLDER + '/news_' + self.download_id
                    with open(temp_logpath, 'a+', encoding='utf-8') as f:
                        f.write('%s\t%s\t%s\t%s\t%s\n' % (timenow, folder_name, date, title, _id))
                except Exception as e:
                    print('Unable to save temp global news log for %s' % self.title)
        except Exception as e:
            return -1
        return 0

    def create_news_log_from_news_log_object(self, result):
        return self.create_news_log(result['date'], result['title'], result['id'])

    def get_news_log_objects(self):
        results = []
        logpath = self.base_folder + '/log/news.log'
        if not os.path.exists(logpath):
            return results
        try:
            with open(logpath, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            for line in lines:
                split1 = line.replace('\n', '').split('\t')
                if len(split1) == 4:
                    results.append({'timestamp': split1[0], 'date': split1[1], 'title': split1[2], 'id': split1[3]})
        except Exception as e:
            print('Error in reading news log %s' % logpath)
            print(e)
        return results

    def get_last_news_log_object(self):
        last_news_cache = self.base_folder + '/log/news_cache'
        if os.path.exists(last_news_cache):
            try:
                with open(last_news_cache, 'r', encoding='utf-8') as f:
                    line = f.read()
                split1 = line.replace('\n', '').split('\t')
                if len(split1) == 3:
                    return {'timestamp': '', 'date': split1[0], 'title': split1[1], 'id': split1[2]}
            except Exception as e:
                print('Error in reading news log %s' % last_news_cache)
                print(e)
        news_logs = self.get_news_log_objects()
        if len(news_logs) > 0:
            latest_log = news_logs[-1]
            with open(last_news_cache, 'w+', encoding='utf-8') as f:
                f.write('%s\t%s\t%s' % (latest_log['date'], latest_log['title'], latest_log['id']))
            return latest_log
        return None

    def create_news_log_cache(self, count, latest_news_obj):
        if count > 0:
            print('Updated news for %s (Count: %s)' % (self.__class__.__name__, str(count)))
        last_news_cache = self.base_folder + '/log/news_cache'
        try:
            with open(last_news_cache, 'w+', encoding='utf-8') as f:
                f.write('%s\t%s\t%s' % (latest_news_obj['date'], latest_news_obj['title'], latest_news_obj['id']))
        except Exception as e:
            print('Unable to create news cache %s ' % last_news_cache)
            print(e)

    @staticmethod
    def create_news_log_object(date='', title='', _id=''):
        if date is None:
            date = ''
        if title is None:
            title = ''
        if _id is None:
            _id = ''
        return {'date': date, 'title': title, 'id': _id}

    @staticmethod
    def format_news_title(title):
        return ' '.join(title.strip().split())

    @staticmethod
    def format_news_date(news_date):
        output_date_str = ''
        try:
            split1 = news_date.split('.')
            if len(split1) == 3:
                year = str(int(split1[0])).zfill(4)
                month = str(int(split1[1])).zfill(2)
                day = str(int(split1[2])).zfill(2)
                output_date_str = '%s.%s.%s' % (year, month, day)
        except:
            pass
        return output_date_str

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
    def extract_image_name_from_url(text, with_extension=False):
        split1 = text.split('?')[0].split('/')[-1]

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
    def generate_image_name_from_url(url, stop_text, separator='_'):
        period_index = url.split('?')[0].rfind('.')
        if period_index >= 0:
            name = url[0:period_index]
        else:
            name = url
        name_split = name.split('/')
        image_name = name_split[-1]
        for i in reversed(range(len(name_split) - 1)):
            if len(name_split[i]) == 0:
                continue

            if name_split[i] == stop_text:
                return image_name
            else:
                image_name = name_split[i] + separator + image_name
        return image_name

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

    def has_content(self, folder):
        filepath = self.base_folder + '/' + folder
        return os.path.exists(filepath) and len(os.listdir(filepath)) > 0

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

    # To replace the bluray directory
    def create_media_directory(self):
        filepath = self.base_folder + '/' + constants.FOLDER_MEDIA
        if not os.path.exists(filepath):
            os.makedirs(filepath)
        return filepath

    def create_custom_directory(self, dir_name):
        filepath = self.base_folder + '/' + dir_name
        if not os.path.exists(filepath):
            os.makedirs(filepath)
        return filepath

    def download_image_objects(self, image_objs, filepath, min_width=None, verify=True):
        is_successful = True
        for image_obj in image_objs:
            if not isinstance(image_obj, dict) or 'name' not in image_obj.keys() or 'url' not in image_obj.keys():
                continue
            if len(image_obj['url']) == 0 or len(image_obj['name']) == 0:
                continue
            filename = filepath + '/' + image_obj['name']
            if os.path.exists(filename + '.jpg') or os.path.exists(filename + '.png') or \
                    os.path.exists(filename + '.gif') or os.path.exists(filename + '.webp'):
                continue

            if 'is_mocanews' in image_obj.keys() and isinstance(image_obj['is_mocanews'], bool) \
                    and image_obj['is_mocanews']:
                result = self.download_image(image_obj['url'], filename, is_mocanews=True, min_width=min_width, verify=verify)
            elif 'to_jpg' in image_obj.keys() and isinstance(image_obj['to_jpg'], bool) and image_obj['to_jpg']:
                result = self.download_image(image_obj['url'], filename, to_jpg=True, min_width=min_width, verify=verify)
            else:
                result = self.download_image(image_obj['url'], filename, min_width=min_width, verify=verify)
            if result == -1:
                is_successful = False
        return is_successful

    def is_image_exists(self, name, filepath=None):
        if filepath is None:
            filepath = self.base_folder
        filename = filepath + '/' + name
        return os.path.exists(filename + '.jpg') \
            or os.path.exists(filename + '.png') \
            or os.path.exists(filename + '.gif') \
            or os.path.exists(filename + '.webp')

    @staticmethod
    def is_valid_url(url, is_image=False):
        if isinstance(url, str) and (url.startswith('http://') or url.startswith('https://')):
            try:
                r = requests.head(url)
                return r.status_code < 400 and (not is_image or (is_image and 'image/' in r.headers['Content-Type']))
            except:
                pass
        return False

    @staticmethod
    def get_content_length(url):
        try:
            return int(requests.head(url).headers['Content-Length'])
        except:
            return -1

    @staticmethod
    def is_matching_content_length(url, lengths):
        content_lengths = []
        if isinstance(lengths, int):
            content_lengths.append(str(lengths))
        elif isinstance(lengths, str):
            content_lengths.append(lengths)
        if isinstance(lengths, list):
            for length in lengths:
                if isinstance(length, int):
                    content_lengths.append(str(length))
                elif isinstance(length, str):
                    content_lengths.append(length)
        try:
            content_length = requests.head(url).headers['Content-Length']
            for cl in content_lengths:
                if cl == content_length:
                    return True
        except:
            pass
        return False

    @staticmethod
    def is_not_matching_content_length(url, lengths):
        content_lengths = []
        if isinstance(lengths, int):
            content_lengths.append(str(lengths))
        elif isinstance(lengths, str):
            content_lengths.append(lengths)
        if isinstance(lengths, list):
            for length in lengths:
                if isinstance(length, int):
                    content_lengths.append(str(length))
                elif isinstance(length, str):
                    content_lengths.append(length)
        try:
            content_length = requests.head(url).headers['Content-Length']
            for cl in content_lengths:
                if cl == content_length:  # As long as one match, return false
                    return False
        except:
            return False  # error in retrieving length, returns False
        return True

    @staticmethod
    def is_content_length_in_range(url, less_than_amount=None, more_than_amount=None,
                                   less_than_equal=False, more_than_equal=False, is_or=False):
        if less_than_amount is None and more_than_amount is None:
            return False
        try:
            content_length = int(requests.head(url).headers['Content-Length'])
            if is_or and less_than_amount is not None and more_than_amount is not None:  # Or Condition
                return (less_than_equal and content_length <= less_than_amount) or\
                    (not less_than_equal and content_length < less_than_amount) or\
                    (more_than_equal and content_length >= more_than_amount) or\
                    (not more_than_equal and content_length > more_than_amount)
            if less_than_amount is not None and\
                    ((less_than_equal and content_length > less_than_amount) or
                     (not less_than_equal and content_length >= less_than_amount)):
                return False
            if more_than_amount is not None and\
                    ((more_than_equal and content_length < more_than_amount) or
                     (not more_than_equal and content_length <= more_than_amount)):
                return False
            return True
        except:
            pass
        return False

    def is_content_length_same_as_existing(self, url, name, filepath=None):
        if filepath is None:
            filepath = self.base_folder
        filename = filepath + '/' + name
        filename_with_extension = ''
        for ext in ['jpg', 'png', 'gif', 'webp']:
            if os.path.exists(filename + '.' + ext):
                filename_with_extension = filename + '.' + ext
                break
        if len(filename_with_extension) == 0:
            return False
        try:
            existing_length = os.path.getsize(filename_with_extension)
            r = requests.head(url)
            if 400 <= r.status_code < 600:
                return True
            content_length = int(r.headers['Content-Length'])
        except Exception as e:
            print(e)
            return True
        return existing_length == content_length

    def download_image_with_different_length(self, url, name, new_dir, filepath=None):
        if filepath is None:
            filepath = self.base_folder
        new_file_dir = filepath + '/' + new_dir
        filename = filepath + '/' + name
        return_value = False
        if not self.is_content_length_same_as_existing(url, name, filepath):
            ext = self.get_image_extension(filename)
            new_file_name = name
            i = 0
            while True:
                if self.is_image_exists(new_file_name, new_file_dir):
                    i += 1
                    new_file_name = name + ' (' + str(i) + ')'
                else:
                    break
            if not os.path.exists(new_file_dir):
                os.makedirs(new_file_dir)
            os.rename(f'{filename}.{ext}', f'{new_file_dir}/{new_file_name}.{ext}')
            result = self.download_image(url, filepath + '/' + name)
            return_value = result == 0
        return return_value

    @staticmethod
    def get_image_url_from_srcset(img_elem, modify_url_func=None):
        '''
        Get biggest image url from img element with srcset
        :param img_elem: img_elem e.g. <img src="" srcset="" />
        :param modify_url_func: A function to modify url if required
        :return: image_url
        '''

        if img_elem is None:
            return None

        image_url = None
        if img_elem.has_attr('srcset'):
            srcset = img_elem['srcset']
            biggest_size = None
            sources = srcset.split(',')
            for source in sources:
                split1 = source.strip().split(' ')
                if len(split1) == 2 and (split1[1].endswith('w') or split1[1].endswith('x')):
                    try:
                        size = int(split1[1][:-1])
                        if biggest_size is None or size > biggest_size:
                            biggest_size = size
                            image_url = split1[0]
                    except:
                        continue
        elif img_elem.has_attr('src'):
            image_url = MainDownload.clear_resize_in_url(img_elem['src'])

        if modify_url_func is not None:
            image_url = modify_url_func(image_url)

        return image_url

    @staticmethod
    def get_image_extension(name_without_extension):
        for ext in ['jpg', 'png', 'gif', 'webp']:
            if os.path.exists(name_without_extension + '.' + ext):
                return ext
        return ''

    @staticmethod
    def clear_resize_in_url(url):
        # Change url in the form http://abc.com/image_name-800x600.jpg to http://abc.com/image-name.jpg
        regex = '(-[0-9]+x[0-9]+.)([A-Za-z]+)$'
        result = re.compile(regex).findall(url)
        if len(result) > 0 and len(result[0]) == 2:
            return url[0:len(url) - len(result[0][0]) - len(result[0][1])] + '.' + result[0][1]
        else:
            try:
                last_slash_index = url.rfind('/')
                filename = url[last_slash_index + 1:]
                front = url[0:last_slash_index]
                period_index = filename.rfind('.')
                filename_without_extension = filename[0:period_index]
                extension = filename[period_index + 1:]
                if '-' not in filename_without_extension:
                    return url
                dash_index = filename_without_extension.rfind('-')
                name_front = filename_without_extension[0:dash_index]
                name_back = filename_without_extension[dash_index + 1:]
                if len(name_back) > 10 and name_back.startswith('e') and name_back[1:].isnumeric():
                    return front + '/' + name_front + '.' + extension
                else:
                    return url
            except:
                return url

    @staticmethod
    def clear_resize_in_url2(url):
        first_pos = url.rfind('-')
        second_pos = url.rfind('.')
        if 0 < first_pos < second_pos < len(url) - 1:
            return url[0:first_pos] + url[second_pos:]
        return url

    @staticmethod
    def remove_string(text, str_list):
        if isinstance(str_list, list):
            string_list = str_list
        elif isinstance(str_list, str):
            string_list = [str_list]
        else:
            return text

        result = text
        for str_ in string_list:
            result = result.replace(str_, '')
        return result

    @staticmethod
    def unix_timestamp_to_text(timestamp):
        '''
        Convert Unit Timestamp in nanoseconds to readable text
        :param timestamp: Timestamp in Unix Timestamp (nanoseconds)
        :return: Readable text in Year-Month-Day Hour:Minute:Second.Nanoseconds
        '''

        if len(str(timestamp)) < 10:
            return ''
        dt = datetime.datetime.fromtimestamp(int(timestamp) // 1e9)
        return dt.strftime('%Y-%m-%d %H:%M:%S') + '.' + str(timestamp[len(timestamp) - 9: len(timestamp)]).zfill(9)

    @staticmethod
    def text_to_unix_timestamp(datetime_str):
        result = ''
        split1 = datetime_str.split('.')
        second_str = split1[0]
        try:
            result = str(int(time.mktime(datetime.datetime.strptime(second_str, "%Y-%m-%d").timetuple())))
        except:
            pass
        if len(result) == 0:
            try:
                result = str(int(time.mktime(datetime.datetime.strptime(second_str, "%Y-%m-%d %H:%M:%S").timetuple())))
            except:
                pass
        if len(result) > 0:
            if len(split1) == 2:
                result += split1[1]
            else:
                result += ''.zfill(9)
        return result

    @staticmethod
    def convert_kanji_to_number(text):
        # Only 1 to 99
        if not isinstance(text, str):
            return None
        if len(text) == 0 or len(text) > 3:
            return None

        kanjis = ['十', '一', '二', '三', '四', '五', '六', '七', '八', '九']
        eval = []
        for character in text:
            for i in range(len(kanjis)):
                if character == kanjis[i]:
                    eval.append(i)

        if len(eval) == 1:
            if eval[0] == 0:
                return 10
            else:
                return eval[0]
        elif len(eval) == 2:
            if eval[0] == 0 and eval[1] > 0:
                return 10 + eval[1]
            if eval[1] == 0 and eval[0] > 1:
                return eval[0] * 10
        elif len(eval) == 3 and eval[1] == 0 and eval[0] > 1:
            return eval[0] * 10 + eval[2]
        return None

    @staticmethod
    def convert_month_string_to_number(month):
        if month is None or len(month) == 0:
            return 0

        month_str = month.lower().strip()
        months = {
            'jan': 1, 'january': 1,
            'feb': 2, 'february': 2,
            'mar': 3, 'march': 3,
            'apr': 4, 'april': 4,
            'may': 5,
            'jun': 6, 'june': 6,
            'jul': 7, 'july': 7,
            'aug': 8, 'august': 8,
            'sep': 9, 'september': 9,
            'oct': 10, 'october': 10,
            'nov': 11, 'november': 11,
            'dec': 12, 'december': 12
        }
        if month_str in months:
            return months[month_str]
        else:
            return 0

    def add_to_image_list(self, name, url, to_jpg=False, is_mocanews=False):
        if len(name) == 0 or len(url) == 0:
            return
        image_obj = {'name': name, 'url': url}
        if to_jpg:
            image_obj['to_jpg'] = True
        if is_mocanews:
            image_obj['is_mocanews'] = True
        self.image_list.append(image_obj)

    def download_image_list(self, folder, clear=True, verify=True):
        if len(self.image_list) == 0:
            return
        self.download_image_objects(self.image_list, folder, verify=verify)
        if clear:
            self.image_list.clear()

    def download_by_template(self, folder, template, zfill=1, start=1, end=99, headers=None,
                             to_jpg=False, is_mocanews=False, min_width=None, max_skip=0, prefix='',
                             save_zfill=None):
        if isinstance(template, str):
            templates = [template]
        elif isinstance(template, list):
            templates = template
        else:
            raise Exception('Unexpected type for template')

        if isinstance(prefix, str):
            prefixes = [prefix]
        elif isinstance(prefix, list):
            prefixes = prefix
        else:
            raise Exception('Unexpected type for prefix')

        # Number of templates must be equal to number of prefixes if there is more than one prefixes
        if len(prefixes) > 1 and len(prefixes) != len(templates):
            raise Exception('Number of templates must be equal to the number of prefixes ' +
                            'if there is more than one prefixes')

        if save_zfill is None:
            save_zfill = zfill

        i = start - 1
        success = False
        skip_remaining = max_skip
        while i < end:
            success_count = 0
            i += 1
            template_index = -1
            for template_ in templates:
                template_index += 1
                if len(prefixes) <= template_index:
                    prefix_index = len(prefixes) - 1
                else:
                    prefix_index = template_index
                image_url = template_ % str(i).zfill(zfill)
                saved_url = template_ % str(i).zfill(save_zfill)  # For the purpose of saved image name
                image_name = prefixes[prefix_index] + self.extract_image_name_from_url(saved_url, with_extension=False)
                if self.is_image_exists(image_name, folder):
                    success_count += 1
                    skip_remaining = max_skip
                    continue
                result = self.download_image(image_url, folder + '/' + image_name, headers, to_jpg, is_mocanews, min_width)
                if result != -1:
                    success_count += 1
            if success_count > 0:
                success = True
                skip_remaining = max_skip
            else:
                skip_remaining -= 1
            if skip_remaining < 0:
                break
        return success

    # Template for guessing url that has 'core_sys' in the image URL
    def download_guess_core_sys(self, prefix, final_episode, images_per_episode, x1, x2, x3, x2m, x3m, print_url=False,
                                check_content_length=False, less_than_amount=None, more_than_amount=None,
                                less_than_equal=False, more_than_equal=False, is_or=False):
        folder = self.create_custom_directory('guess')
        template = prefix + 'core_sys/images/contents/%s/block/%s/%s.jpg'
        is_successful = False
        for i in range(final_episode):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1') or self.is_image_exists(episode + '_1', folder):
                continue
            is_success = False
            first = x1 + i
            second = x2 + x2m * i
            third = x3 + x3m * i
            for j in range(images_per_episode):
                image_url = template % (str(first).zfill(8), str(second).zfill(8), str(third + j).zfill(8))
                if print_url:
                    print(image_url)
                if check_content_length and\
                    not self.is_content_length_in_range(image_url, less_than_amount, more_than_amount,
                                                        less_than_equal, more_than_equal, is_or):
                    break
                image_name = episode + '_' + str(j + 1)
                result = self.download_image(image_url, folder + '/' + image_name)
                if result == 0:
                    is_success = True
                    is_successful = True
                elif result == -1:
                    break
            if is_success:
                print(self.__class__.__name__ + ' - Guessed successfully!')
            else:
                if len(os.listdir(folder)) == 0:
                    os.rmdir(folder)
                return
        if len(os.listdir(folder)) == 0:
            os.rmdir(folder)
        return is_successful

    @staticmethod
    def get_processed_items_from_cache_file(cache_filepath):
        processed_items = []
        if os.path.exists(cache_filepath):
            with open(cache_filepath, 'r') as f:
                inputs = f.read()
            processed_items = inputs.split(';')
        return processed_items, len(processed_items)

    @staticmethod
    def create_cache_file(cache_filepath, processed_items, previous_processed_count):
        if len(processed_items) > previous_processed_count:
            with open(cache_filepath, 'w+') as f:
                for i in range(len(processed_items)):
                    if i > 0:
                        f.write(';')
                    f.write(processed_items[i])

    def print_exception(self, ex, message=None, print_traceback=True):
        output = f"Error in running {self.__class__.__name__}"
        if message is not None and len(message) > 0:
            output += f' - {message}'
        print(f'{output}: {ex}')
        if print_traceback:
            traceback.print_exc()

    @staticmethod
    def get_youtube_thumbnails(soup):
        # Returns a list of tuples (YouTube ID, Thumbnail URL)
        results = []
        if soup is not None:
            contents = str(soup)
            arr = re.findall("((https://img\\.youtube\\.com/vi/)[a-zA-Z0-9|\\-|_]{11}(/maxresdefault\\.jpg))", contents)
            if len(arr) > 0:
                tup = arr[0]
                for item in tup:
                    if len(item) == 56:
                        youtube_id = item.split('/')[-2]
                        results.append((youtube_id, item))
        return results

    def download_youtube_thumbnails(self, url, folder):
        try:
            soup = self.get_soup(url)
            yt_tuples = self.get_youtube_thumbnails(soup)
            self.image_list = []
            for yt_tuple in yt_tuples:
                self.add_to_image_list('yt_' + yt_tuple[0], yt_tuple[1])
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'YouTube')

    @staticmethod
    def get_youtube_thumbnail_url(youtube_id):
        return f"https://i.ytimg.com/vi/{youtube_id}/hq720.jpg"

    def init_youtube_thumbnail_variables(self, yt_episodes=None, yt_folder=None):
        if yt_episodes is None:
            yt_episodes = []
        elif not isinstance(yt_episodes, list):
            raise TypeError('Expected type for yt_episodes: list')
        if yt_folder is None or len(yt_folder) == 0:
            yt_folder = self.create_custom_directory('yt')
        yt_images = os.listdir(yt_folder)
        for yt_image in yt_images:
            if os.path.isfile(yt_folder + '/' + yt_image) and yt_image.endswith('.jpg') \
                    and yt_image[0:2].isnumeric() and yt_image[2] == '_':
                yt_episodes.append(yt_image[0:2])
        return yt_folder, yt_episodes

    def download_youtube_thumbnail_by_id(self, yt_ids, yt_folder, episode):
        if isinstance(yt_ids, str):
            youtube_ids = [yt_ids]
        elif isinstance(yt_ids, list):
            youtube_ids = yt_ids
        else:
            return
        for i in range(len(youtube_ids)):
            yt_id = ' '.join(youtube_ids[i].split())
            yt_image_url = f'https://img.youtube.com/vi/{yt_id}/maxresdefault.jpg'
            if len(youtube_ids) > 1:
                yt_image_name = f'{episode}_{i + 1}_{yt_id}'
            else:
                yt_image_name = f'{episode}_{yt_id}'
            result = self.download_image(yt_image_url, f'{yt_folder}/{yt_image_name}')
            if result == -1:
                yt_image_url = f'https://img.youtube.com/vi/{yt_id}/sddefault.jpg'
                self.download_image(yt_image_url, f'{yt_folder}/{yt_image_name}')

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
        class_name = self.__name__[:-8] if self.__name__.lower().endswith('download') else self.__name__
        class_keywords = self.keywords + [self.folder_name, class_name]
        for filter_keyword in s_filter.keywords:
            for keyword in class_keywords:
                if len(keyword) == 0:
                    continue
                if filter_keyword.lower() in keyword.lower():
                    matched_keywords += 1
                    break
        return matched_keywords == len(s_filter.keywords)


# Generic template with paging
class NewsTemplate:
    def download_template_news(self, page_prefix, article_select, date_select, title_select, id_select,
                               paging_type=0, paging_suffix=None, paging_suffix_zfill=1, decode_response=True,
                               response_headers=None, id_has_id=False, id_attr='id', news_prefix=None,
                               a_tag_prefix=None, stop_date=None, date_separator=None, date_attr=None, date_prefix=None,
                               date_func=None, a_tag_replace_from=None, a_tag_replace_to='',
                               a_tag_start_text_to_remove=None, next_page_select=None, next_page_eval_index_class=None,
                               next_page_eval_index=0, next_page_eval_index_compare_page=False, unescape_title=False,
                               reverse_article_list=False, date_tag_count=1, verify=True, skip_first_page_num=True):
        """
        :param page_prefix: Start of the page URL to evaluate
        :param article_select: Selects article item elements
        :param date_select: Selects element containing date
        :param title_select: Selects element containing title
        :param id_select: If None = article item element itself, else = the select
        :param paging_type: 0 = news/page/2  1 = news/?p=2  2 = /2  3 = [Custom]
        :param paging_suffix: For paging_type 3. E.g. ?paged=%s
        :param paging_suffix_zfill: Apply zfill to the paging_suffix %s
        :param decode_response: Decode HTTP Response
        :param response_headers: Headers to be included in HTTP Request
        :param id_has_id: The element has 'id' attribute
        :param id_attr: Specify the attribute of the selected tag
        :param news_prefix: The prefix of the news page excluding page prefix
        :param a_tag_prefix: The prefix of news page that is missing from the a tag.
        :param stop_date: Stops evaluating item if date starts with stop_date
        :param date_separator: Specify separator to be replace to '.'
        :param date_attr: The attribute of the element where the date is stored
        :param date_prefix: Text to be appended before the date (e.g. append 20 to 21 = 2021)
        :param date_func: A function that takes in a date string, processes and returns a new string before further processing
        :param a_tag_replace_from: Text to be replaced in the 'href' attribute
        :param a_tag_replace_to: Text to replace to in the 'href' attribute
        :param a_tag_start_text_to_remove: Text to be removed at the beginning of a tag 'href' attribute
        :param next_page_select: Selects element containing URL that leads to next page
        :param next_page_eval_index_class: Terminates if next_page_select contains the class
        :param next_page_eval_index: Index number of the elements selected in next_page_select
        :param next_page_eval_index_compare_page: Terminates if the next_page_select's text = current page number
        :param unescape_title: Unescape HTML characters from title
        :param reverse_article_list: Reverse the processing of the articles being scraped. Only works on first page.
        :param date_tag_count: Number of tags in date select to concatenate
        :param verify: Set False to ignore SSLError
        :param skip_first_page_num: If False, include the first page number "1" in the page URL
        """

        if not issubclass(self.__class__, MainDownload):
            return

        if page_prefix.endswith('/'):
            news_url = page_prefix
        else:
            news_url = page_prefix + '/'
        if news_prefix is not None:
            news_url += news_prefix
        else:
            news_url += 'news/'

        stop = False
        try:
            results = []
            news_obj = self.get_last_news_log_object()
            for page in range(1, 100, 1):
                page_url = news_url
                if not skip_first_page_num or page > 1:
                    if paging_type == 1:
                        page_url = news_url + '?p=' + str(page)
                    elif paging_type == 2:
                        page_url = news_url + str(page)
                    elif paging_type == 3 and paging_suffix is not None:
                        page_url = news_url + (paging_suffix % str(page).zfill(paging_suffix_zfill))
                    else:
                        page_url = news_url + 'page/' + str(page)
                if response_headers:
                    soup = self.get_soup(page_url, headers=response_headers, decode=decode_response, verify=verify)
                else:
                    soup = self.get_soup(page_url, decode=decode_response, verify=verify)
                articles = soup.select(article_select)
                if reverse_article_list:
                    articles = reversed(articles)
                for article in articles:
                    tag_titles = article.select(title_select)
                    if date_select is None:
                        tag_dates = [article]
                    else:
                        tag_dates = article.select(date_select)
                    if id_select is None:
                        tag_ids = [article]
                    else:
                        tag_ids = article.select(id_select)
                    if len(tag_dates) > 0 and len(tag_titles) > 0:
                        has_tag_ids = len(tag_ids) > 0
                        if has_tag_ids:
                            if id_has_id:
                                if tag_ids[0].has_attr(id_attr):
                                    article_id = tag_ids[0][id_attr]
                                else:
                                    continue
                                if a_tag_prefix:
                                    article_id = a_tag_prefix + article_id
                            elif tag_ids[0].has_attr('href'):
                                article_id_suffix = tag_ids[0]['href']
                                if a_tag_replace_from:
                                    article_id_suffix = article_id_suffix.replace(a_tag_replace_from, a_tag_replace_to)
                                if a_tag_start_text_to_remove and article_id_suffix.startswith(a_tag_start_text_to_remove):
                                    article_id_suffix = article_id_suffix[len(a_tag_start_text_to_remove):]
                                if a_tag_prefix:
                                    article_id = a_tag_prefix + article_id_suffix
                                else:
                                    article_id = article_id_suffix
                            else:
                                continue
                        else:
                            article_id = ''
                        if date_tag_count > 1:
                            tag_count = 0
                            unformatted_date = ''
                            for tag_date in tag_dates:
                                unformatted_date += ' '.join(tag_date.text.strip().split())
                                tag_count += 1
                                if tag_count == date_tag_count:
                                    break
                        elif date_attr is None:
                            unformatted_date = ' '.join(tag_dates[0].text.strip().split())
                        else:
                            if tag_dates[0].has_attr(date_attr):
                                unformatted_date = ' '.join(tag_dates[0][date_attr].strip().split())
                            else:
                                continue
                        if date_func is not None:
                            unformatted_date = date_func(unformatted_date)
                        if date_separator is not None:
                            unformatted_date = unformatted_date.replace(date_separator, '.')
                        if date_prefix is not None:
                            unformatted_date = date_prefix + unformatted_date
                        date = self.format_news_date(unformatted_date)
                        if len(date) == 0:
                            continue
                        title = ' '.join(tag_titles[0].text.strip().split())
                        if unescape_title:
                            title = unescape(title)
                        if (stop_date is not None and date.startswith(stop_date)) or\
                                (news_obj and ((has_tag_ids and news_obj['id'] == article_id) or
                                               (not has_tag_ids and title == news_obj['title']) or
                                               date < news_obj['date'])):
                            stop = True
                            break
                        results.append(self.create_news_log_object(date, title, article_id))
                if stop or next_page_select is None:
                    break
                next_page_tag = soup.select(next_page_select)
                if len(next_page_tag) == 0:
                    break
                if next_page_eval_index >= len(next_page_tag) or next_page_eval_index < -1:
                    break
                if next_page_eval_index_compare_page and next_page_tag[next_page_eval_index].text.strip() == str(page):
                    break
                if next_page_eval_index_class is not None\
                        and next_page_tag[next_page_eval_index].has_attr('class')\
                        and next_page_eval_index_class in next_page_tag[next_page_eval_index]['class']:
                    break
            success_count = 0
            for result in reversed(results):
                process_result = self.create_news_log_from_news_log_object(result)
                if process_result == 0:
                    success_count += 1
            if len(results) > 0:
                self.create_news_log_cache(success_count, results[0])
        except Exception as e:
            self.print_exception(e, 'News')


# News template
# Where exists div.list_01, date = td.day, title = div.title, nagivation next page = nb_nex
class NewsTemplate2:
    def download_template_news(self, page_prefix, first_page_url=None, stop_date=None, date_select=None):
        if not issubclass(self.__class__, MainDownload):
            return

        if page_prefix.endswith('/'):
            news_url = page_prefix
        else:
            news_url = page_prefix + '/'
        if first_page_url:
            news_url += first_page_url
        else:
            news_url += 'news/'

        stop = False
        try:
            results = []
            news_obj = self.get_last_news_log_object()
            page_url = news_url
            for page in range(1, 100, 1):
                soup = self.get_soup(page_url, decode=True)
                list_div = soup.find('div', id='list_01')
                if not list_div:
                    continue
                trs = list_div.find_all('tr')
                for tr in trs:
                    tag_date = None
                    if date_select is None:
                        tag_date = tr.find('td', class_='day')
                    else:
                        tag_dates = tr.select(date_select)
                        if len(tag_dates) > 0:
                            tag_date = tag_dates[0]
                    tag_title = tr.find('div', class_='title')
                    a_tag = tr.find('a')
                    if tag_date and tag_title:
                        article_id = ''
                        if a_tag and a_tag.has_attr('href'):
                            article_id = page_prefix + a_tag['href'].replace('../', '')
                        date = tag_date.text.replace('/', '.')
                        title = tag_title.text.strip()
                        if (stop_date is not None and date.startswith(stop_date)) or\
                                (news_obj and ((news_obj['id'] == article_id and news_obj['title'] == title)\
                                         or date < news_obj['date'])):
                            stop = True
                            break
                        results.append(self.create_news_log_object(date, title, article_id))
                if stop:
                    break
                nb_nex = soup.find('li', class_='nb_nex')
                if nb_nex is None:
                    break
                nb_nex_a_tag = nb_nex.find('a')
                if nb_nex_a_tag is None or not nb_nex_a_tag.has_attr('href'):
                    break
                page_url = page_prefix + nb_nex_a_tag['href'].replace('../', '')
            success_count = 0
            for result in reversed(results):
                process_result = self.create_news_log_from_news_log_object(result)
                if process_result == 0:
                    success_count += 1
            if len(results) > 0:
                self.create_news_log_cache(success_count, results[0])
        except Exception as e:
            self.print_exception(e, 'News')


# News template which contain article.content-entry, div.entry-date, div.entry-title
class NewsTemplate3:
    def download_template_news(self, page_prefix, first_page_url=None, stop_date=None):
        if not issubclass(self.__class__, MainDownload):
            return

        if page_prefix.endswith('/'):
            news_url = page_prefix
        else:
            news_url = page_prefix + '/'
        if first_page_url:
            news_url += first_page_url
        else:
            news_url += 'news.html'

        try:
            soup = self.get_soup(news_url, decode=True)
            articles = soup.find_all('article', class_='content-entry')
            news_obj = self.get_last_news_log_object()
            results = []
            for article in articles:
                if not article.has_attr('id'):
                    continue
                tag_date = article.find('div', class_='entry-date')
                tag_title = article.select('.entry-title')
                if tag_date and len(tag_title) > 0:
                    article_id = article['id']
                    date = self.format_news_date(tag_date.text.replace('/', '.'))
                    if len(date) == 0:
                        continue
                    title = ' '.join(tag_title[0].text.strip().split())
                    if (stop_date is not None and date.startswith(stop_date)) or\
                            (news_obj and (news_obj['id'] == article_id or date < news_obj['date'])):
                        break
                    results.append(self.create_news_log_object(date, title, article_id))
            success_count = 0
            for result in reversed(results):
                process_result = self.create_news_log_from_news_log_object(result)
                if process_result == 0:
                    success_count += 1
            if len(results) > 0:
                self.create_news_log_cache(success_count, results[0])
        except Exception as e:
            self.print_exception(e, 'News')


class NewsTemplate4:
    def download_template_news(self, name='', print_http_error=False, json_obj=None, json_url=None, verify=True):
        news_url = self.PAGE_PREFIX + 'news/'
        try:
            if json_obj is None:
                if json_url is None:
                    json_obj = self.get_json(self.PAGE_PREFIX + f'wp-json/{name}/init', verify=verify)
                else:
                    json_obj = self.get_json(json_url, verify=verify)
            news_obj = self.get_last_news_log_object()
            results = []
            for item in json_obj['news']:
                article_id = news_url + item['id']
                date = item['date'][0:10].replace('-', '.')
                title = item['title']
                if news_obj and (news_obj['id'] == article_id or date < news_obj['date']):
                    break
                results.append(self.create_news_log_object(date, title, article_id))
            success_count = 0
            for result in reversed(results):
                process_result = self.create_news_log_from_news_log_object(result)
                if process_result == 0:
                    success_count += 1
            if len(results) > 0:
                self.create_news_log_cache(success_count, results[0])
        except requests.exceptions.HTTPError as e:
            if print_http_error:
                print(self.__class__.__name__ + ' - 403 Error when retrieving news API.')
        except Exception as e:
            self.print_exception(e, 'News')


class InvalidImageSizeError(Exception):
    """Raised when image size is not as expected"""
    pass
