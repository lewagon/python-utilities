
from wagon_common.helpers.subprocess import run_command


def are_directories_identical(directory_a, directory_b, ignored_files=[]):
    """
    recursively compare directory structure and file content
    optionally you can pass a list of files to ignore, ex. [".git"]
    """
    # create a list of files to ignore with -x option
    files_to_ignore = sum([["-x", file] for file in ignored_files], [])

    # compare directories
    command = [
        "diff",
        "-r"
        ] + files_to_ignore + [
        directory_a,
        directory_b]

    rc, output, error = run_command(command, verbose=False)

    return rc, output, error
