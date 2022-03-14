# Update packages 
sudo apt-get update -y 
sudo apt-get upgrade -y

#Add NodeJs PPA to the system 
curl -sL https://deb.nodesource.com/setup_16.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh

#install NodeJs 
sudo apt install nodejs

#check if NodeJS is installed 
node –v

if [ $? eq  0]
then
  echo "NodeJS successfully created"
else
  echo "NodeJs installation failed"
  exit 1
fi
