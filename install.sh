sys_user="mob_app_usr"
user_dir=/home/$sys_user
echo "creating user with home directory..."
sudo useradd -m -d $user_dir $sys_user
echo "Cloning forked repository into home directory of user..."
cd $user_dir
echo "removing existing files from user directory..."
sudo rm -rf $user_dir/*
sudo git clone https://github.com/KateProject/Mobalysis.git
