from Github_user_info import Github_user_data
from os import getenv

#Test area
gittest = Github_user_data(getenv('GITTOKEN'))
#print gittest.get_user_repos('blackfalcon')
#print gittest.get_user_following('blackfalcon')
print gittest.get_user_email('blackfalcon')
print gittest.get_user_company('blackfalcon')
print gittest.get_user_location('blackfalcon')
print gittest.get_user_profile_link('blackfalcon')
print gittest.get_user_hireable_status('blackfalcon')
print gittest.get_avatar_link('blackfalcon')
