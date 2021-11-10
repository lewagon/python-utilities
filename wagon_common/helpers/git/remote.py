"""
git remote cli helpers
"""

from wagon_common.helpers.subprocess import run_command


def git_remote_list(path, verbose=False):
    """ retrieve the list of repository remotes """

    # getting remotes
    command = [
        "git",
        "remote",
        ]

    _rc, output, _error = run_command(
        command,
        cwd=path,
        verbose=verbose)

    if verbose:
        print(output.decode("utf-8"))

    # decode output
    remotes = output.decode("utf-8").strip().split("\n")

    # clean remotes
    if len(remotes) == 1 and remotes[0] == "":
        remotes = []

    return remotes


def git_remote_get_url(path, name, verbose=False):
    """ retrieve the remote url """

    # getting remotes
    command = [
        "git",
        "remote",
        "get-url",
        name
        ]

    _rc, output, _error = run_command(
        command,
        cwd=path,
        verbose=verbose)

    if verbose:
        print(output.decode("utf-8"))

    # decode output
    remote_url = output.decode("utf-8").strip()

    return remote_url


def git_remote_add(path, name, url, verbose=False):
    """ add remote to existing repo """

    # add remote
    command = [
        "git",
        "remote",
        "add",
        name,
        url
        ]

    rc, output, error = run_command(
        command,
        cwd=path,
        verbose=verbose)

    if verbose:
        print(output.decode("utf-8"))

    return rc, output, error


if __name__ == '__main__':

    # test remotes
    tld = git_remote_list(".")
    print(f"remotes: >{tld}<", type(tld), len(tld))
