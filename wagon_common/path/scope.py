"""
handles a subset of tree structure passed as an argument
to a command ran in a git repository
"""

from wagon_common.git.git_repo import GitRepo

from wagon_common.helpers.filter import (
    list_files_matching_pattern)
from wagon_common.helpers.output import print_files

from functools import cached_property
import os

from wagon_common.helpers.output import red


class Scope:

    def __init__(self, sources, verbose):

        self.sources = sources
        self.verbose = verbose

        # retrieve the git repo in which the command was ran
        self.repo = GitRepo(self.cwd)

    def filter_git_files(self, include_deleted=False):

        # retrieve git handled files in the scope
        git_files = self.repo.ls_files(
            self.sources, include_deleted=include_deleted)

        if self.verbose:

            # list files not handled by git (or oustide of the repo)
            git_unhandled = set(self.sources) - set(git_files)

            print_files("red", "Files not handled by git", git_unhandled)

        self.sources = git_files

        if not self.sources:

            red("\nNo files controlled by git in the scope 😶‍🌫️",
                "\nPlease make sure to `git add` any files that you want to use")

    def filter_ignored_patterns(self, patterns):

        # exclude files matching unsynced pattern
        excluded_files = list_files_matching_pattern(self.sources, patterns)
        self.sources = sorted(set(self.sources) - set(excluded_files))

        if self.verbose:
            print_files("red", f"Files excluded by {patterns} pattern", excluded_files)

    @classmethod
    def from_sources(cls, sources, verbose=False):

        scope = cls(sources, verbose=verbose)

        # check scope git repo
        if scope.repo.tld is None:

            red("\nCannot run command outside of a git repo 🙃")

            return None

        return scope

    @cached_property
    def cwd(self):
        return os.getcwd()

    def __iter__(self):
        """
        iterator initializer
        """

        self.iterated_position = -1
        return self

    def __next__(self):
        """
        iterator increment
        """

        self.iterated_position += 1

        if self.iterated_position < len(self.sources):
            result = self.sources[self.iterated_position]
            return result
        else:
            raise StopIteration


if __name__ == '__main__':

    scope = Scope.from_sources(["."])
    print(f"{scope=}")
