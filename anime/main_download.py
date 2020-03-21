import requests
import datetime
import urllib.request
import os
from bs4 import BeautifulSoup as bs

class MainDownload:
    
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

        # Create download log:
        timenow = str(datetime.datetime.now())
        split1 = filepath_without_extension.split('/')
        if len(split1) > 2:
            filepath = ''
            for i in range(len(split1) - 1):
                filepath += split1[i] + '/'
            filename = split1[len(split1) - 1]
            logpath = filepath + 'log.txt'
            with open(logpath, 'a+') as f:
                f.write(timenow + '\t' + filename + '\t' + url + '\n')

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
            return False
        
        if headers == None:
            headers = {}
            headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        
        # Download image:
        try:
            with requests.get(url, stream=True, headers=headers) as r:
                r.raise_for_status()
                with open(filepath, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
            print("Downloaded " + url)
            return True
        except Exception as e:
            print("Failed to download " + url + ' - ' + str(e))
            return False
    
    @staticmethod    
    def create_directory(filepath):
        # If directory exists
        if not os.path.exists(filepath):
            os.makedirs(filepath)
    
    @staticmethod
    def is_file_exists(filepath):
        return os.path.isfile(filepath)
