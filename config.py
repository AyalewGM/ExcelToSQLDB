
import urllib.parse
import json
import os
import urllib
import logging.config
import pythonjsonlogger
from path_and_db_config import rasdb


from structlog import configure, processors, stdlib, threadlocal
 
basedir = os.path.abspath(os.path.dirname(__file__))
debug = False

rasdb = rasdb()


SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = False




if rasdb['server'] == 'localhost':

    rasconn = urllib.parse.quote_plus("DRIVER={ODBC Driver 17 for SQL Server};SERVER="+rasdb['server']+";DATABASE=" +rasdb['database']+

                                       ";UID="+user+";PWD="+ password)
else:

    rasconn = urllib.parse.quote_plus("DRIVER={ODBC Driver 17 for SQL Server};SERVER=" + rasdb['server'] + ";DATABASE=" + rasdb['database'] +
                                      ";UID=" + user + ";PWD=" + password)



SQLALCHEMY_DATABASE_URI = "mssql+pyodbc:///?odbc_connect=%s" % rasconn

  

logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'json': {
            'format': '%(message)s %(lineno)d %(pathname)s',
            'class': 'pythonjsonlogger.jsonlogger.JsonFormatter'
        }
    },
    'handlers': {
        'json': {
            'class': 'logging.StreamHandler',
            'formatter': 'json'
        }
    },
    'loggers': {
        '': {
            'handlers': ['json'],
            'level': logging.INFO
        }
    }
})

configure(
    context_class=threadlocal.wrap_dict(dict),
    logger_factory=stdlib.LoggerFactory(),
    wrapper_class=stdlib.BoundLogger,
    processors=[
        stdlib.filter_by_level,
        stdlib.add_logger_name,
        stdlib.add_log_level,
        stdlib.PositionalArgumentsFormatter(),
        processors.TimeStamper(fmt="iso"),
        processors.StackInfoRenderer(),
        processors.format_exc_info,
        processors.UnicodeDecoder(),
        stdlib.render_to_log_kwargs]
)






