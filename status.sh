#!/bin/bash
if cat /home/backup_user/backup_db/log/restore_partial.log | grep "ERROR:" &>/dev/null ; then
	cat /home/backup_user/backup_db/log/restore_partial.log | grep "ERROR:"
else
	if cat /home/backup_user/backup_db/log/restore_partial.log | grep "are restored" &>/dev/null ; then
		cat /home/backup_user/backup_db/log/restore_partial.log | grep "are restored"
	else
		if cat /home/backup_user/backup_db/log/restore_partial.log | grep "INFO: Restoring" &>/dev/null ; then
			cat /home/backup_user/backup_db/log/restore_partial.log | grep "INFO: Restoring"
		else
			echo "sorry, nothing to show right now"
		fi
	fi
fi

