
from wagon_common.path.scope import Scope
from tests.base import GitTestBase

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

    def test_scope(self):

        # Arrange

        # Act
        scope = Scope.from_sources(["."])

        # Assert
        assert scope.repo.tld is not None

        # Cleanup

    def test_scope_git_filter(self):

        # Arrange
        self.create_file("remove_me.md")

        # Act
        scope = Scope.from_sources(self.test_pattern)
        scope.filter_git_files()

        # Assert
        assert scope.sources == self.expected_md

        # Cleanup
        self.delete_file("remove_me.md")

    def test_scope_git_filter_ignore(self):

        # Arrange

        # Act
        scope = Scope.from_sources(self.test_pattern)
        scope.filter_git_files()
        scope.filter_ignored_files()

        # Assert
        assert scope.sources == self.expected_md

        # Cleanup
