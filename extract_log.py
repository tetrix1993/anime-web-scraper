import xlsxwriter
from anime import *
from anime.constants import EXTERNAL_FOLDERS, FOLDER_OUTPUT, FOLDER_IMAGE_LOGS

# This script generates a tab-separated value (TSV) file containing the image URL of the episode previews from a list
# of anime by extracting details from the download.log file in the log folder stored in each of the anime folder.


def run(filename, anime_classes, include_external=False):
    regex = '[0-9]+_[0-9]+'  # Get only images with specific names: 01_1.jpg, 02_5.png etc.
    if not os.path.exists(FOLDER_OUTPUT):
        os.makedirs(FOLDER_OUTPUT)
    output_file = FOLDER_OUTPUT + '/' + filename
    with open(output_file, 'w+', encoding='utf-8') as f:
        for i in anime_classes:
            title = i.title
            fullpath = i.get_full_path()
            logpath_template = fullpath + '%s/log/download.log'
            logpaths = [logpath_template % '']
            if include_external:
                for external_folder in EXTERNAL_FOLDERS:
                    logpaths.append(logpath_template % ('/' + external_folder))
            for logpath in logpaths:
                if os.path.exists(logpath):
                    with open(logpath, 'r', encoding='utf-8') as f2:
                        lines = f2.readlines()
                    output = []
                    for line in lines:
                        split1 = line.split('\t')
                        timestamp = split1[0]
                        filepath = split1[1]
                        if filepath in output:
                            continue
                        url = split1[2].replace('\n', '')
                        split2 = filepath.split('/')
                        url_split = url.split('?')[0]
                        if len(split2) == 2:
                            result = re.compile(regex).findall(filepath)
                            if len(result) == 1:
                                output.append(filepath)
                                f.write(title + '\t' + timestamp + '\t' + filepath + '\t' + url_split + '\n')


def generate_excel(filename, anime_classes, include_external=False):
    regex = '[0-9]+_[0-9]+'  # Get only images with specific names: 01_1.jpg, 02_5.png etc.
    if not os.path.exists(FOLDER_OUTPUT):
        os.makedirs(FOLDER_OUTPUT)
    output_file = FOLDER_OUTPUT + '/' + filename
    if os.path.exists(output_file):
        os.remove(output_file)
    with xlsxwriter.Workbook(output_file) as workbook:
        worksheet = workbook.add_worksheet('Data')

        # Formats
        header_format = workbook.add_format({'bold': True, 'num_format': '@',
                                             'font_color': 'white', 'bg_color': '#538DD5'})
        data_format = workbook.add_format({'num_format': '@'})

        # Headers
        worksheet.write(0, 0, 'Anime', header_format)
        worksheet.write(0, 1, 'Season', header_format)
        worksheet.write(0, 2, 'Timestamp', header_format)
        worksheet.write(0, 3, 'File Name', header_format)
        worksheet.write(0, 4, 'URL', header_format)
        worksheet.write(0, 5, 'Core Sys', header_format)
        worksheet.write(0, 6, 'Sys Contents', header_format)

        row = 0
        for i in anime_classes:
            title = i.title
            season = i.season
            fullpath = i.get_full_path()
            logpath_template = fullpath + '%s/log/download.log'
            logpaths = [logpath_template % '']
            if include_external:
                for external_folder in EXTERNAL_FOLDERS:
                    logpaths.append(logpath_template % ('/' + external_folder))
            for logpath in logpaths:
                if os.path.exists(logpath):
                    with open(logpath, 'r', encoding='utf-8') as f2:
                        lines = f2.readlines()
                    output = []
                    for line in lines:
                        split1 = line.split('\t')
                        timestamp = split1[0]
                        filepath = split1[1]
                        if filepath in output:
                            continue
                        url = split1[2].replace('\n', '')
                        split2 = filepath.split('/')
                        url_split = url.split('?')[0]
                        if len(split2) == 2:
                            result = re.compile(regex).findall(filepath)
                            if len(result) == 1:
                                output.append(filepath)
                                row += 1
                                worksheet.write(row, 0, title, data_format)
                                worksheet.write(row, 1, season, data_format)
                                worksheet.write(row, 2, timestamp, data_format)
                                worksheet.write(row, 3, filepath, data_format)
                                worksheet.write(row, 4, url_split, data_format)
                                worksheet.write_formula(row, 5, '=ISNUMBER(FIND("/core_sys/", E%s))' % str(row + 1))
                                worksheet.write_formula(row, 6, '=ISNUMBER(FIND("/SYS/CONTENTS/", E%s))' % str(row + 1))


