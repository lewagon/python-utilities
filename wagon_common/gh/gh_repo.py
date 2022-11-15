
import requests

from wagon_common.helpers.output import red


class GhRepo:
    """
    helper class for gh api calls
    """

    base_url = "https://api.github.com"

    def __init__(self, name, token=None, is_org=True, verbose=False):
        """
        required gh token scopes:
        - repo: push commits TBC
        - admin:org: create repos TBC
        - workflow: push commits containing `.github/workflows/*.yml` files
        - delete_repo: delete `lewagon-test` and `Le-Wagon-QA` repositories
        """

        self.name, self.owner, self.repo = self.__identify(name)
        self.headers = dict(Authorization=f"token {token}")
        self.is_org = is_org
        self.verbose = verbose

    def __identify(self, name):
        """
        identify owner and repo from provided name
        (gh cli nomenclatura)
        """

        parts = name.split("/", maxsplit=1)

        if len(parts) == 2:
            owner = parts[0]
            repo = parts[1]
        else:
            owner = "lewagon"
            repo = name
            name = f"{owner}/{repo}"

        return name, owner, repo

    def __error(self, request, response, context):
        """
        log api call and raise error
        """

        red(f"\nGH api error in {context} 🤕",
            f"\n- url: {request.url}"
            + f"\n- params: {request.json}"
            + f"\n- status code: {response.status_code}"
            + f"\n- response: {response.content}")

        raise ValueError("GH api error")

    def create(self, params={}):
        """
        create repo
        """

        params["org"] = self.owner
        params["name"] = self.repo

        request = dict(
            url=self.base_url + f"/orgs/{self.owner}/repos",
            headers=self.headers,
            json=params)

        response = requests.post(**request)

        if response.status_code != 201:
            self.__error(request, response, "repo create")

        return response.json()

    def get(self):
        """
        get repo
        """

        request = dict(
            url=self.base_url + f"/repos/{self.owner}/{self.repo}",
            headers=self.headers,
            json={})

        response = requests.get(**request)

        if response.status_code != 200:
            self.__error(request, response, "repo create")

        return response.json()

    def update(self, params={}):
        """
        update repo
        """

        request = dict(
            url=self.base_url + f"/repos/{self.owner}/{self.repo}",
            headers=self.headers,
            json=params)

        response = requests.patch(**request)

        if response.status_code != 200:
            self.__error(request, response, "repo create")

        return response.json()

    def delete(self, params={}, dry_run=True):
        """
        delete repo
        """

        # protect production repositories
        if self.owner not in ["lewagon-test", "Le-Wagon-QA"]:
            raise NameError(f"cannot delete repo in {self.owner} production organisation")

        if dry_run:
            return {}

        # delete repo
        request = dict(
            url=self.base_url + f"/repos/{self.owner}/{self.repo}",
            headers=self.headers,
            json=params)

        response = requests.delete(**request)

        if response.status_code != 204:
            self.__error(request, response, "repo create")
