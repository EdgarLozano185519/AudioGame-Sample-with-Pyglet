@echo off
pyinstaller --windowed --key=key --clean ^
    --add-binary="../nvdaControllerClient32.dll;." ^
    --add-binary="../Tolk.dll;." ^
    --add-binary="../SAAPI32.dll;." ^
    --add-binary="../dolapi32.dll;." ^
    --add-binary="../avbin.dll;." ^
    --add-data="../sounds/music/mainMenuMusic.ogg;sounds/music" ^
    --add-data="../sounds/clicks/click.ogg;sounds/clicks" ^
    --add-data="../sounds/footsteps/wood/fs_wood_1.ogg;sounds/footsteps/wood" ^
    --add-data="../sounds/footsteps/wood/fs_wood_2.ogg;sounds/footsteps/wood" ^
    --add-data="../sounds/footsteps/wood/fs_wood_3.ogg;sounds/footsteps/wood" ^
    --add-data="../sounds/footsteps/wood/fs_wood_4.ogg;sounds/footsteps/wood" ^
    --add-data="../sounds/footsteps/wood/fs_wood_5.ogg;sounds/footsteps/wood" ^
    --add-data="../sounds/footsteps/wood/fs_wood_6.ogg;sounds/footsteps/wood" ^
    --add-data="../sounds/footsteps/wood/fs_wood_7.ogg;sounds/footsteps/wood" ^
    --add-data="../sounds/footsteps/wood/fs_wood_8.ogg;sounds/footsteps/wood" ^
    --add-data="../sounds/footsteps/wood/fs_wood_9.ogg;sounds/footsteps/wood" ^
    --add-data="../sounds/footsteps/wood/fs_wood_10.ogg;sounds/footsteps/wood" ^
    src/pygletTest.py