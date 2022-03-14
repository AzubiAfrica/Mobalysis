#!/bin/bash
sudo apt-get update

#install  curl
sudo apt-get install curl
curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -

#install nginx
sudo apt-get install nginx -y


#install node.js
sudo apt-get install -y nodejs

cd /var/www/html/

#clone repo
sudo git clone https://github.com/sdg000/Mobalysis.git

#cd into frontend to install and run npm
cd Mobalysis/frontend

sudo npm install
sudo npm run build


#copy all files in  frontend/build to /var/www/html
#remove original html file from nginx
sudo cp -r /var/www/html/Mobalysis/frontend/build/* /var/www/html
sudo rm -rf index.nginx.debian.html

#restart nginx
sudo systemctl restart nginx
