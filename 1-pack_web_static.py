#!/usr/bin/python3
"""A Fabric script that generates a .tgz archive from the contents of the web_static folder of your AirBnB Clone repo, using the function do_pack.
"""
from fabric.api import local
from datetime import datetime

@task
def do_pack():
    """Creates a compressed archive of static files and if created successfully it returns the path o       r None
    """
    #timestamp and staic file path variables
    time_stamp = datetime.now().strftime("%Y%m%d%H%M%S")
    static_files_path = "versions/web_static_{}.tgz".format(time_stamp)

    try:
        # Create the versions directory if it doesn't exist
        local("mkdir -p versions")

        #creating archive filename 
        local("tar -czvf {} web_static/".format(static_files_path))
        #return path to file if sucessful
        return static_files_path

    except Exception as e:

        return None
