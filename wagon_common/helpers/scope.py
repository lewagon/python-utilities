"""
scope helpers
"""

from wagon_common.helpers.git.ls import list_git_controlled_files
from wagon_common.helpers.output import print_files

import os
import glob

from colorama import Fore, Style


def resolve_scope(sources, patterns, return_inexisting=False, verbose=False):
    """
    return sets of git controlled files within sources and matching patterns
    """

    if verbose:
        print_files("blue", "Provided scope", sources)

    # correct sources
    if len(sources) == 0:

        # use every files in the current directory
        sources = sorted(glob.glob("*") + glob.glob(".*"))

        if verbose:
            print_files("blue", "Files and directories added to the scope from the current directory", sources)

    # iterate through patterns
    results = []
    inexisting_entries = []

    for pattern in patterns:

        if verbose:
            print(Fore.BLUE
                  + f"\nResolving files matching the {pattern} pattern in the scope..."
                  + Style.RESET_ALL)

        # remove all sources that do not match the pattern
        filtered_sources = []
        ignored_files = []

        for source in sources:

            # testing if source is a directory
            if os.path.isdir(source):

                # apply pattern
                filtered_source = os.path.join(source, pattern)
                filtered_sources.append(filtered_source)

            elif os.path.isfile(source):

                # get file extension
                _, file_ext = os.path.splitext(source)
                _, pattern_ext = os.path.splitext(pattern)

                # verify if file matches pattern
                if file_ext == pattern_ext or pattern_ext == "":

                    # add source
                    filtered_sources.append(source)

                else:

                    # source is ignored
                    ignored_files.append(source)

            else:

                # the source does not exist
                if return_inexisting:
                    inexisting_entries.append(source)

        if verbose:
            print_files("red", f"Files ignored for {pattern}", ignored_files)

        if verbose:
            print_files("blue", f"Files and directory patterns matching {pattern}", filtered_sources)

        if len(filtered_sources) > 0:

            # list git controlled files within sources matching pattern
            res = list_git_controlled_files(filtered_sources, verbose=verbose)

        else:

            # no results
            res = []

        if verbose:
            print_files("green", f"Git controlled files matching {pattern}", res)

        # append sorted unique results
        results.append(sorted(set(res)))

    if return_inexisting:

        unique_inexisting_entries = sorted(set(inexisting_entries))

        if verbose:
            print_files("red", "Inexisting files or directories", unique_inexisting_entries)

        return results, unique_inexisting_entries

    return results


if __name__ == '__main__':

    all, nb, py, rb = resolve_scope(["..", "README.md"], ["*", "*.ipynb", "*.py", "*.rb"], verbose=True)

    print("\nall:")
    [print(line) for line in all]

    print("\nnb:")
    [print(line) for line in nb]

    print("\npy:")
    [print(line) for line in py]

    print("\nrb:")
    [print(line) for line in rb]
