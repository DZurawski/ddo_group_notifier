"""
"""

from ddo_group_notifier import utils
import logging
import requests
from typing import Tuple, List


def get_title_and_message() -> Tuple[str, str]:
    """ Return a title and message string after querying DDO Audit for matching groups. """
    groups = get_groups_data()

    if not groups:
        logging.debug("Did not find any groups matching any of the filters.")
        return "", ""

    if len(groups) == 1:
        title = f"Found {len(groups)} Matching DDO Group"
    else:
        title = f"Found {len(groups)} Matching DDO Groups"

    messages = []
    for group in groups:
        if group.get("Quest", None):
            quest = group["Quest"]["Name"]
        else:
            quest = "No Quest"
        comment = group.get("Comment", "")
        message = f"{quest}: {comment}"
        messages.append(message)
    message = "\n".join(messages)

    return title, message


def get_groups_data() -> List:
    """ Get a list of groups that match up with the filters defined in configs/filters.yaml. """
    filters_configs = utils.get_filter_configs()
    api_configs = utils.get_audit_api_configs()

    if filters_configs.get("server", ""):
        params = {"s": filters_configs["server"]}
    else:
        params = dict()

    response = requests.get(url=api_configs["group_data_url"], params=params)

    if response.status_code not in (200,):
        logging.debug("Unable to get good response from DDO Audit API.")
        logging.debug(response.text)
        return []

    groups = []
    for filters in filters_configs["filters"]:
        for group in response.json()["Groups"]:
            character_level = filters.get("character_level", None)
            if character_level:
                if int(group["MinimumLevel"]) > int(filters["character_level"]):
                    continue
                if int(group["MaximumLevel"]) < int(filters["character_level"]):
                    continue

            difficulties = filters.get("difficulties", [])
            if group["Difficulty"].lower() not in [_.lower().strip() for _ in difficulties]:
                continue

            quests = [_.lower().strip() for _ in filters.get("Quests", [])]
            if quests:
                if not group["Quest"]:
                    continue
                if group["Quest"]["Name"].lower() not in quests:
                    continue

            min_base_quest_level = filters.get("min_base_quest_level", None)
            max_base_quest_level = filters.get("max_base_quest_level", None)
            if min_base_quest_level:
                if not group["Quest"]:
                    continue
                heroic_min = int(min_base_quest_level) > group["Quest"]["HeroicNormalCR"]
                if heroic_min:
                    continue
            if max_base_quest_level:
                if not group["Quest"]:
                    continue
                heroic_max = int(max_base_quest_level) < group["Quest"]["HeroicNormalCR"]
                if heroic_max:
                    continue
            groups.append(group)
    return groups
