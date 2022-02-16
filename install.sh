#!/bin/bash

#Script to create a virtual enviroment env, activate virtual enviroment 
#source/path and install the application packages in the virtusl enviroment

sudo apt-get install python3-pip
sudo pip3 install virtualenv
virtualenv venv 

#command to activate virtual envireoment
source <venv>/bin/activate

#Command to install the application database
python3 /home/mob_app_usr/mobalysis/backend/backend/manage.py makemigrations
python3 /home/mob_app_usr/mobalysis/backend/backend/manage.py migrate
