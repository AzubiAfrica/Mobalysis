#!/bin/bash

#Step 3
#This script clones the repository into the home directory of the mob_app_usr

sudo su mob_app_usr
cd /home/mob_app_usr
git clone https://github.com/koladeA/Mobalysis

sudo chmod +x install.sh


#Step 4
#This adds the environmental variable to mob_db_user
cd ~/ubuntu
echo -e "EXPORT DBNAME=mobalytics\nEXPORT DBUSER=mob_db_user\nEXPORT DBPASS=mob_db_pass\nEXPORT DBHOST=localhost\nEXPORT DBPORT=5432" >> .bashrc

sudo chmod +x .bashrc

 
#This code creates the virtual environment
python3.8 -m venv /home/new/virtualenv
 
#This code activates the virtual environment
source /home/virtualenv/env/bin/activate
 
#This script install packages
sudo apt-get install libpq-dev
sudo apt-get install python3-pip
pip install psycopg3


#Makes a new migration
#Installs the backend migration 
python3 /home/Mobalysis/backend/manage.py makemigrations
python3 /home/Mobalysis/backend/manage.py migrate

