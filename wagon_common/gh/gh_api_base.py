
from wagon_common.helpers.output import red


class GhApiBase:
    """
    base class for gh api
    """

    base_url = "https://api.github.com"

    def __init__(self, token, verbose=False):
        """
        required gh token scopes:
        - repo: for access tokens
        - secrets: for apps
        """

        self.token = token
        self.headers = dict(Authorization=f"token {token}")
        self.verbose = verbose

    def error(self, request, response, context):
        """
        log api call and raise error
        """

        red(f"\nGH api error in {context} 🤕",
            f"\n- url: {request['url'] if 'url' in request else ''}"
            + f"\n- params: {request['json'] if 'json' in request else ''}"
            + f"\n- status code: {response.status_code}"
            + f"\n- response: {response.content}")

        raise ValueError("GH api error")
