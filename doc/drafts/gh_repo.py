
import requests

from wagon_common.helpers.output import red


class GhRepo:
    """
    helper class for gh api calls
    """

    base_url = "https://api.github.com"
    default_path = f"/repos/{self.owner}/{self.repo}"

    def __init__(self, name, token=None, is_org=True, verbose=False):
        """
        required gh token scopes:
        - repo: push commits TBC
        - admin:org: create repos TBC
        - workflow: push commits containing `.github/workflows/*.yml` files
        - delete_repo: delete `lewagon-test` and `lewagon-qa` repositories
        """

        self.name, self.owner, self.repo = self.__identify(name)
        self.token = token
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

    def __call(self, path=None, verb="get", headers={}, params={}, context="", status_code=200, decode_response=True):
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

        # list repo params
        response = call_method(self.base_url + path,
                               headers=headers,
                               json=params)

        if response.status_code != status_code:

            red("\nGH api error 🤕",
                f"\n- context {context}"
                + f"\n- path: {path}"
                + f"\n- verb: {verb}"
                + f"\n- params: {params}"
                + f"\n- expected status code: {status_code}"
                + f"\n- status code: {response.status_code}"
                + f"\n- response: {response.content}")

            raise ValueError("GH api error")

        if decode_response:
            return response.json()

    def create(self, params={}):
        """
        create repo
        """

        params["org"] = self.owner
        params["name"] = self.repo

        return self.__call(path=f"/orgs/{self.owner}/repos",
                           verb="post",
                           params=params,
                           status_code=201)

    def get(self):
        """
        get repo
        """

        return self.__call()

    def update(self, params):
        """
        update repo
        """

        return self.__call(verb="patch", params=params)

    def delete(self, dry_run=True):
        """
        delete repo
        """

        # protect production repositories
        if self.owner.lower() not in ["lewagon-test", "lewagon-qa"]:
            raise NameError("cannot delete repo in production organisation")

        if dry_run:
            return {}

        # delete repo
        return self.__call(verb="delete", status_code=204, decode_response=False)
