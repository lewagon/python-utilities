"""
git ls cli helpers
"""

from wagon_common.helpers.subprocess import run_command


def list_git_controlled_files(sources, verbose=False, include_deleted=False, path=None):
    """
    return a list of git controlled files matching path pattern
    """

    # testing if sources is a list
    if isinstance(sources, str):
        sources = [sources]
    elif isinstance(sources, tuple):
        sources = list(sources)

    # retrieve git controlled files
    command = [
        "git",
        "ls-files",
        ] + sources

    _rc, output, _error = run_command(command, cwd=path, verbose=verbose)

    # decode output
    lines = output.decode("utf-8").strip().split("\n")

    # cleaning empty results
    if len(lines) == 1 and lines[0] == "":
        lines = []

    if not include_deleted:

        # retrieve files that have been deleted but are still in the staging zone
        deleted_command = [
            "git",
            "status",
            "--short",
            ]

        _d_rc, d_output, _d_error = run_command(deleted_command, verbose=verbose)

        # decode output
        deleted_lines = d_output.decode("utf-8").split("\n")
        deleted_files = [f[3:] for f in deleted_lines if f[:1] == "D"]

        # remove files that have been deleted but are still in the staging zone
        lines = sorted(set(lines) - set(deleted_files))

    return lines


if __name__ == '__main__':

    lines = list_git_controlled_files("..")
    [print(line) for line in lines]

    lines = list_git_controlled_files(["..", ".."])
    [print(line) for line in lines]

    lines = list_git_controlled_files(("..", ".."))
    [print(line) for line in lines]
