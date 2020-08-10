import logging
from typing import List, Callable, Tuple, Dict
import gzip
import concurrent.futures

import numpy as np
from tqdm import tqdm

from anom.utils.io import list_files

log = logging.getLogger(__name__)


class Logs:
    """
    Preprocessing for logs.

    Parameters
    ----------
    log_dir : str
        Location of directory containing logs.
    tokenize_function : Callable
        A funtion to return a tokenized list from a given string.

    Attributes
    ----------
    _log_dir : str
        Location of directory containing logs.
    _logs : str
        Giant string containing all logs.
    _log_lines : np.ndarray
        A numpy array of log lines. This is a more convenient way to deal with logs.
    _vocab : Dict[str, int]
        Dictionary of unique words from the logs as key and a unique id as
        value.
    """
    def __init__(
        self,
        log_dir: str,
        tokenize_function: Callable[[str], List[str]]
    ):
        self._log_dir = self._fix_log_dir(log_dir)
        self._tokenize = tokenize_function
        self._logs, self._log_lines = self._get_logs()
        self._vocab = self._get_vocab()

    def get_X(self) -> np.ndarray:
        """
        Format a design matrix for modeling.

        Returns
        -------
            A numpy array of size examples (m) x features (n). The features are
            each word in the log with a 1 representing if the word occured in a
            given example and a 0 otherwise.
        """
        log.info("Generating design matrix for modeling.")
        with concurrent.futures.ProcessPoolExecutor() as executor:
            X = np.array(
                    list(
                        tqdm(
                            executor.map(
                                self._process_log_line,
                                self._log_lines,
                                chunksize=len(self._log_lines) // 160,
                            ),
                            total=len(self._log_lines),
                        )
                    )
                )
        return X


    def _process_log_line(self, log_line: str) -> np.array:
        """Create feature vector out of log line.

        Parameters
        ----------
        log_line : str
            A single line from the logs.

        Returns
        -------
        x : np.array
            Feature vector representing whether words from the vocab were found
            in the line.
        """
        x = np.array([], dtype='int16')
        vocab: np.ndarray = np.array(list(self._vocab.keys()))
        for word in vocab:
            if str(word) in log_line:
                x = np.append(x, 1)
            else:
                x = np.append(x, 0)
        return x


    def _get_logs(self) -> np.ndarray:
        """
        Load log information.

        Returns
        -------
        logs : np.ndarray
            Logs in one string
        log_lines : List[str]
            A numpy array of logs.
        """
        log.info("Loading auth logs.")
        files: List[str] = list_files(self._log_dir)
        logs: str = ''
        # Replacing newlines with a charater we can split on.
        special_char: str = " $$$ "
        for fname in files:
            if '.gz' in fname:
                f = gzip.open(self._log_dir + fname, 'rt')
            else:
                f = open(self._log_dir + fname)
            logs += f.read().replace("\n", special_char)
            f.close()
        logs: str = self._process_logs(logs, None)
        # We drop the last itema sa it is just a blank space from special_char.
        log_lines: np.ndarray = np.array(logs.split(special_char)[:-1])
        return logs, log_lines


    def _get_vocab(self) -> Dict[str, int]:
        """
        Find unique words in the logs and assign a unique id.

        Returns
        -------
            Dictionary of unique tokens with a unique id.
        """
        log.info("Finding unique words in the logs.")
        tokens: List[str] = self._tokenize(self._logs)
        vocab: set = set(tokens)
        return {token: idx for idx, token in enumerate(vocab)}


    @staticmethod
    def _process_logs(logs, replace: List[Tuple]) -> str:
        """Use re.sub to replace certain elements within your logs as
        preprcossesing."""
        log.info("Processing logs.")
        return logs


    @staticmethod
    def _fix_log_dir(log_dir: str) -> str:
        """
        Add the slash at the end of a string path.

        Parameters
        ----------
        log_dir : str
            Location of the log direcotry.

        Returns
        -------
            Location of the log directory with a '/' at the end.
        """
        if log_dir[-1] != '/':
            return log_dir + '/'
        else:
            return log_dir


if __name__ == "__main__":
    from nltk.tokenize import TreebankWordTokenizer
    logs = Logs('data', TreebankWordTokenizer().tokenize)
    X = logs.get_X()
    import ipdb;
    ipdb.set_trace()
