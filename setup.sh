#!/bin/bash

#Script to install PostgreSQL and create a user mob_db_user with a password mob_db_pass

sudo apt-get update -y
sudo apt-get install postgresql postgresql-contrib -y
sudo -u postgres createuser --interactive 
sudo -u postgres -c "ALTER ROLE mob_db_user WITH ENCRYPTED PASSWORD 'mob_db_pass'" 
