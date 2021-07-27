import os
import tempfile

# the name of the program
name           = "PySide2 Template"
# the current version
version        = "1.0"
release_suffix = ""

# complete name of the software including version
full_id = name + " v" + version + release_suffix

# Github
user_name          = "CaptainDario"
repo_name          = "PySide2-template"
repo_url           = "https://github.com/" + user_name + "/" + repo_name
pull_url           = "https://github.com/" + user_name + "/" + repo_name + "/pulls"
latest_release_url = "https://github.com/" + user_name + "/" + repo_name + "/releases/latest"

# Github API
latest_release_api = "https://api.github.com/repos/" + user_name + "/" + repo_name + "/releases/latest"

# Data file name (file in which settings will be stored)
data_file_name = "config.txt"

def toString():
    """Returns an about string.
    """

    about =  "# " + name + "\n\n"
    about += "version:" + full_id + "\n\n\n"

    about += "## GitHub info \n\n"
    about += "repository name: " + repo_name + "\n\n"
    about += "repository url: [" + repo_url + "](" + repo_url +")\n\n"
    about += "latest releases: [" + latest_release_url + "](" + latest_release_url + ")\n\n"

    about += "config file stored at: " + os.path.join(tempfile.gettempdir(), name, data_file_name)

    return about