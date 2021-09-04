from search import SearchFilter
from multiprocessing import Pool
from anime import *
import migrate


def run_process(download, download_id):
    pid = str(os.getpid())
    download.download_id = download_id
    class_name = download.__class__.__name__
    filepath = constants.FOLDER_PROCESS + '/' + class_name
    print("Running %s" % class_name)
    if os.path.exists(constants.FOLDER_PROCESS):
        with open(filepath, 'w+') as f:
            f.write(pid)
    download.run()
    # print("Ending %s" % class_name)
    if os.path.exists(filepath):
        os.remove(filepath)


def process_download(downloads):
    if not os.path.exists(constants.FOLDER_PROCESS):
        os.makedirs(constants.FOLDER_PROCESS)
    if constants.MAX_PROCESSES <= 0 or len(downloads) == 0:
        return

    if len(downloads) > 1:
        with Pool(min(constants.MAX_PROCESSES, len(downloads))) as p:
            results = []
            download_id = 1
            for download in downloads:
                result = p.apply_async(run_process, (download(), str(download_id).zfill(5)))
                results.append(result)
                download_id += 1
            for result in results:
                result.wait()
    else:
        run_process(downloads[0](), '00001')
    update_global_logs()
    if len(os.listdir(constants.FOLDER_PROCESS)) == 0:
        os.rmdir(constants.FOLDER_PROCESS)

    print("Download completed")


def update_global_logs():
    if os.path.exists(constants.GLOBAL_TEMP_FOLDER):
        files = os.listdir(constants.GLOBAL_TEMP_FOLDER)
        for file in files:
            if file.startswith('download_'):
                logpath = constants.GLOBAL_DOWNLOAD_LOG_FILE
            elif file.startswith('news_'):
                logpath = constants.GLOBAL_NEWS_LOG_FILE
            else:
                continue
            filepath = constants.GLOBAL_TEMP_FOLDER + '/' + file
            with open(logpath, 'a+', encoding='utf-8') as f:
                with open(filepath, 'r', encoding='utf-8') as f2:
                    lines = f2.readlines()
                for line in lines:
                    if len(line) > 0:
                        if line[-1] != '\n':
                            f.write(line + '\n')
                        else:
                            f.write(line)
            os.remove(filepath)
        files = os.listdir(constants.GLOBAL_TEMP_FOLDER)
        if len(files) == 0:
            os.removedirs(constants.GLOBAL_TEMP_FOLDER)


def run():
    migrate.run()
    update_global_logs()

    while True:
        print_intro_message()
        try:
            choice = int(input("Enter choice: ").strip())
        except:
            print("Invalid input. Please enter an integer.")
            continue

        if choice == 1:
            process_query(True, False, False)
        elif choice == 2:
            process_query(False, True, False)
        elif choice == 3:
            process_query(True, True, False)
        elif choice == 4:
            process_query(True, False, True)
        elif choice == 5:
            download_from_news_website()
        elif choice == 0:
            break
        else:
            print("Invalid choice.")
    print("Exiting...")


def print_intro_message():
    print("Enter choice:")
    print("1 - Search anime by keyword")
    print("2 - Search anime by season")
    print("3 - Search anime by keyword and season")
    print("4 - Identify the season the anime belongs to")
    print("5 - Download from news website")
    print("0 - Exit")


def get_numbers_from_expression(expr):
    results = []

    valid_chars = "0123456789-,"

    for i in expr:
        if i not in valid_chars:
            raise ValueError("Invalid characters - Usage Example: 1-5,6-8,10")

    split1 = expr.split(",")
    for ex in split1:
        split2 = ex.split("-")
        if len(split2) == 1:
            try:
                results.append(int(split2[0]))
            except:
                raise ValueError("Processing error - Usage Example: 1-5,6-8,10")
        elif len(split2) == 2:
            try:
                first_num = int(split2[0])
                last_num = int(split2[1])
                for j in range(first_num, last_num + 1, 1):
                    results.append(j)
            except:
                raise ValueError("Processing error - Usage Example: 1-5,6-8,10")
        else:
            raise ValueError("Processing error - Usage Example: 1-5,6-8,10")
    return results


def process_query(has_keyword, has_season, print_season):
    keyword = None
    season = None

    season_classes = None
    if has_season:
        season_classes = get_season_classes()
        if len(season_classes) == 0:
            print("No season found.")
            return

    if has_keyword:
        if print_season:
            keyword = input("Enter anime name or keyword: ").strip()
        else:
            keyword = input("Enter keyword: ").strip()

    if has_season:
        print_season_choice(season_classes)
        choices = []
        while True:
            try:
                expr = input("Enter choice(s) of season: ").strip()
                choices = get_numbers_from_expression(expr)
                break
            except ValueError:
                print("Invalid characters - Usage Example: 1-5,6-8,10")
                continue
        filtered_season_classes = filter_season_classes(season_classes, choices)
        season = get_season_queries(filtered_season_classes)
        if len(filtered_season_classes) == 0:
            print("No season is selected.")
            return
        else:
            season_output = ''
            for i in range(len(filtered_season_classes)):
                if i > 4:
                    season_output += '...'
                    break
                season_output += filtered_season_classes[i].season_name
                if i < len(filtered_season_classes) - 1:
                    season_output += ', '
            if len(filtered_season_classes) == 1:
                suffix = 'Season'
            else:
                suffix = '%s Seasons' % str(len(filtered_season_classes))
            print('Selected %s: %s' % (suffix, season_output))

    sf = SearchFilter(query=keyword, season=season)
    anime_classes = get_all_anime_classes(sf)
    print_anime_choice(anime_classes)

    if len(anime_classes) == 0:
        print("No results found")
        return
    else:
        choices = []
        while True:
            try:
                if print_season:
                    expr = input("Enter choice(s) of anime to identify the season: ").strip()
                else:
                    expr = input("Enter choice(s) of anime to download: ").strip()
                choices = get_numbers_from_expression(expr)
                break
            except ValueError:
                print("Invalid characters - Usage Example: 1-5,6-8,10")
                continue
        filtered_anime_classes = filter_anime_classes(anime_classes, choices)
        if len(filtered_anime_classes) == 0:
            print("No anime selected.")
            return
        elif print_season:
            print_season_out(filtered_anime_classes)
        else:
            process_download(filtered_anime_classes)


