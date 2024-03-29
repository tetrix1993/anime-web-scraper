let $navbar = $('#navbar');
let $subdirs = $('#subdirs');
let $additionalInfo = $('#additionalInfo');
let $title = $('#title');
let $twitterData = $('#twitter_data');
let $images = $('#images');
let $logs = $('#logs');
let $globalLogs = $('#global_logs');
let $audios = $('#audios');
let $videos = $('#videos');
let $htmlFiles = $('#html_files');
let $lastRun = $('#lastRun');
let $footer = $('#footer');
let $imageSize = $('#imageSize');
let imageSize = '24';

let additionalInfoVisible = true;

let getphp = function(dir) {
    hideDivs();
    $globalLogs.attr("hidden", (dir != '../download'));
    $.ajax({
        type: 'GET',
        url: 'static/get.php?dir=' + dir,
        data: {},
        statusCode: {
            200: function(data) {
                obj = JSON.parse(data);
                populateNavbar(obj.dir.parent);
                populateSubdirs(obj.dir.sub);
                populateImages(obj.images);
                populateLogs(obj.logs);
                populateAudios(obj.audios);
                populateVideos(obj.videos);
                populateHtmlFiles(obj.html);
                // Meta Data
                if ('title' in obj.meta)
                    populateTitle(obj.meta);
                if ('twitter' in obj.meta || 'hashtags' in obj.meta)
                    populateTwitterData(obj.meta.twitter, obj.meta.hashtags);
                if ('lastRun' in obj.meta)
                    populateLastRun(obj.meta.lastRun);
                showDivs(obj);
            },
            400: function(xhr, status, error) {
                alert("Error - 400 Bad Request");
            },
            404: function(xhr, status, error) {
                alert("Error - 404 Not Found");
            }
        }
    });
}

let populateNavbar = function(dirs) {
    $navbar.empty();
    $content = 'Filepath: ';
    for (i = 0; i < dirs.length; i++)
    {
        if (i > 0)
            $content += " > ";
        if (i == dirs.length - 1)
            $content += dirs[i].name;
        else
            $content += '<a href="#" onclick="getphp(\'' + dirs[i].path + '\')">' + dirs[i].name + '</a>';
    }
    $navbar.html($content);
}

let populateSubdirs = function(dirs) {
    $subdirs.empty();
    if (dirs.length == 0)
        return;
    $content = 'Sub-directories: ';

    for (i = 0; i < dirs.length; i++)
    {
        if (i > 0)
            $content += " | ";
        $content += '<a href="#" onclick="getphp(\'' + dirs[i].path + '\')">' + dirs[i].name + '</a>';
    }
    $subdirs.html($content);
}

let populateTitle = function(meta) {
    $title.empty();
    if (meta.title.length == 0)
        return;
    content = 'Title: '
    if ('website' in meta && meta.website.length > 0)
        content += '<a href="' + meta.website + '" target="_blank">' + meta.title + '</a>';
    else
        content += meta.title;
    $title.html(content);
}

let populateTwitterData = function(twitter, hashtags) {
    $twitterData.empty();
    if (hashtags.length == 0 || twitter.length == 0)
        return;
    content = 'Twitter: ';
    let twitterContent = '';
    let hashtagsContent = '';
    for (i = 0; i < twitter.length; i++)
    {
        if (i > 0)
            twitterContent += " ";
        twitterContent += '<a href="https://twitter.com/' + twitter[i] + '" target="_blank">@' + twitter[i] + '</a>';
    }
    for (i = 0; i < hashtags.length; i++)
    {
        if (i > 0)
            hashtagsContent += " ";
        hashtagsContent += '<a href="https://twitter.com/hashtag/' + hashtags[i] + '" target="_blank">#' + hashtags[i] + '</a>';
    }
    content += twitterContent;
    if (twitterContent.length > 0 && hashtagsContent.length > 0)
        content += " | ";
    content += hashtagsContent;
    $twitterData.html(content);
}

let populateImages = function(images) {
    $images.empty();
    $content = '<h2>Images</h2>';
    let class_name = 'container-image-50';
    if (imageSize == '100')
        class_name = 'container-image-100';
    else if (imageSize == '24')
        class_name = 'container-image-25';
    for (i = 0; i < images.length; i++)
    {
        $content += '<div class="container-image ' + class_name + '"><div class="container-filename">' + images[i].name + '</div><a href="' + images[i].path + '" target="_blank"><img class="image" title="' + images[i].name + '" src="' + images[i].path + '" alt="' + images[i].name + '" /></a></div>';
    }
    $images.html($content);
}

