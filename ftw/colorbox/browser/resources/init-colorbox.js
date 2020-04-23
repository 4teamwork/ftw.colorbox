(function (root, factory) {
    // environment detection
    if (typeof define === 'function' && define.amd) {
        // AMD. Register a module with required dependencies
        define(['jquery', 'jquery_colorbox'], function ($, colorbox) {
            // Also create a global in case some scripts (main.js in ftw.simplelayout)
            // that are loaded still are looking for
            // a global even when an AMD loader is in use.
            return (root.ftwColorboxInitialize = factory($, colorbox));
        });
    } else {
        // TODO delete the browser view implemented by 'colorbox_view.py' so that this
        // actually is used in Plone 4 !!

        // Browser globals
        // root.ftwColorboxInitialize = factory(window.jQuery, window.jQuery.fn.colorbox);
    }
}(typeof self !== 'undefined' ? self : this, function ($, colorbox) {
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

    $(document).ready(function() {
        ftwColorboxInitialize();
    });

    // For backwards compatibility in ftw.simplelayout we pass the function
    // (It would be more conventional to pass an object)
    return ftwColorboxInitialize;

}));
