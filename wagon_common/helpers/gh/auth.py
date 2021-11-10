"""
gh auth cli helpers
"""

from wagon_common.helpers.subprocess import run_command


def gh_auth(token, verbose=False):
    """ gh auth """

    # gh auth
    command = [
        "gh",
        "auth",
        "login",
        "--with-token",
        ]

    rc, output, error = run_command(
        command,
        input_bytes=str.encode(token),
        verbose=verbose)

    if verbose:
        print(output.decode("utf-8"))

    return rc, output, error


if __name__ == '__main__':

    from wagon_myriad.github.auth import load_gh_token

    gh_pat = load_gh_token()

    rc, output, error = gh_auth(gh_pat)
    print(rc, output, error)
