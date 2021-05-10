<?php
    if (isset($_GET["name"])) {
        $filepath = '../out/'.$_GET["name"].'_log.tsv';
        echo '<code>'.@nl2br(@file_get_contents($filepath)).'</code>';
    } else {
        http_response_code(400);
    }
?>
