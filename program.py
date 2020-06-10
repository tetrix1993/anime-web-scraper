from search import SearchFilter
from anime import MainDownload
from multiprocessing import Process
from anime import *
import migrate


def run_process(download):
    print("Running " + download.__class__.__name__ + " (" + str(os.getpid()) + ")")
    download.run()


def process_download(downloads):
    processes = []
    for download in downloads:
        process = Process(target=run_process, args=(download(),))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print("Download completed")


def run():
    migrate.run()
    while True:
        print_intro_message()
        try:
            choice = int(input("Enter choice: ").strip())
        except:
            print("Invalid input. Please enter an integer.")
            continue

        if choice == 1:
            process_query(True, False)
        elif choice == 2:
            process_query(False, True)
        elif choice == 3:
            process_query(True, True)
        elif choice == 0:
            break
        else:
            print("Invalid choice.")
    print("Exiting...")


def print_intro_message():
    print("Search for anime to download:")
    print("1 - Filter by keyword only")
    print("2 - Filter by season only")
    print("3 - Filter by keyword and season")
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


def process_query(has_keyword, has_season):
    keyword = None
    season = None

    season_classes = None
    if has_season:
        season_classes = get_season_classes()
        if len(season_classes) == 0:
            print("No season found.")
            return

    if has_keyword:
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
        else:
            process_download(filtered_anime_classes)


def get_all_anime_classes(s_filter):
    if not isinstance(s_filter, SearchFilter):
        return TypeError("Unexpected type - Type is not SearchFilter")

    anime_classes = []
    subclasses = MainDownload.__subclasses__()
    for subclass in subclasses:
        if subclass.__name__ != "ExternalDownload" and subclass.season is not None:
            if s_filter.season is None or (s_filter.season is not None and subclass.season in s_filter.season):
                for subsubclass in subclass.__subclasses__():
                    if subsubclass.match(subsubclass, s_filter):
                        anime_classes.append(subsubclass)

    anime_classes.sort(key=lambda x: x.title)
    return anime_classes


def get_season_classes():
    season_classes = []
    subclasses = MainDownload.__subclasses__()
    for subclass in subclasses:
        if subclass.__name__ != "ExternalDownload" and subclass.season is not None:
            season_classes.append(subclass)
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
        print("%i - %s" % (i + 1, season_classes[i].season_name))
    return result_classes


def get_season_queries(season_classes):
    result = []
    for sc in season_classes:
        result.append(sc.season)
    return result


def print_anime_choice(anime_classes):
    result_classes = []
    for i in range(len(anime_classes)):
        print("%i - %s" % (i + 1, anime_classes[i].title))
    return result_classes


def filter_anime_classes(anime_classes, choices):
    result_classes = []
    choices = list(dict.fromkeys(choices)) # remove duplicates
    for choice in choices:
        if 0 < choice <= len(anime_classes):
            result_classes.append(anime_classes[choice - 1])
    return result_classes


if __name__ == "__main__":
    run()
    #classes = get_all_anime_classes(SearchFilter(query="", season="2020-2"))
    #print(classes)
