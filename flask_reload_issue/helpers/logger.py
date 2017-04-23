import logging

from config import LOGGING_CONFIG

def configure(app):
    #RaiseSyntaxError

    log_formatter = logging.Formatter('%(asctime)s %(levelname)-8s :: %(message)s  [in %(pathname)s:%(lineno)d]')

    log_handler = logging.FileHandler(LOGGING_CONFIG['logfile_path'])
    log_handler.setFormatter(log_formatter)

    app.logger.setLevel(logging.INFO)
    app.logger.addHandler(log_handler)
