"""
git grep cli helpers
"""

from wagon_common.helpers.subprocess import run_command


def list_git_controlled_env_vars(sources, verbose=False):
    """
    return a list of occurences of environment variables in git files
    """

    # testing if sources is a list
    if isinstance(sources, str):
        sources = [sources]
    elif isinstance(sources, tuple):
        sources = list(sources)

    # get strings matching pattern within git controlled files
    # -E extended regexp
    # -I ignore binary files
    # -r recursive
    # -h do not print filename headers
    # -o only print the matching parts of the line
    # "[$][A-Z_]+" match env var pattern for challengify delimiters
    command = [
        "git",
        "grep",
        "-EIrho",
        "[$][A-Z_]+",
        ] + sources

    _rc, output, _error = run_command(command, verbose=verbose)

    if verbose:
        print(output.decode("utf-8"))

    # decode output
    matches = output.decode("utf-8").strip().split()

    return matches


if __name__ == '__main__':

    matches = list_git_controlled_env_vars("..")
    print(matches)

    matches = list_git_controlled_env_vars(["..", ".."])
    print(matches)

    matches = list_git_controlled_env_vars(("..", ".."))
    print(matches)
