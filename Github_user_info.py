from urllib2 import urlopen, Request
import json

class Github_user_data:
    apiToken = ''
    git_user_object = None
    obj_username = None
    custom_url=None

    def __init__(self,usertoken,username=None,cust_api_url=None):
        self.apiToken = str(usertoken)
        self.obj_username = username
        self.custom_url = cust_api_url

    def get_raw_json(self,url=None):
        temp_api_url = None

        if(url!=None):
            temp_api_url = self.custom_url
            self.custom_url = url

        headers = {'Authorization': 'token %s' % self.apiToken}
        request = Request(self.custom_url, headers=headers)
        response = urlopen(request)
        raw_json = json.loads(response.read())

        self.custom_url = temp_api_url
        return raw_json

    # Returns List of all the repos else returns empty list if username does not exits.
    def get_user_repos(self,username=None):
        temp_obj_username = None

        if(username != None):
            temp_obj_username = self.obj_username
            self.obj_username = username

        user_repo_list = list()

        userurl = "https://api.github.com/users/"+ str(self.obj_username)
        user_json_data = self.get_raw_json(userurl)

        total_pages = 0
        total_repos =int(user_json_data['public_repos'])

        if(total_repos % 30  < 1):
                total_pages = 1
        else:
                total_pages= (total_repos % 30)+1

        for page_number in range(1,total_pages):
                page_repo_url = "https://api.github.com/users/"+ self.obj_username +"/repos?page="+str(page_number)+"&per_page=30'"
                repo_json_data = self.get_raw_json(page_repo_url)
                for i in range(0,len(repo_json_data)):
                    user_repo_list.append(repo_json_data[i]['name'])

        self.obj_username = temp_obj_username
        return user_repo_list

    # Returns total number of repositories of a user
    def get_total_repo_count(self,username=None):
        temp_obj_username = self.obj_username
        if(username!=None):
            self.obj_username = username
        user_repo_count_url = "https://api.github.com/users/"+ str(self.obj_username)
        self.obj_username = temp_obj_username
        return self.get_raw_json(user_repo_count_url)['public_repos']


    # Returns list of all the followers or returns an empy list if none exist or user not found
    def get_user_followers(self,username=None):
        temp_obj_username = None

        if(username != None):
                temp_obj_username = self.obj_username
                self.obj_username = username

        user_follower_list = list()

        userurl = "https://api.github.com/users/"+ str(self.obj_username)
        user_json_data = self.get_raw_json(userurl)

        total_pages = 0
        total_followers =int(user_json_data['followers'])

        if(total_followers % 30  < 1):
                    total_pages = 1
        else:
                    total_pages= (total_followers % 30)+1

        for page_number in range(1,total_pages):
                    page_follower_url = "https://api.github.com/users/"+ self.obj_username +"/followers?page="+str(page_number)+"&per_page=30'"
                    followers_json_data = self.get_raw_json(page_follower_url)
                    for i in range(0,len(followers_json_data)):
                        user_follower_list.append(followers_json_data[i]['login'])

        self.obj_username = temp_obj_username
        return user_follower_list

    # Returns number of followers
    def get_total_followers_count(self,username=None):
        temp_obj_username = self.obj_username
        if(username!=None):
                self.obj_username = username
        user_follwer_count_url = "https://api.github.com/users/"+ str(self.obj_username)
        self.obj_username = temp_obj_username
        return self.get_raw_json(user_follwer_count_url)['followers']

    # Returns list of random 30 followers or returns an empy list if none exist or user not found
    def get_user_following(self,username=None):
        temp_obj_username = None

        if(username != None):
                    temp_obj_username = self.obj_username
                    self.obj_username = username

        user_following_list = list()

        userurl = "https://api.github.com/users/"+ str(self.obj_username)
        user_json_data = self.get_raw_json(userurl)

        total_pages = 0
        total_following =int(user_json_data['followers'])

        if(total_following % 30  < 1):
                        total_pages = 1
        else:
                        total_pages= (total_following % 30)+1

        for page_number in range(1,total_pages):
                        page_following_url = "https://api.github.com/users/"+ self.obj_username +"/following?page="+str(page_number)+"&per_page=30'"
                        following_json_data = self.get_raw_json(page_following_url)
                        for i in range(0,len(following_json_data)):
                            user_following_list.append(following_json_data[i]['login'])

        self.obj_username = temp_obj_username
        return user_following_list

    # Returns number of followers
    def get_total_following_count(self,username=None):
        temp_obj_username = self.obj_username
        if(username!=None):
                self.obj_username = username
        user_follwing_count_url = "https://api.github.com/users/"+ str(self.obj_username)
        self.obj_username = temp_obj_username
        return self.get_raw_json(user_follwing_count_url)['following']

    def get_user_location(self,username):
        location_retrive_url = "https://api.github.com/users/"+ str(username)
        return self.get_raw_json(location_retrive_url)['location']

    def get_user_company(self,username):
        company_retrive_url = "https://api.github.com/users/"+ str(username)
        return self.get_raw_json(company_retrive_url)['company']

    def get_user_email(self,username):
        user_mail_retrive_url = "https://api.github.com/users/"+ str(username)
        return self.get_raw_json(user_mail_retrive_url)['email']
    def get_user_full_name(self,username):
        user_full_name_url = "https://api.github.com/users/"+ str(username)
        return self.get_raw_json(user_full_name_url)['name']
    def get_user_hireable_status(self,username):
        user_hireable_status_url = "https://api.github.com/users/"+ str(username)
        return self.get_raw_json(user_hireable_status_url)['hireable']
    def get_avatar_link(self,username):
        avatar_user_link_url ="https://api.github.com/users/"+ str(username)
        return self.get_raw_json(avatar_user_link_url)['avatar_url']
    def get_user_profile_link(self,username):
        user_profile_link_url = "https://api.github.com/users/"+ str(username)
        return self.get_raw_json(user_profile_link_url)['html_url']
    def is_following(self,fromuser,touser):
        following_url = "https://api.github.com/users/"
