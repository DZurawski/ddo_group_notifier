"""
"""

import pathlib


def get_project_root() -> pathlib.Path:
    """ Return this project's root directory. """
    return pathlib.Path(__file__).parent.parent
