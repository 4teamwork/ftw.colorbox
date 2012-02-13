from ftw.colorbox import colorboxMessageFactory as _
from zope import schema
from zope.interface import Interface


class IColorboxSettings(Interface):
    """Interface for registry entries.
    """
    image_size = schema.Text(
        title=_(u'label_imagesize', default=u'Image size'),
        description=_(u'help_imagesize',
            default=u'Provide the name of an image size configured in the '
            'imaging control panel (e.g. large). If no size is given images '
            'will be displayed in original size.'),
        default=u'',
        required=False,
    )

    colorbox_config = schema.List(
        title=_(u'label_colorboxconfig', default=u'Colorbox config'),
        description=_(u'help_colorboxconfig',
            default=u'One item per line. For example speed:500.'),
        value_type=schema.TextLine(),
        default=[
            "'photo': true",
            "'current': '{current}/{total}'",
            "'maxWidth': '100%'",
            "'maxHeight': '100%'"])

    show_link = schema.Bool(
        title=_(u'label_showlink', default=u'Show link'),
        description=_(u'help_showlink',
            default=u'Should a link to the original?'),
        default=False)
