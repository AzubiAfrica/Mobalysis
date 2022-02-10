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
echo "create user president with password 'president';" > ~/user.txt

# Change int the postgresql bin directory to run psql
cd /usr/bin

# login as root and create the role
sudo -u postgres psql -a -f ~/user.txt

#sudo -u postgres createuser --interactive

