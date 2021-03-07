"""
"""

import os
import webbrowser

from infi.systray import SysTrayIcon

from ddo_group_notifier import utils


def open_configs(_: SysTrayIcon) -> None:
    """ Open the configs using the default YAML text editor. """
    configs_path = os.path.join(utils.get_project_root(), "configs", "configs.yaml")
    webbrowser.open(configs_path)


def open_filters(_: SysTrayIcon) -> None:
    """ Open the configs using the default YAML text editor. """
    filters_path = os.path.join(utils.get_project_root(), "configs", "filters.yaml")
    webbrowser.open(filters_path)


# The path to the "example.ico" icon file used on the system tray.
icon_path = os.path.join(utils.get_project_root(), "resources", "ddo_group_notifier_icon.ico")

# The text that is displayed when the mouse hovers over the system tray icon.
hover_text = "DDO Group Notifier"

# Available options when the system tray icon is right-clicked.
menu_options = (
    ("Configs", None, open_configs),
    ("Filters", None, open_filters),
)

# Put the icon on the system tray.
with SysTrayIcon(icon_path, hover_text, menu_options) as systray:
    pass
