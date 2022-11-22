
from wagon_common.gh.gh_api_base import GhApiBase

import requests


class GhOrgSecret(GhApiBase):
    """
    helper class for gh action secret api
    """

    def __init__(self, org, name, visibility, created_at, updated_at, token, verbose=False):
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
