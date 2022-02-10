# for mac user with homebrew installed use this command to update homebrew before installation of postgreSQL:
brew doctor
brew update
#for mac user without homebrew installed type this below in your terminal: 
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" #automatically installs homebrew
brew install postgresql #this will download and install it on your terminal. Do this after installing homebrew
brew services start postgresql # command to start using the database service
psql postgress # to start terminal with root privileges 
# to create a new user inside the psql terminal use new role user WITH 'PASSWORD'
CREATE ROLE mob_db WITH LOGIN PASSWORD 'mob_db_pass';
brew services stop postgresql # to stop using postgreSQL.
