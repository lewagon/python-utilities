
from wagon_common.gh.gh_repo import GhRepo

from wagon_common.helpers.subprocess import manage_command

from wagon_common.helpers.git.repo import get_git_top_level_directory
from wagon_common.helpers.git.ls import list_git_controlled_files

from typing import Union

from functools import cached_property


class GitRepo:
    """
    helper class for git cli commands
    provides a mapping to the git cli commands
    does no try to control the state of the targeted git repo
    """

    def __init__(self, path, verbose=False):

        self.path = path                # repo tld
        self.verbose = verbose

    def __command(self, desc, command, valid_errors=[]):

        return manage_command(
            desc,
            command,
            valid_errors,
            cwd=self.path,              # run commands at the repo tld
            show_progress=True,         # show commands output as it occurs
            verbose=self.verbose)       # show commands being ran

    @cached_property
    def tld(self):

        tld = get_git_top_level_directory(
            verbose=self.verbose,
            path=self.path)

        return tld

    def clone(self, url: Union[str, GhRepo], quiet=False):

        if isinstance(url, GhRepo):
            url = url.ssh_url

        return self.__command(
            "Initialize git repo",
            [
                "git",
                "clone",
                url,
                ".",
            ] + (["--quiet"] if quiet else []))

    def init(self):

        return self.__command(
            "Initialize git repo",
            [
                "git",
                "init"
            ])

    def add(self):

        return self.__command(
            "Add repo content to the staging zone",
            [
                "git",
                "add",
                "--all"
            ])

    def commit(self, message: str):

        return self.__command(
            "Commit content in the staging zone",
            [
                "git",
                "commit",
                "-m",
                message
            ],
            [
                "nothing to commit, working tree clean"
            ])

    def remote_add(self, url: Union[str, GhRepo], remote: str = "origin"):

        if isinstance(url, GhRepo):
            url = url.ssh_url

        return self.__command(
            "Add remote",
            [
                "git",
                "remote",
                "add",
                remote,
                url
            ])

    def current_branch(self):

        output = self.__command(
            "Add remote",
            [
                "git",
                "rev-parse",
                "--abbrev-ref",
                "HEAD",
            ])

        branch = output.strip().strip("\n")

        return branch

    def push(self, remote: str = "origin", branch=None, force=False):

        if branch is None:
            branch = self.current_branch()

        return self.__command(
            "Add remote",
            [
                "git",
                "push",
                remote,
                branch,
            ] + (["--force"] if force else []))

    def ls_files(self, sources, include_deleted=False, path=None):

        files = list_git_controlled_files(
            sources,
            verbose=self.verbose,
            include_deleted=include_deleted,
            path=path)

        return files


if __name__ == '__main__':

    repo = GitRepo(__file__, verbose=True)
    repo.tld
    repo.tld
    repo.tld
    print(f"repo tld: {repo.tld=}")
