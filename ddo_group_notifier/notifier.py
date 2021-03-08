"""
"""

import os
import sys
import logging
import plyer
import threading
import time
import datetime
from ddo_group_notifier import utils
from ddo_group_notifier import ddo_audit_data

logging.basicConfig(stream=sys.stderr, level=utils.get_logging_level())

quit_event = threading.Event()


def notify() -> None:
    """ The notification loop. Will send notifications through Windows 10 notifications system. """
    logging.debug("Starting notify() function.")

    start_time = time.time()

    while not quit_event.is_set():
        # Load in configs.
        configs = utils.get_basic_configs()
        if not configs:
            logging.debug("Unable to load in configs.")
            return

        # Get number of seconds between getting data from the DDO Audit API.
        try:
            query_seconds_gap = float(configs.get("query_seconds_gap", ""))
        except ValueError as error:
            logging.debug("Unable to read variable 'query_seconds_gap'")
            logging.debug(error)
            return

        # Get number of seconds that notifications are displayed for.
        try:
            display_seconds_gap = float(configs.get("display_seconds_gap", ""))
        except ValueError as error:
            logging.debug("Unable to read variable 'display_seconds_gap'")
            logging.debug(error)
            return

        logging.debug("Getting data from DDO Audit.")
        title, message = ddo_audit_data.get_title_and_message()

        if title or message:
            logging.debug(f"Sending notification at {datetime.datetime.now()}.")
            plyer.notification.notify(
                title=title,
                message=message,
                timeout=display_seconds_gap,
                app_name=configs.get("app_name", "[app name is missing from configs.]"),
                app_icon=os.path.join(utils.get_project_root(), "resources", "ddo_group_notifier_icon_2.ico"),
            )
        else:
            logging.debug(f"Not sending any notification at {datetime.datetime.now()}")

        # Sleep until ready for next iteration.
        sleep_duration = query_seconds_gap - ((time.time() - start_time) % query_seconds_gap)
        logging.debug(f"Sleeping for {sleep_duration} seconds.")
        quit_event.wait(sleep_duration)

    logging.debug("The notifier loop has ended.")
