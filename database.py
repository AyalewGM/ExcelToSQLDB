

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
 
import urllib.parse
from contextlib import contextmanager
from  config import db, user,password  



def db_connection(server, database, user, password):
    return "mssql+pyodbc:///?odbc_connect=%s" % \
           urllib.parse.quote_plus("DRIVER={ODBC Driver 17 for SQL Server};"
                                   "SERVER="+server+";"
                                   "DATABASE="+database+";"
                                   "UID="+user+";"
                                   "PWD="+password+";")
# 

db_connection_string = db_connection(server=db['server'], database=db['database'], user=user, password=password)
engine = create_engine(db_connection_string,connect_args={'convert_unicode': True})

 