import os
import socket


def pythonAppName():
    return 'filepath'

prod = ['production server']
stage = ['staging server'] 
local=['local server ']


def gethostname():
    return socket.gethostname()


def db():
    host = gethostname()
    if host in prod:
        db = {'server': 'prod', 'database': 'Name of database'}
    elif host in stage:
        db = {'server': 'staging server', 'database': 'staging database'}
    
    elif host in local:
        db = {'server': 'localhost', 'database': 'local db'}

    else:
        raise Exception('path_and_db_config.py: No local db ')
    return db

def  filepath():
    """Returns filepath to the file 
    
    """
    host = gethostname()
    if host in prod:
        filepath = "\\\\to file "
    elif host in stage:
        filepath =  "\\\\to file" 
    elif host in local:
        filepath = os.path.join(os.path.expanduser("~"), "Documents" )
    else:
        raise Exception('config.py: No approvalfilepath')
    return filepath

rootpath = os.path.dirname(os.path.realpath(__file__))


logpath = rootpath+"/logs/"

logconfig = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "%(asctime)s|%(levelname)s|%(message)s"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "stream": "ext://sys.stdout"
        },
        "info_file_handler": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "INFO",
            "formatter": "simple",
            "filename": logpath+"info.log",
            "maxBytes": 10485760,
            "backupCount": 20,
            "encoding": "utf8",
        },
        "error_file_handler": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "ERROR",
            "formatter": "simple",
            "filename": logpath+"errors.log",
            "maxBytes": 10485760,
            "backupCount": 20,
            "encoding": "utf8"
        }


    },
    "loggers": {
        "my_module": {
            "level": "ERROR",
            "handlers": ["console"],
            "propagate": "no"
        }
    },
    "root": {
        "level": "INFO",
        "handlers": ["console", "info_file_handler", "error_file_handler"]
    }
}
