#!/bin/bash
# Navigate to home directory
echo "Navigating to home folder"
cd $HOME
echo -e "Current directory: $(pwd)\n"
# Check if Mobalysis repo exists - if yes, delete it
if [[ -f "./Mobalysis" ]]
then
    echo -e "Mobalysis folder exists in current directory. Deleting it..."
    rm -rf ./Mobalysis
    echo -e "Deletion complete.\n"
fi
# Clone Mobalysis repo
echo -e "Cloning Mobalysis repo\n"
wget https://github.com/PatProMath/Mobalysis
echo -e "Finished cloning\n"
