let $navbar = $('#navbar');
let $subdirs = $('#subdirs');
let $images = $('#images');
let $logs = $('#logs');
let $globalLogs = $('#global_logs');
let $audios = $('#audios');
let $videos = $('#videos');
let $footer = $('#footer');
let $imageSize = $('#imageSize');
let imageSize = '24';

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
                showDivs(obj);
            },
            400: function(xhr, status, error) {
                alert("Error - " + xhr.responseText);
            },
            404: function(xhr, status, error) {
                alert(xhr.responseText);
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
    $content = 'Sub-directories: ';
    if (dirs.length == 0)
    {
        return;
    }

    for (i = 0; i < dirs.length; i++)
    {
        if (i > 0)
            $content += " | ";
        $content += '<a href="#" onclick="getphp(\'' + dirs[i].path + '\')">' + dirs[i].name + '</a>';
    }
    $subdirs.html($content);
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
        $content += '<div class="container-log"><div class="container-filename">' + logs[i].name + '</div><iframe src="' + logs[i].path + '" title="' + logs[i].name + '" width="100%" height="300px"></iframe></div>';
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

let goToTop = function() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}

let hideDivs = function() {
    list = [$subdirs, $images, $logs, $audios, $videos, $footer];
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
    if (obj.images.length > 0 || obj.logs.length > 1 || obj.audios.length > 0 || obj.videos.length > 0)
        $footer.attr("hidden", false);
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

$(document).ready(function() {
    getphp('../download');
});
