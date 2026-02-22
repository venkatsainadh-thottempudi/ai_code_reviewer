import tomllib
import os


def load_config():
    config_path = "pyproject.toml"

    if not os.path.exists(config_path):
        return {}

    with open(config_path, "rb") as f:
        data = tomllib.load(f)

    return data.get("tool", {}).get("ai_reviewer", {})