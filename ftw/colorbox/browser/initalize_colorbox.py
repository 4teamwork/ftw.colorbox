from ftw.colorbox.interfaces import IColorboxSettings
from Products.Five.browser import BrowserView
from zope.component import getUtility
from plone.registry.interfaces import IRegistry


class InitColorBoxView(BrowserView):

    def __call__(self):
        registry = getUtility(IRegistry)
        settings = registry.forInterface(IColorboxSettings)
        return """
            var ftwColorboxInitialize = function() {
                var staticOptions = {
                    'title': function(){
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
                var options = {%s}  // The options stored in the Plone registry.
                $.extend(options, staticOptions)
                $('a.colorboxLink').colorbox(options);
            }
            jQuery(function($) {
                ftwColorboxInitialize();
            });
        """ % ','.join(settings.colorbox_config)
