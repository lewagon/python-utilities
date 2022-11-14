
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
        assert repo.name == "lewagon-test/data-solutions"

        assert lw_repo.owner == "lewagon"
        assert lw_repo.repository == "myriad"
        assert lw_repo.name == "lewagon/myriad"

        # Cleanup

    def test_gh_repo_delete_prod(self):
        """
        verify that a production repo cannot be deleted
        """

        exception_catched = False

        try:
            GhRepo("lewagon/data-solutions").delete()
        except NameError as e:
            exception_catched = True
            assert str(e) == "cannot delete repo in production organisation"

        assert exception_catched

    def test_gh_repo_delete_test(self):
        """
        verify that a test or QA repo can be deleted
        """

        # test gh repo can be deleted
        exception_catched = False

        try:
            GhRepo("lewagon-test/data-solutions").delete()
        except NameError:
            exception_catched = True

        assert not exception_catched

        # QA gh repo can be deleted
        exception_catched = False

        try:
            GhRepo("Le-Wagon-QA/data-solutions").delete()
        except NameError:
            exception_catched = True

        assert not exception_catched

    def test_gh_repo_crud(self):
        """
        verifies repo crud
        """

        # Arrange

        # Act
        repo = GhRepo("Le-Wagon-QA/automated-test")
        create_response = repo.create()
        get_response = repo.get()
        update_response = repo.update(dict(description="automated update test"))
        repo.delete()

        # Assert
        assert "node_id" in create_response
        assert "node_id" in get_response
        assert "node_id" in update_response

        create_node_id = create_response["node_id"]
        get_node_id = get_response["node_id"]
        update_node_id = update_response["node_id"]

        assert create_node_id == get_node_id
        assert create_node_id == update_node_id

        # Cleanup
