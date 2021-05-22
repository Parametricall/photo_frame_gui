# photo_frame_gui

## About

TBA

## Installation Guide

* poetry should already be installed on the developers system
  * https://python-poetry.org/docs/
    
1. Clone repo into desired directory
2. From the terminal (within the repo's directory) execute:
```commandline
poetry install
```
3. Create a new file called config.ini
    * The contents of config.ini should copy that of config.ini.default but 
    replace the values with your own requirements
4. start photo_frame_gui.py
```commandline
poetry run python photo_frame_gui.py
```

## Deployment Procedure

This project is bundled into an executable so that it can be run from any
computer that does not have python previously installed on it. Alongside
the executable will be a config.ini file that users can edit to their 
requirements. I.E the config.ini file contains the username and password 
required to log into the raspberry pi.

1. From the terminal (within the repo's directory) execute:
```commandline
pyinstaller --onefile --noconsole photo_frame_gui.py
```
This will find all python dependencies required to run photo_frame_gui.py and
bundle them into one executable (.exe) file. The '--noconsole' flag is used
to prevent a terminal from appearing when running the executable.

The executable will appear within the 'dist' directory. This directory will be
created if it does not already exist.

The executable can now be copied and placed where ever the user desires. 
Remembering that the config.ini file should also be placed alongside the 
executable file.