#!/usr/bin/bash
echo "" > /home/pi/bot.log
/usr/bin/bash /home/pi/Git/RaspberryPiBot/sh/kill_bots.sh
/usr/bin/bash /home/pi/Git/RaspberryPiBot/sh/git_pull.sh
/usr/bin/bash /home/pi/Git/RaspberryPiBot/sh/start_bots.sh

/home/pi/miniconda3/envs/bot/bin/python /home/pi/Git/RaspberryPiBot/bots/logger.py >> /home/pi/bot.log 2>&1
