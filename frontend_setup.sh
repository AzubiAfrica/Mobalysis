#!/bin/bash
sudo apt update
sudo apt install node.js nginx -y

cd frontend
npm install
npm run build

# Copy build files 
sudo cp -r build/* /var/www/html
# Remove nginx index file
sudo rm -rf /var/www/html/index.nginx.debian.html

# Restart nginx 
sudo systemctl restart nginx
