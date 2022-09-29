#!/usr/bin/env python3
"""
generate an archive from the web_static folder
"""
from datetime import datetime
import os
from fabric import api


def do_pack():
    with api.settings(warn_only=True):
        check_dir = os.path.isdir("versions")
        if not check_dir:
            create_dir = api.local('mkdir versions')
            if create_dir.failed:
                return None
            suffix = datetime.now().strftime('%Y%m%d%M%S')
            path = 'versions/web_static_{}.tgz'.format(suffix)
            tar = api.local('tar -cvzf {} web_static'.format(path))
            if tar.failed:
                return None
            size = os.stat(path).st_size
            print('web_static packed: {} -> {}Bytes'.format(path, size))
            return path
