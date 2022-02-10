sudo apt update
sudo apt install postgresql postgresql-contrib
sudo -u postgres createuser --interactive
#insert name of user which is mob_db_user
sudo -u postgres psql -c "ALTER ROLE mob_db_user WITH password 'mob_db_pass'"
sudo -u postgres createuser --interactive
#insert name of user which is mob_app_usr
sudo -u postgres psql -c "ALTER ROLE mob_db_user WITH password 'mob_app_pass'"
#sudo -i -u postgress to enter into the postgres session
#to exit the interactive postgres session, user must type 'exit'
