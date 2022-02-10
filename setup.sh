sudo apt update
sudo apt install postgresql postgresql-contrib
sudo -u postgres createuser --interactive
#insert name of user which is mob_db_user
sudo -u postgres psql -c "ALTER ROLE mob_db_user WITH password 'mob_db_pass'"
sudo -u postgres createuser --interactive
#insert name of user which is mob_db_user
ALTER USER mob_app_usr PASSWORD 'mob_app_pass';
#to exit the interactive postgres session, user must type '\q'
