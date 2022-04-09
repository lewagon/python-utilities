
from wagon_common.helpers.git.ls import list_git_controlled_files
from wagon_common.helpers.subprocess import run_command

import os


class TestHelperGitLs():

    def test_git_ls_markdown(self):

        # Arrange

        # Act
        files = list_git_controlled_files(["*.md"])

        # Assert
        excpected_md = [
            "CHANGELOG.md", "README.md", "doc/TESTS.md", "tests/data/test.md"]

        assert files == excpected_md

        # Cleanup

    def test_git_ls_deleted_markdown(self):

        # Arrange
        self.__git_delete_file("tests/data/test.md")

        # Act
        files = list_git_controlled_files(["*.md"])

        # Assert
        excpected_md = ["CHANGELOG.md", "README.md", "doc/TESTS.md"]

        assert files == excpected_md

        # Cleanup
        self.__git_restore_file("tests/data/test.md")

    def test_git_ls_deleted_markdown_with(self):

        # Arrange
        self.__git_delete_file("tests/data/test.md")

        # Act
        files = list_git_controlled_files(["*.md"], include_deleted=True)

        # Assert
        excpected_md = [
            "CHANGELOG.md", "README.md", "doc/TESTS.md", "tests/data/test.md"]

        assert files == excpected_md

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
