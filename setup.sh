#!/bin/bash
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

sudo apt-get update

sudo apt-get -y install postgresql

sudo systemctl is-active --quiet  postgresql

if [ $? -ne 0 ]
then
  sudo systemctl start --quiet postgresql
  sudo systemctl enable --quiet postgresql
fi

sudo -u postgres psql -c "create user mob_db_user  with password 'mob_db_pass';"

echo "Postgresql installation completed"

#create user and home directory 
sudo useradd -m  mob_app_usr -p mob_app_usr

#install python-venv
res=$(python3 -c 'import sys; print(sys.version_info[0])')
if [[ "$res" -eq 3 ]]
then
   echo "python 3 version installed"  
   virtualenv --version
   if [[ "$?" -gt 0 ]]
   then
     sudo apt -y install python3-virtualenv
   fi
elif [[ "$res" -eq 2 ]]
then
  echo "python 2 version installed"
  virtualenv --version
  if [[ "$?" -gt 0 ]]
  then
    sudo apt -y install python-virtualenv
  fi
else
echo "python not installed"
sudo apt -y install python3
sudo apt -y install python3-virtualenv
fi

#create the database and assign it to the mob_db_user
sudo -u postgres psql <<EOF 
CREATE DATABASE Mobalytics; 
ALTER DATABASE Mobalytics OWNER TO mob_db_user;
EOF

