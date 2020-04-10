from anime import *
import requests

def run():
    pass
    #ShachibatoDownload().run()
    #MocaNewsDownload("20200405/2020040500010a_", "2020-2/kaguyasama2-moca", 1).run()
    #MocaNewsDownload("20200407/2020040720000a_", "2020-2/kakushigoto-moca", 2).run()
    #TeiboDownload().run()
    #GleipnirDownload().run()

    # https://kakushigoto-anime.com/wp/wp-content/uploads/2020/03/th_01_0011.jpg
    #TEMPLATE_URL = 'https://kakushigoto-anime.com/wp/wp-content/uploads/2020/%s/th_%s_%s.%s'
    #file_type = ['jpg', 'png']
    #for i in range(4, 5, 1):
    #    for j in range(2, 3, 1):
    #        for k in range(0, 201, 1):
    #            for l in range(len(file_type)):
    #                url = TEMPLATE_URL % (str(i).zfill(2), str(j).zfill(2), str(k).zfill(4), file_type[l])
    #                print(str(i) + ' ' + str(j) + ' ' + str(k) + ' ' + file_type[l])
    #                r = requests.get(url)
    #                if r.status_code != 404:
    #                    print('Success: ' + url)
    #NamiyoDownload().run()
    YesterdayDownload().run()


if __name__ == "__main__":
    run()
