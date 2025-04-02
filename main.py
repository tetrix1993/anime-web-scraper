from multiprocessing import Process, Pool
from anime import *
import migrate


def run():
    migrate.run()
    update_global_logs()
    if not os.path.exists(constants.FOLDER_OUTPUT):
        os.makedirs(constants.FOLDER_OUTPUT)

    downloads = []
    # skip = [SalarymanShitennouDownload.__name__, NeetKunoichiDownload.__name__,
    #         BehenekoDownload.__name__, BotsurakuKizokuDownload.__name__]
    for subclass in Spring2025AnimeDownload.__subclasses__():
        downloads.append(subclass())
    downloads += [Kusuriya2Download(), AparidaDownload(), Kimisen2Download(), ShoshiminDownload(), Watakon2Download()]
    # for subclass in [GimaiSeikatsuDownload]:
    #     # if subclass.enabled and subclass.__name__ not in skip:
    #     if subclass.enabled:
    #         new_subclass = subclass()
    #         new_subclass.download_media_only = True
    #         downloads.append(new_subclass)
    subclasses = Summer2025AnimeDownload.__subclasses__()\
                 + UnconfirmedDownload.__subclasses__()
    for subclass in subclasses:
        if subclass.enabled:
            downloads.append(subclass())
    process_download(downloads)

    #downloads = []
    #subclasses = Winter2021AnimeDownload.__subclasses__() \
    #             + UnconfirmedDownload.__subclasses__()
    #for subclass in subclasses:
    #    downloads.append(subclass())
    #process_download(downloads)


def run_process(download, download_id):
    pid = str(os.getpid())
    download.download_id = download_id
    class_name = download.__class__.__name__
    filepath = constants.FOLDER_PROCESS + '/' + class_name
    message = "Running %s" % class_name
    if download.download_media_only:
        message += ' (Media)'
    elif download.guess_only:
        message += ' (Guess)'
    print(message)
    if os.path.exists(constants.FOLDER_PROCESS):
        with open(filepath, 'w+') as f:
            f.write(pid)
    if download.download_media_only:
        download.download_media()
    elif download.guess_only:
        download.download_episode_preview_guess()
    else:
        download.run()
    #print("Ending %s" % class_name)
    if os.path.exists(filepath):
        os.remove(filepath)


def run_process_function(fn):
    print("Running " + fn.__name__ + " (" + str(os.getpid()) + ")")
    fn()


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
                result = p.apply_async(run_process, (download, str(download_id).zfill(5)))
                results.append(result)
                download_id += 1
            for result in results:
                result.wait()
    else:
        run_process(downloads[0], '00001')

    update_global_logs()
    if len(os.listdir(constants.FOLDER_PROCESS)) == 0:
        os.rmdir(constants.FOLDER_PROCESS)

    #if len(downloads) % MAX_PROCESSES == 0:
    #    num_of_iterations = len(downloads) / MAX_PROCESSES
    #else:
    #    num_of_iterations = int(len(downloads) / MAX_PROCESSES) + 1

    #for i in range(num_of_iterations):
    #    processes = []
    #    max_index = min((i + 1) * MAX_PROCESSES, len(downloads))
    #    for download in downloads[(i * MAX_PROCESSES):max_index]:
    #        process = Process(target=run_process, args=(download,))
    #        processes.append(process)
    #        process.start()

    #    for process in processes:
    #        process.join()

    #processes = []
    #for download in downloads:
    #    process = Process(target=run_process, args=(download,))
    #    processes.append(process)
    #    process.start()
    
    #for process in processes:
    #    process.join()


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


def process_download_function(fns):
    processes = []
    for fn in fns:
        process = Process(target=run_process_function, args=(fn,))
        processes.append(process)
        process.start()
    
    for process in processes:
        process.join()


