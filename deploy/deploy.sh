#!/bin/bash
DIRECTORY=$(cd $(dirname $0) && pwd)

cd ..
virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt

cd deploy

sudo ln -s $DIRECTORY/clinic.supervisor.conf /etc/supervisor/conf.d/clinic.supervisor.conf
sudo supervisorctl reread
# sudo supervisorctl reload
sudo supervisorctl restart clinic
echo "enter any key to continue."
read
sudo ln -s $DIRECTORY/clinic.nginx.conf /etc/nginx/sites-available/

sudo ln -s $DIRECTORY/clinic.nginx.conf /etc/nginx/sites-available/clinic.nginx.conf
sudo ln -s /etc/nginx/sites-available/clinic.nginx.conf /etc/nginx/sites-enabled/clinic.nginx.conf
sudo nginx -t
echo "enter any key to continue with restarting nginx"
read
sudo service nginx restart
