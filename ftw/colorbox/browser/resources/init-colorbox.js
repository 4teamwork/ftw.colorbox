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

    var ftwColorboxInitialize = function () {
        var staticOptions = {
            'title': function () {
                var link = $(this);
                var title = link.attr('title');

                // Use the value from the attrib "data-caption" if there is one.
                var caption = link.data('caption');
                if (caption) {
                    title = caption;
                }

                return title;
            }
        }
        // The options stored in the Plone registry.
        var options = $('body').data('ftw-colorbox-options');
        $.extend(options, staticOptions)
        $('a.colorboxLink').colorbox(options);
    };

    ftwColorboxInitialize();

}));
