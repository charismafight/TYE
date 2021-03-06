function selectSection(a) {
    $("#aPic").attr("class", "btn btn-secondary");
    $("#aVideo").attr("class", "btn btn-secondary");

    $(a).attr("class", "btn btn-primary");

    $("#divPic").hide();
    $("#divVideo").hide();

    if ($(a).attr("id") == "aPic") {
        $("#divPic").show();
        //暂停播放视频
        $('video').trigger("pause");
        $('video').removeClass('play');
    } else {
        $("#divVideo").show();
    }
}

$(function () {
    //video play
    $('video').click(function () {
        if ($(this).hasClass('pause')) {
            $(this).trigger("play");
            $(this).removeClass('pause');
            $(this).addClass('play');
        } else {
            $(this).trigger("pause");
            $(this).removeClass('play');
            $(this).addClass('pause');
        }
    });
});