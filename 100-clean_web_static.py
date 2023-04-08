#!/usr/bin/python3
"""A module for web application deployment with Fabric."""
import os
from datetime import datetime
from fabric.api import env, local, put, run 

env.hosts = ['34.207.253.223', '100.25.135.33']
env.key_filename = '~/.ssh/school'
env.user = 'ubuntu'


def do_pack():
    """ a method to compress a file and return it's path """

    """saving the current timestamp and creatinf filename"""
    time_str = datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = "versions/web_static_{}.tgz".format(time_str)

    try:
        """create a directory called versions"""
        local("mkdir -p versions")

        """create an archive file"""
        local("tar -cvzf {} web_static/".format(file_path))

        """return the path to the archive file created"""
        return "{}".format(file_path)

        """return none if an error occurs"""
    except Exception as e:
        return None


def do_deploy(archive_path):
    """a function to deploy code and decompress it"""

    if not os.path.isfile(archive_path):
        return False
    compressed_filename = archive_path.split("/")[-1]
    no_extension_file = compressed_filename.split(".")[0]

    try:
        remote_path = "/data/web_static/releases/{}/".format(no_extension_file)
        sym_link = "/data/web_static/current"
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(remote_path))
        run("sudo tar -xvzf /tmp/{} -C {}".format(compressed_filename,
                                                  remote_path))
        run("sudo rm /tmp/{}".format(compressed_filename))
        run("sudo mv {}/web_static/* {}".format(remote_path, remote_path))
        run("sudo rm -rf {}/web_static".format(remote_path))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -sf {} {}".format(remote_path, sym_link))
        return True
    except Exception as e:
        return False


def deploy():
    """Create and deploy an archive to a web server."""
    file_path = do_pack()
    if file_path is None:
        return False
    return do_deploy(file_path)

def do_clean(number=0):
    """Deletes out-of-date archives of the static files.
    Args:
        number (Any): The number of archives to keep.
    """
    #list of all archives in the 'versions' directory
    archives = os.listdir('versions/')
    archives.sort(reverse=True)
    # Determines the index of the first archive to delete
    start = int(number)
    if not start:
        start += 1
    if start < len(archives):
        archives = archives[start:]
    else:
        archives = []
    for archive in archives:
        os.unlink('versions/{}'.format(archive))
    #shell command to delete old releases from server
    cmd_parts = [
        "rm -rf $(",
        "find /data/web_static/releases/ -maxdepth 1 -type d -iregex",
        " '/data/web_static/releases/web_static_.*'",
        " | sort -r | tr '\\n' ' ' | cut -d ' ' -f{}-)".format(start + 1)
    ]
    run(''.join(cmd_parts))
