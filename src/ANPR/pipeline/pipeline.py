from collections import namedtuple
from datetime import datetime
import uuid
from src.ANPR.config.configuration import Configuration
from src.ANPR.logger.log import logging, get_log_file_name
from src.ANPR.exception import ANPR_Exceptioon
from threading import Thread
from typing import List
from multiprocessing import Process

from src.ANPR.entity.config_entity import DataIngestionConfig
from src.ANPR.constants import EXPERIMENT_DIR_NAME, EXPERIMENT_FILE_NAME

import os ,sys
import pandas as pd

Experiment = namedtuple("Experiment",["experiment_id", "initialization_timestamp", "artifact_time_stamp",
"running_status", "start_time", "stop_time", "execution_time", "message",
"experiment_file_path", "accuracy", "is_model_accepted"])

class Pipeline(Thread) :
    experiment: Experiment = Experiment(*([None]*11))
    experiment_file_path = None

    def __init__(self, config: Configuration) -> None :
        try :
            os.makedirs(config.training_pipeline_config.artifact_dir, exist_ok=True)
            Pipeline.experiment_file_path = os.path.join(config.training_pipeline_config.artifact_dir, EXPERIMENT_DIR_NAME, EXPERIMENT_FILE_NAME)
            super().__init__(daemon=False, name="pipeline")
            self.config = config
        except Exception as e:
            raise ANPR_Exceptioon(e, sys) from e
        