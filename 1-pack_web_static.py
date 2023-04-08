#!/usr/bin/python3
"""A Fabric script that generates a .tgz archive from the contents of the web_static folder of your AirBnB Clone repo, using the function do_pack.
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """ a method to compress a file and return it's path """

    #saving the current timestamp and creatinf filename
    time_str = datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = "versions/web_static_{}.tgz".format(time_str)

    try:
        #creates  directory called versions
        local("mkdir -p versions")

        #create an archive file
        local("tar -cvzf {} web_static/".format(file_path))

        #return the path to the archive file created
        return "{}".format(file_path)

        #return none if an error occurs
    except Exception as e:
        return None

