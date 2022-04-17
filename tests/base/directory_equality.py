
from wagon_common.helpers.directories import are_directories_identical

from colorama import Fore, Style

import os
import shutil


class TestBaseDirectoryEquality():

    tests_root = os.path.normpath(os.path.join(
        os.path.dirname(__file__), "..", "data"))

    def run_test_directory_identical(self, test_data_root, act_function, equal=True):

        # Arrange
        self.source_root = os.path.join(test_data_root, "source")
        self.processed_root = os.path.join(test_data_root, "processed")
        control_root = os.path.join(test_data_root, "control")

        # Act
        act_function()

        # Assert
        rc, output, error = are_directories_identical(
            self.processed_root, control_root)

        if equal:

            if rc != 0:

                print(Fore.RED
                      + "\nDirectory content does not match 🤕"
                      + Style.RESET_ALL
                      + f"\n- rc: {rc}"
                      + f"\n- output: {output}"
                      + f"\n- error: {error}")
                print(output.decode("utf-8"))

            assert rc == 0

        else:

            if rc == 0:

                print(Fore.RED
                      + "\nDirectory content matches 😬"
                      + Style.RESET_ALL
                      + f"\n- rc: {rc}"
                      + f"\n- output: {output}"
                      + f"\n- error: {error}")
                print(output.decode("utf-8"))

            assert rc != 0

        # Cleanup
        shutil.rmtree(self.processed_root, ignore_errors=True)