# region 2017 Anime
def download_spring_2017_anime():
    downloads = []

    downloads.append(AliceToZourokuDownload())
    downloads.append(BusouShoujoMachiavellismDownload())
    downloads.append(ClockworkPlanetDownload())
    downloads.append(EromangaSenseiDownload())
    downloads.append(HinakoNoteDownload())
    downloads.append(ReCreatorsDownload())
    downloads.append(RenaiBoukunDownload())
    downloads.append(RokuakaDownload())
    downloads.append(Saekano2Download())
    downloads.append(SakuradaResetDownload())
    downloads.append(SakuraQuestDownload())
    downloads.append(SukasukaDownload())
    downloads.append(SwordOratoriaDownload())
    downloads.append(ZeronosyoDownload())

    process_download(downloads)


def download_summer_2017_anime():
    downloads = []

    downloads.append(GamersDownload())
    downloads.append(IsesumaDownload())
    downloads.append(NewGame2Download())
    downloads.append(TenshiNo3PDownload())
    downloads.append(TsurezureChildrenDownload())
    downloads.append(YouzitsuDownload())

    process_download(downloads)


def download_fall_2017_anime():
    downloads = []

    downloads.append(AnimegatarisDownload())
    downloads.append(BlendSDownload())
    downloads.append(ImotosaeDownload())
    downloads.append(KonohanaKitanDownload())
    downloads.append(ShoujoShuumatsuRyokouDownload())

    process_download(downloads)
# endregion

# region 2018 Anime
def download_winter_2018_anime():
    downloads = []
    
    downloads.append(BeatlessDownload())
    downloads.append(DarlingInTheFranxxDownload())
    downloads.append(DeathMarchDownload())
    downloads.append(GrancrestSenkiDownload())
    downloads.append(HakumikoDownload())
    downloads.append(MarchenMadchenDownload())
    downloads.append(MitsuboshiColorsDownload())
    downloads.append(Overlord2Download())
    downloads.append(PopTeamEpicDownload())
    downloads.append(RamenKoizumiDownload())
    downloads.append(RyuohDownload())
    downloads.append(SlowStartDownload())
    downloads.append(TakagisanDownload())
    downloads.append(TojiNoMikoDownload())
    downloads.append(YorimoiDownload())
    downloads.append(YuruCampDownload())
    
    process_download(downloads)


def download_spring_2018_anime():
    downloads = []
    
    downloads.append(AliceOrAliceDownload())
    downloads.append(Amanchu2Download())
    downloads.append(ComicGirlsDownload())
    downloads.append(GunGaleOnlineDownload())
    downloads.append(GoldenKamuyDownload())
    downloads.append(HinamatsuriDownload())
    downloads.append(HisomasoDownload())
    downloads.append(LastPeriodDownload())
    downloads.append(LostorageConflatedWixossDownload())
    downloads.append(TadakoiDownload())
    downloads.append(WotakoiDownload())
    
    process_download(downloads)


def download_summer_2018_anime():
    downloads = []
    
    downloads.append(AngolmoisDownload())
    downloads.append(AsobiAsobaseDownload())
    downloads.append(ChioChanDownload())
    downloads.append(GrandBlueDownload())
    downloads.append(HanebadoDownload())
    downloads.append(HappySugarLifeDownload())
    downloads.append(HarukanaReceiveDownload())
    downloads.append(HatarakuSaibouDownload())
    downloads.append(HiScoreGirlDownload())
    downloads.append(HyakurenDownload())
    downloads.append(IsekaiMaouDownload())
    downloads.append(IslandDownload())
    downloads.append(Overlord3Download())
    downloads.append(SatsurikuDownload())
    downloads.append(ShichiseiNoSubaruDownload())
    downloads.append(TsukumogamiDownload())
    downloads.append(YuragisouDownload())
    
    process_download(downloads)


def download_fall_2018_anime():
    downloads = []
    
    downloads.append(AkanesasuShoujoDownload())
    downloads.append(AnimaYellDownload())
    downloads.append(AobutaDownload())
    downloads.append(BeelmamaDownload())
    downloads.append(ConceptionDownload())
    downloads.append(GoblinSlayerDownload())
    downloads.append(GoldenKamuy2Download())
    downloads.append(HangyakuseiMillionArthurDownload())
    downloads.append(ImoimoDownload())
    downloads.append(IrodukuDownload())
    downloads.append(KishukuJulietDownload())
    downloads.append(MercStoriaDownload())
    downloads.append(ReleaseTheSpyceDownload())
    downloads.append(SoraumiDownload())
    downloads.append(SsssGridmanDownload())
    downloads.append(TensuraDownload())
    downloads.append(TonariNoKyuuketsukiSanDownload())
    downloads.append(UlyssesDownload())
    downloads.append(UzamaidDownload())
    
    process_download(downloads)

