#elevate privelleges and update system os 
sudo su
apt-get update

#install  curl  
apt-get install curl
curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -

#install nginx 
apt-get install nginx -y


#install node.js 
apt-get install -y nodejs

cd /var/www/html/

#clone repo
sudo git clone https://github.com/sdg000/Mobalysis.git

#cd into frontend to install and run npm
cd Mobalysis/frontend
npm install
npm run build


#copy all files in  frontend/build to /var/www/html 
#remove original html file from nginx
cp -r /var/www/html/Mobalysis/frontend/build/* /var/www/html
rm -rf index.nginx.debian.html

#restart nginx
systemctl restart nginx
