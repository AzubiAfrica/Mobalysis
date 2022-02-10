#!/bin/bash
#To install PostgreSQL on Ubuntu 20.04
# Run Ubuntu 20.04 system update 
sudo apt update
#Add PostgreSQL GPG key & repository
wget -q https://www.postgresql.org/media/keys/ACCC4CF8.asc -O- | sudo apt-key add -
#Add repository in Ubuntu 20.04
echo "deb [arch=amd64] http://apt.postgresql.org/pub/repos/apt/ focal-pgdg main" | sudo tee /etc/apt/sources.list.d/postgresql.list
# Run system update command
sudo apt update
sudo apt install postgresql-13
sudo systemctl status postgresql
# Add user
sudo useradd mob_db_user
sudo passwd mob_db_user
# add OS user
sudo useradd -m mob_app_usr
# check for initialization files
ls -la /home/mob_app_user/