# endregion

# region 2019 Anime
def download_winter_2019_anime():
    downloads = []
    
    downloads.append(CircletPrincessDownload())
    downloads.append(DateALive3Download())
    downloads.append(DomeKanoDownload())
    downloads.append(EgaoNoDaikaDownload())
    downloads.append(EndroDownload())
    downloads.append(GirlyAirForceDownload())
    downloads.append(GotoubunDownload())
    downloads.append(GrimmsNotesDownload())
    downloads.append(KaguyasamaDownload())
    downloads.append(MahouShoujoTokushusenAsukaDownload())
    downloads.append(MiniTojiDownload())
    downloads.append(PastelMemoriesDownload())
    downloads.append(TateNoYuushaDownload())
    downloads.append(WatatenDownload())
    
    process_download(downloads)


def download_spring_2019_anime():
    downloads = []
    
    downloads.append(BokubenDownload())
    downloads.append(ChoukadouGirlDownload())
    downloads.append(HachinaiDownload())
    downloads.append(HangyakuseiMillionArthur2Download())
    downloads.append(HitoribocchiDownload())
    downloads.append(IsekaiQuartetDownload())
    downloads.append(KenjaNoMagoDownload())
    downloads.append(MidaraNaAochanDownload())
    downloads.append(NankokoDownload())
    downloads.append(NobutsumaDownload())
    downloads.append(SenkosanDownload())
    downloads.append(SenryuuShoujoDownload())
    downloads.append(YatogameDownload())
    downloads.append(YunoDownload())
    
    process_download(downloads)


def download_summer_2019_anime():
    downloads = []
    
    downloads.append(ArifuretaDownload())
    downloads.append(DumbbellDownload())
    downloads.append(GranbelmDownload())
    downloads.append(HensukiDownload())
    downloads.append(IsekaiCheatDownload())
    downloads.append(JyoshimudaDownload())
    downloads.append(KanataNoAstraDownload())
    downloads.append(MachikadoMazokuDownload())
    downloads.append(MaousamaRetryDownload())
    downloads.append(OkaasanOnlineDownload())
    downloads.append(SounanDesukaDownload())
    downloads.append(TejinaDownload())
    downloads.append(UchinokoDownload())
    downloads.append(YunoDownload())
    
    downloads.append(AniverseMagazineDownload("34869", "2019-3/arifureta_aniverse", 13, 8))
    
    process_download(downloads)


