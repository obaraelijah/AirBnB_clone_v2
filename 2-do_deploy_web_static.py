#!/usr/bin/python3
# Fabric script (based on the file 1-pack_web_static.py) that distributes an archive to your web servers, using the function do_deploy

from fabric.api import run, env, put
import os.path

env.hosts = ['34.207.253.223', '100.25.135.33']
env.key_filename = '~/.ssh/school'
env.user = 'ubuntu'

def do_deploy(archive_path):
    """Deploys and decompresses code"""

    if not os.path.isfile(archive_path):
        return False
    compressed_filename = archive_path.split("/")[-1]
    no_extension_filename = compressed_filename.split(".")[0]

    try:
        remote_path = "/data/web_static/releases/{}/".format(no_extension_filename)
        symbol_link = "/data/web_static/current"
        put(archive_path, "/tmp/")
        run("sudo mkdir - p {}".format(remote_path))
        run("sudo tar -xvzf /tmp/{} -C {}".format(compressed_filename, remote_path))
        run("sudo rm /tmp/{}".format(compressed_filename))
        run("sudo mv {}/web_static/* {}".format(remote_path))
        run("sudo rm -rf {}/web_static".format(remote_path))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -sf {} {}".format(remote_path, symbol_link))
        return True

    except Exception as e:
        return False

