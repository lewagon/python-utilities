
from wagon_common.gh.gh_api_base import GhApiBase
from wagon_common.gh.gh_repo import GhRepo

from wagon_common.helpers.output import cyan

import requests


class GhOrgSecret(GhApiBase):
    """
    helper class for gh action secret api
    """

    def __init__(self, org, name, visibility=None, created_at=None, updated_at=None, token=None, verbose=False, **kwargs):
        """
        required gh token scopes:
        - repo: for access tokens
        - secrets: for apps
        """

        super().__init__(token, verbose)

        self.org = org
        self.name = name
        self.visibility = visibility
        self.created_at = created_at
        self.updated_at = updated_at
        self.kwargs = kwargs

    def repositories(self):
        """
        list org secret repositories
        """

        if self.verbose:
            cyan(f"\nApi call: get org secret `{self.name}` repositories")

        params = dict(
            org=self.org,
            secret_name=self.name)

        request = dict(
            url=f"{self.base_url}/orgs/{self.org}/actions/secrets/{self.name}/repositories",
            headers=self.headers,
            json=params)

        response = requests.get(**request)

        if response.status_code != 200:
            self.error(request, response, "org secret repositories list")

        is_org = True  # 🔥 TODO

        return [GhRepo(**repo, is_org=is_org, token=self.token, verbose=self.verbose)
                for repo in response.json()["repositories"]]

    def add_repo(self, repository_id):
        """
        add repo to org secret
        """

        if self.verbose:
            cyan(f"\nApi call: add repo `{repository_id}` to org secret `{self.name}`")

        params = {}

        request = dict(
            url=f"{self.base_url}/orgs/{self.org}/actions/secrets/{self.name}/repositories/{repository_id}",
            headers=self.headers,
            json=params)

        response = requests.put(**request)

        if response.status_code != 204:
            self.error(request, response, "org secret add repo")
