

#!/bin/bash
sudo apt update
sudo apt install node.js nginx -y
cd Mobalysis/frontend
npm install
npm run build

