# Anime Web Scraper Developer Guide
Work in progress...
## Introduction
The Anime Web Scraper is a script that downloads images of previews of episodes and other contents from official anime websites.

## Download Classes
The program is structured by the `Download` classes, which contains logic to scrape the websites. The name of the `Download` classes ends with `Download`.

There are three inheritance levels for the structure of the program:
1. `MainDownload`
2. The season classes (e.g. `Winter2020AnimeDownload`), and `ExternalDownload`.
3. The anime classes (e.g. `TateNoYuushaDownload`) inherited from the season classes, and the external download classes (e.g. `AniverseMagazineDownload`) inherited from `ExternalDownload`.

All `Download` classes must be instantiated in order to use the methods in it, unless the method is a class method. In most cases, the classes must be instantiated.

## MainDownload Class
All `Download` classes inherits from the `MainDownload` classes which contains attributes and methods used by most `Download` classes. The class is found in the `main_download.py` file.

### Attributes
| Name | Type | Description |
| --- | --- | --- |
| folder_name | str | Name of the folder where files are to be saved |
| enabled | bool | If true, the anime classes will show up in search results. Default value is `True`. |
| image_list | list(dict) | List containing dictionary with image information (url, name). Not to be called directly. |
| keywords | list(str) | Keywords used as filters to search for the anime classes. |
| season | str | The season of the anime when it first started airing. Format: Year-Season, where Season: 1 - Winter, 2 - Spring, 3 - Summer, 4 - Fall. E.g. Winter 2020 is `2020-1`)
| season_name | str | Name of the season. E.g. `Winter 2020` |
| title | str | Anime title. Used by the anime classes. |

### Instance Methods
#### run
Main method to run the scraper logic in the class. All anime classes and external download classes must use this method.

#### download_image
Downloads image based on the image URL to the specific filepath without extension. This method also creates a log in the anime class's log folder, as well as `download_log.tsv` in the `out` folder.

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| url | str | Yes | URL of the image |
| filepath_without_extension | str | Yes | Filepath of the image to be saved to without extension |
| headers | dict | No | Headers used for HTTP GET request. Default value: `None` |
| to_jpg | bool | No | Converts image downloaded to jpg if the image is of type `image\webp`. Default value: `False` |
| is_mocanews | bool | No | Specify this to true if the image is from MocaNews website. Default value: `False` | 
| min_width | int | No | Downloads the image if its width is >= min_width. Default value: `None` |

#### has_website_updated
Checks if the website has updated by comparing the response size saved. Prints a message if updated and creates a log and a copy of the webpage in the `log` folder of the class.

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| url | str | Yes | URL of the website |
| cache_name | str | No | Name of the log containing the response size. Default value: `story` |
| headers | dict | No | Headers used for HTTP GET request. Default value: `None` |
| charset | str | No | Charset used by the website for decoding purposes. Default value: `None` |
| diff | int | No | Returns true if the difference between the size of the responses is greater than the value. Default value: `0` |

### Class Methods
#### get_full_path
Gets the path of the folder of the anime classes and external download classes where the files are saved. The filepath are based on the `folder_name` of the class and its parent classes.

For example, `TateNoYuushaDownload` class inherits from `Winter2019AnimeDownload` class, which also inherits from `MainDownload` class:

| Class | folder_name |
| --- | --- |
| TateNoYuushaDownload | tate-no-yuusha |
| Winter2019AnimeDownload | 2019-1 |
| MainDownload | download |

Executing `TateNoYuushaDownload.get_full_path()` will return `download/2019-1/tate-no-yuusha`.

### Static Methods
#### get_soup
Parse HTTP response of the url provided and returns a BeautifulSoup object.

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| url | str | Yes | URL of the website |
| headers | dict | No | Headers used for HTTP GET request. Default value: `None` |
| decode | bool | No | If true, decode the HTTP response. Default value: `False` |

#### get_json
Parse HTTP response into JSON object

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| url | str | Yes | URL of the website containing JSON |
| headers | dict | No | Headers used for HTTP GET request. Default value: `None` |

## Season Classes

## Anime Classes

## ExternalDownload Class

## External Download Classes

## Scan Classes

## SearchFilter Class

## Logging

## Others
### Migration

### Log Extractor
