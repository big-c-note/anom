import click

from anom.logs.runner import process_logs


@click.group()
def cli():
    """The cli for the anom package thatgroups various scripts."""
    pass

cli.add_command(process_logs, name="process_logs")
