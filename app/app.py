import tornado.web
from .handlers import main_handler


def make_app():
    return tornado.web.Application([
        (r"/", main_handler.MainHandler),
    ])
