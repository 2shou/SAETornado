# coding: utf-8

from os import environ

import sae.const

debug = 'SERVER_SOFTWARE' not in environ

if debug:
    # 根据你本地的MySQL配置
    db_name = 'test'
    db_user = 'root'
    db_passwd = ''
    db_host = '127.0.0.1'
    db_port = '3306'
else:
    db_name = sae.const.MYSQL_DB
    db_user = sae.const.MYSQL_USER
    db_passwd = sae.const.MYSQL_PASS
    db_host = sae.const.MYSQL_HOST
    db_port = sae.const.MYSQL_PORT

db_config = 'mysql+mysqldb://%s:%s@%s:%s/%s?charset=utf8' % (db_user, db_passwd, db_host, db_port, db_name)

# cookie加密的密钥
cookie_secret = 'test' if debug else sae.const.SECRET_KEY