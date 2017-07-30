# Tracks and fetches Github Users and Related info.
from github import Github
from urllib2 import urlopen, Request
import json

class Github_user_data:
    apiToken = ''
    git_user_object = None
    obj_username = None

    def __init__(self,usertoken,username=None):
        self.apiToken = str(usertoken)
        self.git_user_object = Github(self.apiToken)
        self.obj_username = username

    # Returns List of all the repos else returns empty list if username does not exits.
    def get_user_repos(self,username=None):
            if(username != None):
                temp_obj_username = self.obj_username
                self.obj_username = username

            user_repo_list = list()
            try:
                url = "https://api.github.com/users/"+ self.obj_username +"/repos"
                headers = {'Authorization': 'token %s' % self.apiToken}
                request = Request(url, headers=headers)
                response = urlopen(request)
                jsondata = json.loads(response.read())
                for i in range(0,len(jsondata)):
                    user_repo_list.append(jsondata[i]['name'])
            except:
                print "urllib2 connection error or bad input error! Run again."

            self.obj_username = temp_obj_username
            return user_repo_list

    # Returns total number of repositories of a user
    def get_total_repo_count(self,username=None):
        if(username !=None):
            return(len(self.get_user_repos(username)))
        return len(self.get_user_repos(self.obj_username))

    # Returns list of all the followers or returns an empy list if none exist or user not found
    def get_user_followers(self,username=None):
        if(username != None):
            temp_obj_username = self.obj_username
            self.obj_username =username

        user_follower_list = list()
        try:
            url = "https://api.github.com/users/"+ self.obj_username +"/followers"
            headers = {'Authorization': 'token %s' % self.apiToken}
            request = Request(url, headers=headers)
            response = urlopen(request)
            jsondata = json.loads(response.read())
            for i in range(0,len(jsondata)):
                user_follower_list.append(jsondata[i]['login'])
        except:
            print "urllib2 connection error or bad input error! Run again."

            self.obj_username = temp_obj_username
        return user_follower_list

    # Returns number of followers
    def get_total_followers_count(self,username=None):
        if(username !=None):
            return(len(self.get_user_followers(username)))
        return len(self.get_user_followers(self.obj_username))

    # Returns list of random 30 followers or returns an empy list if none exist or user not found
    def get_user_following(self,username=None):
        if(username != None):
            temp_obj_username = self.obj_username
            self.obj_username =username

        user_following_list = list()
        try:
            url = "https://api.github.com/users/"+ self.obj_username +"/following"
            headers = {'Authorization': 'token %s' % self.apiToken}
            request = Request(url, headers=headers)
            response = urlopen(request)
            jsondata = json.loads(response.read())
            for i in range(0,len(jsondata)):
                user_following_list.append(jsondata[i]['login'])
        except:
            print "urllib2 connection error or bad input error! Run again."

            self.obj_username = temp_obj_username
        return user_following_list

    # Returns number of followers
    def get_total_following_count(self,username=None):
        if(username !=None):
            return(len(self.get_user_following(username)))
        return len(self.get_user_following(self.obj_username))
