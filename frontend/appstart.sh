#!/bin/bash
sudo apt-get update

#install  curl
sudo apt-get install curl
curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -

#install nginx
sudo apt-get install nginx -y

