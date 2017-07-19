#!/usr/bin/bash
# Used to clear PIDs and start every bot.
echo "" > process_ids.txt
$HOME/.conda/envs/bot/bin/python bot.py
