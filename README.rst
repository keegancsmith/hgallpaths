============
 hgallpaths
============

A mercurial extension to allow pushing and pulling from all paths specified in
the configuration.

Installation
============

Add hgallpaths extension to your ~/.hgrc::

  [extensions]
  hgallpaths = /path/to/hgallpaths.py

The list of all paths is available from the ``paths`` command::

  $ hg paths

You can exclude certain paths in the configuration. For example to always
exclude the path ``foo`` and ``bar``, as well as exclude ``baz`` when pushing
you add this to your ~/.hgrc (or repo hgrc)::

  [hgallpaths]
  exclude = foo bar
  exclude_push = baz

Usage
=====

The two commands supported at the moment are ``pushall`` and ``pullall``. For
example to push to all paths run::

  $ hg pushall
