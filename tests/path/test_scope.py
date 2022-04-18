
from wagon_common.path.scope import Scope
from tests.base import GitTestBase

from wagon_common.tests.base.glob import glob_sources

import os


class TestScope(GitTestBase):

    test_pattern = [
        "./CHANGELOG.md",
        "./README.md",
        "doc/*.md",
        "tests/data/ls/*.md"]

    expected_md = [
        "CHANGELOG.md",
        "README.md",
        os.path.join("doc", "TESTS.md"),
        os.path.join("tests", "data", "ls", "test.md")]

    cwd = os.getcwd()

    def test_scope(self):

        # Arrange

        # Act
        scope = Scope.from_sources(glob_sources(["."], self.cwd))

        # Assert
        assert scope.repo.tld is not None

        # Cleanup

    def test_scope_git_filter(self):

        # Arrange
        self.create_file(os.path.join("doc", "remove_me.md"))

        # Act
        scope = Scope.from_sources(glob_sources(self.test_pattern, self.cwd), verbose=True)
        scope.filter_git_files()

        # Assert
        assert scope.sources == self.expected_md

        # Cleanup
        self.delete_file(os.path.join("doc", "remove_me.md"))
