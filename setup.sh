#!/bin/bash
sudo apt update
sudo apt upgrade -y
sudo apt-get -y install postgresql
sudo -u postgresql psql -c "CREATE USER mob_db_user PASSWORD 'mob_db_pass'"
\q
exit
sudo useradd mob_app_usr -p 'Project4'
