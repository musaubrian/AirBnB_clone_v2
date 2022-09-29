#!/usr/bin/python3
"""
distributes archives to my web servers
"""
from fabric import api
from os import path


api.env.hosts = ["34.231.247.104", "35.170.64.140"]


def do_deploy(archive_path):
    if path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    if api.put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    if api.run("rm -rf /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if api.run("mkdir -p /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if api.run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(file, name)).failed is True:
        return False
    if api.run("rm /tmp/{}".format(file)).failed is True:
        return False
    if api.run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if api.run("rm -rf /data/web_static/releases/{}/web_static".
           format(name)).failed is True:
        return False
    if api.run("rm -rf /data/web_static/current").failed is True:
        return False
    if api.run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(name)).failed is True:
        return False
    return True
