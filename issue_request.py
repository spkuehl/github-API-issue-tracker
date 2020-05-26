import requests

class IssueRequest:
    '''Access the github api to get issues based on label.
    '''

    def __init__(self, label, email, password, filter='all'):
        self.label = label
        self.filter = filter
        self.email = email
        self.password = password

    def get_issues(self):
        r = requests.get('https://api.github.com/issues?filter=%s&labels=%s'%(self.filter, self.label),
                          auth=(self.email, self.password))
        return r
