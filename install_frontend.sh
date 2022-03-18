# Update packages 
sudo apt-get update -y 
sudo apt-get upgrade -y

#Add NodeJs PPA to the system 
curl -sL https://deb.nodesource.com/setup_16.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh

#install NodeJs 
sudo apt install nodejs

if [ $? -eq  0 ]
then
  echo "NodeJS successfully created"
else
  echo "NodeJs installation failed"
fi

#install Nginx
sudo apt -y install nginx
if [ $? -eq  0 ]
then
  echo "Nginx installed sucessfully"
else
  echo "Nginx installation failed!"
fi

#Allow Nginx through firewall
sudo ufw allow 'Nginx HTTP'

#Enable and restart Nginx service
sudo systemctl enable nginx
sudo systemctl restart nginx

#CD to WWW directory and clone the frontend directory from the repo
sudo git clone --branch dev https://github.com/redmicelles/Mobalysis /var/www/html/tmp
sudo mv /var/www/html/tmp/frontend /var/www/html
sudo rm -r /var/www/html/tmp

# #remove the nginx files 
# cd /var/www/html 
# rm index.nginx-debian.html index.html

# #install the necessary packages and build
# cd /var/www/html/frontend
# npm install 
# npm build

# #move the build files to /var/www/html
# sudo mv /var/www/html/frontend/build/* /var/www/html 

# #delete the frontend
# sudo rm -r /var/www/html/frontend

