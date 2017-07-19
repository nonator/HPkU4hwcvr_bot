#!/usr/bin/bash
# kill bots
# git pull
# start bots
kill 'cat process_ids.txt'
cd $HOME/Git/rpibot/
git pull
cd $HOME/Git/cryptobot
git pull
python stuff.py
