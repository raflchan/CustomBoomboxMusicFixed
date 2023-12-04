from subprocess import run
from zipfile import ZipFile

BUILD_COMMAND =  'msbuild ./CustomBoomboxMusicFixed.sln  -t:Rebuild -p:Configuration=Release'


run(BUILD_COMMAND, shell=True, check=True)

with ZipFile('CustomBoomboxMusicFixed.zip', 'w') as zipObj:
    zipObj.write('./bin/Release/CustomBoomboxMusicFixed.dll', 'CustomBoomboxMusicFixed.dll')
    zipObj.write('./thunderstore/icon.png', 'icon.png')
    zipObj.write('./thunderstore/README.md', 'README.md')
    zipObj.write('./thunderstore/manifest.json', 'manifest.json')
    zipObj.write('./thunderstore/config/custom-boombox-music-fixed.cfg', 'config/custom-boombox-music-fixed.cfg')
