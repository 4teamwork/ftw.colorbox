from zope.i18n import translate
from ftw.colorbox.interfaces import IColorboxSettings
from Products.Five.browser import BrowserView
from zope.component import getUtility
from plone.registry.interfaces import IRegistry
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class ColorBoxView(BrowserView):
    template = ViewPageTemplateFile('colorbox_view.pt')

    def __call__(self):
        registry = getUtility(IRegistry)
        self.settings = registry.forInterface(IColorboxSettings)
        return self.template()

    def image_title(self, image):
        """ Returns the image title and the link to the original file if
            'show_link' in registry is true.
        """
        title = [image.Title().decode('utf8')]
        if self.settings.show_link:
            title.append('<a href="%s/at_download/image">%s</a>' % (
                image.absolute_url(),
                translate(u'download',
                          domain='ftw.colorbox',
                          context=self.request)))
        return ' '.join(title)

    def init_colorbox(self):
        return """
            jQuery(function($) {
                jq('a.colorboxLink').colorbox({
                    %s
                });
            });
        """ % ','.join(self.settings.colorbox_config)

