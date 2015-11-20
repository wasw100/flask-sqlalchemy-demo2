# -*- coding: utf-8 -*-
from flask import Flask


app = Flask(__name__)
app.config.from_pyfile('hello.cfg')


@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    app.run(port=9999)
