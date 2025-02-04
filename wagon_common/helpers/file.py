"""
cli helper
"""

import os
import subprocess

from wagon_common.helpers.output import magenta
from wagon_common.helpers.subprocess import run_command


def ensure_path_directory_exists(destination):

    # create destination directory
    destination_directory = os.path.dirname(destination)
    if destination_directory != "":
        os.makedirs(destination_directory, exist_ok=True)


def cp(source, destination, recursive=False, verbose=False):
    """
    copies file along with missing sub directories
    """

    # create destination directory
    ensure_path_directory_exists(destination)

    # move file
    command = [
        "cp",
        ] + (
            ["-R"] if recursive else []
        ) + [
        source,
        destination,
        ]

    if verbose:
        magenta('\nRunning `"' + '" "'.join(command) + '"`')

    # copy file
    subprocess.call(command)


def mv(source, destination, verbose=False):
    """
    move source whether file or directory
    """

    # move file
    command = [
        "mv",
        source,
        destination,
        ]

    rc, output, error = run_command(command, verbose=verbose)

    if verbose:
        print(output.decode("utf-8"))

    return rc == 0, output, error
