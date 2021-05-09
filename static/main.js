let $navbar = $('#navbar');
let $subdirs = $('#subdirs');
let $images = $('#images');
let $logs = $('#logs');
let $btnTop = $('#btnTop');

let getphp = function(dir) {
    $btnTop.attr("hidden", true);
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
                if (obj.images.length > 0 || obj.logs.length > 1)
                    $btnTop.attr("hidden", false);
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
    $content = '';
    for (i = 0; i < images.length; i++)
    {
        $content += '<img class="image" title="' + images[i].name + '" src="' + images[i].path + '" alt="' + images[i].name + '" />';
    }
    $images.html($content);
}

let populateLogs = function(logs) {
    $logs.empty();
    $content = '';
    for (i = 0; i < logs.length; i++)
    {
        $content += '<h3>' + logs[i].name + '</h3><iframe src="' + logs[i].path + '" title="' + logs[i].name + '" width="100%" height="300px"></iframe>';
    }
    $logs.html($content);
}

let goToTop = function() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}

$(document).ready(function() {
    getphp('../download');
});
