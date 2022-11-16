
from wagon_common.gh.gh_repo import GhRepo

from wagon_common.helpers.git.repo import get_git_top_level_directory
from wagon_common.helpers.git.clone import clone_repo
from wagon_common.helpers.git.create import git_init, git_add, git_commit
from wagon_common.helpers.git.remote import git_remote_add, git_remote_show_head_branch
from wagon_common.helpers.git.branch import get_current_branch
from wagon_common.helpers.git.push import git_push
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

        self.path = path
        self.verbose = verbose

    @cached_property
    def tld(self):

        tld = get_git_top_level_directory(
            verbose=self.verbose,
            path=self.path)

        return tld

    def clone(self, url: Union[str, GhRepo]):
        if isinstance(url, GhRepo):
            url = url.ssh_url
        clone_repo(url, self.path, verbose=self.verbose)

    def init(self):
        git_init(self.path, verbose=self.verbose)

    def add(self):
        git_add(self.path, verbose=self.verbose)

    def commit(self, message: str):
        git_commit(self.path, message, verbose=self.verbose)

    def remote_add(self, url: Union[str, GhRepo], remote: str = "origin"):
        if isinstance(url, GhRepo):
            url = url.ssh_url
        git_remote_add(self.path, remote, url, verbose=self.verbose)

    def remote_head_branch(self, remote: str = "origin"):
        return git_remote_show_head_branch(
            path=self.path,
            remote=remote,
            verbose=self.verbose)

    def current_branch(self):
        rc, output, error, branch = get_current_branch(self.path, verbose=self.verbose)
        return branch

    def push(self, remote: str = "origin", branch=None):
        if branch is None:
            branch = self.current_branch()
        git_push(self.path, branch, remote, verbose=self.verbose)

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
