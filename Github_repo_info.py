from urllib2 import urlopen, Request
import json

class Github_repo_data:
    apiToken = ''
    git_user_object = None
    obj_username = None
    custom_repo_name=None
    custom_url = None

    def __init__(self,usertoken,username=None,repo_name=None):
        self.apiToken = str(usertoken)
        self.obj_username = username
        self.custom_repo_name = repo_name

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

    def get_latest_commit(self,username=None,repo_name=None,branch='master'):
        temp_obj_username=None
        temp_obj_reponame=None
        if(username!=None and repo_name!=None):
            temp_obj_reponame = self.obj_username
            temp_obj_reponame = self.custom_repo_name
            self.obj_username=username
            self.custom_repo_name = repo_name

        latest_commit_url = "https://api.github.com/repos/"+str(self.obj_username)+"/"+str(self.custom_repo_name)+"/commits?per_page=1&sha="+str(branch)
        latest_commit_json = self.get_raw_json(latest_commit_url)
        commit_detail_dict = dict()

        commit_detail_dict['name']=latest_commit_json[0]['commit']['committer']['name']
        commit_detail_dict['date']=latest_commit_json[0]['commit']['committer']['date']
        commit_detail_dict['msg']=latest_commit_json[0]['commit']['message']
        commit_detail_dict['url']=latest_commit_json[0]['html_url']

        self.obj_username = temp_obj_username
        self.custom_repo_name = temp_obj_reponame
        return commit_detail_dict

    def get_commits(self,username,repo_name,branch='master',last_n=5,all_commits=False):
        temp_obj_username=None
        temp_obj_reponame=None
        if(username!=None and repo_name!=None):
            temp_obj_reponame = self.obj_username
            temp_obj_reponame = self.custom_repo_name
            self.obj_username=username
            self.custom_repo_name = repo_name

        commit_dict_list = list()
        range_count = last_n

        isNotLastCommit = True
        page_index=0

        while isNotLastCommit != []:

            latest_commit_url = "https://api.github.com/repos/"+str(self.obj_username)+"/"+str(self.custom_repo_name)+"/commits?page=" + str(page_index) + "&per_page=100&sha="+str(branch)
            latest_commit_json = self.get_raw_json(latest_commit_url)
            isNotLastCommit = latest_commit_json[len(latest_commit_json)-1]['parents']

            if(all_commits == True):
                range_count = len(latest_commit_json)

            for i in range(0,range_count):
                commit_detail_dict=dict()
                commit_detail_dict['name']=latest_commit_json[i]['commit']['committer']['name']
                commit_detail_dict['date']=latest_commit_json[i]['commit']['committer']['date']
                commit_detail_dict['msg']=latest_commit_json[i]['commit']['message']
                commit_detail_dict['url']=latest_commit_json[i]['html_url']
                commit_dict_list.append(commit_detail_dict)

            if(range_count == last_n):
                break;
            page_index+=1


        self.obj_username = temp_obj_username
        self.custom_repo_name = temp_obj_reponame

        return commit_dict_list
    def get_latest_pull_request(self,username=None,repo_name=None,branch='master'):
        temp_obj_username=None
        temp_obj_reponame=None
        if(username!=None and repo_name!=None):
            temp_obj_reponame = self.obj_username
            temp_obj_reponame = self.custom_repo_name
            self.obj_username=username
            self.custom_repo_name = repo_name

        latest_pulls_url = "https://api.github.com/repos/"+str(self.obj_username)+"/"+str(self.custom_repo_name)+"/pulls"
        latest_pulls_json = self.get_raw_json(latest_pulls_url)
        pulls_detail_dict = dict()

        pulls_detail_dict['Title'] = latest_pulls_json[0]['title']
        pulls_detail_dict['Body'] = latest_pulls_json[0]['body']
        pulls_detail_dict['Url'] = latest_pulls_json[0]['diff_url']
        pulls_detail_dict ['login'] = latest_pulls_json[0]['user']['login']


        self.obj_username = temp_obj_username
        self.custom_repo_name = temp_obj_reponame
        return pulls_detail_dict

    def get_pulls(self,username,repo_name,last_n=5,all_pulls=False):
        temp_obj_username=None
        temp_obj_reponame=None
        if(username!=None and repo_name!=None):
            temp_obj_reponame = self.obj_username
            temp_obj_reponame = self.custom_repo_name
            self.obj_username=username
            self.custom_repo_name = repo_name

        pulls_dict_list = list()

        latest_pulls_url = "https://api.github.com/repos/"+str(self.obj_username)+"/"+str(self.custom_repo_name)+"/pulls"
        latest_pulls_json = self.get_raw_json(latest_pulls_url)

        if(all_pulls == True):
            range_count = len(latest_pulls_json)
        else:
            range_count = last_n

        for i in range(0,range_count):
            pulls_detail_dict=dict()

            pulls_detail_dict['Title'] = latest_pulls_json[i]['title']
            pulls_detail_dict['Body'] = latest_pulls_json[i]['body']
            pulls_detail_dict['Url'] = latest_pulls_json[i]['diff_url']
            pulls_detail_dict ['login'] = latest_pulls_json[i]['user']['login']

            pulls_dict_list.append(pulls_detail_dict)

        self.obj_username = temp_obj_username
        self.custom_repo_name = temp_obj_reponame

        return pulls_dict_list
