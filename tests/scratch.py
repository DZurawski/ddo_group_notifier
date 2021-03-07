"""
"""

import time

from infi.systray import SysTrayIcon


def say_hello(_):
    print("Hello, World!")


menu_options = (("Say Hello", None, say_hello),)

with SysTrayIcon(None, "Hi", menu_options) as systray:
    time.sleep(10)
