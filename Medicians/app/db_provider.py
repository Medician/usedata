__author__ = 'manya'
import sqlite3
from app import app
from contextlib import closing
from flask import g


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


def init_db():
    with closing(connect_db()) as x:
        with app.open_resource('database/create.sql', mode='r') as f:
            x.cursor().executescript(f.read())
        x.commit()


@app.before_request
def before_request():
    g.db = connect_db()


@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()


def _get_new_id():
    cur = g.db.execute('SELECT last_insert_rowid()')
    data = cur.fetchone()
    return data[0]


def insert_item(query, *args):
    g.db.execute(query, args)
    g.db.commit()



def get_item(query, *args):
    cur = g.db.execute(query, args)
    row = cur.fetchone()
    return row


def get_items(query, *args):
    cur = g.db.execute(query, args)
    rows = cur.fetchall()
    return rows