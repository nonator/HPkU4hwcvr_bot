#!/usr/bin/bash
# git pull in every directory
cd /home/pi/Git/RaspberryPiBot
git stash
git pull
cd /home/pi/Git/cryptobot
git stash
git pull
cd $HOME
