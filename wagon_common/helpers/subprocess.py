
from wagon_common.helpers.output import red, green, magenta

import subprocess


def run_command(command, cwd=None, input_bytes=None, verbose=False):
    """
    Executes a command in a subprocess
    command - a terminal command as a list, ex. ['cp', 'file', 'folder']
    cwd - current working directory to execute the command in
    input_bytes - any input params to communicate to the command

    NOTE: commands run in 'bash' shell
    """

    if verbose:
        command_text = '"' + '" "'.join(command) + '"'
        magenta(f"\nRunning `{command_text}` in {cwd}")

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


def manage_command(desc, command, cwd=None, verbose=False):
    """
    run command in subprocess and return output
    """

    green(desc)

    rc, output, error = run_command(command, cwd=cwd, verbose=verbose)

    if rc != 0:

        red("\nError running command 🤕",
            f"\n- command {command}"
            + f"\n- rc {rc}"
            + f"\n- output {output}"
            + f"\n- error {error}")

        raise ValueError("Error running command")

    return output.decode("utf-8")
