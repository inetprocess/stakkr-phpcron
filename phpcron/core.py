import click
import os

from clint.textui import colored, puts
from nginx_proxy import utils


@click.command(help='phpcron', name='phpcron')
@click.pass_context
def phpcron(ctx):
    print("here")