"""
git remote cli helpers
"""

from wagon_common.helpers.gh.url import GitHubRepo

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


def git_remote_get_probable_url(path, gh_nickname, verbose=False):
    """
    retrieve the first repo remote url matching the provided github nickname
    or the last remote url if there are no matches
    """

    # retrieve remote list
    remotes = git_remote_list(path=path, verbose=verbose)

    if not remotes:
        return None

    # search for matches
    remote_url = None

    for potential_remote in remotes:

        # retrieve remote url
        potential_url = git_remote_get_url(
            path=path, name=potential_remote, verbose=verbose)

        if gh_nickname in potential_url:
            remote_url = potential_url
            break

    # use last remote if no match found
    if not remote_url:
        remote_url = potential_url

    # convert to ssh clone address
    clone_ssh_addess = GitHubRepo.from_url(remote_url).to_clone_ssh()

    return clone_ssh_addess


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
