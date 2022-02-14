#Modify the setup.sh script to add an operating system user mob_app_usr 
#The script should install a home directory for the user

username="mob_app_usr"
if getent passwd "$username" > /dev/null 2>&1; then
    #echo "The username '$username' exits."
else
    #echo "The user '$username' does not exit. Lets create the user.
    useradd mob_app_usr -m -d /home/mob_app_usr
    #echo "User successfully created"
fi