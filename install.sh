#!/usr/bin/env bash
#Clone repo and  create environment varables
sudo -i -u mob_app_usr bash << EOF
#clone mobalysis repo
# git clone https://github.com/redmicelles/Mobalysis

# #set Environment Variables
# echo export DBNAME=\'mobalytics\' >> .profile
# echo export DBUSER=\'mob_db_user\' >> .profile
# echo export DBPASS=\'mob_db_pass\' >> .profile
# echo export DBHOST=\'localhost\' >> .profile
# echo export DBPORT=\'5432\' >> .profile

#create and activate venv
python3 -m venv ~/Mobalysis/venv
source  ~/Mobalysis/venv/bin/activate

#pip install requirements
pip3 install -r ~/Mobalysis/backend/requirements.txt

#makemigrations
python3 ~/Mobalysis/backend/manage.py makemigrations

#migrate django models
python3 ~/Mobalysis/backend/manage.py migrate
EOF