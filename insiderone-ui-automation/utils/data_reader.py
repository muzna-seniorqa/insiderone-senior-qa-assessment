"""Load YAML test data by path (e.g. get_data('data/filter_data.yaml')). Same pattern as Utils.data_reader.get_data in other projects."""
import os
import yaml

_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_data(relative_path: str) -> dict:
    """
    Load a YAML file from the project. Path is relative to project root.

    Example:
        from utils.data_reader import get_data
        test_data = get_data("data/filter_data.yaml")
        location = test_data["filter"]["location"]
    """
    path = os.path.join(_PROJECT_ROOT, relative_path)
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)
