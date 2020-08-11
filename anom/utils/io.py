import logging
from typing import List, Dict
from os import listdir
from os.path import isfile, join
import datetime
from pathlib import Path

import yaml

log = logging.getLogger(__name__)


def list_files(directory: str) -> List[str]:
    """List files in a directory.

    Parameters
    ----------
    directory : str
        Location of directory to find files in.
    """
    files = [f for f in listdir(directory) if isfile(join(directory, f))]
    return files


def create_dir():
    """Create and get a unique dir path to save to using a timestamp."""
    time = str(datetime.datetime.now())
    for char in ":- .":
        time = time.replace(char, "_")
    path: Path = Path(f"./results_{time}")
    path.mkdir(parents=True, exist_ok=True)
    return path


def get_config(save_dir: Path, config: Dict[str, int]):
    """Get configurations

    Parameters
    ----------
    save_dir : Path
        Path object of the directory to save the output to.
    config : Dict[str, int]
        Dictionary of locals.
    """
    with open(save_dir / "config.yaml", "w") as steam:
        yaml.dump(config, steam)
