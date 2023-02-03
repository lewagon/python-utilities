"""
git repo cli helpers
"""

from wagon_common.helpers.subprocess import run_command

import os


def get_git_top_level_directory(verbose=False, path=None):
    """ retrieve the top level of the git repository """

    # check path
    if path and not os.path.isdir(path):
        path = os.path.dirname(os.path.abspath(path))

        # verify path
        if not os.path.isdir(path):
            return None

    # get git repo top level directory
    command = [
        "git",
        "rev-parse",
        "--show-toplevel",
        ]

    rc, output, _error = run_command(command, cwd=path, verbose=verbose)

    if rc != 0:
        return None

    if verbose:
        print(output.decode("utf-8"))

    # decode output
    top_level_directory = output.decode("utf-8").strip()

    return top_level_directory

def git_rm_and_clean(path=None, verbose=False):
    """ run git rm -rf . and git clean -fdx in `path` """
    # check path
    if path and not os.path.isdir(path):
        path = os.path.dirname(os.path.abspath(path))

        # verify path
        if not os.path.isdir(path):
            return None

    rm_command = [
      "git",
      "rm",
      "-rf",
      "."
    ]

    rc, output, _error = run_command(rm_command, cwd=path, verbose=verbose)

    if rc != 0:
        print(_error.decode("utf-8"))
        return None

    if verbose:
        print(output.decode("utf-8"))

    clean_command = [
      "git",
      "clean",
      "-fdx"
    ]

    rc2, output2, _error2 = run_command(clean_command, cwd=path, verbose=verbose)

    if rc2 != 0:
        print(_error2.decode("utf-8"))
        return None

    if verbose:
        print(output2.decode("utf-8"))

    return True


if __name__ == '__main__':

    data_challenges_inner_path = os.path.normpath(os.path.join(
        os.path.dirname(__file__), "..", "..", "..", "..",
        "data-challenges", "00-Setup", "01-Check", "tests", "test_demo.py"))

    # test tld
    tld = get_git_top_level_directory(
        path=data_challenges_inner_path, verbose=True)

    print(f"data challenges tld: {tld}")
