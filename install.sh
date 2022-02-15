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

#install pip 
pip -V
if [[ $? -gt 0 ]]
then 
sudo apt install -y python3-pip
fi
# create the virtual env (env), active it, and install necessary app packages
sudo su - mob_app_usr -c "virtualenv env && . env/bin/activate && pip install -r ./Mobalysis/backend/requirements.txt"
