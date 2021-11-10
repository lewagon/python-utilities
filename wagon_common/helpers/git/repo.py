"""
git repo cli helpers
"""

from wagon_common.helpers.subprocess import run_command


def get_git_top_level_directory(verbose=False):
    """ retrieve the top level of the git repository """

    # getting git repo top level
    command = [
        "git",
        "rev-parse",
        "--show-toplevel",
        ]

    _rc, output, _error = run_command(command, verbose=verbose)

    if verbose:
        print(output.decode("utf-8"))

    # decode output
    top_level_directory = output.decode("utf-8").strip()

    return top_level_directory


if __name__ == '__main__':

    # test tld
    tld = get_git_top_level_directory()
    print(f"top level directory: >{tld}<")
