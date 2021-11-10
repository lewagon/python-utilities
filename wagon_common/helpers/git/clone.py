"""
git clone cli helpers
"""

from wagon_common.helpers.subprocess import run_command

import os

from colorama import Fore, Style


def clone_repo(source, destination, verbose=False):
    """
    git clone source url to destination path
    """

    # clone repository
    command = [
        "git",
        "clone",
        source,
        destination,
        "--quiet"
        ]

    rc, output, error = run_command(command, verbose=verbose)

    if verbose:
        print(output.decode("utf-8"))

    return rc == 0, output, error


def pull_remote(destination, remote="origin", branch="master", verbose=False):
    """
    fetch remote branch
    """

    # clone repository
    command = [
        "git",
        "pull",
        remote,
        branch
        ]

    rc, output, error = run_command(command, cwd=destination, verbose=verbose)

    if verbose:
        print(output.decode("utf-8"))

    return rc == 0, output, error


def fetch_repo(source, destination, verbose=False):
    """
    clone repo if destination does not exist
    fetch remote master otherwise
    """

    # check if directory does not exist
    if not os.path.isdir(destination):

        if verbose:

            print(Fore.BLUE + "\nClone repo"
                  + Style.RESET_ALL
                  + f"\n- source: {source}"
                  + f"\n- destination: {destination}")

        # clone repo
        return clone_repo(source, destination, verbose=verbose)

    if verbose:

        print(Fore.BLUE + "\nFetch remote master"
              + Style.RESET_ALL
              + f"\n- destination: {destination}")

    # clone repo
    return pull_remote(destination, verbose=verbose)


if __name__ == '__main__':

    source = "https://github.com/lewagon/dotfiles"
    destination = "test_destination"
    fetch_repo(source, destination, verbose=True)  # should clone
    fetch_repo(source, destination, verbose=True)  # should fetch
