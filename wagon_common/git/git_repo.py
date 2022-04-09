
from wagon_common.helpers.git.repo import get_git_top_level_directory

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


if __name__ == '__main__':

    repo = GitRepo(__file__)
    print(f"repo tld: {repo.tld=}")
