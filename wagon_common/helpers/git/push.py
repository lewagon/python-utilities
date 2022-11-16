"""
git push cli helpers
"""

from wagon_common.helpers.subprocess import run_command


def git_push(path, branch, remote="origin", force=False, verbose=False):
    """ push git repo """

    # push git repo
    command = [
        "git",
        "push",
        remote,
        branch,
        ] + (["--force"] if force else [])

    rc, output, error = run_command(
        command,
        cwd=path,
        verbose=verbose)

    if verbose:
        print(output.decode("utf-8"))

    return rc, output, error