def download_fall_2019_anime():
    downloads = []
    
    downloads.append(AssassinsPrideDownload())
    downloads.append(Bokuben2Download())
    downloads.append(ChoyoyuDownload())
    downloads.append(HiScoreGirl2Download())
    downloads.append(HonzukiDownload())
    downloads.append(IrumaKunDownload())
    downloads.append(KandagawaJetGirlsDownload())
    downloads.append(KemonomichiDownload())
    downloads.append(NoukinDownload())
    downloads.append(NullPetaDownload())
    downloads.append(OresukiDownload())
    downloads.append(RifleIsBeautifulDownload())
    downloads.append(SaikoroDownload())
    downloads.append(ShinchouYuushaDownload())
    downloads.append(ValLoveDownload())
    
    downloads.append(WebNewtypeDownload("208294", "2019-4/assassins-pride_wnt", 1))
    downloads.append(WebNewtypeDownload("208880", "2019-4/assassins-pride_wnt", 2))
    downloads.append(WebNewtypeDownload("209704", "2019-4/assassins-pride_wnt", 3))
    downloads.append(WebNewtypeDownload("210703", "2019-4/assassins-pride_wnt", 4))
    downloads.append(WebNewtypeDownload("211398", "2019-4/assassins-pride_wnt", 5))
    downloads.append(WebNewtypeDownload("212209", "2019-4/assassins-pride_wnt", 6))
    downloads.append(WebNewtypeDownload("213070", "2019-4/assassins-pride_wnt", 7))
    downloads.append(WebNewtypeDownload("213790", "2019-4/assassins-pride_wnt", 8))
    downloads.append(WebNewtypeDownload("214863", "2019-4/assassins-pride_wnt", 9))
    downloads.append(WebNewtypeDownload("215815", "2019-4/assassins-pride_wnt", 10))
    downloads.append(WebNewtypeDownload("216713", "2019-4/assassins-pride_wnt", 11))
    downloads.append(WebNewtypeDownload("217804", "2019-4/assassins-pride_wnt", 12))
    
    downloads.append(WebNewtypeDownload("208291", "2019-4/choyoyu_wnt", 3))
    downloads.append(WebNewtypeDownload("209067", "2019-4/choyoyu_wnt", 4))
    downloads.append(WebNewtypeDownload("209944", "2019-4/choyoyu_wnt", 5))
    downloads.append(WebNewtypeDownload("210865", "2019-4/choyoyu_wnt", 6))
    downloads.append(WebNewtypeDownload("211645", "2019-4/choyoyu_wnt", 7))
    downloads.append(WebNewtypeDownload("212481", "2019-4/choyoyu_wnt", 8))
    
    downloads.append(MocaNewsDownload("20191003/2019100323000a_", "2019-4/choyoyu-moca", 2))
    downloads.append(MocaNewsDownload("20191010/2019101023000a_", "2019-4/choyoyu-moca", 3))
    downloads.append(MocaNewsDownload("20191017/2019101723000a_", "2019-4/choyoyu-moca", 4))
    downloads.append(MocaNewsDownload("20191024/2019102423000a_", "2019-4/choyoyu-moca", 5))
    downloads.append(MocaNewsDownload("20191031/2019103123000a_", "2019-4/choyoyu-moca", 6))
    downloads.append(MocaNewsDownload("20191107/2019110723000a_", "2019-4/choyoyu-moca", 7))
    downloads.append(MocaNewsDownload("20191114/2019111423000a_", "2019-4/choyoyu-moca", 8))
    downloads.append(MocaNewsDownload("20191121/2019112123000a_", "2019-4/choyoyu-moca", 9))
    downloads.append(MocaNewsDownload("20191129/2019112911010a_", "2019-4/choyoyu-moca", 10))
    downloads.append(MocaNewsDownload("20191205/2019120523000a_", "2019-4/choyoyu-moca", 11))
    downloads.append(MocaNewsDownload("20191212/2019121223000a_", "2019-4/choyoyu-moca", 12))
    
    downloads.append(WebNewtypeDownload("205490", "2019-4/honzuki_wnt", 1))
    downloads.append(WebNewtypeDownload("208052", "2019-4/honzuki_wnt", 2))
    downloads.append(WebNewtypeDownload("208957", "2019-4/honzuki_wnt", 3))
    downloads.append(WebNewtypeDownload("209711", "2019-4/honzuki_wnt", 4))
    downloads.append(WebNewtypeDownload("210697", "2019-4/honzuki_wnt", 5))
    downloads.append(WebNewtypeDownload("210860", "2019-4/honzuki_wnt", 6))
    downloads.append(WebNewtypeDownload("211508", "2019-4/honzuki_wnt", 7))
    downloads.append(WebNewtypeDownload("212358", "2019-4/honzuki_wnt", 8))
    downloads.append(WebNewtypeDownload("213152", "2019-4/honzuki_wnt", 9))
    
    downloads.append(MocaNewsDownload("20191009/2019100922300a_", "2019-4/honzuki-moca", 2))
    downloads.append(MocaNewsDownload("20191016/2019101622300a_", "2019-4/honzuki-moca", 3))
    downloads.append(MocaNewsDownload("20191023/2019102322300a_", "2019-4/honzuki-moca", 4))
    downloads.append(MocaNewsDownload("20191030/2019103022300a_", "2019-4/honzuki-moca", 5))
    downloads.append(MocaNewsDownload("20191031/2019103111000a_", "2019-4/honzuki-moca", 6))
    downloads.append(MocaNewsDownload("20191107/2019110711000a_", "2019-4/honzuki-moca", 7))
    downloads.append(MocaNewsDownload("20191114/2019111411000a_", "2019-4/honzuki-moca", 8))
    downloads.append(MocaNewsDownload("20191121/2019112111000a_", "2019-4/honzuki-moca", 9))
    downloads.append(MocaNewsDownload("20191128/2019112811000a_", "2019-4/honzuki-moca", 10))
    downloads.append(MocaNewsDownload("20191205/2019120511000a_", "2019-4/honzuki-moca", 11))
    downloads.append(MocaNewsDownload("20191212/2019121211000a_", "2019-4/honzuki-moca", 12))
    downloads.append(MocaNewsDownload("20191219/2019121911000a_", "2019-4/honzuki-moca", 13_14))
    
    downloads.append(WebNewtypeDownload("207655", "2019-4/noukin_wnt", 1))
    downloads.append(WebNewtypeDownload("208297", "2019-4/noukin_wnt", 2))
    downloads.append(WebNewtypeDownload("209168", "2019-4/noukin_wnt", 3))
    downloads.append(WebNewtypeDownload("209900", "2019-4/noukin_wnt", 4))
    downloads.append(WebNewtypeDownload("210867", "2019-4/noukin_wnt", 5))
    downloads.append(WebNewtypeDownload("211518", "2019-4/noukin_wnt", 6))
    downloads.append(WebNewtypeDownload("212512", "2019-4/noukin_wnt", 7))
    downloads.append(WebNewtypeDownload("213132", "2019-4/noukin_wnt", 8))
    downloads.append(WebNewtypeDownload("214252", "2019-4/noukin_wnt", 9))
    downloads.append(WebNewtypeDownload("215231", "2019-4/noukin_wnt", 10))
    downloads.append(WebNewtypeDownload("215904", "2019-4/noukin_wnt", 11))
    downloads.append(WebNewtypeDownload("216980", "2019-4/noukin_wnt", 12))
    
    downloads.append(WebNewtypeDownload("210195", "2019-4/hi-score-girl_wnt", 16))
    downloads.append(WebNewtypeDownload("211041", "2019-4/hi-score-girl_wnt", 17))
    downloads.append(WebNewtypeDownload("211749", "2019-4/hi-score-girl_wnt", 18))
    downloads.append(WebNewtypeDownload("213526", "2019-4/hi-score-girl_wnt", 20))
    
    downloads.append(MocaNewsDownload("20191126/2019112622130a_", "2019-4/shinchou-yuusha-moca", 8))
    downloads.append(MocaNewsDownload("20191203/2019120322270a_", "2019-4/shinchou-yuusha-moca", 9))
    
    process_download(downloads)

