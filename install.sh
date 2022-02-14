cd /home/mob_app_usr
git clone https://github.com/koladeA/Mobalysis

#Modify install.sh shell script.When executed install.sh should: Add the following environment variables and values to the mob_app_usr’s bashrc file
echo -e "DBNAME =mobalytics\nDBUSER=mob_db_user\nDBPASS=mob_db_pass\nDBHOST=localhost\nDBPORT=5432" >>config.bashrc