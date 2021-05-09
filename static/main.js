let getphp = function(dir) {
    $.ajax({
        type: 'GET',
        url: 'static/get.php?dir=../' + dir,
        data: {},
        statusCode: {
            200: function(data) {
                console.log(data);
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

$(document).ready(function() {
    getphp('download');
});
