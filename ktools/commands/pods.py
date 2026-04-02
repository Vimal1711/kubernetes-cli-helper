#! /usr/bin/python
import click
import subprocess

@click.command(name="pods")
def list_pods():
    """List Kubernetes pods"""
    subprocess.run(["kubectl", "get", "pods"])
