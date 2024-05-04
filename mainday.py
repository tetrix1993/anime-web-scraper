from anime import *
import migrate
import datetime
import main


DAY_MONDAY = 0
DAY_TUESDAY = 1
DAY_WEDNESDAY = 2
DAY_THURSDAY = 3
DAY_FRIDAY = 4
DAY_SATURDAY = 5
DAY_SUNDAY = 6


def run():
    migrate.run()
    main.update_global_logs()
    if not os.path.exists(constants.FOLDER_OUTPUT):
        os.makedirs(constants.FOLDER_OUTPUT)

    downloads = []
    day_of_week = datetime.datetime.today().weekday()
    if day_of_week == DAY_MONDAY:
        print('MONDAY')
        downloads += [Konosuba3Download(), DungeonMeshiDownload()]
    elif day_of_week == DAY_TUESDAY:
        print('TUESDAY')
        downloads += [Lv2CheatDownload(), HensaraDownload(), UruseiYatsura2Download(), Mahouka3Download()]
    elif day_of_week == DAY_WEDNESDAY:
        print('WEDNESDAY')
        downloads += [YorukuraDownload(), UnnamedMemoryDownload(), MushokuTensei2Download()]
    elif day_of_week == DAY_THURSDAY:
        print('THURSDAY')
        downloads += [SeiyuRadioDownload(), TsukimichiDownload(), Maohgakuin2Download(), JisanBasanDownload(),
                      TheNewGateDownload(), Kaiju8Download()]
    elif day_of_week == DAY_FRIDAY:
        print('FRIDAY')
        downloads += [TenseiKizokuDownload(), YuruCamp3Download(), HibikiEuphonium3Download(), KamiueDownload(),
                      DainanaojiDownload()]
    elif day_of_week == DAY_SATURDAY:
        print('SATURDAY')
        downloads += [SasakoiDownload(), YozakurasanDownload(), OokamitoKoushinryouDownload()]
    elif day_of_week == DAY_SUNDAY:
        print('SUNDAY')
        downloads += [ReMonsterDownload(), ShinigamiBocchan3Download()]
    main.process_download(downloads)


if __name__ == '__main__':
    run()
    print("Download completed")

