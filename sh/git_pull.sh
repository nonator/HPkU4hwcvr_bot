#!/usr/bin/bash
# git pull in every directory
cd /home/pi/Git/RaspberryPiBot
git stash > /home/π/bot.log 2>&1
git pull > /home/π/bot.log 2>&1
# git stash > /dev/null 2>&1
# git pull > /dev/null 2>&1
cd /home/pi/Git/cryptobot
git stash > /home/π/bot.log 2>&1
git pull > /home/π/bot.log 2>&1
# git stash > /dev/null 2>&1
# git pull > /dev/null 2>&1
cd $HOME
