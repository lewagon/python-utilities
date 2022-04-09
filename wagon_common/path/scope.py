
from wagon_common.git.git_repo import GitRepo

from functools import cached_property
import os

from colorama import Fore, Style


class Scope:

    def __init__(self, sources, verbose):

        self.sources = sources
        self.verbose = verbose

        # retrieve the git repo in which the command was ran
        self.repo = GitRepo(self.cwd)

    def filter_git_files(self, include_deleted=False):

        self.sources = self.repo.ls_files(
            self.sources, include_deleted=include_deleted)

    @classmethod
    def from_sources(cls, sources, verbose=False):

        scope = cls(sources, verbose=verbose)

        # check scope git repo
        if scope.repo.tld is None:

            print(Fore.RED
                  + "\nCannot run command outside of a git repo 🙃"
                  + Style.RESET_ALL)

            return None

        return scope

    @cached_property
    def cwd(self):
        return os.getcwd()


if __name__ == '__main__':

    scope = Scope.from_sources(["."])
    print(f"{scope=}")
