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


