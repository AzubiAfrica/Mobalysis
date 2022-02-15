#!/bin/bash
# Albert Banda
# Friday, February 11, 12:08 AM
# Bash script to install postgres database and create a user

# Update system and dependencies
sudo apt-get update

# Install postgres and prompt yes to any questions, also add postgresql-contrib for extra features
sudo apt-get -y install postgresql postgresql-contrib

# Start the postgresql service via systemd
sudo systemctl start postgresql

# Create a user file
touch ~/user.txt

# Specify the command and user parameters to use as input to the user creation process
echo "create user mob_db_user with password 'mob_db_pass';" > ~/user.txt

# Change int the postgresql bin directory to run psql
cd /usr/bin

# login as root and create the role
sudo -u postgres psql -a -f ~/user.txt

#sudo -u postgres createuser --interactive


# -s /bin/bash – Set /bin/bash as login shell of the new account
# -d /home/mob_app_usr/ – Set /home/mob_app_usr/ as home directory of the new user
# -m – Create the user’s home directory
# -G sudo – Make sure mob_app_usr user can sudo i.e. give admin access to the new user
sudo useradd -s /bin/bash -d /home/mob_app_usr/ -m -G sudo mob_app_usr

#create password for the new user
sudo passwd mob_app_usr

#Install pip first
sudo apt-get install python3-pip -y

#install virtualenv using pip3
pip3 install virtualenv --user

#create a virtual environment
virtualenv -p python3 myenv

# virtualenv ~/.environment


#Active your virtual environment:
source venv/bin/activate

# source ~/environment/bin/activate
# create an empty database with the name mobalytics and set the owner of the mobalytics database to mob_db_user
sudo -u postgres createdb -O mob_db_user mobalytics 
