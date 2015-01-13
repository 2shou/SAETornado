# coding: utf-8

import os

import tornado.wsgi

from settings import cookie_secret

from handler import *

metadata = dict(
    static_path=os.path.join(os.path.dirname(__file__), 'static'),
    template_path=(os.path.join(os.path.dirname(__file__), "templates")),
    # 设置SAE的app_secret为secret_cookie的加密密钥
    cookie_secret=cookie_secret,
)

urls = [
    (r'/test', TestHandler),
]


class SAEApplication(tornado.wsgi.WSGIApplication):
    def __init__(self):
        tornado.wsgi.WSGIApplication.__init__(self, urls, **metadata)
