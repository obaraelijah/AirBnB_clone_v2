#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

#installing nginx
sudo apt-get update
sudo apt-get -y install nginx

#creating the directories
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# Create a fake HTML file
echo "<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create symbolic link and give ownership to ubuntu user and group
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/

#Update Nginx configuration
sudo sed -i '/server_name _;/a \ \tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n' /etc/nginx/sites-available/default

#restart the server
sudo service nginx restart

