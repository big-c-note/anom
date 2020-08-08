import logging
from typing import List
from os import listdir
from os.path import isfile, join

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
