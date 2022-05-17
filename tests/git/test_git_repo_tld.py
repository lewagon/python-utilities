
from wagon_common.git.git_repo import GitRepo

import os


class TestGitRepoTLD():

    def test_git_repo_tld(self):

        # Arrange
        repo_tld = os.path.normpath(os.path.join(
            os.path.dirname(__file__), "..", ".."))

        # Act
        repo = GitRepo(__file__)
        repo_top_level_directory = repo.tld

        # Assert
        assert repo_top_level_directory == repo_tld

        # Cleanup
