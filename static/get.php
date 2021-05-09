<?php
    if (isset($_GET["dir"])) {
        $currDir = $_GET["dir"];
        $files = scandir($currDir);
        $parentDirs = array();
        $subDirs = array();
        $images = array();
        $imageTypes = array("jpg", "jpeg", "png", "gif", "webp");
        $logs = array();
        $logTypes = array("download.log", "news.log");
        foreach ($files as $file)
        {
            if (str_starts_with($file, '.'))
                continue;

            // Insert sub-directories
            $filepath = $currDir.'/'.$file;
            if (is_dir($filepath)) {
                array_push($subDirs, array("name"=>$file, "path"=>$filepath));
            }

            // Insert images
            foreach ($imageTypes as $imageType) {
                if (str_ends_with($file, '.'.$imageType))
                {
                    array_push($images, array("name"=>$file, "path"=>$filepath));
                }
            }

            // Logs
            foreach ($logTypes as $logType) {
                if ($file == $logType)
                {
                    array_push($logs, array("name"=>$file, "path"=>$filepath));
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

        $output = array("dir"=>array("current"=>array("name"=>$currDirName, "path"=>$currDir), "parent"=>$parentDirs, "sub"=>$subDirs), "images"=>$images, "logs"=>$logs);
        echo json_encode($output);
    } else {
        http_response_code(400);
    }
?>