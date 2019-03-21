<h1 align="center">
  DailyBingDesktopWallpaper
</h1>

> Small python script to set the Bing Image of the Day as your Raspbian desktop background 

> note - this is just a fork of zhangzp9970/GnomeBingLockScreen with tweeks for Raspian

## Have you ever been tired of the same lock screen all the day?
## Have you ever dreamed of having a Windows Spotlight lock screen on your Raspbian desktop?
## That's why this project has been started.
## There already exists a similar and better project https://github.com/neffo/bing-wallpaper-gnome-extension but it's a great practice for me to make my own　using python. So, I insist on making this project better.

## Features
* change your GNOME lock screen pictures daily with Bing Image of the day
* the pictures are stored at ~/Pictures/Bing/ by default
* have a configuration file at ~/.config/Bing/
* delete pictures more than 7 days (to be improved)
  
## Todo
* add a GUI for configure
* add proxy support
* add requirements
* make a pip package
* add systemd service file
  
## Usage
clone this repo and add python3 bing_screen_saver.py to start up applications

## Screenshot
![lock](/img/Screenshot.png)
## License
GNU General Public License v3

Copyright (C) 2018 by 张泽平 <zhang9zp970@gmail.com>

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see http://www.gnu.org/licenses/.

![gpl](/img/GPLv3_Logo.png)