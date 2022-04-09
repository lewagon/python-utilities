
from wagon_common.helpers.git.ls import list_git_controlled_files
from wagon_common.helpers.subprocess import run_command

import os


class TestHelperGitLs():

    expected_md = [
        "CHANGELOG.md",
        "README.md",
        os.path.join("doc", "TESTS.md"),
        os.path.join("tests", "data", "test.md")]

    def test_git_ls_markdown(self):

        # Arrange

        # Act
        files = list_git_controlled_files(["*.md"])

        # Assert
        assert files == self.expected_md

        # Cleanup

    def test_git_ls_deleted_markdown(self):

        # Arrange
        self.__git_delete_file("tests/data/test.md")

        # Act
        files = list_git_controlled_files(["*.md"])

        # Assert
        assert files == self.expected_md[:3]

        # Cleanup
        self.__git_restore_file("tests/data/test.md")

    def test_git_ls_deleted_markdown_with(self):

        # Arrange
        self.__git_delete_file("tests/data/test.md")

        # Act
        files = list_git_controlled_files(["*.md"], include_deleted=True)

        # Assert
        assert files == self.expected_md

        # Cleanup
        self.__git_restore_file("tests/data/test.md")

    def __git_delete_file(self, file):

        # retrieve git controlled files
        os.remove(file)

    def __git_restore_file(self, file):

        # restore file
        command = [
            "git",
            "restore",
            ] + [file]

        _rc, output, _error = run_command(command)

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
