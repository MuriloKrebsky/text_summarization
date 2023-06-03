import os
from box.exceptions import BoxValueError
from box import ConfigBox
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Read yaml file and returns.

    Parameters
    ----------
    path_to_yaml (Path):
        Path like object to yaml file

    Raises
    ------
    ValueError: if yaml file is empty
        e: Empty file

    Returns
    --------
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Create list of directories.

    Parameters
    ----------
        path_to_directories (list):
            List of path of directories
        verbose (bool):
            Whether to print directory creation status (default: True)
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get size in GB.

    Parameters
    ----------
    path (Path):
        Path like object

    Returns
    -------
        str: Size in GB
    """
    size_in_bytes = os.path.getsize(path)
    size_in_gb = size_in_bytes / 1024 / 1024 / 1024
    
    return f"{size_in_gb:.2f}"