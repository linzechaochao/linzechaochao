#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('jsplumb_copy.html')


if __name__ == '__main__':
    app.run()
