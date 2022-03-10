#!/bin/bash

# To clone into current directory
cd /home/mob_app_usr
sudo git clone https://github.com/wanguij/Mobalysis.git 

# Add environment variables and values to mob_app_usr's bashrc file
sudo  bash -c 'echo "export DBUSER=mob_db_user" >> /home/mob_app_usr/.bashrc'
sudo  bash -c 'echo "export DBNAME=mobalysis" >> /home/mob_app_usr/.bashrc'
sudo  bash -c 'echo "export DBHOST=127.0.0.1" >> /home/mob_app_usr/.bashrc'
sudo  bash -c 'echo "export DBPASS=mobdbpass" >> /home/mob_app_usr/.bashrc'
sudo  bash -c 'echo "export DBPORT=5432" >> /home/mob_app_usr/.bashrc'
sudo -u mob_app_user sh -c 'cd /home/mob_app_user/ && /usr/bin/python3 -m venv .env'
sudo -u mob_app_user bash -c 'cd /home/mob_app_user/ && source /home/mob_app_user/.env/bin/activate && pip3 install -r /home/mob_app_user/Mobalysis/backend/requirements.txt && python /home/mob_app_user/Mobalysis/backend/manage.py migrate'


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
python3 /home/mob_app_usr/Mobalysis/backend/backend/manage.py makemigrations
python3 /home/mob_app_usr/Mobalysis/backend/backend/manage.py migrate

#create frontenddeploy.sh
sudo touch frontenddeploy.sh

#update ubuntu instance
sudo -u apt-get update >> /home/mob_app_usr/frontenddeploy.sh

#update ubuntu system
sudo -u apt-get upgrade >> /home/mob_app_usr/frontenddeploy.sh

#install nginx
sudo -u apt-get install nginx-y >> /home/mob_app_usr/frontenddeploy.sh

#nginx version
sudo -u nginx-v 