# endregion

# region 2020 Anime
def download_winter_2020_anime():
    downloads = []
    
    #downloads.append(BofuriDownload())
    #downloads.append(DarwinsGameDownload())
    #downloads.append(EizoukenDownload())
    #downloads.append(HatenaIllusionDownload())
    #downloads.append(HeyaCampDownload())
    #downloads.append(InfiniteDendrogramDownload())
    #downloads.append(IsekaiQuartet2Download())
    #downloads.append(IshuzokuReviewersDownload())
    #downloads.append(HanakoKunDownload())
    #downloads.append(KoisuruAsteroidDownload())
    #downloads.append(KyokouSuiriDownload())
    #downloads.append(MurenaseSetonGakuenDownload())
    #downloads.append(NekoparaDownload())
    #downloads.append(OshibudoDownload())
    downloads.append(PlundererDownload())
    downloads.append(RailgunTDownload())
    #downloads.append(RailgunTDownload2())
    #downloads.append(RikekoiDownload())
    #downloads.append(RunwayDeWaratteDownload())
    #downloads.append(SomaliDownload())
    
    #downloads.append(MocaNewsDownload("20191225/2019122518000c_", "2020-1/heya-camp-moca", 1))
    
    #downloads.append(WebNewtypeDownload("219613", "2020-1/nekopara-wnt", 2))
    #downloads.append(WebNewtypeDownload("220518", "2020-1/nekopara-wnt", 3))
    #downloads.append(WebNewtypeDownload("228317", "2020-1/nekopara-wnt", 12))
    
    process_download(downloads)


