#!/usr/bin/bash
# git pull in every directory
cd /home/pi/Git/RaspberryPiBot
git pull >> /home/pi/bot.log 2>&1

cd /home/pi/Git/cryptobot
git pull >> /home/pi/bot.log 2>&1

cd $HOME
