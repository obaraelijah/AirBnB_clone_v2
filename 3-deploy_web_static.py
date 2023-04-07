#!/usr/bin/pytho
"""A module for web application deployment with Fabric."""
import os
from datetime import datetime
from fabric.api import env, local, put, run 

env.hosts = ['100.25.135.33', '34.207.253.223']
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
    compressed_file = archive_path.split("/")[-1]
    no_extension = compressed_file.split(".")[0]

    try:
        remote_path = "/data/web_static/releases/{}/".format(no_extension)
        sym_link = "/data/web_static/current"
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(remote_path))
        run("sudo tar -xvzf /tmp/{} -C {}".format(compressed_file,
                                                  remote_path))
        run("sudo rm /tmp/{}".format(compressed_file))
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
