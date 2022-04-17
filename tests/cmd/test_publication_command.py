
from wagon_common.cmd.publication_command import PublicationCommand
from wagon_common.path.scope import Scope

from wagon_common.tests.base.directory_equality import TestBaseDirectoryEquality

import os


class TestPublicationCommand(TestBaseDirectoryEquality):

    tests_root = os.path.normpath(os.path.join(
        os.path.dirname(__file__), "..", "data", "functional"))

    def test_publication_command_publish(self):
        """
        source: /path/project/  command/root/   content/path
        target: /path/target/   target/root/    content/path
        """

        # Arrange

        # Act
        def act():

            scope = Scope([
                os.path.join(self.source_root, "07", "04", "01", "in_scope.py"),
                os.path.join(self.source_root, "04", "*.py")])

            PublicationCommand().run(
                scope=scope,
                target_tld=self.processed_root)

        # Assert
        self.run_test_directory_identical(
            os.path.join(self.tests_root, "publish"), act)

        # Cleanup

    def test_publication_command_subpub(self):
        """
        source: /path/project/  command/root/   content/path
        target: /path/target/   target/root/    content/path
        """

        # Arrange

        # Act
        def act():

            scope = Scope([
                os.path.join(self.source_root, "07", "04", "01", "in_scope.py"),
                os.path.join(self.source_root, "04", "*.py")])

            PublicationCommand().run(
                scope=scope,
                target_tld=self.processed_root,
                command_root=os.path.join("command", "root"),
                target_root=os.path.join("target", "root"))

        # Assert
        self.run_test_directory_identical(
            os.path.join(self.tests_root, "subpub"), act)

        # Cleanup

    def test_publication_command_command_root(self):
        """
        source: /path/project/  command/root/   content/path
        target: /path/target/   target/root/    content/path
        """

        # Arrange

        # Act
        def act():

            scope = Scope([
                os.path.join(self.source_root, "07", "04", "01", "in_scope.py"),
                os.path.join(self.source_root, "04", "*.py")])

            PublicationCommand().run(
                scope=scope,
                target_tld=self.processed_root,
                command_root=os.path.join("command", "root"))

        # Assert
        self.run_test_directory_identical(
            os.path.join(self.tests_root, "command"), act)

        # Cleanup

    def test_publication_command_target_root(self):
        """
        source: /path/project/  command/root/   content/path
        target: /path/target/   target/root/    content/path
        """

        # Arrange

        # Act
        def act():

            scope = Scope([
                os.path.join(self.source_root, "07", "04", "01", "in_scope.py"),
                os.path.join(self.source_root, "04", "*.py")])

            PublicationCommand().run(
                scope=scope,
                target_tld=self.processed_root,
                target_root=os.path.join("target", "root"))

        # Assert
        self.run_test_directory_identical(
            os.path.join(self.tests_root, "target"), act)

        # Cleanup
