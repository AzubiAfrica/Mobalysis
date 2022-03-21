#!/bin/bash
#create frontenddeploy.sh
sudo touch frontenddeploy.sh

#update ubuntu instance
sudo -u apt-get update -y

#update ubuntu system
sudo -u apt-get upgrade -y

#install nginx
sudo -u apt-get install nginx -y

#nginx version
sudo -u nginx -v


sudo apt-get install curl
curl --version

#install nodejs 
sudo apt-get install -y nodejs 

#Deploy the react app inside /var/www/html directory and run it
sudo cd /var/www/html
sudo git clone https://github.com/wanguij/Mobalysis
sudo cd Mobalysis/frontend
sudo npm start 
sudo npm run build 

#Copy the build files into the /var/ww/html, delete the default index.html and replace with the new index file from the build operation and restart the nginx server
sudo -r cp /var/www/html/Mobalysis/frontend/build/* /var/www/html
sudo rm -rf index.nginx.debian.html
sudo systemctl restart nginx