def download_spring_2020_anime():
    downloads = []

    downloads.append(ArteDownload())
    downloads.append(BrandNewAnimalDownload())
    downloads.append(GleipnirDownload())
    downloads.append(HachinanDownload())
    downloads.append(HamehuraDownload())
    downloads.append(Honzuki2Download())
    downloads.append(Kaguyasama2Download())
    downloads.append(KakushigotoDownload())
    downloads.append(Kingdom3Download())
    downloads.append(NamiyoDownload())
    downloads.append(PriconneDownload())
    downloads.append(ShachibatoDownload())
    downloads.append(TamayomiDownload())
    downloads.append(TeiboDownload())
    downloads.append(Tsugumomo2Download())
    downloads.append(YesterdayDownload())
    
    #downloads.append(MocaNewsDownload("20200329/2020032917000a_", "2020-2/arte-moca", 1))
    
    #downloads.append(MocaNewsDownload("20200306/2020030612000a_", "2020-2/honzuki2-moca", 15))
    #downloads.append(MocaNewsDownload("20200406/2020040612000a_", "2020-2/honzuki2-moca", 16))
    #downloads.append(MocaNewsDownload("20200413/2020041312000a_", "2020-2/honzuki2-moca", 17))
    #downloads.append(MocaNewsDownload("20200420/2020042012000a_", "2020-2/honzuki2-moca", 18))

    #downloads.append(WebNewtypeDownload("228052", "2020-2/priconne-wnt", 1))

    #downloads.append(MocaNewsDownload("20200325/2020032518220a_", "2020-2/tamayomi-moca", 1))
    
    process_download(downloads)


def download_summer_2020_anime():
    downloads = []

    subclasses = Summer2020AnimeDownload.__subclasses__()
    for subclass in subclasses:
        downloads.append(subclass())

    #downloads.append(HxErosDownload())
    #downloads.append(KanokariDownload())
    #downloads.append(MaohgakuinDownload())
    #downloads.append(MonIshaDownload())
    #downloads.append(OchifuruDownload())
    #downloads.append(Oregairu3Download())
    #downloads.append(PeterGrillDownload())
    #downloads.append(ReZero2Download())
    #downloads.append(UzakiChanDownload())

    process_download(downloads)
# endregion

def download_all():
    fns = []
    fns.append(download_spring_2017_anime)
    fns.append(download_summer_2017_anime)
    fns.append(download_fall_2017_anime)
    fns.append(download_winter_2018_anime)
    fns.append(download_spring_2018_anime)
    fns.append(download_summer_2018_anime)
    fns.append(download_fall_2018_anime)
    fns.append(download_winter_2019_anime)
    fns.append(download_spring_2019_anime)
    fns.append(download_summer_2019_anime)
    fns.append(download_fall_2019_anime)
    fns.append(download_winter_2020_anime)
    fns.append(download_spring_2020_anime)
    fns.append(download_summer_2020_anime)
    
    process_download_function(fns)


if __name__ == '__main__':
    run()
    #download_all()

    #download_spring_2017_anime()
    #download_summer_2017_anime()
    #download_fall_2017_anime()

    #download_winter_2018_anime()
    #download_spring_2018_anime()
    #download_summer_2018_anime()
    #download_fall_2018_anime()
    
    #download_winter_2019_anime()
    #download_spring_2019_anime()
    #download_summer_2019_anime()
    #download_fall_2019_anime()
    
    #download_winter_2020_anime()
    #download_spring_2020_anime()
    #download_summer_2020_anime()
    
    print("Download completed")

