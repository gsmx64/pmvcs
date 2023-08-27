""" App file for Python MVC Shell Framework Package """
try:
    from pmvcs.core.router import Router

    def main():
        app = Router()
        app.create_app()

except ModuleNotFoundError:
    def main():
        print('>'*54)
        print('>>> Please first run:')
        print('>>>   pip install -r requirements.txt')
        print('>>>   or pip3 install -r requirements.txt')
        print('>'*54)
