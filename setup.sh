sudo apt update
sudo apt install postgresql postgresql-contrib
sudo -i -u postgres #to enter the postgres session
sudo -u postgres createuser --interactive
#insert name of user which is mob_db_user
ALTER USER mob_db_user PASSWORD 'mob_db_pass';
#to exit the interactive postgres session, user must type '\q'