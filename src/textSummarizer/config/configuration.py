from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml, create_directories

from textSummarizer.entity import DataIngestionConfig, DataValidationConfig


class ConfigurationManager:
    def __init__(self, config_file_path=CONFIG_FILE_PATH, params_file_path=PARAMS_FILE_PATH):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)

        # Creates artifacts folder
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        data_ingestion_config = self.config.data_ingestion

        # Creates data_ingestion folder
        create_directories([data_ingestion_config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=data_ingestion_config.root_dir,
            source_URL=data_ingestion_config.source_URL,
            local_data_file=data_ingestion_config.local_data_file,
            unzip_dir=data_ingestion_config.unzip_dir
        )

        return data_ingestion_config

    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            FILES_TO_VALIDATE=config.FILES_TO_VALIDATE
        )

        return data_validation_config
