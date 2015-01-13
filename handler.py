# coding: utf-8

import tornado.web

from models import DB_Session


class BaseHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.session = DB_Session()

    def on_finish(self):
        self.session.close()


class TestHandler(BaseHandler):
    def get(self):
        # 业务逻辑
        self.write('')