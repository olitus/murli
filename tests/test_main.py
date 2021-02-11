from click.testing import CliRunner
from pyto import cli


def test_init():
    """
    """

    runner = CliRunner()
    result = runner.invoke(cli, ['init'])

    assert result.exit_code == 0
    assert result.output == 'Initialize Python project in given directory\n'