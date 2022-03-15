import os
import requests
from anime.constants import FOLDER_OUTPUT, HTTP_HEADER_USER_AGENT


TEMPLATE = 'https://aniverse-mag.com/wp-content/uploads/%s/%s/%s.jpg'
BASE_FOLDER = FOLDER_OUTPUT + '/aniverse'
MAX_LIMIT = 50
MAX_LIMIT_J = 100


def run_old(_year, _month):
    try:
        folder = BASE_FOLDER + '/' + _year + '/' + _month
        for i in range(MAX_LIMIT):
            success_count = 0
            for j in range(MAX_LIMIT_J):
                first = str(j + 1).zfill(2)
                if i == 0:
                    image_name = first
                else:
                    image_name = first + '-' + str(i)
                image_url = TEMPLATE % (_year, _month, image_name)
                result = download_image(image_url, folder, image_name + '.jpg')
                if result == -1:
                    break
                success_count += 1
            if success_count == 0:
                break
    except Exception as e:
        print(e)


def run(_year, _month, has_zfill=True):
    try:
        folder = BASE_FOLDER + '/' + _year + '/' + _month
        for i in range(MAX_LIMIT):
            success_count = 0
            if has_zfill:
                first = str(i + 1).zfill(2)
            elif i < 9:
                first = str(i + 1)
            else:
                return
            for j in range(MAX_LIMIT_J):
                if j == 0:
                    image_name = first
                else:
                    image_name = f'{first}-{j}'
                image_url = TEMPLATE % (_year, _month, image_name)
                filename = image_name + '.jpg'
                if os.path.exists(f'{folder}/{filename}'):
                    success_count += 1
                    continue
                result = download_image(image_url, folder, image_name + '.jpg')
                if result == -1:
                    break
                success_count += 1
            if success_count == 0:
                break
    except Exception as e:
        print(e)


def download_image(image_url, folder, filename):
    try:
        if not os.path.exists(folder):
            os.makedirs(folder)
        filepath = folder + '/' + filename
        if os.path.exists(filepath):
            return 1
        headers = HTTP_HEADER_USER_AGENT
        with requests.get(image_url, stream=True, headers=headers) as r:
            if r.status_code == 404:
                print("[ERROR] File not found: " + image_url)
                return -1
            r.raise_for_status()
            if 'image' not in r.headers['Content-Type']:
                return -1
            with open(filepath, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
        print("[INFO] Downloaded " + image_url)
        return 0
    except Exception as e:
        print("[ERROR] Failed to download " + image_url + ' - ' + str(e))
        return -1


if __name__ == '__main__':
    while True:
        year = input('Enter year: ')
        if len(year) == 0:
            break
        month = input('Enter month: ').zfill(2)
        run(year, month, True)
        run(year, month, False)
