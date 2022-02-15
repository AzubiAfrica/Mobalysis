sudo apt update
sudo apt install postgresql postgresql-contrib
sudo -u postgres createuser 'mob_db_user'
sudo -u postgres psql -c "ALTER ROLE mob_db_user WITH password 'mob_db_pass'"
sudo -u postgres createuser 'mob_app_usr'
sudo -u postgres psql -c "ALTER ROLE mob_app_usr WITH password 'mob_app_pass'"
#sudo -i -u postgress to enter into the postgres session
#to exit the interactive postgres session, user must type 'exit'
sudo apt-get install python3-pip
sudo pip3 install virtualenv 
virtualenv python3-venv 
sudo -u postgres createdb mobalytics
sudo -u postgres psql -c "ALTER DATABASE mobalytics OWNER TO mob_db_user"