def news_log_to_excel(filename, anime_classes):
    if not os.path.exists(FOLDER_OUTPUT):
        os.makedirs(FOLDER_OUTPUT)
    output_file = FOLDER_OUTPUT + '/' + filename
    if os.path.exists(output_file):
        os.remove(output_file)
    with xlsxwriter.Workbook(output_file) as workbook:
        worksheet = workbook.add_worksheet('Data')

        # Formats
        header_format = workbook.add_format({'bold': True, 'num_format': '@',
                                             'font_color': 'white', 'bg_color': '#538DD5'})
        data_format = workbook.add_format({'num_format': '@'})

        # Headers
        worksheet.write(0, 0, 'Anime', header_format)
        worksheet.write(0, 1, 'Season', header_format)
        worksheet.write(0, 2, 'Timestamp', header_format)
        worksheet.write(0, 3, 'Date', header_format)
        worksheet.write(0, 4, 'Title', header_format)
        worksheet.write(0, 5, 'ID', header_format)

        row = 0
        for i in anime_classes:
            title = i.title
            season = i.season
            fullpath = i.get_full_path()
            logpath_template = fullpath + '%s/log/news.log'
            logpaths = [logpath_template % '']
            for logpath in logpaths:
                if os.path.exists(logpath):
                    with open(logpath, 'r', encoding='utf-8') as f2:
                        lines = f2.readlines()
                    for line in lines:
                        split1 = line.split('\t')
                        if len(split1) != 4:
                            continue
                        timestamp = split1[0]
                        date = split1[1]
                        news_title = split1[2]
                        id_ = split1[3].replace('\n', '')
                        row += 1
                        worksheet.write(row, 0, title, data_format)
                        worksheet.write(row, 1, season, data_format)
                        worksheet.write(row, 2, timestamp, data_format)
                        worksheet.write(row, 3, date, data_format)
                        worksheet.write(row, 4, news_title, data_format)
                        worksheet.write(row, 5, id_, data_format)


def download_log_to_md_file(filename, title, anime_classes):
    if not os.path.exists(FOLDER_IMAGE_LOGS):
        os.makedirs(FOLDER_IMAGE_LOGS)
    output_file = FOLDER_IMAGE_LOGS + '/' + filename
    if os.path.exists(output_file):
        os.remove(output_file)

    with open(output_file, 'w+', encoding='utf-8') as f:
        f.write(f'# {title}\n\n')
        for i in anime_classes:
            f.write(f'## {i.title}\n<details>\n<summary>Click to expand...</summary>\n\n')
            fullpath = i.get_full_path()
            logpath = fullpath + '/log/download.log'
            links = {}
            if os.path.exists(logpath):
                with open(logpath, 'r', encoding='utf-8') as f2:
                    lines = f2.readlines()
                for line in lines:
                    split1 = line.split('\t')
                    if len(split1) != 3:
                        continue
                    filename = split1[1][1:] if split1[1].startswith('/') else split1[1]
                    if '/' in filename:
                        continue
                    filenumber = filename.split('_')[0].split('.')[0]
                    try:
                        int(filenumber)
                        if filename in links:
                            continue
                        url = split1[2].replace('\n', '')
                        links[filename.split('.')[0]] = (filename, url)
                    except:
                        continue
            keys = links.keys()
            if len(keys) > 0:
                f.write(f'Name | URL\n--- | ---\n')
                for key in sorted(links.keys()):
                    f.write(f'{links[key][0]} | {links[key][1]}\n')
            f.write(f'\n</details>\n\n')


if __name__ == '__main__':
    pass
