#!/bin/bash

# To clone into current directory
sudo git clone https://github.com/wanguij/Mobalysis.git -mob_app_usr

# Add environment variables and values to mob_app_usr's bashrc file
sudo echo 'export DBNAME=mobalytics' >> /home/mob_app_usr/.bashrc
sudo echo 'export DBUSER=mob_db_user' >> /home/mob_app_usr/.bashrc 
sudo echo 'export DBPASS=mob_db_passs' >> /home/mob_app_usr/.bashrc 
sudo echo 'export DBHOST=localhost' >> /home/mob_app_usr/.bashrc 
sudo echo 'export DBPORT=5432' >> /home/mob_app_usr/.bashrc 

#Execute the bashrc file
sudo source .bashrc

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
