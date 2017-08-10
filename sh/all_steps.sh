#!/usr/bin/bash
# simple script to call
# - kill_bots.sh
# - git_pull.sh
# - start_bots.sh
# in that order.
echo "" > /home/pi/bot.log
/usr/bin/bash /home/pi/Git/RaspberryPiBot/sh/kill_bots.sh
/usr/bin/bash /home/pi/Git/RaspberryPiBot/sh/git_pull.sh
/usr/bin/bash /home/pi/Git/RaspberryPiBot/sh/start_bots.sh
# send log
/home/pi/miniconda3/envs/bot/bin/python /home/pi/Git/RaspberryPiBot/bots/logger.py >> /home/pi/bot.log 2>&1
