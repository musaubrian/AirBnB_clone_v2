#!/usr/bin/env bash
# sets-up web server for deployment of web_static

index_path="/data/web_static/releases/test/"
sudo apt update
sudo apt upgrade -y
sudo apt install nginx -y
sudo mkdir -p $index_path
echo "Hello world!!" | sudo tee $index_path/index.html
sudo ln -sf "/data/web_static/current" "/data/web_static/releases/test/"
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias
/data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx start
