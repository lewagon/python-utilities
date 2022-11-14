
from wagon_common.gh.gh_repo import GhRepo


class TestGhRepo():

    def test_gh_repo_creation(self):

        # Arrange

        # Act
        repo = GhRepo("lewagon-test/data-solutions")
        lw_repo = GhRepo("myriad")

        # Assert
        assert repo.owner == "lewagon-test"
        assert repo.repository == "data-solutions"
        assert lw_repo.owner == "lewagon"
        assert lw_repo.repository == "myriad"

        # Cleanup
