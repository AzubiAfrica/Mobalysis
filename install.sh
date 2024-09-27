#!/usr/bin/env bash
#Clone repo and  create environment varables
sudo -i -u mob_app_usr bash << EOF

#clone mobalysis repo
git clone -b dev https://github.com/redmicelles/Mobalysis

#set Environment Variables
echo export DBNAME=\'mobalytics\' >> .bashrc
echo export DBUSER=\'mob_db_user\' >> .bashrc
echo export DBPASS=\'mob_db_pass\' >> .bashrc
echo export DBHOST=\'localhost\' >> .bashrc
echo export DBPORT=\'5432\' >> .bashrc

#install env
sudo apt-get install -y python3-venv
#create and activate venv
python3 -m venv ~/Mobalysis/venv
.  ~/Mobalysis/venv/bin/activate

#install pip
sudo apt-get install -y python3-pip

#update the settings.py 
sed -i 's/'*'/'ec2-18-215-156-51.compute-1.amazonaws.com'/g' ~/Mobalysis/backend/backend/settings.py 
echo "STATIC_ROOT = os.path.join(BASE_DIR, 'static/')" >> ~/Mobalysis/backend/backend/settings.py

#create user
sudo -u postgres createuser mob_app_usr

#install a different version of python 
sudo apt-get install python3.8-dev 

#install a different version of python 
sudo apt-get install gcc 

#install uwsgi
sudo pip3 install uwsgi

#pip install requirements
sudo pip3 install -r ~/Mobalysis/backend/requirements.txt

#remove old migration 
cd /home/mob_app_usr/Mobalysis/backend/api/migrations
rm 0005_auto_20220218_1335.py 0004_auto_20220218_1334.py 0003_auto_20220218_1315.py 0002_auto_20220218_1313.py 0001_initial.py

#makemigrations
python3 ~/Mobalysis/backend/manage.py makemigrations

#migrate django models
python3 ~/Mobalysis/backend/manage.py migrate

#migrate static to the static folder created 
python3 ~/Mobalysis/backend/manage.py collectstatic

#create directory for the media files
sudo mkdir /home/mob_app_usr/Mobalysis/backend/media

#create server block configuration files 
sudo touch /etc/nginx/sites-available/mobalysis
sudo cp ~/Mobalysis/mobalysis_serverblock /etc/nginx/sites-available/mobalysis

#create add uwsgi_params 
sudo touch ~/Mobalysis/backend/uwsgi_params 
sudo cp ~/Mobalysis/uwsgi_params ~/Mobalysis/backend/uwsgi_params

#create a symbolic link for nginx to server the backend
sudo ln -s /etc/nginx/sites-available/mobalysis /etc/nginx/sites-enabled/

#
sudo mkdir /home/mob_app_usr/env/env/vassals
sudo ln -s /etc/nginx/sites-available/mobalysis /home/mob_app_usr/env/env/vassals 

#make directory for uwsgi
sudo mkdir -p /etc/uwsgi/sites
sudo touch /etc/uwsgi/sites/mobalysis.ini 
sudo cp ~/Mobalysis/mobalysis_uwsgi.ini /etc/uwsgi/sites/mobalysis.ini

#make a systemd unitfile for uWSGI
sudo touch /etc/systemd/system/uwsgi.service
sudo cp ~/Mobalysis/uwsgi.service /etc/systemd/system/uwsgi.service

sudo systemctl restart nginx
sudo systemctl start uwsgi

#start automatically at boot 
sudo systemctl enable nginx
sudo systemctl enable uwsgi

EOF

