
from wagon_common.gh.gh_repo import GhRepo

from wagon_common.helpers.git.repo import get_git_top_level_directory
from wagon_common.helpers.git.create import git_init, git_commit
from wagon_common.helpers.git.remote import git_remote_add, git_remote_show_head_branch
from wagon_common.helpers.git.push import git_push
from wagon_common.helpers.git.ls import list_git_controlled_files

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

    def init(self):
        git_init(self.path)

    def commit(self, message: str):
        git_commit(self.path, message)

    def remote_add(self, url: str, name: str = "origin"):
        if isinstance(url, GhRepo):
            url = GhRepo.ssh_url
        git_remote_add(self.path, name, url)

    def remote_head_branch(self, remote: str = "origin"):
        return git_remote_show_head_branch(
            path=self.path,
            remote=remote,
            verbose=self.verbose)

    def push(self, remote="origin", branch=None):
        if branch is None:
            branch = self.remote_head_branch(remote)
        git_push(self.path, branch, remote)

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
