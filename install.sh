#!/bin/bash

#Step 3 creating install.sh (clones the repository into the home directory of the mob_app_usr) VERONICA

cd /home/mob_app_usr
sudo git clone https://github.com/sdg000/Mobalysis

sudo chmod +x install.sh


#Step 4  add environment variables to mob_db

echo -e "DBNAME=mobalytics\nDBUSER=mob_db_user\nDBPASS=mob_db_pass\nDBHOST=localhost\nDBPORT=5432" >> .bashrc

sudo chmod +x .bashrc


#step 6. create /activate virtual environment and install its packages

#This script creates the virtual environment

python3.8 -m venv /home/new/virtualenv


#This scripts activates the virtual environment

source /home/virtualenv/env/bin/activate



#This script Installs application packages in venv

sudo apt-get install libpq-dev
sudo apt-get install python3-pip
pip install psycopg3


#step 7 making new migrations and backend migrations.

#this script creates new migration / installs backend

python3 /home/Mobalysis/backend/manage.py makemigrations
python3 /home/Mobalysis/backend/manage.py migrate
