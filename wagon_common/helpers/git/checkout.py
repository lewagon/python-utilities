
from wagon_common.helpers.subprocess import run_command


def checkout_branch(path, branch, verbose=False):

    # retrieve current branch
    command = [
        "git",
        "checkout",
        branch,
        ]

    rc, output, error = run_command(command, cwd=path, verbose=verbose)

    if verbose:
        print(output.decode("utf-8"))

    return rc == 0, output, error
