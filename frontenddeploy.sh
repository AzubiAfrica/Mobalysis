#!/bin/bash



#Deploy the react app inside /var/www/html directory and run it
sudo cd /var/www/html
sudo git clone https://github.com/wanguij/Mobalysis
sudo cd Mobalysis/frontend
sudo npm start 
sudo npm run build 


