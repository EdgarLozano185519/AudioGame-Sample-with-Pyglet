@echo off
pyinstaller --windowed --onefile --clean ^
    --add-binary="dlls/nvdaControllerClient32.dll;." ^
    --add-binary="dlls/Tolk.dll;." ^
    --add-binary="dlls/SAAPI32.dll;." ^
    --add-binary="dlls/dolapi32.dll;." ^
    --add-binary="dlls/avbin.dll;." ^
    --add-data="sounds/music/mainMenuMusic.ogg;sounds/music" ^
    --add-data="sounds/clicks/click.ogg;sounds/clicks" ^
    --add-data="sounds/footsteps/wood/fs_wood_1.ogg;sounds/footsteps/wood" ^
    --add-data="sounds/footsteps/wood/fs_wood_2.ogg;sounds/footsteps/wood" ^
    --add-data="sounds/footsteps/wood/fs_wood_3.ogg;sounds/footsteps/wood" ^
    --add-data="sounds/footsteps/wood/fs_wood_4.ogg;sounds/footsteps/wood" ^
    --add-data="sounds/footsteps/wood/fs_wood_5.ogg;sounds/footsteps/wood" ^
    --add-data="sounds/footsteps/wood/fs_wood_6.ogg;sounds/footsteps/wood" ^
    --add-data="sounds/footsteps/wood/fs_wood_7.ogg;sounds/footsteps/wood" ^
    --add-data="sounds/footsteps/wood/fs_wood_8.ogg;sounds/footsteps/wood" ^
    --add-data="sounds/footsteps/wood/fs_wood_9.ogg;sounds/footsteps/wood" ^
    --add-data="sounds/footsteps/wood/fs_wood_10.ogg;sounds/footsteps/wood" ^
    src/pygletTest.py