##########################
 
from datetime import datetime
import traceback
import structlog
logger =structlog.getLogger(__name__)

from database import ras_db_connection_string 
from dataframe_generator import excel_to_dataframe
 
def excel_to_database_writer():
    """Writes excel file to the database 
    
    """
  
    dfs = excel_to_dataframe()

    for key, value in dfs.items():
        value.to_sql(str(key), ras_db_connection_string, if_exists='replace')


if __name__ == '__main__':

    try:
        rundatetime = datetime.now()
       
        if run:
            logger.info('Writing records from excel to database started ...')
            excel_to_database_writer()
            logger.info('Data sucessfully written to the database')
            
    except Exception:
        logger.error(str(traceback.format_exc()))
        raise

