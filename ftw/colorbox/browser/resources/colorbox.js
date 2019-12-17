(function (factory) {
    // environment detection
    if (typeof define === 'function' && define.amd) {
        // AMD. require the modules we need
        require(['jquery', 'jquery_colorbox'], factory);
    } else {
        // Browser globals
        factory(window.jQuery, window.jQuery.fn.colorbox);
    }
}(function ($, colorbox) {
    "use strict";
    // Use $ and colorbox here
    $(document).on('cbox_complete', function () {
        var cboxTitle = $('#cboxTitle');

        if ($('#cboxCurrent').is(':visible')) {
            cboxTitle.css({'padding-left': '95px'});
        } else {
            cboxTitle.css({'padding-left': '20px'});
        }
    });
}));
