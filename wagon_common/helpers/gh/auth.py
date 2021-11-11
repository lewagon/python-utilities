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

    gh_pat = "xxx"

    rc, output, error = gh_auth(gh_pat)
    print(rc, output, error)
