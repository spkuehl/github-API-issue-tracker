# Github API Issue Requests

Python library utilizing the Github API to find Issues by keyword.

## Installation

Clone the repository.

Install the requirements in a virtual environment.

Securely add your Github credentials as local environment variables (`your_gh_email` and `your_gh_pw`). [(docs)](https://docs.python.org/3/library/os.html#os.environ)

## Usage


    import os
    import issue_request as ir

    issue_request = ir.IssueRequest(label = 'good first issue',
                                    email = os.environ['your_gh_email'],
                                    password = os.environ['your_gh_pw'])
    r = issue_request.get_issues()

Or open a jupyter notebook and play around.

## Notebook Sample



## Contributing
Pull requests are always welcome. For major changes, please open an issue first to discuss what you would like to change.
