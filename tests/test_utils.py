"""
"""

import sys
import os
import pathlib


def get_project_root() -> str:
    """ Return this project's root directory. """
    return str(pathlib.Path(os.path.realpath(__file__)).parent.parent)


def add_to_sys_path(path: str) -> None:
    """ Add the path to the python path. """
    abspath = os.path.abspath(path)
    if abspath not in sys.path:
        sys.path.insert(0, abspath)
