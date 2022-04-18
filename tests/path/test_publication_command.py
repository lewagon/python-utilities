
from wagon_common.path.publication_command import PublicationCommand
from wagon_common.path.scope import Scope

from wagon_common.tests.base.directory_equality import TestBaseDirectoryEquality

import os
import glob


class TestPublicationCommand(TestBaseDirectoryEquality):

    tests_root = os.path.normpath(os.path.join(
        os.path.dirname(__file__), "..", "data", "functional"))

    cwd = os.getcwd()

    def __glob(self, sources):

        globbed = []

        # iterate through sources
        for source in sources:
            for resolved in glob.glob(source, recursive=True):
                relative = os.path.relpath(
                    resolved, start=self.cwd)
                globbed.append(relative)

        return globbed

    def test_publication_command_publish(self):
        """
        source: /path/project/  command/root/   content/path
        target: /path/target/   target/root/    content/path
        """

        # Arrange

        # Act
        def act():

            sources = [
                os.path.join(self.source_root, "07", "04", "01", "in_scope.py"),
                os.path.join(self.source_root, "04", "**", "*.py")]

            scope = Scope.from_sources(self.__glob(sources))

            PublicationCommand().run(
                scope=scope,
                target_tld=self.processed_root)

        # Assert
        self.run_test_directory_identical(
            os.path.join(self.tests_root, "publish"), act)

        # Cleanup

    def test_publication_command_command_root(self):
        """
        source: /path/project/  command/root/   content/path
        target: /path/target/   target/root/    content/path
        """

        # Arrange

        # Act
        def act():

            command_root = os.path.join(self.source_root, "command", "root")

            sources = [
                os.path.join(command_root, "07", "04", "01", "in_scope.py"),
                os.path.join(command_root, "04", "**", "*.py")]

            scope = Scope.from_sources(self.__glob(sources))

            PublicationCommand().run(
                scope=scope,
                target_tld=self.processed_root,
                command_root=command_root)

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

            sources = [
                os.path.join(self.source_root, "07", "04", "01", "in_scope.py"),
                os.path.join(self.source_root, "04", "**", "*.py")]

            scope = Scope.from_sources(self.__glob(sources))

            PublicationCommand().run(
                scope=scope,
                target_tld=self.processed_root,
                target_root=os.path.join("target", "root"))

        # Assert
        self.run_test_directory_identical(
            os.path.join(self.tests_root, "target"), act)

        # Cleanup

    def test_publication_command_subpub(self):
        """
        source: /path/project/  command/root/   content/path
        target: /path/target/   target/root/    content/path
        """

        # Arrange

        # Act
        def act():

            command_root = os.path.join(self.source_root, "command", "root")

            sources = [
                os.path.join(command_root, "07", "04", "01", "in_scope.py"),
                os.path.join(command_root, "04", "**", "*.py")]

            scope = Scope.from_sources(self.__glob(sources))

            PublicationCommand().run(
                scope=scope,
                target_tld=self.processed_root,
                command_root=command_root,
                target_root=os.path.join("target", "root"),
                verbose=True)

        # Assert
        self.run_test_directory_identical(
            os.path.join(self.tests_root, "subpub"), act)

        # Cleanup
