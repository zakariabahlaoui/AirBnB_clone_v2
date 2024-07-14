#!/usr/bin/python3
"""This script generates a .tgz archive from the contents of the web_static"""

from fabric.api import local
from time import strftime
import tarfile


def do_pack():
    """archive web_static folder as .tgz"""

    # create versions directory
    local("mkdir -p versions")

    # create the archive
    try:
        time_label = strftime("%Y%m%d%H%M%S")
        archive_name = f"versions/web_static_{time_label}.tgz"
        with tarfile.open(archive_name, 'w:gz') as tar:
            tar.add('web_static')

        return archive_name

    except Exception as e:
        return None
