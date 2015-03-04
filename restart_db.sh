#!/bin/bash
#
#-----------------------------------
# @autor: Wendell P. Barreto
# @email: wendellp.barreto@gmail.com
# @project: geroc
# @doc: restart_db.sh
# ----------------------------------


while true; do
    read -p "Are you using Linux (y or n)? " yn
    case $yn in
        [Yy]* )
        	sudo -u postgres psql -c 'DROP DATABASE geroc'
			sudo -u postgres psql -c 'CREATE DATABASE geroc'
			sudo -u postgres psql -c 'CREATE USER geroc_admin'
			sudo -u postgres psql -c 'GRANT ALL PRIVILEGES ON DATABASE geroc TO geroc_admin'
			# sudo -u postgres psql -d geroc -c 'CREATE EXTENSION hstore'

			break;;
        [Nn]* )
			psql -c 'DROP DATABASE geroc'
			psql -c 'CREATE DATABASE geroc'
			psql -c 'CREATE USER geroc_admin'
			psql -c 'GRANT ALL PRIVILEGES ON DATABASE geroc TO geroc_admin'
			# psql -d geroc -c 'CREATE EXTENSION hstore'

			break;;
        * ) echo "Please answer yes or no.";;
    esac
done

python manage.py syncdb
python manage.py collectstatic --noinput