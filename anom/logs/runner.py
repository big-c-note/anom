"""Usage: anom process_logs [OPTIONS]

Process the logs.

Options:
--log_dir TEXT            Path to the directory where you are keeping your
                          auth logs.
--tokenize_function TEXT  Tokenize function.
--help                    Show this message and exit."""
from typing import Callable, List, Dict
from pathlib import Path

import click
from nltk.tokenize import TreebankWordTokenizer

from anom.logs.logs import Logs
from anom.utils.io import create_dir, get_config


@click.command()
@click.option(
    "--log_dir",
    default='.',
    help=(
        "Path to the directory where you are keeping your auth logs."
    )
)
def process_logs(
    log_dir: str,
    # TODO: Need to override base parameter class for click so I can pass a
    # func.
    tokenize_function: Callable[[str], List[str]]=TreebankWordTokenizer().tokenize
):
    """Process the logs."""
    save_dir: Path = create_dir()
    config: Dict[str, int] = {**locals()}
    # Save the config file to the save_dir.
    get_config(save_dir, config)
    logs = Logs(
        log_dir=log_dir,
        tokenize_function=tokenize_function,
        save_dir=save_dir
    )
    X = logs.process_logs()


if __name__ == "__main__":
    process_logs()
