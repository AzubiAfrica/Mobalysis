#!/bin/bash

#Step 1









#Step 2
# -d /home/mob_app_usr/ – Set /home/mob_app_usr/ as home directory of the new user
# -m – Create the user’s home directory
# -G sudo – Make sure mob_app_usr user can sudo i.e. give admin access to the new user
sudo useradd -s /bin/bash -d /home/mob_app_usr/ -m -G sudo mob_app_usr
sudo passwd mob_app_usr





#Step 3
#This script clones the repository into the home directory of the mob_app_usr
cd /home/mob_app_usr
git clone https://github.com/koladeA/Mobalysis