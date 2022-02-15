#!/bin/bash
sudo su - mob_app_usr -c"git clone https://github.com/redmicelles/Mobalysis"

#install pip 
pip -V
if [[ $? -gt 0 ]]
then 
sudo apt install -y python3-pip
fi
# create the virtual env (env), active it, and install necessary app packages
sudo su - mob_app_usr -c "virtualenv env && . env/bin/activate && pip install -r ./Mobalysis/backend/requirements.txt"
