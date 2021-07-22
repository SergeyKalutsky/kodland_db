from sqlalchemy.sql.expression import table
from .db import sess
from . import tables

t = {}
for attr_desc in dir(tables):
    attr = getattr(tables, attr_desc)
    if hasattr(attr, '__tablename__'):
        t[attr.__tablename__] = attr


def put(tablename, data):
    sess.add(t[tablename](**data))
    sess.commit()


def delete(tablename, key, val):
    sess.query(t[tablename]).filter(getattr(t[tablename], key) == val).delete()
    sess.commit()


def get(tablename, key, val):
    return sess.query(t[tablename]).filter(getattr(t[tablename], key) == val).first()


def get_all(tablename):
    return sess.query(t[tablename]).all()