let populateLogs = function(logs) {
    $logs.empty();
    $content = '<h2>Logs</h2>';
    for (i = 0; i < logs.length; i++)
    {
        $content += '<div class="container-log"><div class="container-filename-log">' + logs[i].name + '</div><div class="container-button-log"><button onclick="reloadFrame(\'' + logs[i].logname + '\')">Reload</button></div><div class="container-button-log"><button onclick="scrollToTop(\'' + logs[i].logname + '\')">Scroll to Top</button></div><iframe id="' + logs[i].logname + '" src="../static/get_logs.php?dir=' + logs[i].path + '" title="' + logs[i].name + '" width="100%" height="300px"></iframe></div>';
    }
    $logs.html($content);
}

let populateAudios = function(audios) {
    $audios.empty();
    $content = '<h2>Audios</h2>';
    for (i = 0; i < audios.length; i++)
    {
        $content += '<div class="container-media"><div class="container-filename">' + audios[i].name + '</div><audio controls><source src="' + audios[i].path + '">Your browser does not support the audio element.</audio></div>';
    }
    $audios.html($content);
}

let populateVideos = function(videos) {
    $videos.empty();
    $content = '<h2>Videos</h2>';
    for (i = 0; i < videos.length; i++)
    {
        $content += '<div class="container-media"><div class="container-filename">' + videos[i].name + '</div><video controls><source src="' + videos[i].path + '">Your browser does not support HTML video.</video></div>';
    }
    $videos.html($content);
}

let populateHtmlFiles = function(htmlFiles) {
    $htmlFiles.empty();
    $content = '<h2>HTML Files</h2>';
    for (i = 0; i < htmlFiles.length; i++)
    {
        $content += '<div class="container-log"><div class="container-filename-log">' + htmlFiles[i].name + '</div><div class="container-button-log"><button onclick="loadFrame(\'' + htmlFiles[i].htmlname + '\')">Load</button></div><div id="' + htmlFiles[i].htmlname + '" data-src="' + htmlFiles[i].path + '"></div></div>';
    }
    $htmlFiles.html($content);
}

let populateLastRun = function(lastRun) {
    $lastRun.empty();
    if (lastRun.length == 0)
        return;
    let content = 'Last run: ' + lastRun;
    $lastRun.html(content);
}

let goToTop = function() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}

let scrollToTop = function(id) {
    $('#' + id).contents().scrollTop(0);
}

let hideDivs = function() {
    list = [$subdirs, $title, $twitterData, $images, $logs, $audios, $videos, $htmlFiles, $lastRun, $footer];
    for (i = 0; i < list.length; i++)
        hideDiv(list[i]);
}

let hideDiv = function($elem) {
    $elem.attr('hidden', true);
}

let showDivs = function(obj) {
    showDiv(obj.dir.sub, $subdirs);
    showDiv(obj.images, $images);
    showDiv(obj.logs, $logs);
    showDiv(obj.audios, $audios);
    showDiv(obj.videos, $videos);
    showDiv(obj.html, $htmlFiles);
    if (obj.images.length > 0 || obj.logs.length > 1 || obj.audios.length > 0 || obj.videos.length > 0 || obj.html.length > 1 ||
        (obj.logs.length > 0 && obj.html.length > 0))
        $footer.attr("hidden", false);

    // Meta Data
    if ('title' in obj.meta)
        $title.attr('hidden', false);
    if ('twitter' in obj.meta || 'hashtags' in obj.meta)
        $twitterData.attr('hidden', false);
    if ('lastRun' in obj.meta)
        $lastRun.attr('hidden', false);
}

let showDiv = function(list, $elem) {
    if (list.length > 0)
        $elem.attr('hidden', false);
}

let resizeImage = function() {
    if (imageSize == '49') {
        imageSize = '100';
        $imageSize.html('100');
    }
    else if (imageSize == '100') {
        imageSize = '24';
        $imageSize.html('25');
    }
    else {
        imageSize = '49';
        $imageSize.html('50');
    }
    $('.container-image').css('max-width', imageSize + '%');
}

let reloadFrame = function(id)
{
    document.getElementById(id).src = document.getElementById(id).src;
}

let loadFrame = function(id)
{
    $frame = $('#' + id);
    $frame.empty();
    $frame.html('<iframe src="../static/get_logs.php?dir=' + $frame.attr('data-src') + '" width="100%" height="300px"></iframe>');
}

let toggleInfo = function()
{
    if (additionalInfoVisible)
    {
        additionalInfoVisible = false;
        $additionalInfo.attr('hidden', true);
    }
    else
    {
        additionalInfoVisible = true;
        $additionalInfo.attr('hidden', false);
    }
}

$(document).ready(function() {
    getphp('../download');
});
