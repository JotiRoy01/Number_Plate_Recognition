# __init__.py for logger
import logging
from datetime import datetime
import os
import pandas as pd
from ANPR.constants import get_current_time_stamp

LOG_DIR = 'D:/Develops/ML_PROJECT/Number_Plate_Recognition/logs'

def get_log_file_name() :
    return f"log_{get_current_time_stamp()}.log"

LOG_FILE_NAME = get_log_file_name()

os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE_NAME)

logging.basicConfig(filename=LOG_FILE_PATH,
                    filemode="w",
                    format='[%(asctime)s]^;%(levelname)s^;%(lineno)d^;%(filename)s^;%(funcName)s()^;%(message)s',
                    level=logging.INFO
                    )

def get_log_dataframe(filepath):
    data = []
    with open(filepath) as log_file :
        for line in log_file.readlines():
            data.append(line.split("^;"))
    log_df = pd.DataFrame(data)
    columns = ["Time stamp", "log lavel", "line number", "file name", "function name", "mesages"]
    log_df.columns = columns
    log_df["log_message"] = log_df["Time stamp"].astype(str) + ":$" + log_df["message"]
    return log_df[["log_message"]]