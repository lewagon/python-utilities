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


"""
print colored text
"""
def black(text, desc=""): print(Fore.BLACK + text + Style.RESET_ALL + desc)
def red(text, desc=""): print(Fore.RED + text + Style.RESET_ALL + desc)
def green(text, desc=""): print(Fore.GREEN + text + Style.RESET_ALL + desc)
def yellow(text, desc=""): print(Fore.YELLOW + text + Style.RESET_ALL + desc)
def blue(text, desc=""): print(Fore.BLUE + text + Style.RESET_ALL + desc)
def magenta(text, desc=""): print(Fore.MAGENTA + text + Style.RESET_ALL + desc)
def cyan(text, desc=""): print(Fore.CYAN + text + Style.RESET_ALL + desc)
def white(text, desc=""): print(Fore.WHITE + text + Style.RESET_ALL + desc)


if __name__ == '__main__':
    black("text")
    red("text")
    green("text")
    yellow("text")
    blue("text")
    magenta("text")
    cyan("text")
    white("text")
    black("text", "desc")
    red("text", "desc")
    green("text", "desc")
    yellow("text", "desc")
    blue("text", "desc")
    magenta("text", "desc")
    cyan("text", "desc")
    white("text", "desc")
