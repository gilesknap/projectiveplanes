from typing import Optional

import typer

from planes import __version__
from planes.projective import Projective

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
    """ main entry point for typer cli """


@cli.command()
def generate(
    order: int = typer.Argument(
        ..., help="The order of the projective plane to generate"
    )
):
    """
    Generate a projective plane to assign symbols to cards in the style of Dobble
    """
    p = Projective(order)
    p.project()


# test with:
#     pipenv run python -m planes
if __name__ == "__main__":
    cli()
