from ftw.colorbox import colorboxMessageFactory as _
from zope import schema
from zope.interface import Interface


class IColorboxLayer(Interface):
    """Request layer for ftw.colorbox
    """


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

    colorbox_exclude = schema.Text(
        title=_(u'label_colorbox_exclude', default=u'Colorbox Exclude'),
        description=_(u'help_colorbox_exlude',
            default=u'Javascript that runs inside a jquery '
                      '".not(function() { ... })" expression, where "this" is '
                      'the a.colorbox element. The expression has to '
                      'return either "true" for removing an item from the set '
                      'or "false" to keep an item in the set. An example would '
                      'bt to exlude certain classes: '
                      '"return $(this).hasClass(\'slick-cloned\');"'),
        default=u'return false;',
        required=False,
    )

    show_link = schema.Bool(
        title=_(u'label_showlink', default=u'Show link'),
        description=_(u'help_showlink',
            default=u'If enabled, a link to download the original image is '
                     'displayed in the overlay.'),
        default=False)

    row_size = schema.Int(
        title=_(u'label_row_size', default=u'Row Size'),
        description=_(u'help_row_size',
            default=u'The number of images shown per row. If set to 0 all '
                     'images are floated in the same row.'),
        default=0
    )

    batch_size = schema.Int(
        title=_(u'label_batch_size', default=u'Batch Size'),
        description=_(u'help_batch_size',
            default=u'The number of thumbnails shown on a page.'),
        default=12
    )
