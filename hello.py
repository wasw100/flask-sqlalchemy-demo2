# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile('hello.cfg')
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))


@app.route('/')
def index():
    return 'index'


@app.route('/create')
def create():
    db.create_all()
    return 'ok'


@app.route('/drop')
def drop():
    db.drop_all()
    return 'ok'


@app.route('/query')
def query():
    subquery = Todo.query.subquery()
    print subquery
    print 'aaaaa'
    print Todo.query
    return 'query'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999)
