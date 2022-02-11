#!/bin/bash

#Script to install PostgreSQL and create a user mob_db_user with a password mob_db_pass

sudo apt-get update -y
sudo apt-get install postgresql postgresql-contrib -y
sudo -u postgres createuser 'mob_db_user' 
sudo -u postgres -c "ALTER ROLE mob_db_user WITH ENCRYPTED PASSWORD 'mob_db_pass'" 

#Script to create a mob_app_usr and install a home directory for the user

#add user with a home directory
sudo useradd mod_app_usr -m
cd /etc/home/mod_app_usr
