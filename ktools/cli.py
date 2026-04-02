#! /usr/bin/python
import click
from ktools.commands.pods import list_pods

@click.group()
def cli():
    """Kubernetes CLI Helper"""
    pass

cli.add_command(list_pods)

if __name__ == "__main__":
    cli()
