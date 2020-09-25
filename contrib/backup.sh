#!/bin/bash
echo "Delete backup before 60 days ago"
rm -rf /home/backup/netbox.$(date -d -60days "+%Y-%m-%d").bak
echo "Begin database backup"
export PGPASSWORD="Superuser001"
pg_dump -U postgres -p 6060 -h 10.0.10.4 -F c -d netbox -f /home/backup/netbox.$(date "+%Y-%m-%d").bak
echo "Backup finished"
