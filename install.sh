<<<<<<< HEAD
#!/bin/bash

# Navigate to user home directory
sys_user="mob_app_usr"
sys_user_dir=/home/$sys_user

cd $sys_user_dir
echo -e "Current directory: $(pwd)\n"

# Check if Mobalysis repo exists - if yes, delete it
if [[ -d "./Mobalysis" ]]
then
    echo -e "Mobalysis folder exists in current directory. Deleting it..."
    rm -rf ./Mobalysis
    echo -e "Deletion complete.\n"
fi

# Clone Mobalysis repo
sudo git clone https://github.com/PatProMath/Mobalysis.git

# Switch from current user to sys_user -> because we want to run the commands to set the environment variables as the sys_user
# Altenative: use command below for each line to set variable
# sudo su --login --command 'echo "export DBNAME=mobalytics" >> ~/.bashrc' $sys_user 
sudo -u $sys_user bash << EOF
# Add environment variables to user .bashrc file
echo "export DBNAME=mobalytics" >> ~/.bashrc
echo "export DBUSER=mob_db_user" >> ~/.bashrc
echo "export DBPASS=mob_db_pass" >> ~/.bashrc
echo "export DBHOST=localhost" >> ~/.bashrc
echo "export DBPORT=5432" >> ~/.bashrc

# Reinitialise .bashrc file to activate environment variables
source ~/.bashrc

# Finish executing script as sys_user
EOF
