
import requests

from colorama import Fore, Style


def fetch_repos(org, token):
    """
    fetch org repos
    """

    print(Fore.GREEN
          + "\nFetch repos"
          + Style.RESET_ALL
          + f"\n- org: {org}")

    # build url
    url = f"https://api.github.com/orgs/{org}/repos"

    # build headers
    headers = {
        "Authorization": f"token {token}"
    }

    # iterate through pagination
    current_page = 1
    pagination = 100

    repos = []
    page_repos = []

    while True:

        # build params
        params = dict(
            per_page=pagination,
            page=current_page)

        print(f"retrieve page {current_page}")

        # list repos
        response = requests.get(url, headers=headers, params=params)

        if response.status_code != 200:

            print(Fore.RED
                  + "\nUnable to retrieve repositories 🤕"
                  + Style.RESET_ALL
                  + f"\n- response: {response.content}")

        # retrieve repos
        page_repos = response.json()

        # store response
        repos += page_repos

        # stop iteration
        if (len(page_repos) < pagination) or (page_repos == []):
            break

        # increment page
        current_page += 1

    return repos


if __name__ == '__main__':

    repos = fetch_repos("lewagon-test", "xxx")

    print(repos)
