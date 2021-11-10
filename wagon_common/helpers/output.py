"""
cli print helper
"""

from colorama import Fore, Style


def print_files(color, name, files):
    """
    outputs list of files
    """

    colors = dict(
        red=Fore.RED,
        green=Fore.GREEN,
        blue=Fore.BLUE,
        )

    print(colors[color]
          + f"\n{name}:"
          + Style.RESET_ALL)

    [print(f) for f in sorted(files)]
