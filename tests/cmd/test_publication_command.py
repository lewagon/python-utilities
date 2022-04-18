
from wagon_common.cmd.publication_command import PublicationCommand
from wagon_common.path.scope import Scope

from wagon_common.tests.base.directory_equality import TestBaseDirectoryEquality

import os
import glob


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

            sources = [
                os.path.join(self.source_root, "07", "04", "01", "in_scope.py"),
                os.path.join(self.source_root, "04", "**", "*.py")]

            globbed = [r for s in sources for r in glob.glob(s, recursive=True)]

            scope = Scope.from_sources(globbed)

            PublicationCommand().run(
                scope=scope,
                target_tld=self.processed_root)

        # Assert
        self.run_test_directory_identical(
            os.path.join(self.tests_root, "publish"), act)

        # Cleanup
