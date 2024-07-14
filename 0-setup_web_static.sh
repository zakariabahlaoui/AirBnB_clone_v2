#!/usr/bin/env bash
# This script sets up our web servers for the deployment of web_static

# install Nginx, if not installed
sudo apt-get update
sudo apt-get -y install nginx

# open port 80 on the firewall to allow incoming HTTP traffic
sudo ufw allow 'Nginx HTTP'

# create folders
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html

# fill index.html with fake content for testing sake
sudo echo "<!DOCTYPE html>
<html>
<head>
    <title>Document</title>
</head>
<body>
    <h1>I love Python ❤️</h1>
</body>
</html>" | sudo tee /data/web_static/releases/test/index.html


# create a symbolic link
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

# give ownership
sudo chown -R ubuntu:ubuntu /data/

# update the Nginx configuration to serve the content
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

# restart Nginx web server
sudo service nginx restart
