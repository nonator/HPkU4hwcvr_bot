#!/usr/bin/bash
# git pull in every directory
cd /home/pi/Git/RaspberryPiBot
/usr/local/bin/git stash >> /home/pi/bot.log 2>&1
/usr/local/bin/git pull >> /home/pi/bot.log 2>&1
# git stash > /dev/null 2>&1
# git pull > /dev/null 2>&1
cd /home/pi/Git/cryptobot
/usr/local/bin/git stash >> /home/pi/bot.log 2>&1
/usr/local/bin/git pull >> /home/pi/bot.log 2>&1
# git stash > /dev/null 2>&1
# git pull > /dev/null 2>&1
cd $HOME
