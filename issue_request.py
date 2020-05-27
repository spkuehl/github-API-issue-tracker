import requests

class IssueRequest:
    '''Access the github api to get issues based on label.
    '''

    def __init__(self, label, email, password):
        self.label = label
        self.email = email
        self.password = password

    def get_issues(self):
        r = requests.get('https://api.github.com/search/issues?q=label:"%s"'%(self.label),
                          auth=(self.email, self.password))
        return r
