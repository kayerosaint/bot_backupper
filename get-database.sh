#!/bin/bash
psql -h $1 -U postgres -A -t -c "SELECT datname FROM pg_database;" > /home/backup_user/scripts/databases_$1.txt
