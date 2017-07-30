from Github_user_info import Github_user_data
from os import getenv

#Test area
gittest = Github_user_data(getenv('GITTOKEN'),'user_login_name')
print gittest.get_user_followers()
