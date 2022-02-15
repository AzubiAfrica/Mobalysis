sudo apt update #to update your system
sudo apt install postgresql postgresql-contrib # helps you install postgresql with additional dependencies
sudo -i -u postgres 
sudo -u postgres createuser --interactive # takes you into the interactive mode
# go ahead a create the user with the username 
ALTER USER mob_db_user Password 'mob_db_pass'; 
use the command /q to exit the interactive session.
