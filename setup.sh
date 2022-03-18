#!/bin/bash
  
#Script to install PostgreSQL and create a user mob_db_user with a password mob_db_pass

sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install postgresql postgresql-contrib -y
sudo -u postgres createuser 'mob_db_user'
sudo -u postgres -c "ALTER ROLE mob_db_user WITH ENCRYPTED PASSWORD 'mob_db_pass'"

#Script to create a mob_app_usr and install a home directory for the user

#add user with a home directory
sudo useradd mob_app_usr -m
cd /home/mob_app_usr

#Script to install python3-venv and create and database mobalytics and set owner to mob_db_user

sudo -u postgres createdb -O mob_db_user mobalytics
sudo apt-get install python3-pip -y
sudo apt-get install python3-venv -y


