# VSCodium Nautilus Extension
#
# Place me in ~/.local/share/nautilus-python/extensions/,
# ensure you have python-nautilus package, restart Nautilus, and enjoy :)
#
# This script is released to the public domain.

from gi.repository import Nautilus, GObject
from subprocess import call
import os

# path to vscodium
VSCODIUM = 'codium'

# what name do you want to see in the context menu?
VSCODIUMNAME = 'Codium'

# always create new window?
NEWWINDOW = False


class VSCodiumExtension(GObject.GObject, Nautilus.MenuProvider):

    def launch_vscodium(self, menu, files):
        safepaths = ''
        args = ''

        for file in files:
            filepath = file.get_location().get_path()
            safepaths += '"' + filepath + '" '

            # If one of the files we are trying to open is a folder
            # create a new instance of vscodium
            if os.path.isdir(filepath) and os.path.exists(filepath):
                args = '--new-window '

        if NEWWINDOW:
            args = '--new-window '

        call(VSCODIUM + ' ' + args + safepaths + '&', shell=True)

    def get_file_items(self, *args):
        files = args[-1]
        item = Nautilus.MenuItem(
            name='VSCodiumOpen',
            label='Open in ' + VSCODIUMNAME,
            tip='Opens the selected files with VSCodium'
        )
        item.connect('activate', self.launch_vscodium, files)

        return [item]

    def get_background_items(self, *args):
        file_ = args[-1]
        item = Nautilus.MenuItem(
            name='VSCodiumOpenBackground',
            label='Open in ' + VSCODIUMNAME,
            tip='Opens the current directory in VSCodium'
        )
        item.connect('activate', self.launch_vscodium, [file_])

        return [item]
