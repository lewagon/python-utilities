
import glob
import os


def glob_sources(sources, cwd):

    globbed = []

    # iterate through sources
    for source in sources:
        for resolved in glob.glob(source, recursive=True):
            relative = os.path.relpath(
                resolved, start=cwd)
            globbed.append(relative)

    return globbed