def print_season_out(anime_classes):
    for anime_class in anime_classes:
        print('%s | %s' % (anime_class.season, anime_class.title))


def get_all_anime_classes(s_filter):
    if not isinstance(s_filter, SearchFilter):
        return TypeError("Unexpected type - Type is not SearchFilter")

    anime_classes = []
    subclasses = MainDownload.__subclasses__()
    for subclass in subclasses:
        if subclass.__name__ != "ExternalDownload" and subclass.season is not None:
            if s_filter.season is None or (s_filter.season is not None and subclass.season in s_filter.season):
                for subsubclass in subclass.__subclasses__():
                    if subsubclass.enabled and subsubclass.match(subsubclass, s_filter):
                        anime_classes.append(subsubclass)

    anime_classes.sort(key=lambda x: x.title)
    return anime_classes


def get_season_classes():
    season_classes = []
    subclasses = MainDownload.__subclasses__()
    for subclass in subclasses:
        if subclass.__name__ != "ExternalDownload" and subclass.season is not None:
            subsubclasses = subclass.__subclasses__()
            if len(subsubclasses) > 0:
                for subsubclass in subsubclasses:
                    if subsubclass.enabled:
                        season_classes.append(subclass)
                        break
    season_classes.sort(key=lambda x: x.season, reverse=True)
    return season_classes


def filter_season_classes(season_classes, choices):
    result_classes = []
    choices = list(dict.fromkeys(choices)) # remove duplicates
    for choice in choices:
        if 0 < choice <= len(season_classes):
            result_classes.append(season_classes[choice - 1])
    return result_classes


def print_season_choice(season_classes):
    result_classes = []
    for i in range(len(season_classes)):
        choice = str(i + 1).rjust(len(str(len(season_classes))))
        season_class = season_classes[i]
        print("%s - %s (%s)" % (choice, season_class.season, season_class.season_name))
    return result_classes


def get_season_queries(season_classes):
    result = []
    for sc in season_classes:
        result.append(sc.season)
    return result


def print_anime_choice(anime_classes):
    result_classes = []
    for i in range(len(anime_classes)):
        choice = str(i + 1).rjust(len(str(len(anime_classes))))
        print("%s - %s" % (choice, anime_classes[i].title))
    return result_classes


def filter_anime_classes(anime_classes, choices):
    result_classes = []
    choices = list(dict.fromkeys(choices)) # remove duplicates
    for choice in choices:
        if 0 < choice <= len(anime_classes):
            result_classes.append(anime_classes[choice - 1])
    return result_classes


def download_from_news_website():
    while True:
        print_news_website_choice()
        try:
            choice = int(input("Enter choice of news website: ").strip())
        except:
            print("Invalid input. Please enter an integer.")
            continue

        if 0 < choice < 6:
            id = input('Enter article ID: ').strip()
            if len(id) == 0:
                print('Invalid article ID')
                continue
            base_folder = 'news/%s/%s'
            if choice == 1:
                AnimeRecorderDownload(str(id), base_folder % (constants.EXTERNAL_FOLDER_ANIME_RECORDER, str(id)), None).run()
            if choice == 2:
                AniverseMagazineDownload(str(id), base_folder % (constants.EXTERNAL_FOLDER_ANIVERSE, str(id)), None).run()
            if choice == 3:
                if len(id) != 15:
                    print('Invalid article ID')
                    continue
                article_id = id[0:8] + '/' + id
                MocaNewsDownload(article_id, base_folder % (constants.EXTERNAL_FOLDER_MOCANEWS, str(id)), None).run()
            elif choice == 4:
                NatalieDownload(str(id), base_folder % (constants.EXTERNAL_FOLDER_NATALIE, str(id)), None).run()
            elif choice == 5:
                WebNewtypeDownload(str(id), base_folder % (constants.EXTERNAL_FOLDER_WEBNEWTYPE, str(id)), None).run()
        elif choice == 0:
            break
        else:
            print("Invalid choice.")
    print("Exiting...")


def print_news_website_choice():
    print('1 - Anime Recorder')
    print('2 - Aniverse')
    print('3 - Moca News')
    print('4 - Natalie')
    print('5 - WebNewtype')
    print("0 - Return")


if __name__ == "__main__":
    run()
    #classes = get_all_anime_classes(SearchFilter(query="", season="2020-2"))
    #print(classes)
