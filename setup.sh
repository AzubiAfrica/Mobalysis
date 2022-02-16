#!/bin/bash

#Step 1.  setup.sh This code updates the package installer, installs postgresSQL and creates a new user with password.

sudo yum update -y
sudo yum install postgresql -y postgresql-contrib
sudo systemctl start postgresql
sudo -u postgres createuser -s mob_db_user
sudo -u postgres psql -c "ALTER USER mob_db_user WITH ENCRYPTED PASSWORD 'mob_db_pass';"
