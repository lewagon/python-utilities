
import requests

from wagon_common.helpers.output import red


class GhRepo:
    """
    helper class for gh api commands
    """

    def __init__(self, name, token=None, is_org=True, verbose=False):

        self.is_org = is_org
        self.name, self.owner, self.repository = self.__identify(name)
        self.base_url = f"https://api.github.com/repos/{self.owner}/{self.repository}"
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

    def __call(self, path="", verb="get", headers={}, params={}, context=""):
        """
        resolve api call
        """

        # resolve http verb call method
        call_method = dict(
            get=requests.get,
            put=requests.put,
            patch=requests.patch,
            post=requests.post,
            delete=requests.delete)[verb]

        # add auth
        headers["Authorization"] = f"token {self.token}"

        # list repo params
        response = call_method(self.base_url + path,
                               headers=headers,
                               json=params)

        if response.status_code != 200:

            red("\nGH api error 🤕",
                f"\n- context {context}"
                + f"\n- status code: {response.status_code}"
                + f"\n- response: {response.content}")

            raise ValueError("GH api error")

        return response.json()

    def delete(self):
        """
        delete repository
        """

        # protect production repositories
        if self.owner not in ["lewagon-test", "Le-Wagon-QA"]:
            raise NameError("cannot delete repo in production organisation")

        # delete repo
        params = dict(
            owner=self.owner,
            repo=self.repository)

        self.__call(verb="delete", params=params)
