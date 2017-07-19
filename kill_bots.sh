#!/usr/bin/bash
# Used to kill all bots given the process id in the file process_ids.txt,
# which the bots write their PID into.
kill `cat process_ids.txt`
echo "" > process_ids.txt
