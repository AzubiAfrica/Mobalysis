#!/bin/bash




#install nginx 
sudo apt -get install nginx

#Check the nginx version and validate its installation
nginx -v 

sudo apt -get install curl
curl --version

#install nodejs 
sudo apt -get install -y nodejs 

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

