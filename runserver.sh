#!/bin/sh
# switch to project root..
cd /var/www/forum

# start the server..
manage.py runserver `hostname -i`:80

# restart apache2..
service apache2 reload

