import os
import re
from anime import Winter2021AnimeDownload
from anime.constants import EXTERNAL_FOLDERS

# This script generates a tab-separated value (TSV) file containing the image URL of the episode previews from a list
# of anime by extracting details from the download.log file in the log folder stored in each of the anime folder.


def run(filename, anime_classes, include_external=False):
    regex = '[0-9]+_[0-9]+'  # Get only images with specific names: 01_1.jpg, 02_5.png etc.
    with open(filename, 'w+', encoding='utf-8') as f:
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


if __name__ == '__main__':
    run('2021-1_Log.tsv', Winter2021AnimeDownload.__subclasses__(), True)
