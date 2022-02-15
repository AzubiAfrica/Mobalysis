#!/bin/bash
sudo su - mob_app_usr -c"git clone https://github.com/redmicelles/Mobalysis"

#install pip 
sudo apt install -y python3-pip
# create the virtual env (env), active it, and install necessary app packages
sudo su - mob_app_usr -c "virtualenv env && . env/bin/activate && pip3 install -r ./Mobalysis/backend/requirements.txt"
