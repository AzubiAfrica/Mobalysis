#!/bin/bash

#install postgre db 

#prepare a repository for the db
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

#get a key. did not work
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

#get updates for the postgredb
sudo apt-get update

#install the db
sudo apt-get install postgresql



#TASK 2

#add user with a home directory
sudo useradd mod_app_usr -m