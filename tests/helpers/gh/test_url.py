
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
