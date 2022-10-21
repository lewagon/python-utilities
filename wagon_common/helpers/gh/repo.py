"""
gh repo cli helpers
"""

import json

from wagon_common.helpers.subprocess import run_command


def gh_repo_create(path, fullname_or_url, verbose=False):
    """ create gh repo """

    # create gh repo
    command = [
        "gh",
        "repo",
        "create",
        fullname_or_url,  # supports org/repo vs gh full url
        "--private",
        "--confirm",
        ]

    rc, output, error = run_command(
        command,
        cwd=path,
        verbose=verbose)

    if verbose:
        print(output.decode("utf-8"))

    return rc, output, error


def gh_repo_list(org, max_count, json_fields, verbose=False):
    """
    list the repos of an organisation
    possible values for json_fields:
    https://api.github.com/orgs/lewagon/repos?per_page=1
    """

    # list gh repo
    command = [
        "gh",
        "repo",
        "list",
        org,
        "-L",
        max_count,
        "--json",
        ",".join(json_fields),
        ]

    rc, output, error = run_command(
        command,
        verbose=verbose)

    if verbose:
        print(output.decode("utf-8"))

    decoded_repos = output.decode("utf-8")

    # load json response
    try:
        repos = json.loads(decoded_repos)
    except json.decoder.JSONDecodeError:
        repos = None

    return rc, output, error, repos


if __name__ == '__main__':

    rc, output, error, repos = gh_repo_list("lewagon", "5", ["id", "name"])
    print(rc, output, error, repos)
