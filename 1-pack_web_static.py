#!/usr/bin/python3
"""Compress the contents of the web_static folder"""

from fabric import api
from datetime import datetime
import os


def do_pack():
    """Creates tarball of webstatic files from the web_static
    folder in Airbnb_v2.
    Returns: path of .tgz file on success, None otherwise
    """
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if os.isdir("versions") is False:
            api.local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        api.local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except:
        return None
