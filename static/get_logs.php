<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Content Viewer Logs</title>
</head>
<body style="background-color: #dddddd;">
<pre style="word-wrap: break-word; line-height: 0.6em;"><?php
    if (isset($_GET["name"])) {
        $filepath = '../out/'.$_GET["name"].'_log.tsv';
        echo @nl2br(@file_get_contents($filepath));
    }
    elseif (isset($_GET["dir"])) {
        $filepath = $_GET["dir"];
        echo @nl2br(@file_get_contents($filepath));
    }
    else {
        http_response_code(400);
    }
?></pre>
</body>
</html>
