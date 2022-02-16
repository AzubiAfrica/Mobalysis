#!/bin/bash

# To clone into current directory
sudo su -c 'git clone https://github.com/wanguij/Mobalysis.git' - mob_app_usr

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
