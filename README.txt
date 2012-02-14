.. contents::

Introduction
============

ColorBox is a lightweight customizable lightbox plugin for jQuery. More
information about ColorBox can be found here:
http://jacklmoore.com/colorbox/

ftw.colorbox adds a new view called `colorbox_view` for folders and topics
which integrates ColorBox in Plone.

Configuration
=============

Configuration options are stored in the configuration registry
(plone.app.registry).

image_size
  The name of an image size configured in the imaging control panel
  (e.g. large). If no size is given (default) images will be displayed in
  original size.

batch_size
  The number of thumbnails shown on a page. Default is 12.

row_size
  The number of images shown per row. If set to 0 (default) all images are
  floated in the same row.

colorbox_config
  The options passed to the colorbox function (see ColorBox documentation for
  more details). Provide one option per line. Example::

    transition: "fade"
    speed: 250
    maxWidth: "90%"
    maxHeight: "90%"
