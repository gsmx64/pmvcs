""" App file for Python MVC Shell Framework Package """
from pmvcs.core.router import Router


if __name__ == '__main__':
    app = Router()
    app.create_app()
