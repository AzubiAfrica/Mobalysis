#!/usr/bin/env bash
#Clone repo and  create environment varables
sudo -i -u mob_app_usr bash << EOF

#clone mobalysis repo
git clone https://github.com/redmicelles/Mobalysis

#set Environment Variables
echo export DBNAME=\'mobalytics\' >> .bashrc
echo export DBUSER=\'mob_db_user\' >> .bashrc
echo export DBPASS=\'mob_db_pass\' >> .bashrc
echo export DBHOST=\'localhost\' >> .bashrc
echo export DBPORT=\'5432\' >> .bashrc

#create and activate venv
python3 -m venv ~/Mobalysis/venv
.  ~/Mobalysis/venv/bin/activate

#install pip
sudo apt install -y python3-pip

#install uwsgi
sudo -H pip3 install uwsgi

#pip install requirements
pip3 install -r ~/Mobalysis/backend/requirements.txt

#create user
sudo -u postgres createuser mob_app_usr

#remove old migration 
cd /home/mob_app_usr/Mobalysis/backend/api/migrations
rm 0005_auto_20220218_1335.py 0004_auto_20220218_1334.py 0003_auto_20220218_1315.py 0002_auto_20220218_1313.py 0001_initial.py

#makemigrations
python3 ~/Mobalysis/backend/manage.py makemigrations

#migrate django models
python3 ~/Mobalysis/backend/manage.py migrate

#make directory for uwsgi
sudo mkdir -p /etc/uwsgi/sites
sudo touch /etc/uwsgi/sites/mobalysis.ini 
sudo cp ~/Mobalysis/uswgi_config.ini /etc/uwsgi/sites/mobalysis.ini

#make a systemd unitfile for uWSGI
sudo touch /etc/systemd/system/uwsgi.service
sudo cp ~/Mobalysis/uwsgi.service /etc/systemd/system/uwsgi.service

#create server block configuration files 
sudo touch /etc/nginx/sites-available/mobalysis
sudo cp ~/Mobalysis/mobalysis_serverblock /etc/nginx/sites-available/mobalysis

#create a symbolic link 
sudo ln -s /etc/nginx/sites-available/mobalysis /etc/nginx/sites-enabled

sudo systemctl restart nginx
sudo systemctl start uwsgi

sudo ufw allow 'Nginx Full'

#start automatically at boot 
sudo systemctl enable nginx
sudo systemctl enable uwsgi

EOF

