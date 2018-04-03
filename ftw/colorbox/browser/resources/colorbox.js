$(document).on('cbox_complete', function(){
    var cboxTitle = $('#cboxTitle');

    if ($('#cboxCurrent').is(':visible')) {
        cboxTitle.css({'padding-left': '95px'});
    } else {
        cboxTitle.css({'padding-left': '20px'});
    }
});
