"""
"""

import os
import sys
import logging
import plyer

import test_utils

# Add the project root path to the system path.
test_utils.add_to_sys_path(test_utils.get_project_root())

from ddo_group_notifier import utils
from ddo_group_notifier import notifier

notifier.notify()
