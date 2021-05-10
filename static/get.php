<?php
    if (isset($_GET["dir"])) {
        $currDir = $_GET["dir"];
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
                    break;
                }
            }
        }

        $dirSplits = explode('/', $currDir);
        $parentDir = "";
        foreach ($dirSplits as $dirSplit)
        {
            if (strlen($parentDir) > 0) {
                $parentDir = $parentDir."/";
            }
            $parentDir = $parentDir.$dirSplit;
            if ($dirSplit == "..")
                continue;
            array_push($parentDirs, array("name"=>$dirSplit, "path"=>$parentDir));
        }
        $currDirName = $dirSplits[count($dirSplits) - 1];

        $output = array("dir"=>array("current"=>array("name"=>$currDirName, "path"=>$currDir), "parent"=>$parentDirs, "sub"=>$subDirs),
            "images"=>$images, "logs"=>$logs, "audios"=>$audios, "videos"=>$videos);
        echo @json_encode($output);
    } else {
        http_response_code(400);
    }
?>