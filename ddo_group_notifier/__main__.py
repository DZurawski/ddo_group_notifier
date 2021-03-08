"""
"""

import os
import time
import logging
import webbrowser

from infi.systray import SysTrayIcon

from ddo_group_notifier import utils
from ddo_group_notifier import notifier


def open_configs(_: SysTrayIcon) -> None:
    """ Open the configs using the default YAML text editor. """
    configs_path = os.path.join(utils.get_project_root(), "configs", "configs.yaml")
    logging.debug(f"Opening the basic configs at {configs_path}")
    webbrowser.open(configs_path)


def open_filters(_: SysTrayIcon) -> None:
    """ Open the configs using the default YAML text editor. """
    filters_path = os.path.join(utils.get_project_root(), "configs", "filters.yaml")
    logging.debug(f"Opening the filters configs at {filters_path}")
    webbrowser.open(filters_path)


def on_quit(_: SysTrayIcon) -> None:
    logging.debug("The tray icon received the quit signal.")
    notifier.quit_event.set()


# The path to the "example.ico" icon file used on the system tray.
icon_path = os.path.join(utils.get_project_root(), "resources", "ddo_group_notifier_icon.ico")

# The text that is displayed when the mouse hovers over the system tray icon.
configs = utils.get_basic_configs()
hover_text = configs.get("app_name", "")

# Available options when the system tray icon is right-clicked.
menu_options = (
    ("Configs", None, open_configs),
    ("Filters", None, open_filters),
)

# Put the icon on the system tray.
with SysTrayIcon(icon_path, hover_text, menu_options, on_quit) as systray:
    # Sleep for a little bit just so we do not get a notification right as the program starts.
    time.sleep(2)
    notifier.notify()

logging.debug("The program has reached the end.")
