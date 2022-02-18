#!/bin/bash

# To clone into current directory
cd /home/mob_app_usr
sudo git clone https://github.com/wanguij/Mobalysis.git 

# Add environment variables and values to mob_app_usr's bashrc file
cd /home/mob_app_usr/.bashrc
export DBNAME=mobalytics
export DBUSER=mob_db_user
export DBPASS=mob_db_pass
export DBHOST=localhost
export DBPORT=5432
echo "$DBNAME,$DBUSER,$DBPASS,$DBHOST,$DBPORT"

#Execute changes to the current session of the bashrc file
source .bashrc

#Script to create a virtual enviroment env, activate virtual enviroment 
#source/path and install the application packages in the virtusl enviroment

sudo apt-get install python3-pip
sudo pip3 install virtualenv
virtualenv venv 

#command to activate virtual envireoment
source venv/bin/activate

#to confirm the virtualenv path
which python

#command to install packages in the virtualenv
python3 -m pip install requests

#leave virtual env
deactivate

#Command to install the application database
python3 /home/mob_app_usr/mobalysis/backend/backend/manage.py makemigrations
python3 /home/mob_app_usr/mobalysis/backend/backend/manage.py migrate
