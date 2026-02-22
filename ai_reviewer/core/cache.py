import hashlib
import json
import os

CACHE_FILE = ".ai_reviewer_cache.json"


def calculate_file_hash(file_path):
    """
    Calculate_file_hash function.

    Args:
        file_path (type): Description of file_path.

    Returns:
        type: Description of return value.
    """
    hasher = hashlib.sha256()
    with open(file_path, "rb") as f:
        hasher.update(f.read())
    return hasher.hexdigest()


def load_cache():
    """
    Load_cache function.

    Returns:
        type: Description of return value.
    """
    if not os.path.exists(CACHE_FILE):
        return {}

    with open(CACHE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_cache(cache_data):
    """
    Save_cache function.

    Args:
        cache_data (type): Description of cache_data.

    Returns:
        type: Description of return value.
    """
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache_data, f, indent=2)