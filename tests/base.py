
from wagon_common.helpers.subprocess import run_command

import os


class GitTestBase:

    def create_file(self, file):

        # add file
        with open(file, 'w'):
            pass

    def delete_file(self, file):

        # retrieve git controlled files
        os.remove(file)

    def git_restore_file(self, file):

        # restore file
        command = [
            "git",
            "restore",
            ] + [file]

        _rc, output, _error = run_command(command)
