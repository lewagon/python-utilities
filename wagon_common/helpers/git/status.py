"""
git status cli helpers
"""

from wagon_common.helpers.subprocess import run_command


def git_status(path, verbose=False):
    """
    return repo status
    """

    # list git status
    command = [
        "git",
        "status",
        ]

    _rc, output, _error = run_command(
        command,
        cwd=path,
        verbose=verbose)

    if verbose:
        print(output.decode("utf-8"))

    status = output.decode("utf-8")

    clean = "nothing to commit, working tree clean" in status

    return clean


if __name__ == '__main__':

    clean = git_status(".")
    print(clean)
