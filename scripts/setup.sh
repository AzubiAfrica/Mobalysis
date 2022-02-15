
#!/bin/bash

#Step 1
# This code updates the package installer, installs postgresSQL and creates a new user with password.
sudo apt update
sudo apt install postgresql -y postgresql-contrib
sudo -u postgres psql
sudo -u postgres createuser -s mob_db_user
sudo -u postgres psql -c "ALTER USER mob_db_user WITH ENCRYPTED PASSWORD 'mob_db_pass' ";



#Step 2
# -d /home/mob_app_usr/ – Set /home/mob_app_usr/ as home directory of the new user
# -m – Create the user’s home directory
# -G sudo – Make sure mob_app_usr user can sudo i.e. give admin access to the new user
sudo useradd -s /bin/bash -d /home/mob_app_usr/ -m -G sudo mob_app_usr









