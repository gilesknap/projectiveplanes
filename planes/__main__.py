from typing import Optional

import typer

from planes import __version__
from planes.projective import project

cli = typer.Typer()


def version_callback(value: bool):
    if value:
        typer.echo(__version__)
        raise typer.Exit()


@cli.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        callback=version_callback,
        is_eager=True,
        help="Print the version of planes and exit",
    )
):
    """Do stuff ..."""


@cli.command()
def generate(
    order: int = typer.Argument(
        ..., help="The order of the projective plane to generate"
    )
):
    """
    Generate a projective plane to assign symbols to cards in the style of Dobble
    """
    project(order)


# test with:
#     pipenv run python -m planes
if __name__ == "__main__":
    cli()
