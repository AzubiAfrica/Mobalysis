#!/bin/bash
##### NUMBER HERE
#clone the repository
git clone https://github.com/President-Banda/Mobalysis.git

#Move project files to mob_app_usr home directory
sudo mv Mobalysis /home/mob_app_usr/

# SPRINT NUMBER 7 TO EDIT BASHRC AND ENVIRONMENT VARIABLES
# Create the file
touch ~/variables.txt

# Append data to the file
echo "export DBNAME=mobalytics" > ~/variables.txt
echo "export DBUSER=mob_db_user" >> ~/variables.txt
echo "export DBPASS=mob_db_pass" >> ~/variables.txt
echo "export DBHOST=localhost" >> ~/variables.txt
echo "export DBPORT=5432" >> ~/variables.txt

# Make bashrc file writeable
sudo chmod 666 /home/mob_app_usr/.bashrc

# Write the variables to the file
sudo cat ~/variables.txt >> /home/mob_app_usr/.bashrc

# Revert the mode
sudo chmod 644 /home/mob_app_usr/.bashrc

# Run the bashrc file
source /home/mob_app_usr/./.bashrc

###### SPRINT NUMBER 9 TO INSTALL APPLICATION PACKAGES FOR BACKEND
# Create the virtual environment
virtualenv ~/env

# Activate the virtual environment
source ~/env/bin/activate

# Install application packages
python3 -m pip install -r backend/requirements.txt

##### SPRINT NUMBER 10 TO INSTALL APPLICATION DATABASE
# Run new migrations
python3 backend/manage.py makemigrations

# Install backend migrations
python3 backend/manage.py migrate


