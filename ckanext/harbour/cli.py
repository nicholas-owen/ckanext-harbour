import click


@click.group(short_help="harbour CLI.")
def harbour():
    """harbour CLI.
    """
    pass


@harbour.command()
@click.argument("name", default="harbour")
def command(name):
    """Docs.
    """
    click.echo("Hello, {name}!".format(name=name))


def get_commands():
    return [harbour]
