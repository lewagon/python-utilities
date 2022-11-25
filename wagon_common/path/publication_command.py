"""
resolves the command destination for each source in the scope
runs the command on each source
"""

from wagon_common.helpers.file import cp
from wagon_common.helpers.output import print_files

import os

from wagon_common.helpers.output import red, blue


class PublicationCommand:

    def run(self, scope, target_tld, command_root=None, target_root=None, verbose=False):

        if verbose:
            print_files("blue", "Files in scope", scope)

        # process tld relative target
        abs_target_tld = os.path.relpath(os.path.join(
            scope.repo.tld, target_tld))

        if verbose:
            blue("\nResolved target tld:",
                 f"\n- source repo tld: {scope.repo.tld}"
                 + f"\n- target tld: {target_tld}"
                 + f"\n- resolved target tld: {abs_target_tld}")

        if verbose:
            blue("\nProcess files:",
                 f"\n- from cwd: {scope.cwd}"
                 + f"\n- command root: {command_root}"
                 + f"\n- target root: {target_root}")

        # iterate through scope files
        for source in scope:

            # process cwd relative source
            tld_source = self.__rebase_on_tld(
                source, scope.cwd, scope.repo.tld)

            # process file destination path
            destination = self.__get_destination(
                source=tld_source,
                target_tld=abs_target_tld,
                command_root=command_root,
                target_root=target_root)

            if verbose:
                print(f"- {source}: {destination}")

            # run transformation
            self.__transform(source, destination)

    def __rebase_on_tld(self, source, cwd, tld):
        """
        rebase cwd relative path to tld
        """

        # process source full path
        cwd_source = os.path.normpath(os.path.join(
            cwd, source))

        # process source rel path
        tld_source = os.path.relpath(
            cwd_source, start=tld)

        return tld_source

    def __get_destination(
            self,
            source,
            target_tld,
            command_root,     # path fragment
            target_root):     # path fragment

        processed_source = source

        # substract command root
        if command_root is not None:
            processed_source = os.path.relpath(
                processed_source, start=command_root)

            if processed_source[:2] == "..":

                red("\nFile in scope outside of provided command root 🤕",
                    f"\n- source file: {processed_source}"
                    + f"\n- command root: {command_root}")

                raise Exception("File in scope outside of repo")

        # process target root
        if target_root is None:
            target_root = "."

        # process destination
        destination = os.path.normpath(os.path.join(
            target_tld, target_root, processed_source))

        return destination

    def __transform(self, source, destination):
        """
        default transformation to override
        """

        # copy file as is
        cp(source, destination)
