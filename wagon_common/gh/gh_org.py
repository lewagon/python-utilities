
from wagon_common.gh.gh_api_base import GhApiBase
from wagon_common.gh.gh_org_secret import GhOrgSecret

import requests


class GhOrg(GhApiBase):
    """
    helper class for gh org api
    """

    def __init__(self, org, token, verbose=False):
        """
        required gh token scopes:
        - TBD
        """

        super().__init__(token, verbose)

        self.org = org

    def secrets(self):
        """
        list org secrets
        """

        params = dict(
            org=self.org)

        request = dict(
            url=f"{self.base_url}/orgs/{self.org}/actions/secrets",
            headers=self.headers,
            json=params)

        response = requests.get(**request)

        if response.status_code != 200:
            self.error(request, response, "org secret list")

        return [GhOrgSecret(org=self.org, **secret, token=self.token, verbose=self.verbose)
                for secret in response.json()["secrets"]]
