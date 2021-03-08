"""
"""

import os
import yaml
import pathlib
from typing import Dict


def get_project_root() -> pathlib.Path:
    """ Return this project's root directory. """
    return pathlib.Path(os.path.realpath(__file__)).parent.parent


def get_basic_configs() -> Dict:
    configs_path = os.path.join(get_project_root(), "configs", "configs.yaml")
    with open(configs_path, "r") as file:
        try:
            configs = yaml.safe_load(file)
            return configs
        except yaml.YAMLError:
            return dict()


def get_audit_api_configs() -> Dict:
    configs_path = os.path.join(get_project_root(), "configs", "ddo_audit_api.yaml")
    with open(configs_path, "r") as file:
        try:
            configs = yaml.safe_load(file)
            return configs
        except yaml.YAMLError:
            return dict()


def get_filter_configs() -> Dict:
    configs_path = os.path.join(get_project_root(), "configs", "filters.yaml")
    with open(configs_path, "r") as file:
        try:
            configs = yaml.safe_load(file)
            return configs
        except yaml.YAMLError:
            return dict()


def get_logging_level() -> str:
    configs = get_basic_configs()
    return configs.get("logging_verbosity", "")
