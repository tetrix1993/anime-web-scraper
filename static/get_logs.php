<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Content Viewer Logs</title>
</head>
<body style="background-color: #dddddd;">
<?php
    if (isset($_GET["name"])) {
        $filepath = '../out/'.$_GET["name"].'_log.tsv';
        echo '<pre style="word-wrap: break-word; line-height: 0.6em;">';
        echo @nl2br(@file_get_contents($filepath));
        echo '</pre><script src="global_log.js"></script>';
    }
    elseif (isset($_GET["dir"]) && str_ends_with($_GET["dir"], '.html')) {
        $filepath = $_GET["dir"];
        echo '<pre style="word-wrap: break-word; line-height: 1em;">';
        echo @htmlspecialchars(@file_get_contents($filepath));
        echo '</pre>';
    }
    elseif (isset($_GET["dir"])) {
        $filepath = $_GET["dir"];
        echo '<pre style="word-wrap: break-word; line-height: 0.6em;">';
        echo @nl2br(@file_get_contents($filepath));
        echo '</pre><script src="global_log.js"></script>';
    }
    else {
        http_response_code(400);
    }
?>
</body>
</html>
