
import requests

from wagon_common.helpers.output import red


class GhRepo:
    """
    helper class for gh api commands
    """

    def __init__(self, name, token=None, is_org=True, verbose=False):

        self.is_org = is_org
        self.name, self.owner, self.repository = self.__identify(name)
        self.base_url = "https://api.github.com"
        self.default_path = f"/repos/{self.owner}/{self.repository}"
        self.token = token
        self.verbose = verbose

    def __identify(self, name):
        """
        identify owner and repository from provided name
        (gh cli nomenclatura)
        """

        parts = name.split("/", maxsplit=1)

        if len(parts) == 2:
            owner = parts[0]
            repository = parts[1]
        else:
            owner = "lewagon"
            repository = name
            name = f"{owner}/{repository}"

        return name, owner, repository

    def __call(self, path=None, verb="get", headers={}, params={}, context="", status_code=200):
        """
        resolve api call
        """

        # set path
        if path is None:
            path = self.default_path

        # resolve http verb call method
        call_method = dict(
            get=requests.get,
            put=requests.put,
            patch=requests.patch,
            post=requests.post,
            delete=requests.delete)[verb]

        # add auth
        headers["Authorization"] = f"token {self.token}"

        # add owner and repo
        params = dict(
            owner=self.owner,
            repo=self.repository)

        # list repo params
        response = call_method(self.base_url + path,
                               headers=headers,
                               json=params)

        if response.status_code != status_code:

            red("\nGH api error 🤕",
                f"\n- context {context}"
                + f"\n- expected status code: {status_code}"
                + f"\n- status code: {response.status_code}"
                + f"\n- response: {response.content}")

            raise ValueError("GH api error")

        return response.json()

    def create(self, params={}):
        """
        create repository
        """

        params["org"] = self.owner
        params["name"] = self.repository
        # description
        # homepage
        # private
        # has_issues
        # has_projects
        # has_wiki

        return self.__call(path=f"/orgs/{self.owner}/repos",
                           verb="post",
                           params=params,
                           status_code=201)

    def get(self):
        """
        get repository
        """

        return self.__call()

    def update(self, params):
        """
        update repository
        """

        return self.__call(verb="patch", params=params)

    def delete(self, dry_run=True):
        """
        delete repository
        """

        # protect production repositories
        if self.owner not in ["lewagon-test", "Le-Wagon-QA"]:
            raise NameError("cannot delete repo in production organisation")

        if dry_run:
            return {}

        # delete repo
        return self.__call(verb="delete", status_code=204)
