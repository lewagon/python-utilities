
from wagon_common.helpers.git.remote import (
    git_remote_list, git_remote_get_url, git_remote_get_probable_url)


class TestRemotes():

    def test_remote_list(self):
        """
        visual test (use `pytest -s`)
        """

        # Arrange

        # Act
        remotes = git_remote_list(path=".")

        print(f"\nremotes:\n- {remotes=}")

        # Assert
        assert True

        # Cleanup

    def test_remote_url(self):
        """
        visual test (use `pytest -s`)
        """

        # Arrange

        # Act
        remotes = git_remote_list(path=".")
        url = git_remote_get_url(path=".", name=remotes[0])

        print(f"\nremote url:\n- {url=}")

        # Assert
        assert True

        # Cleanup

    def test_git_remote_get_probable_url(self):
        """
        visual test (use `pytest -s`)
        """

        # Arrange

        # Act
        url = git_remote_get_probable_url(path=".", gnn="lewagon")

        print(f"\nremote probable url:\n- {url=}")

        # Assert
        assert True

        # Cleanup
