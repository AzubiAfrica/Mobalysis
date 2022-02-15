#!/bin/bash
#Clone repo and  create environment varables
sudo -i -u mob_app_usr bash << EOF
#clone mobalysis repo
git clone https://github.com/redmicelles/Mobalysis

#set Environment Variables
echo export DBNAME=\'mobalytics\' >> .bashrc
echo export DBUSER=\'mob_db_user\' >> .bashrc
echo export DBPASS=\'mob_db_pass\' >> .bashrc
echo export DBHOST=\'localhost\' >> .bashrc
echo export DBPORT=\'5432\' >> .bashrc
sudo -s source ~/.bashrc
EOF

#Create and Activate Virtual Environment
sudo -i -u mob_app_usr bash << EOF
python3 -m venv ~/Mobalysis/venv
# chmod 700 ~/Mobalysis/venv/bin/activate
# echo "mob_app_usr" | sudo -S -k whoami
EOF