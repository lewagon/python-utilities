
from tests.base.directory_equality import TestBaseDirectoryEquality

from wagon_common.helpers.file import cp

import os


class TestDirectoryEquality(TestBaseDirectoryEquality):

    def test_directory_identical(self):
        """
        test that the `are_directories_identical` function works
        through the use of the `TestBaseDirectoryEquality` test base class
        """

        # Arrange

        # Act
        def act():
            cp(self.source_root, self.processed_root, recursive=True)

        # Assert
        self.run_test_directory_identical(
            os.path.join(
                self.tests_root, "helpers", "directory", "equal"),
            act)

        # Cleanup

    def test_directory_not_identical(self):

        # Arrange

        # Act
        def act():
            cp(self.source_root, self.processed_root, recursive=True)

        # Assert
        self.run_test_directory_identical(
            os.path.join(
                self.tests_root, "helpers", "directory", "not_equal"),
            act, equal=False)

        # Cleanup
