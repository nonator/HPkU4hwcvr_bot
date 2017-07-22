#!/usr/bin/bash
# Used to kill all bots given the process id in the file process_ids.txt,
# which the bots write their PID into
# end empty process id file.
kill `cat /home/pi/Git/RaspberryPiBot/temp/process_ids.txt` > /dev/null 2>&1
echo "" > /home/pi/Git/RaspberryPiBot/temp/process_ids.txt
