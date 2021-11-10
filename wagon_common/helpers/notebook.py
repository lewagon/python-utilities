
from wagon_common.helpers.file import ensure_path_directory_exists

import json


def read_notebook(notebook_path):
    """return a dictionary read from the notebook"""

    # read file
    with open(notebook_path, encoding='utf-8') as file:
        data = json.load(file)

    # return dictionary
    return data


def save_notebook(notebook_content, notebook_path):
    """save notebook"""

    # create destination directory
    ensure_path_directory_exists(notebook_path)

    # save notebook to disk
    with open(notebook_path, "w", encoding='utf-8') as file:

        # make sure that we save unicode so that emojis are not decomposed
        json.dump(notebook_content, file, indent=1, ensure_ascii=False)
        file.write("\n")  # add the otherwise missing end of file empty line
