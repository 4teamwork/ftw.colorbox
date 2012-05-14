from ftw.colorbox.interfaces import IColorboxSettings
from Products.Five.browser import BrowserView
from zope.component import getUtility
from plone.registry.interfaces import IRegistry


class InitColorBoxView(BrowserView):

    def __call__(self):
        registry = getUtility(IRegistry)
        settings = registry.forInterface(IColorboxSettings)
        return """
            jQuery(function($) {
                jq('a.colorboxLink').colorbox({
                    %s
                });
            });
        """ % ','.join(settings.colorbox_config)

