#!/bin/bash
#Task 1 install and setup postgresql and create a user
#Task 14 install python3-venv, create db mobalytics and set owner to mob_app_user
sudo apt-get update 
sudo apt-get install python3-pip python3-venv postgresql postgresql-contrib -y
sudo -u postgres psql -c "create user mob_db_usr with encrypted password 'mobdbpass'"
sudo -u postgres psql -c "create database mobalysis"
sudo -u postgres psql -c "grant all privileges on database mobalysis to mob_app_usr"

#Add operating system user mob_app_user
#install a home directory for the user
sudo useradd -m mob_app_usr
sudo chsh -s /sbin/nologin mob_app_usr

sudo -u mob_app_user bash -c 'cd /home/mob_app_user/ && /usr/bin/python3 -m venv .env'



