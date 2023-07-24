""" PMVCS file for Python MVC Shell Framework Package """
from pmvcs.core.setup.setup import SetupModel
from pmvcs.core.models.configuration import Configuration
from pmvcs.core.models.about import About
from pmvcs.__version__ import __version__


def main():
    """ Main function, returns pmvcs example """
    task = input('(1) Setup / (2) Menu: ')
    setup = SetupModel(None)

    if task == '1':
        return setup.install_app()

    if task == '2':
        return setup.install_multiple_module_setup()

    cfg = Configuration()
    pmvcs_about = About(cfg)
    pmvcs_about.tag = 'en'
    pmvcs_about.update

    returns = pmvcs_about.get('framework')
    returns += f"\n{pmvcs_about.get('framework_copyright')} {__version__}"
    print(returns)

    return returns
