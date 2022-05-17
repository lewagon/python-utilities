
from wagon_common.helpers.git.repo import get_git_top_level_directory
from wagon_common.helpers.git.ls import list_git_controlled_files

from functools import cached_property


class GitRepo:

    def __init__(self, path, verbose=False):

        self.path = path
        self.verbose = verbose

    @cached_property
    def tld(self):

        tld = get_git_top_level_directory(
            verbose=self.verbose,
            path=self.path)

        return tld

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
