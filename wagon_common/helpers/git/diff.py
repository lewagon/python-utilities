"""
git diff cli helpers
"""

from wagon_common.helpers.subprocess import run_command


def git_diff_filenames(path, branch, verbose=False):
    """
    return a list of filenames committed between current branch and branch
    """

    # retrieve the list of filenames committed
    command = [
        "git",
        "diff",
        "--name-only",
        branch,
        ]

    _rc, output, _error = run_command(
        command,
        cwd=path,
        verbose=verbose)

    if verbose:
        print(output.decode("utf-8"))

    # decode output
    filenames = output.decode("utf-8").strip().split()

    return filenames


if __name__ == '__main__':

    filenames = git_diff_filenames(".", "upstream/master")
    print(filenames)
