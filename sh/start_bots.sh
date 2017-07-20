#!/usr/bin/bash
# Used to clear PIDs and start every bot.
echo "" > /home/pi/Git/RaspberryPiBot/process_ids.txt
nohup /home/pi/miniconda3/envs/bot/bin/python /home/pi/Git/cryptobot/bot.py > /dev/null 2>&1 &
nohup /home/pi/miniconda3/envs/bot/bin/python /home/pi/Git/RaspberryPiBot/bots/traffic.py > /dev/null 2>&1 &
