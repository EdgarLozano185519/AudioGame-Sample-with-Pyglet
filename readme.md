# AudioGame Sample with Pygame
This is a sample AudioGame written in Python. It should serve only as a decent starting point to the basics of implementing simple game utilities.
## Introduction
If you are new to AudioGame development, welcome to my attempt at creating a sample game from which one can learn to lay the groundwork for constructing a game from scratch. If you are unfamiliar with audio gaming, it is essential to understand that this style of playing a game is usually intended for visually impaired people. The main difference between games typically found in the mainstream and this style of game play is the missing component--the visuals. These games are played by relying on audio cues, environmental sounds, panning, and other elements. For more information, one can visit the [AudioGames.net website.](http://audiogames.net)
## Aim of the Game
As of now, there is no real aim to the game. The project is currently under development. However, some modular development techniques are presented in the hopes that one will gain some insight into development strategies for the developer, and an introduction to this style of gaming for the average gamer. Currently, there is a concise menu system, simplistic walking facilities, a map system, timers, and a few extra utilities. This project will definitely be expanded upon as time permits.
## How to Build
This game will build with the following requirements in place: Python 3.6 or higher, Pycrypto library, Pyinstaller for packaging, screen reader libraries, and finally, Pygame. Pyinstaller, and Pycrypto can be installed using pip. A simple google search can reveal how to install these mainstream dependencies. However, the screen reader libraries are special. You can view the source and prebuilt binaries [at this link.](https://github.com/dkager/tolk) This is a library that offers generous support for major screen readers and their APIs.
Please review the commits and source code for information about this project's current status.

## Alternative Setup

Alternatively, use a [virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/). See the previous link for an indepth guide, but that might look like:

```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```

This project's dependencies are now installed locally into its own directory, and are only available once the venv is activated (E.g. `source venv/bin/activate`.)
# Things to Do
Check out the [ToDo](docs/todo.md) to see if you can contribute.
# Contributors
Check out the [list of contributors.](docs/contributors.md)
