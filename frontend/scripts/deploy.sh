#Update ubuntu instance
sudo apt-get update

#Upgrade ubuntu
sudo apt-get upgrade -y

#Create the react-app
npx create-react-app react-tutorial

#Build the react project
cd react-tutorial
npm run build

#Run the project
npm start
