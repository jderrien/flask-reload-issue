import os
import sys

from flask import Flask, request
from helpers import logger

app = Flask(__name__)
logger.configure(app)

app.logger.info('Application started (pid=%s, debug=%s)' % (os.getpid(), app.debug))
app.logger.info('Path: %s' % sys.path)


@app.route("/")
def hello():
    return "Hello world!\n"


@app.route("/debug")
def debug():
    app.logger.info('debug enpoint called')
    return '<pre>\nApplication is started\n- pid=%s\n- debug=%s\n- mod_wsgi.process_group=%s\n</pre>\n' % (os.getpid(), app.debug, repr(request.environ['mod_wsgi.process_group']))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
