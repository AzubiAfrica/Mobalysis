#!/bin/bash

dbuser="mob_db_user"
dbpass="mob_db_pass"
sys_user="mob_app_usr"

sys_user_dir=/home/$sys_user

# Runs Ubuntu 20.04 system update 
sudo apt-get update -y

sudo apt-get install python3-venv

# Installs the PostgreSQL 
sudo apt-get install postgresql -y

# Starts PostgreSQL and creates a user to the database
sudo -u postgres createuser  $dbuser 

#
sudo -u postgres psql -c "ALTER ROLE $dbuser WITH PASSWORD '$dbpass'"

# adds the system/OS user and makes a home directory for the user
sudo useradd -d $sys_user_dir $sys_user

sudo -u postgres psql -c "CREATE DATABASE mobalytics";

sudo -u postgres psql -c "ALTER DATABASE mobalytics 
OWNER TO mob_db_user";
