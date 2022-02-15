#!/bin/bash

#Step 3
#This script clones the repository into the home directory of the mob_app_usr


cd /home/mob_app_usr
git clone https://github.com/koladeA/Mobalysis

chmod +x install.sh


#Step 4
#This adds the environmental variable to mob_db_user
echo -e "DBNAME =mobalytics\nDBUSER=mob_db_user\nDBPASS=mob_db_pass\nDBHOST=localhost\nDBPORT=5432" >>.bashrc