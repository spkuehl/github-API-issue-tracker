import os
import issue_request as ir
import pytest
import requests


def test_request_status_ok():
    issue_request = ir.IssueRequest(label = 'bug',
                                    email = os.environ['your_gh_email'],
                                    password = os.environ['your_gh_pw'])
    r = issue_request.get_issues()
    assert r.status_code == requests.codes.ok
