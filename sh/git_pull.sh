#!/usr/bin/bash
# git pull in every directory
echo "" > /home/pi/bot.log
cd /home/pi/Git/RaspberryPiBot
git stash >> /home/pi/bot.log 2>&1
git pull >> /home/pi/bot.log 2>&1
# git stash > /dev/null 2>&1
# git pull > /dev/null 2>&1
cd /home/pi/Git/cryptobot
git stash >> /home/pi/bot.log 2>&1
git pull >> /home/pi/bot.log 2>&1
# git stash > /dev/null 2>&1
# git pull > /dev/null 2>&1
cd $HOME
