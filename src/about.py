name           = "ProgramName"
version        = "0.1"
release_suffix = "a"

full_id = name + " v" + version + release_suffix

#Github
user_name          = "username"
repo_name          = "reponame"
repo_url           = "https://github.com/" + user_name + "/" + repo_name
pull_url           = "https://github.com/" + user_name + "/" + repo_name + "/pulls"
latest_release_url = "https://github.com/" + user_name + "/" + repo_name + "/releases/latest"

#Github API
latest_release_api = "https://api.github.com/repos/" + user_name + "/" + repo_name + "/latest"

#Data file
data_file_name = "config.txt"