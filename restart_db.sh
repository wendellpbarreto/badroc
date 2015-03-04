#!/bin/bash
#
#-----------------------------------
# @autor: Wendell P. Barreto
# @email: wendellp.barreto@gmail.com
# @project: badroc
# @doc: restart_db.sh
# ----------------------------------


while true; do
    read -p "Are you using Linux (y or n)? " yn
    case $yn in
        [Yy]* )
        	sudo -u postgres psql -c 'DROP DATABASE badroc'
			sudo -u postgres psql -c 'CREATE DATABASE badroc'
			sudo -u postgres psql -c 'CREATE USER badroc_admin'
			sudo -u postgres psql -c 'GRANT ALL PRIVILEGES ON DATABASE badroc TO badroc_admin'
			# sudo -u postgres psql -d badroc -c 'CREATE EXTENSION hstore'

			break;;
        [Nn]* )
			psql -c 'DROP DATABASE badroc'
			psql -c 'CREATE DATABASE badroc'
			psql -c 'CREATE USER badroc_admin'
			psql -c 'GRANT ALL PRIVILEGES ON DATABASE badroc TO badroc_admin'
			# psql -d badroc -c 'CREATE EXTENSION hstore'

			break;;
        * ) echo "Please answer yes or no.";;
    esac
done

python manage.py syncdb
python manage.py collectstatic --noinput