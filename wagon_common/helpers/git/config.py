"""
git config cli helpers
"""

from wagon_common.helpers.subprocess import run_command


def git_config(key, value, verbose=False):
    """
    runs git config
    """

    # config name
    command = [
        "git",
        "config",
        "--global",
        key,
        f"\"{value}\"",
        ]

    rc, output, error = run_command(
        command,
        verbose=verbose)

    if verbose:
        print(output.decode("utf-8"))

    return rc, output, error
