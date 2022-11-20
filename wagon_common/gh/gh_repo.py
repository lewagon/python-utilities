
import requests

from wagon_common.helpers.output import green

from threading import Event

from wagon_common.helpers.output import red


class GhRepo:
    """
    helper class for gh api calls
    """

    base_url = "https://api.github.com"

    def __init__(self, name, token, is_org=True, verbose=False):
        """
        required gh token scopes:
        - repo: push commits TBC
        - admin:org: create repos TBC
        - workflow: push commits containing `.github/workflows/*.yml` files
        - delete_repo: delete `lewagon-test` and `lewagon-qa` repositories

        TODO: ssh credentials require additional setup
        """

        self.name, self.owner, self.repo = self.__identify(name)
        self.ssh_url = f"git@github.com:{self.owner}/{self.repo}.git"
        self.https_url = f"https://{token}@github.com/{self.owner}/{self.repo}.git"
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
            f"\n- url: {request['url']}"
            + f"\n- params: {request['json']}"
            + f"\n- status code: {response.status_code}"
            + f"\n- response: {response.content}")

        raise ValueError("GH api error")

    def create(self, params={}):
        """
        create repo
        """

        params["org"] = self.owner
        params["name"] = self.repo
        params["private"] = True

        request = dict(
            url=f"{self.base_url}/orgs/{self.owner}/repos",
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
            url=f"{self.base_url}/repos/{self.owner}/{self.repo}",
            headers=self.headers,
            json={})

        response = requests.get(**request)

        # check if repo exists
        if response.status_code == 404:
            return None  # repo does not exist

        if response.status_code != 200:
            self.__error(request, response, "repo get")

        return response.json()

    def update(self, params={}):
        """
        update repo
        """

        request = dict(
            url=f"{self.base_url}/repos/{self.owner}/{self.repo}",
            headers=self.headers,
            json=params)

        response = requests.patch(**request)

        if response.status_code != 200:
            self.__error(request, response, "repo update")

        return response.json()

    def delete(self, params={}, dry_run=True):
        """
        delete repo
        """

        # protect production repositories
        if self.owner.lower() not in ["lewagon-test", "lewagon-qa"]:
            raise NameError(f"cannot delete repo in {self.owner} production organisation")

        if dry_run:
            return {}

        # delete repo
        request = dict(
            url=f"{self.base_url}/repos/{self.owner}/{self.repo}",
            headers=self.headers,
            json=params)

        response = requests.delete(**request)

        # checking whether repo was deleted or did not exist
        if response.status_code != 204 and response.status_code != 404:
            self.__error(request, response, "repo delete")

    def wait_for_creation(self):
        """
        wait until the repo is created
        the use case is having a gha create the repo and waiting for its creation
        """

        repo = None

        index = 0
        max_tries = 12 * 3  # 3 minutes

        green(f"\nWait for the creation of the {self.name} repo")

        while repo is None and index < max_tries:

            index += 1

            # check if repo exists
            repo = self.get()

            print("Wait for 5 seconds...")

            # wait 5 more seconds for repo to be created (non blocking)
            Event().wait(5)

        if repo is None:
            raise NameError(f"repo in {self.name} was not created")
