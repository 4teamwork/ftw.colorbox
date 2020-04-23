.. contents::

Introduction
============

ColorBox is a lightweight customizable lightbox plugin for jQuery. More
information about ColorBox can be found here:
http://jacklmoore.com/colorbox/

In Plone 4 ftw.colorbox also adds a view called `colorbox_view` for folders and topics
which provides a ColorBox gallery when images are clicked on.
The above view has been removed in Plone 5, though we are open to restoring it via a PR.

Caveat
======

As noted in `the colorbox source code <https://github.com/jackmoore/colorbox/blob/c78f880d17c19df3f29b8138df4dcc8afd364efd/jquery.colorbox.js#L467-L469>`_
you must ensure that colorbox's CSS is loaded before its JavaScript.


Configuration
=============

Configuration options are stored in the configuration registry
(plone.app.registry).

colorbox_config
  The options passed to the colorbox function (see ColorBox documentation for
  more details). Provide one option per line. Example::

    transition: "fade"
    speed: 250
    maxWidth: "90%"
    maxHeight: "90%"

The following configuration options ONLY apply to the `colorbox_view` on Plone 4.

image_size
  The name of an image size configured in the imaging control panel
  (e.g. large). If no size is given (default) images will be displayed in
  original size.

batch_size
  The number of thumbnails shown on a page. Default is 12.

row_size
  The number of images shown per row. If set to 0 (default) all images are
  floated in the same row.


Links
=====

- Github: https://github.com/4teamwork/ftw.colorbox
- Issues: https://github.com/4teamwork/ftw.colorbox/issues
- Pypi: http://pypi.python.org/pypi/ftw.colorbox


Copyright
=========

This package is copyright by `4teamwork <http://www.4teamwork.ch/>`_.

``ftw.colorbox`` is licensed under GNU General Public License, version 2.
