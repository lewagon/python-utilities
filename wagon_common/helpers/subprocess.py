
from wagon_common.helpers.output import red, green, magenta

import subprocess


def run_command(command, cwd=None, input_bytes=None, show_progress=False, show_errors=False, verbose=False):
    """
    Executes a command in a subprocess
    command - a terminal command as a list, ex. ['cp', 'file', 'folder']
    cwd - current working directory to execute the command in
    input_bytes - any input params to communicate to the command
    show_progress - print command output as it occurs (for `gcloud compute ssh ...` commands)

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

    # show command output as it runs
    output = ""
    if show_progress:
        for line in p.stdout:
            decoded_line = line.decode("utf-8")
            output += decoded_line
            print(decoded_line, end="")

    # show command error as it runs
    errors = ""
    if show_errors:
        for line in p.stderr:
            decoded_line = line.decode("utf-8")
            errors += decoded_line
            print(decoded_line, end="")

    # validate input
    if input_bytes is None:
        input_bytes = b""

    # get output and errors
    com_output, error = p.communicate(input_bytes)  # binary input passed as parameter

    # get process return code
    rc = p.returncode

    return rc, output.encode() + com_output, error


def manage_command(desc, command, valid_errors=[], cwd=None, show_progress=False, show_errors=False, verbose=False):
    """
    run command in subprocess and return output
    """

    green(f"\n{desc}")

    rc, raw_output, error = run_command(command, cwd=cwd, show_progress=show_progress, show_errors=show_errors, verbose=verbose)

    output = raw_output.decode("utf-8")

    if rc != 0:

        # check if output contains a valid error (ie `rc != 0` is not an issue)
        valid_error = False
        for valid_error in valid_errors:
            if valid_error in output:
                valid_error = True
                break

        if not valid_error:

            red("\nError running command 🤕",
                f"\n- command {command}"
                + f"\n- rc {rc}"
                + f"\n- output {output}"
                + f"\n- error {error}")

            raise ValueError("Error running command")

    return output


# # ipython test:
# from wagon_common.helpers.subprocess import manage_command
# ssh_command = "gcloud compute ssh b2b-vm-vscode-setup --command"
# command = "ls -la"
# out = manage_command("Run ssh command", ssh_command.split() + [command], show_progress=True, verbose=True)
# out
# print(out)
