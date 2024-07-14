#!/usr/bin/python3
"""This script distributes the created archive to the web servers"""

from fabric.api import local, put, run, env
import os


# add web servers details to environement
env.hosts = ["35.153.67.198", "54.144.197.101"]
env.user = "ubuntu"
env.key_filename = "~/.ssh/id_rsa"


def do_deploy(archive_path):
    """distributes an archive to the web servers"""

    # check given archive path
    if not os.path.isfile(archive_path):
        return False

    try:
        # upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")

        # uncompress the archive to the target folder
        time_label = archive_path[-18:-4]  # extract timestamp, no extension
        server_archive = f"/tmp/web_static_{time_label}.tgz"
        target_folder = f"/data/web_static/releases/web_static_{time_label}"
        run(f"sudo mkdir -p {target_folder}")
        run(f"sudo tar -xzf {server_archive} -C {target_folder}/")

        # get content outside of web_static directory
        run(f"sudo mv {target_folder}/web_static/* {target_folder}/")
        run(f"sudo rm -rf {target_folder}/web_static")  # delete web_static dir

        # delete archive from /tmp - not needed anymore
        run(f"sudo rm {server_archive}")

        # delete any existing symbolic link
        run("sudo rm -rf /data/web_static/current")

        # create new symbolic link
        run(f"sudo ln -s {target_folder}/ /data/web_static/current")

        return True

    except Exception as e:
        return False