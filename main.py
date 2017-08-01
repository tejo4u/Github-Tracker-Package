from Github_user_info import Github_user_data
from os import getenv

#Test area
gittest = Github_user_data(getenv('GITTOKEN'))
#print gittest.get_user_repos('gajeshbhat')
#print gittest.get_user_following('blackfalcon')
print gittest.get_user_email('gajeshbhat')
print gittest.get_user_company('gajeshbhat')
print gittest.get_user_location('gajeshbhat')
print gittest.get_user_profile_link('gajeshbhat')
print gittest.get_user_hireable_status('gajeshbhat')
print gittest.get_avatar_link('gajeshbhat')
