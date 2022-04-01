
from wagon_common.helpers.gh.url import GitHubRepo


class TestGitHubRepo():

    def test_url_to_org_repo(self):

        # Arrange
        url = "https://github.com/lewagon/data-challenges.git"

        # Act
        data_cha = GitHubRepo.from_url(url)

        # Assert
        assert data_cha.org == "lewagon"
        assert data_cha.repo == "data-challenges"

        # Cleanup

    def test_repo_to_url(self):

        # Arrange
        url = "https://github.com/lewagon/data-challenges.git"

        # Act
        data_cha = GitHubRepo.from_url(url)
        repo_url = data_cha.to_url()
        repo_clone_url = data_cha.to_clone_url()
        repo_clone_ssh = data_cha.to_clone_ssh()

        # Assert
        assert repo_url == "https://github.com/lewagon/data-challenges"
        assert repo_clone_url == "https://github.com/lewagon/data-challenges.git"
        assert repo_clone_ssh == "git@github.com:lewagon/data-challenges.git"

        # Cleanup

    def test_repo_creation(self):

        # Arrange
        data_solutions = GitHubRepo("lewagon", "data-solutions")

        # Act

        # Assert
        assert data_solutions.url == "https://git@github.com/lewagon/data-solutions"

        # Cleanup

    def test_repo_creation_auth(self):

        # Arrange
        authed_data_so = GitHubRepo("lewagon", "data-solutions", "user", "token")

        # Act

        # Assert
        assert authed_data_so.url == "https://user:token@github.com/lewagon/data-solutions"

        # Cleanup
