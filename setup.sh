#!/bin/bash
sudo dpkg -s posgresql

if [ $? -eq 0 ]
then
  sudo apt-get --purge remove postgresql
  sudo rm -rf /var/lib/postgresql/
  sudo rm -rf /var/log/postgresql/
  sudo rm -rf /etc/postgresql/
fi

sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

sudo apt-get update

sudo apt-get -y install postgresql

sudo -u postgres psql -c "create user mod_db_user  with password 'mod_db_pass';"

sudo systemctl is-active --quiet  postgresql

if [ $? -ne 0 ]
then
  sudo systemctl start --quiet postgresql
  sudo systemctl enable --quiet postgresql
fi

echo "Postgresql installation completed"

