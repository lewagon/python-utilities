
from wagon_common.path.scope import Scope
from tests.base import GitTestBase

import os


class TestScope(GitTestBase):

    expected_md = [
        "CHANGELOG.md",
        "README.md",
        os.path.join("doc", "TESTS.md"),
        os.path.join("tests", "data", "test.md")]

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
        scope = Scope.from_sources(["*.md"])
        scope.filter_git_files()

        # Assert
        assert scope.sources == self.expected_md

        # Cleanup
        self.delete_file("remove_me.md")
