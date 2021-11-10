
import subprocess

from colorama import Fore, Style


def run_command(command, cwd=None, input_bytes=None, verbose=False):
    """
    executes a command in a subprocess
    """

    if verbose:

        print(Fore.MAGENTA
              + "\nRunning `"
              + "\"" + "\" \"".join(command) + "\""
              + f"` in {cwd}"
              + Style.RESET_ALL)

    p = subprocess.Popen(command,
                         cwd=cwd,                 # set current working directory
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)

    # validate input
    if input_bytes is None:
        input_bytes = b""

    # get output and errors
    output, error = p.communicate(input_bytes)  # binary input passed as parameter

    # get process return code
    rc = p.returncode

    return rc, output, error
