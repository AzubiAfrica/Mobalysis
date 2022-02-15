#!/bin/bash

#clone the repository
git clone https://github.com/President-Banda/Mobalysis.git

#Move project files to mob_app_usr home directory
sudo mv Mobalysis /home/mob_app_usr/

# remove any previous files
#rm ~/variables_data_capstone.txt

# Create the file
touch ~/variables.txt

# Append data to the file
echo "DBNAME = mobalytics" > ~/variables.txt
echo "DBUSER = mob_db_user" >> ~/variables.txt
echo "DBPASS = mob_db_pass" >> ~/variables.txt
echo "DBHOST = localshost" >> ~/variables.txt
echo "DBPORT = 5432" >> ~/variables.txt

# Make bashrc file writeable
sudo chmod 666 /home/mob_app_usr/.bashrc

# Write the variables to the file
sudo cat ~/variables.txt >> /home/mob_app_usr/.bashrc

# Revert the mode
sudo chmod 644 /home/mob_app_usr/.bashrc

#sudo cp /home/mob_app_usr/.bashrc ~/bashrc
#cat ~/variables.txt >> ~/bashrc
#sudo rm /home/mob_app_usr/.bashrc
#sudo cp ~/bashrc /home/mob_app_usr/.bashrc

source /home/mob_app_usr/./.bashrc
