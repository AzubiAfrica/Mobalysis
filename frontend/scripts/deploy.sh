#Update ubuntu instance
sudo apt-get update

#Upgrade ubuntu
sudo apt-get upgrade -y

#install ngnix
sudo apt-get install nginx -y


#nginx version
nginx -v


#restart nginx
sudo systemctl restart nginx
