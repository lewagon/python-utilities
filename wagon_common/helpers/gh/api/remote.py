"""
gh api remote cli helpers
"""

import requests


from wagon_common.helpers.git.remote import git_remote_get_url
from wagon_common.helpers.gh.url import extract_gnn_repo_from_github_url
from wagon_common.helpers.output import red


def gh_get_params_from_remote(path, name, token):
    """
    retrieve gh repo name and gh repo id from git remote
    """

    # get remote url
    remote_url = git_remote_get_url(path, name)

    # extract gnn and repo name from gh remote url
    extracted_gnn, extracted_repo = extract_gnn_repo_from_github_url(remote_url)

    # build gh api query url
    # url = f"https://api.github.com/orgs/{org}/repos"
    url = f"https://api.github.com/repos/{extracted_gnn}/{extracted_repo}"

    # build headers
    headers = {
        "Authorization": f"token {token}"
    }

    # list repo params
    response = requests.get(url, headers=headers)

    if response.status_code != 200:

        red("\nUnable to retrieve repository params 🤕",
            f"\n- response: {response.content}")

    # retrieve repo data
    data = response.json()

    gh_repo_id = data.get("id")
    gh_repo_node_id = data.get("node_id")
    gh_repo_name = data.get("name")
    gh_repo_fullname = data.get("full_name")
    gh_repo_url = data.get("html_url")

    return gh_repo_id, gh_repo_node_id, gh_repo_name, gh_repo_fullname, gh_repo_url


if __name__ == '__main__':

    res = gh_get_params_from_remote(
        "../../data-myriad/02-Data-Toolkit/02-Data-Sourcing/01-Stock-Market-API",
        "origin",
        "xxx")
    print(res)
