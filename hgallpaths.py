# hgallpaths.py - pull and push too all paths
#
# Copyright 2012 Keegan Carruthers-Smith <keegan.csmith@gmail.com>
#
# This software may be used and distributed according to the terms of the
# GNU General Public License version 2 or any later version.

'''push and pull too all paths'''

from mercurial import commands

cmdtable = {}


def do_command(command, path_kw, ui, *args, **opts):
    cmd = getattr(commands, command)
    paths = ui.configitems('paths')
    exclude = set(ui.configlist('hgallpaths', 'exclude', []) +
                  ui.configlist('hgallpaths', 'exclude_%s' % command, []))

    for name, path in paths:
        if name not in exclude:
            opts[path_kw] = path
            cmd(ui, *args, **opts)


def create_command(command, path_kw):

    def cmd(*args, **opts):
        return do_command(command, path_kw, *args, **opts)

    cmd.__doc__ = 'See help for %s' % command

    global cmdtable
    cmdtable[command + 'all'] = (cmd, [])
    return cmd

pullall = create_command('pull', 'source')
pushall = create_command('push', 'dest')
