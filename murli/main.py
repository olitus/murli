"""
"""

import click


@click.group()
def murli():
    pass


@murli.command()
@click.option('--python', 
              type=PythonVersion)
@click.argument('path')
def new(path: PythonVersion):
    click.echo("Create new Python project at {path}")


@murli.command()
def init():
    click.echo("Initialize Python project in given directory")




class PythonVersion(click.ParamType):
    name = "integer"

    def convert(self, value, param, ctx):
        try:
            if value[:2].lower() == "0x":
                return int(value[2:], 16)
            elif value[:1] == "0":
                return int(value, 8)
            return int(value, 10)
        except TypeError:
            self.fail(
                "expected string for int() conversion, got "
                f"{value!r} of type {type(value).__name__}",
                param,
                ctx,
            )
        except ValueError:
            self.fail(f"{value!r} is not a valid integer", param, ctx)