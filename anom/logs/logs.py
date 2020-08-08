import logging

import numpy as np

log = logging.getLogger(__name__)


class Logs:
    """
    Logs.

    Parameters
    ----------
    log_dir : str
        Location of directory containing logs.

    Attributes
    ----------
    _log_dir : str
        Location of directory containing logs.
    """
    def __init__(
        self,
        log_dir: str
    ):
        self._log_dir = log_dir
        self.logs = self._get_logs()

    def _get_logs(self) -> np.ndarray:
        """
        Load log information.

        Returns
        -------
        logs : np.ndarray
            A numpy array of logs.
        """
        pass

