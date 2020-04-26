import requests
import random
import datetime
import urllib.request
import os
import re
from bs4 import BeautifulSoup as bs
from search import *


class MainDownload:

    title = ""
    keywords = []
    season = None
    season_name = ""

    def __init__(self):
        self.base_folder = "download"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
        
    def run(self):
        pass

    @staticmethod
    def get_response(url, headers=None, decode=False):
        response = ""
        if headers == None:
            headers = {}
            headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        try:
            result = requests.get(url, headers=headers)
            if (decode):
                response = str(result.content.decode())
            else:
                response = str(result.content)
        except Exception as e:
            print(e)
        return response
        
    @staticmethod
    def get_soup(url, headers=None, decode=False):
        if headers == None:
            headers = {}
            headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
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
    def get_json(url,  headers=None):
        response = ""
        if headers == None:
            headers = {}
            headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
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
            headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        try:
            result = requests.post('https://moca-news.net/pd.php', headers=headers, data=data)
            response = str(result.content.decode())
        except Exception as e:
            print(e)
        return response
    
    @staticmethod
    def download_image(url, filepath_without_extension, headers=None):
        """
        Download image to the filepath
        :param url:
        :param filepath_without_extension:
        :param headers:
        :return: 0 - Success, 1 - File Exists, -1 - Error
        """

        if ".png" in url:
            filepath = filepath_without_extension + ".png"
        elif ".jpeg" in url:
            filepath = filepath_without_extension + ".jpeg"
        elif ".gif" in url:
            filepath = filepath_without_extension + ".gif"
        else:
            filepath = filepath_without_extension + ".jpg"
        
        # Check local directory if the file exists
        if (MainDownload.is_file_exists(filepath)):
            #print("File exists: " + filepath)
            return 1
        
        if headers == None:
            headers = {}
            headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        
        # Download image:
        try:
            with requests.get(url, stream=True, headers=headers) as r:
                # File not found or redirected to main page
                if r.status_code == 404:
                    return -1
                r.raise_for_status()
                with open(filepath, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
            print("Downloaded " + url)

            # Create download log:
            timenow = str(datetime.datetime.now())
            split1 = filepath_without_extension.split('/')
            if len(split1) > 2:
                filepath = ''
                for i in range(len(split1) - 1):
                    filepath += split1[i] + '/'
                filename = split1[len(split1) - 1]
                logpath = filepath + 'log.txt'
                with open(logpath, 'a+', encoding='utf-8') as f:
                    f.write(timenow + '\t' + filename + '\t' + url + '\n')
            return 0
        except Exception as e:
            print("Failed to download " + url + ' - ' + str(e))
            return -1
    
    def download_image_if_exists(self, url, filepath_without_extension, old_filepath, headers=None):
        if headers == None:
            headers = {}
            headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        
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
