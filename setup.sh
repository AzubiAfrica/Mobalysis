sudo apt update
sudo apt install postgresql postgresql-contrib
sudo -i -u postgres
sudo -u postgres createuser --interactive
ALTER USER mob_db_user Password 'mob_db_pass';
use the command /q to exit the interactive session.
