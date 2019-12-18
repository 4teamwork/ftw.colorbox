from ftw.colorbox.interfaces import IColorboxSettings
from plone.registry.interfaces import IRegistry
from Products.Five.browser import BrowserView
from zope.component import getUtility


# Generating JavaScript is not sustainable especially when we are now using AMD
# patterns. So we inject a data element into the body tag for Plone 5.
# Unfortunately this is not easy to replicate in Plone 4, so we leave the JS
# generation as is, knowing that Plone 4 isn't supported forever anyway.

class SettingsInjector(object):
    """
    Injects colorbox settings into the body tag borrowing technology from patternslib
    """

    def __init__(self, context, request, field):
        self.request = request
        self.context = context
        self.field = field

    def __call__(self):
        registry = getUtility(IRegistry)
        settings = registry.forInterface(IColorboxSettings)
        # Admittably horrible, but this is what we get from settings
        jsonized = "{%s}" % ",".join(settings.colorbox_config).replace('\'', '"')
        data = {
            'data-ftw-colorbox-options': jsonized
        }
        return(data)


# Plone 4 ONLY - this should be considered deprecated (see comment above)

class InitColorBoxView(BrowserView):

    def __call__(self):
        registry = getUtility(IRegistry)
        settings = registry.forInterface(IColorboxSettings)
        exclude_expression = settings.colorbox_exclude
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
                $('a.colorboxLink').not(function(){%s}).colorbox(options);
            }
            jQuery(function($) {
                ftwColorboxInitialize();
            });
        """ % (','.join(settings.colorbox_config), exclude_expression)
