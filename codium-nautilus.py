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
VSCODIUMNAME = 'VSCodium'

# always create new window?
NEWWINDOW = False

lang = os.environ.get("LANG")
label = ""
if "zh" in lang:
    label = '在 ' + VSCODIUMNAME + ' 中打开'
    tip_files = '用 VSCodium 打开所选择的文件'
    tip_backgroud = '在 VSCodium 中打开当前目录'

elif "tr" in lang:
    label = VSCODIUMNAME + '\'da aç'
    tip_files = 'Seçilen dosyaları VSCodium ile açar'
    tip_backgroud = 'Anlık dizini VSCodium ile açar'

else:
    label = 'Open in ' + VSCODIUMNAME
    tip_files = 'Opens the selected files in VSCodium'
    tip_backgroud = 'Opens the current directory in VSCodium'


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
        item = Nautilus.MenuItem(
            name='VSCodiumOpen',
            label=label,
            tip=tip_files
        )
        item.connect('activate', self.launch_vscodium, files)

        return [item]

    def get_background_items(self, *args):
        file_ = args[-1]
        item = Nautilus.MenuItem(
            name='VSCodiumOpenBackground',
            label=label,
            tip=tip_files
        )
        item.connect('activate', self.launch_vscodium, [file_])

        return [item]
