
import re
import os

from colorama import Fore, Style

from wagon_common.helpers.git.clone import clone_repo


class GitHubRepo:
    """
    allows to handle repo url from parameters and vice versa
    """

    def __init__(self, org: str, repo: str,
                 username: str = None, token: str = None):

        self.org = org
        self.repo = repo
        self.username = username
        self.token = token

        self.fullname = f"{org}/{repo}"

        self.url = github_url(
            fullname=self.fullname,
            username=username,
            token=token)

    @classmethod
    def from_url(cls, url):

        org, repo = extract_gnn_repo_from_github_url(url)

        return cls(org, repo)

    def to_url(self):
        return f"https://github.com/{self.org}/{self.repo}"

    def to_clone_url(self):
        return f"https://github.com/{self.org}/{self.repo}.git"

    def to_clone_ssh(self):
        return f"git@github.com:{self.org}/{self.repo}.git"

    def clone(self, path, verbose=False):

        if os.path.isdir(path):

            print(Fore.RED
                  + "\nDestination directory already exists 🤒"
                  + Style.RESET_ALL
                  + "\nCannot clone the repo to existing location"
                  + f"\n- path: {path}")

            raise FileExistsError(f"Repo directory already exists: {path}")

        cloned, output, error = clone_repo(self.url, path, verbose=verbose)

        if not cloned:

            print(Fore.RED
                  + "\nUnable to clone repo 🤒"
                  + Style.RESET_ALL
                  + "\nCannot clone the repo to existing location"
                  + f"\n- url: {self.url}"
                  + f"\n- path: {path}"
                  + f"\n- output: {output}"
                  + f"\n- error: {error}")

            raise Exception(f"Unable to clone repo: {self.url}, {path}")


def github_url(fullname, username="git", token=None):
    """
    build gh repo url
    formats:
    - https://git@github.com/{org}/{repo}
    - https://{username}@github.com/{org}/{repo}
    - https://{username}:{token}@github.com/{org}/{repo}
    """

    auth = "git" if username is None else username

    if token is not None:
        auth += f":{token}"

    repo_url = f"https://{auth}@github.com/{fullname}"

    return repo_url


def extract_gnn_repo_from_github_url(url):
    """
    extract gnn and repo name from github url
    formats:
    - git@github.com:github_nickname/repo-name.git
    - https://github.com/github_nickname/repo-name.git
    - http://github.com/github_nickname/repo-name.git
    - git@github.com:github_nickname/repo-name
    - https://github.com/github_nickname/repo-name
    - http://github.com/github_nickname/repo-name
    """

    # extract github nickname and repo from url
    re_pattern = r".*https?:\/\/github.com\/([^\/]*)\/(.*)(\.git)?|git@github.com:([^\/]*)\/(.*)(\.git)?"
    compiled_re = re.compile(re_pattern)
    matches = compiled_re.match(url)

    # retrieve matched groups
    groups = []
    if matches is not None:
        groups = matches.groups()

    # clean groups
    groups = [g for g in groups if g is not None]

    # retrieve extracted gnn
    extracted_gnn = groups[0] if len(groups) > 0 else ""
    extracted_repo = groups[1] if len(groups) > 1 else ""

    # remove .git from repo name
    if extracted_repo is not None and extracted_repo.endswith(".git"):
        extracted_repo = extracted_repo[:-4]

    return extracted_gnn, extracted_repo


if __name__ == '__main__':

    print(github_url("lewagon/setup"))
    print(github_url("lewagon/setup", "gnn", "token"))
