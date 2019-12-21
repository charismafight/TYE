function selectSection(a) {
    $("#aPic").attr("class", "btn btn-secondary");
    $("#aVideo").attr("class", "btn btn-secondary");

    $(a).attr("class", "btn btn-primary");

    $("#divPic").hide();
    $("#divVideo").hide();

    if ($(a).attr("id") == "aPic") {
        $("#divPic").show();
    } else {
        $("#divVideo").show();
    }
}