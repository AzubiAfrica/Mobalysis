#!/bin/bash

sudo apt update

# Install postgres chosing 'yes' for all prompts if possible
sudo apt install -y postgresql postgresql-contrib

# Create Postgres User: mob_db_user with password mob_db_password
sudo -u postgres psql -c "CREATE USER mob_db_user;"
sudo -u postgres psql -c "ALTER USER mob_db_user password 'mob_db_pass';" 
