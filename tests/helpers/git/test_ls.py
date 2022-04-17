
from wagon_common.helpers.git.ls import list_git_controlled_files
from tests.base import GitTestBase

import os


class TestHelperGitLs(GitTestBase):

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

    def test_git_ls_markdown(self):

        # Arrange

        # Act
        files = list_git_controlled_files(self.test_pattern)

        # Assert
        assert files == self.expected_md

        # Cleanup

    def test_git_ls_deleted_markdown(self):

        # Arrange
        self.delete_file("tests/data/ls/test.md")

        # Act
        files = list_git_controlled_files(self.test_pattern)

        # Assert
        assert files == self.expected_md[:3]

        # Cleanup
        self.git_restore_file("tests/data/ls/test.md")

    def test_git_ls_deleted_markdown_with(self):

        # Arrange
        self.delete_file("tests/data/ls/test.md")

        # Act
        files = list_git_controlled_files(self.test_pattern, include_deleted=True)

        # Assert
        assert files == self.expected_md

        # Cleanup
        self.git_restore_file("tests/data/ls/test.md")

    def test_git_ls_outside(self):

        # Arrange

        # Act
        files = list_git_controlled_files(["../*.md"])

        # Assert
        expected_md = []

        assert files == expected_md

        # Cleanup

    # def test_git_ls_other_repo(self):

    #     # Arrange

    #     # Act
    #     repo_path = os.path.join("..", "data-challenges")
    #     files = list_git_controlled_files([".gitignore"], path=repo_path, verbose=True)

    #     # Assert
    #     expected_md = [".gitignore"]

    #     assert files == expected_md

    #     # Cleanup
