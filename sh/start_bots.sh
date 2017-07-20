#!/usr/bin/bash
# Used to clear PIDs and start every bot.
echo "" > /path/process_ids.txt
nohup (bot)python /path/bot.py > /dev/null 2>&1 &
