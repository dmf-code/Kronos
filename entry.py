from abstracts.singleton import Singleton
from application import Application
from core.browser import Browser
from core.engine import Engine
from core.facade import Facade
import argparse


class Entry(metaclass=Singleton):
    def __init__(self):
        super().__init__()
        self.parser = argparse.ArgumentParser(description='Run Spider')
        self.args = self.build_parser()

    def build_parser(self):
        self.parser.add_argument('--type', dest='spider_type', required=False, help='spider type', default='default')
        self.parser.add_argument('--name', dest='task_name', required=False, help='task name', default='default')
        self.parser.add_argument('--debug', dest='debug', required=False, help='debug signal', default=False)
        return self.parser.parse_args()

    @staticmethod
    def run():
        try:
            app = Application().app()
            app.set('browser', Browser())
            app.set('engine', Engine())
            app.set('facade', Facade())
            Facade().init(app)
            print('app', app)
            app.run()
        except Exception as e:
            print('into exception')
            print(e)


if __name__ == '__main__':
    Entry().run()
