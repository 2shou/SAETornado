# coding: utf-8

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from sqlalchemy import Column
from sqlalchemy.types import Integer

from settings import db_config


# 修复「MySQL has gone away」的错误
engine = create_engine(db_config, pool_recycle=5, poolclass=NullPool)

DB_Session = sessionmaker(bind=engine)
BaseModel = declarative_base()


def init_db():
    BaseModel.metadata.create_all(engine)


def drop_db():
    BaseModel.metadata.drop_all(engine)


class TestModel(BaseModel):
    __tablename__ = 'test'

    # 配置你的字段
    id = Column(Integer, primary_key=True)


if __name__ == '__main__':
    init_db()