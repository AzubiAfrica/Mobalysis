#!/bin/bash

#Step 1.  setup.sh This code updates the package installer, installs postgresSQL and creates a new user with password.

sudo yum update -y
sudo yum install postgresql -y postgresql-contrib
sudo systemctl start postgresql
sudo -u postgres createuser -s mob_db_user
sudo -u postgres psql -c "ALTER USER mob_db_user WITH ENCRYPTED PASSWORD 'mob_db_pass';"




# step 2. modify setup.sh to create another linux user (mob_app_usr) VERONICA


# -d /home/mob_app_usr/ | set home directory of mob_app_usr
# -m | Create mob_app_usr home directory
# -G sudo | give sudo permissions to mob_app_usr

sudo useradd -s /bin/bash -d /home/mob_app_usr/ -m -G sudo mob_app_usr

