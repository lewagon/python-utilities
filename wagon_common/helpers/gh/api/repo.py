"""
gh api repo cli helpers
"""

import requests

from colorama import Fore, Style


def gh_repo_list(fullname, token=None):
    """
    list repo
    """

    # build gh api query url
    # url = f"https://api.github.com/orgs/{org}/repos"
    url = f"https://api.github.com/repos/{fullname}"

    # build headers
    headers = {}

    if token is not None:

        headers = {
            "Authorization": f"token {token}"
        }

    # list repo
    response = requests.get(url, headers=headers)

    if response.status_code == 404:

        # repo does not exist
        return None

    if response.status_code != 200:

        print(Fore.RED
              + "\nUnable to get repository 🤕"
              + Style.RESET_ALL
              + f"\n- response: {response.content}")

        return None

    return response.json()


def gh_repo_rename(fullname, new_name, token):
    """
    change repo name
    """

    # build gh api query url
    # url = f"https://api.github.com/orgs/{org}/repos"
    url = f"https://api.github.com/repos/{fullname}"

    # build headers
    headers = {
        "Authorization": f"token {token}"
    }

    # build json params
    json_params = {
        "name": new_name
    }

    # list repo params
    response = requests.patch(url, headers=headers, json=json_params)

    if response.status_code != 200:

        print(Fore.RED
              + "\nUnable to update repository name 🤕"
              + Style.RESET_ALL
              + f"\n- response: {response.content}")


def gh_api_repo_create(org, name, token):
    """
    create repo
    """

    # build gh api query url
    url = f"https://api.github.com/orgs/{org}/repos"

    # build headers
    headers = {
        "Authorization": f"token {token}"
    }

    # build json params
    json_params = {
        "name": name,
        "private": True
    }

    # list repo params
    response = requests.post(url, headers=headers, json=json_params)

    if response.status_code != 201:

        print(Fore.RED
              + "\nUnable to create repository 🤕"
              + Style.RESET_ALL
              + f"\n- status code: {response.status_code}"
              + f"\n- response: {response.content}")

        return None

    return response.json()


def gh_api_repo_update(org, name, token):
    """
    update repo
    """

    # build gh api query url
    url = f"https://api.github.com/repos/{org}/{name}"

    # build headers
    headers = {
        "Authorization": f"token {token}"
    }

    # build json params
    json_params = {
        "private": True
    }

    # list repo params
    response = requests.patch(url, headers=headers, json=json_params)

    if response.status_code != 200:

        print(Fore.RED
              + "\nUnable to update repository 🤕"
              + Style.RESET_ALL
              + f"\n- status code: {response.status_code}"
              + f"\n- response: {response.content}")

        return None

    return response.json()


if __name__ == '__main__':

    gh_pat = "xxx"

    # gh_repo_rename(
    #     "lewagon-test/data-01-02-optional-01-olympic-winter-games",
    #     "some-tmp-name",
    #     gh_pat)

    # repo = gh_repo_list(
    #     "lewagon/data-solutions",
    #     gh_pat)

    # print(repo)

    # gh_api_repo_create(
    #     "lewagon-test",
    #     "abcd",
    #     gh_pat)

    gh_api_repo_update(
        "lewagon-test",
        "abcd",
        gh_pat)
