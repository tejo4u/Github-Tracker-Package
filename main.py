from Github_user_info import Github_user_data
from Github_repo_info import Github_repo_data
from os import getenv

gittest = Github_repo_data(getenv('GITTOKEN'))
