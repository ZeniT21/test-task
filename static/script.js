function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function(e) {
            $('.image-upload-wrap').hide();
            $('.file-upload-image').attr('src', e.target.result);
            $('.file-upload-content').show();
            $('.image-title').html(input.files[0].name);
        };
        reader.readAsDataURL(input.files[0]);
    } else {
        removeUpload();
    }
}

function removeUpload() {
    $('.file-upload-input').replaceWith($('.file-upload-input').clone());
    $('.file-upload-content').hide();
    $('.image-upload-wrap').show();
}
$().ready(function() {
    $('.image-upload-wrap').bind('dragover', function() {
        $('.image-upload-wrap').addClass('image-dropping');
    });
    $('.image-upload-wrap').bind('dragleave', function() {
        $('.image-upload-wrap').removeClass('image-dropping');
    });

    $(".upload-image").on('click', function() {
        const formData = new FormData();
        formData.append("file", $('.file-upload-input')[0].files[0], 'test');
        $.ajax({
            url: '/uploadfile/',
            type: 'post',
            data: formData,
            processData: false,
            contentType: false,
            success: function(data) {
                if (data) {
                    data = JSON.parse(data);
                    var str = '';
                    for (var key in data) {
                        str += key + ' ' + data[key] + '</br>';
                    }
                    $(".image-avarage").css("background", 'rgb(' + data['AvarageColor[RGB]'] + ')');
                } else {
                    var str = 'Not exif for this image';
                }
                $(".image-info").html(str);
            }
        });
    })
})