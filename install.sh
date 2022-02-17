#!/bin/bash

# Creates a virtual environment env
python3 -m venv env

# Activates the virtual environment env
source env/bin/activate

# Install the packages that are found in the requirements.txt file
# pip3 install -r Mobalysis/backend/requirements.txt
python3 -m pip install -r Mobalysis/backend/requirements.txt