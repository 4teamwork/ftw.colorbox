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
                $('a.colorboxLink').colorbox({
                    %s
                });
            }
            jQuery(function($) {
                ftwColorboxInitialize();
            });
        """ % ','.join(settings.colorbox_config)
