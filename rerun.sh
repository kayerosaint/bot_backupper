#!/bin/bash
if ! pgrep -f "python3.7 /home/backup_user/scripts/main.py" > /dev/null; then
	/usr/local/bin/python3.7 /home/backup_user/scripts/main.py &
fi

