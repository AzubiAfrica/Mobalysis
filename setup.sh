#!/bin/bash
sudo apt update
sudo apt-get -y install postgresql
sudo su postgres
sudo -u postgres psql
sudo service postgresql start
sudo -u postgres createuser --interactive
CREATE USER mob_db_user PASSWORD 'mob_db_pass'
\q
exit
sudo useradd mob_app_usr -p 'Project4'
