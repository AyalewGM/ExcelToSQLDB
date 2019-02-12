##########################
 

import os
import pandas as pd
from  path_and_db_config import filepath 
import structlog


logger = structlog.getLogger(__name__)

filename = 'put excel file name in here;
path = filepath()
file_path = os.path.join(path, filename)


def excel_to_dataframe():
    
    logger.info('excel_to_dataframe method called ')
    temp_records = pd.ExcelFile(file_path)
    dfs = {sheet: temp_records.parse(sheet, header=None) for sheet in temp_records.sheet_names}
    dict_of_dataFrames = {}
    for key, value in dfs.items():
        df = None
        header = None
        if (str(key).startswith('File') or str(key).startswith('TIP')):
            header = value.iloc[0]
            df = value[1:]
        else:
            header = value.iloc[1]
            df = value[2:]

        df.columns = header

        df.columns = df.columns.str.replace('\s+', '_')

        dict_of_dataFrames[key] = df

    logger.info('excel_to_dataframe returned ... ')

    return dict_of_dataFrames
