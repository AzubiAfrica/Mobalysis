#Update ubuntu instance
sudo apt-get update

#Upgrade ubuntu
sudo apt-get upgrade -y



#Create the react-app
npx create-react-app react-tutorial

#Clone react project
cd /var/www/html/
sudo git clone https://github.com/koladeA/Mobalysis
cd Mobalysis/frontend
sudo npm install
sudo npm run build

#Run the project
npm start


#install ngnix
sudo apt-get install nginx -y


#nginx version
nginx -v


#restart nginx
sudo systemctl restart nginx


#install nodejs ubuntu
sudo apt-get install curl
curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
sudo apt-get install -y nodejs
