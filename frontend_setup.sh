#!/bin/bash
sudo apt update
sudo apt install node.js nginx -y
cd frontend
npm install
npm run build
