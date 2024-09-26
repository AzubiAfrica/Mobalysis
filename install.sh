#!/bin/bash
#clone the repository into home directory of the mob_app_usr
sudo -u mob_app_usr sh -c 'cd /home/mob_app_usr/ && git clone https://github.com/bmokase3093/Mobalysis.git'

#install environment variables
#to the mob_app_usr bashrc file
sudo bash -c 'echo "export DBNAME=mobalytics" >> /home/mob_app_user/.bashrc'
sudo bash -c 'echo "export DBUSER=mob_db_user" >> /home/mob_app_user/.bashrc'
sudo bash -c 'echo "export DBPASS=mob_db_pass" >> /home/mob_app_user/.bashrc'
sudo bash -c 'echo "export DBHOST=127.0.0.1" >> /home/mob_app_user/.bashrc'
sudo bash -c 'echo "export DBPORT=5432" >> /home/mob_app_user/.bashrc'
sudo -u mob_app_user sh -c 'cd /home/mob_app_user/ && /usr/bin/python3 -m venv .env'
sudo -u mob_app_user bash -c 'cd /home/mob_app_user/ && source /home/mob_app_user/.env/bin/activate && pip3 install -r /home/mob_app_user/Mobalysis/backend/requirements.txt && python /home/mob_app_user/Mobalysis/backend/manage.py migrate'
