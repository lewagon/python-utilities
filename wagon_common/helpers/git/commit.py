"""
git commit cli helpers
"""

from wagon_common.helpers.subprocess import run_command


def get_latest_commit(
        latest_merged_commit=False, commit_sha=None, verbose=False):
    """
    retrieve latest commit message or latest merged commit message
    """

    # get latest commit message
    command = [
        "git",
        "log",
        "-1",
        "--pretty=format:%B",
        ] + (
            ["HEAD^2"] if latest_merged_commit else []
        ) + (
            [commit_sha] if commit_sha is not None else []
        )

    _rc, output, _error = run_command(
        command,
        verbose=verbose)

    if verbose:
        print(output.decode("utf-8"))

    # decode output
    latest_commit_message = output.decode("utf-8").strip()
    ### PAVEL: no check for errors
    return latest_commit_message


if __name__ == '__main__':

    latest_commit_message = get_latest_commit()
    print(latest_commit_message)

    latest_commit_message = get_latest_commit(latest_merged_commit=True)
    print(latest_commit_message)

    latest_commit_message = get_latest_commit(commit_sha="2915d86")
    print(latest_commit_message)
