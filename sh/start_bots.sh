#!/usr/bin/bash
# Used to clear PIDs and start every bot.
nohup /home/pi/miniconda3/envs/bot/bin/python /home/pi/Git/cryptobot/bot.py >> /home/pi/bot.log 2>&1 &
nohup /home/pi/miniconda3/envs/bot/bin/python /home/pi/Git/RaspberryPiBot/bots/traffic.py >> /home/pi/bot.log 2>&1 &
