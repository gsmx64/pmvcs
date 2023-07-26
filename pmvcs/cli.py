""" Cli file for Python MVC Shell Framework Package """
import argparse
from typing import Sequence

from pmvcs.core.setup.setup import SetupModel
from pmvcs.__version__ import __version__

from pmvcs.core.models.configuration import Configuration
from pmvcs.core.models.about import About


def main(argv: Sequence[str] | None = None) -> int:
    """
    Main function, prepare console arguments and args,
    returns functions values
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('task', type=str, help='Usage: pmvcs-cli setup -l en / pmvcs-cli menu -l en')
    parser.add_argument('-l', '--language', help='Usage: -l en (for english) / -l es (for spanish)')
    parser.add_argument('-v', '--version', action='version',
                        version=f'Python MVC Shell Framework Package {__version__}')
    args_values = parser.parse_args(argv)

    if args_values.language.lower() == 'es':
        setup = SetupModel('es')
    else:
        setup = SetupModel('en')

    try:
        if args_values.task.lower() == 'setup':
            return setup.install_app()

        if args_values.task.lower() == 'menu':
            return setup.install_multiple_module_setup()

        cfg = Configuration()
        pmvcs_about = About(cfg)
        pmvcs_about.tag = 'en'

        returns = pmvcs_about.get('framework')
        returns += f"\n{pmvcs_about.get('framework_copyright')} {__version__}"
        print(returns)

        return returns
    except ValueError as error:
        print(error)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
