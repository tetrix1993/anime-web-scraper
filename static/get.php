<?php
    if (isset($_GET["dir"])) {
        $currDir = $_GET["dir"];
        $testPaths = explode('..', $currDir);
        if (count($testPaths) != 2 || !str_starts_with($currDir, "../download"))
        {
            http_response_code(400);
        }

        $files = @scandir($currDir);
        $parentDirs = array();
        $subDirs = array();
        $images = array();
        $imageTypes = array("jpg", "jpeg", "png", "gif", "webp");
        $logs = array();
        $logTypes = array("download.log", "news.log");
        $audios = array();
        $audioTypes = array("mp3", "ogg", "wav");
        $videos = array();
        $videoTypes = array("mp4");
        $htmlFiles = array();
        $meta = new stdClass();

        $hasCheckMeta = false;
        foreach ($files as $file)
        {
            if (str_starts_with($file, '.'))
                continue;

            $stop = false;

            // Insert sub-directories
            $filepath = $currDir.'/'.$file;
            if (is_dir($filepath)) {
                array_push($subDirs, array("name"=>$file, "path"=>$filepath));
                continue;
            }

            // Insert images
            foreach ($imageTypes as $imageType) {
                if (str_ends_with($file, '.'.$imageType))
                {
                    array_push($images, array("name"=>$file, "path"=>$filepath));
                    $stop = true;
                    break;
                }
            }
            if ($stop)
                continue;

            // Logs
            foreach ($logTypes as $logType) {
                if ($file == $logType)
                {
                    $logname = "log_".explode('.log', $file)[0];
                    array_push($logs, array("name"=>$file, "logname"=>$logname, "path"=>$filepath));
                    $stop = true;
                    break;
                }
            }
            if ($stop)
                continue;

            // Audio
            foreach ($audioTypes as $audioType) {
                if (str_ends_with($file, '.'.$audioType))
                {
                    array_push($audios, array("name"=>$file, "path"=>$filepath));
                    $stop = true;
                    break;
                }
            }
            if ($stop)
                continue;

            // Video
            foreach ($videoTypes as $videoType) {
                if (str_ends_with($file, '.'.$videoType))
                {
                    array_push($videos, array("name"=>$file, "path"=>$filepath));
                    $stop = true;
                    break;
                }
            }
            if ($stop)
                continue;

            // HTML Sources
            if (str_ends_with($file, '.html')) {
                $htmlname = "html_".explode('.html', $file)[0];
                array_push($htmlFiles, array("name"=>$file, "htmlname"=>$htmlname, "path"=>$filepath));
            }
        }

        $dirSplits = explode('/', $currDir);
        $parentDir = "";
        $i = 0;
        foreach ($dirSplits as $dirSplit)
        {
            if (strlen($parentDir) > 0) {
                $parentDir = $parentDir."/";
            }
            $parentDir = $parentDir.$dirSplit;
            if ($dirSplit == "..")
                continue;
            $i++;
            if (!$hasCheckMeta && $i == 3) {
                if (file_exists($parentDir.'/log/meta.json'))
                    $meta = @json_decode(@file_get_contents($parentDir.'/log/meta.json'));
                $hasCheckMeta = true;
            }
            array_push($parentDirs, array("name"=>$dirSplit, "path"=>$parentDir));
        }
        $currDirName = $dirSplits[count($dirSplits) - 1];

        $output = array("dir"=>array("current"=>array("name"=>$currDirName, "path"=>$currDir), "parent"=>$parentDirs, "sub"=>$subDirs),
            "images"=>$images, "logs"=>$logs, "audios"=>$audios, "videos"=>$videos, "html"=>array_reverse($htmlFiles), "meta"=>$meta);
        echo @json_encode($output);
    } else {
        http_response_code(400);
    }
?>