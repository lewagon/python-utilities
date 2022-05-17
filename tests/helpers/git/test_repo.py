
from wagon_common.helpers.git.repo import get_git_top_level_directory

import os


class TestHelperGitRepoTLD():

    repo_tld = os.path.normpath(os.path.join(
        os.path.dirname(__file__), "..", "..", ".."))

    def test_git_repo_tld(self):

        # Arrange

        # Act
        tld = get_git_top_level_directory()

        # Assert
        assert tld == self.repo_tld

        # Cleanup

    def test_git_repo_tld_from_file_path(self):

        # Arrange

        # Act
        tld = get_git_top_level_directory(path=__file__)

        # Assert
        assert tld == self.repo_tld

        # Cleanup

    def test_git_repo_tld_from_directory_path(self):

        # Arrange

        # Act
        tld = get_git_top_level_directory(path=os.path.dirname(__file__))

        # Assert
        assert tld == self.repo_tld

        # Cleanup

    def test_git_repo_tld_from_tld(self):

        # Arrange

        # Act
        tld = get_git_top_level_directory(path=self.repo_tld)

        # Assert
        assert tld == self.repo_tld

        # Cleanup

    def test_git_repo_tld_from_outside(self):

        # Arrange
        outside_path = os.path.normpath(os.path.join(
            self.repo_tld, ".."))

        # Act
        tld = get_git_top_level_directory(path=outside_path)

        # Assert
        assert tld is None

        # Cleanup

    # def test_git_repo_tld_from_outside_repo(self):

    #     # Arrange
    #     outside_repo_path = os.path.normpath(os.path.join(
    #         self.repo_tld, "..", "data-challenges"))

    #     # Act
    #     tld = get_git_top_level_directory(path=outside_repo_path)

    #     # Assert
    #     assert tld == outside_repo_path

    #     # Cleanup
