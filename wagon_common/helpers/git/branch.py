"""
git branch cli helpers
"""

from wagon_common.helpers.subprocess import run_command


def get_current_branch(path, verbose=False):
    """ get current branch """

    # add all files to the staging zone
    command = [
        "git",
        "rev-parse",
        "--abbrev-ref",
        "HEAD",
        ]

    rc, output, error = run_command(
        command,
        cwd=path,
        verbose=verbose)

    if verbose:
        print(output.decode("utf-8"))

    # decode output
    branch = output.decode("utf-8").strip().strip("\n")

    return rc, output, error, branch

def rename_branch(path, new_branch_name, verbose=False):
  """
  Rename the branch to 'new_branch_name'
  """
  command = [
      "git",
      "branch",
      "-m",
      new_branch_name,
      ]

  rc, output, error = run_command(
      command,
      cwd=path,
      verbose=verbose)

  return rc, output, error
