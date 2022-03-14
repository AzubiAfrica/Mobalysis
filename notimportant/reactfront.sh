#!/bin/bash
# step 1 elevate privelleges and update system os  ME
sudo su
apt-get update

# step 2 install  curl  ME
apt-get install curl
curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -

# step 4 create react application ME
cd /var/www/html/
npx create-react-app react-tutorial
