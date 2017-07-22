#!/usr/bin/bash
# git pull in every directory
cd /home/pi/Git/RaspberryPiBot
git stash > /dev/null 2>&1
git pull > /dev/null 2>&1
cd /home/pi/Git/cryptobot
git stash > /dev/null 2>&1
git pull > /dev/null 2>&1
cd $HOME
