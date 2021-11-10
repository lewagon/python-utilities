"""
git create repo cli helpers
"""

from wagon_common.helpers.subprocess import run_command


def git_init(path, verbose=False):
    """ create git repo """

    # initialize git repo
    command = [
        "git",
        "init",
        ]

    rc, output, error = run_command(
        command,
        cwd=path,
        verbose=verbose)

    if verbose:
        print(output.decode("utf-8"))

    return rc, output, error


def git_add(path, verbose=False):
    """ add all files """

    # add all files to the staging zone
    command = [
        "git",
        "add",
        "--all",
        ]

    rc, output, error = run_command(
        command,
        cwd=path,
        verbose=verbose)

    if verbose:
        print(output.decode("utf-8"))

    return rc, output, error


def git_commit(path, message, verbose=False):
    """ commit git repo """

    # add all files to the staging zone
    command = [
        "git",
        "add",
        "--all",
        ]

    rc, output, error = run_command(
        command,
        cwd=path,
        verbose=verbose)

    if verbose:
        print(output.decode("utf-8"))

    # commit
    command = [
        "git",
        "commit",
        "-m",
        message,
        ]

    rc2, output2, error2 = run_command(
        command,
        cwd=path,
        verbose=verbose)

    if verbose:
        print(output2.decode("utf-8"))

    return (rc, rc2), (output, output2), (error, error2)
