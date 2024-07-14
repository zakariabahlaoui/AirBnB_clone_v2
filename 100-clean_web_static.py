#!/usr/bin/python3
"""This script contains do-clean function that deletes out-of-date archives"""
import os
from fabric.api import local, put, run, env, lcd, cd

# add web servers details to environement
env.hosts = ["100.26.20.174", "54.90.26.5"]
env.user = "ubuntu"
env.key_filename = "~/.ssh/id_rsa"


def do_clean(number=0):
    """Delete out-of-date archives

    Arguments:
        number (int): number of archives to keep.

                If number is 0 or 1, keeps only the most recent archive. If
                number is 2, keeps the most and second-most recent archives,
                etc.
    """
    number = 1 if int(number) == 0 else int(number)

    # local
    archives = sorted(os.listdir("versions"))
    # remove elements from the archives list
    for _ in range(number):
        archives.pop()
    # delete target files
    with lcd("versions"):
        for file in archives:
            local(f"rm ./{file}")

    # remote
    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        # remove elements from the archives list
        for _ in range(number):
            archives.pop()
        # delete target files
        for a in archives:
            run(f"rm -rf ./{file}")
