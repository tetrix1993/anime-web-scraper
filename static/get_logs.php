<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Content Viewer Logs</title>
</head>
<body style="background-color: #dddddd;">
<pre style="word-wrap: break-word; line-height: 1.1em;">
<?php
    if (isset($_GET["name"])) {
        $filepath = '../out/'.$_GET["name"].'_log.tsv';
        //echo @nl2br(@file_get_contents($filepath));
        echo @htmlspecialchars(@file_get_contents($filepath));
        echo '</pre><script src="global_log.js"></script>';
    }
    elseif (isset($_GET["dir"]) && str_ends_with($_GET["dir"], '.html')) {
        $filepath = $_GET["dir"];
        echo @htmlspecialchars(@file_get_contents($filepath));
        echo '</pre>';
    }
    elseif (isset($_GET["dir"])) {
        $filepath = $_GET["dir"];
        echo @htmlspecialchars(@file_get_contents($filepath));
        echo '</pre><script src="global_log.js"></script>';
    }
    else {
        http_response_code(400);
    }
?>
</body>
</html>
