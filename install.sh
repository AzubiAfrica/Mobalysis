#!/bin/bash

#Step 3 creating install.sh (clones the repository into the home directory of the mob_app_usr) VERONICA

cd /home/mob_app_usr
git clone https://github.com/sdg000/Mobalysis

sudo chmod +x install.sh


#Step 4  add environment variables to mob_db

echo -e "DBNAME=mobalytics\nDBUSER=mob_db_user\nDBPASS=mob_db_pass\nDBHOST=localhost\nDBPORT=5432" >> .bashrc

sudo chmod +x .bashrc




