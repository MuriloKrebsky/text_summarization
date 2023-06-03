import os 
import urllib.request as request
import zipfile
from pathlib import Path

from textSummarizer.logging import logger
from textSummarizer.utils.common import get_size
from textSummarizer.entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        """
        Download file from source URL and save it to local_data_file path.
        
        If file already exists, it will be skipped.
        """
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f'{filename} downloaded successfully. Header is: \n {headers}')
        else:
            logger.info(f'File already exists. Size is: \n {get_size(Path(self.config.local_data_file))}')

    def extract_zip_file(self):
        """
        Extract zip file to unzip_dir path.
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
            logger.info(f'File {self.config.local_data_file} extracted to {self.config.unzip_dir}')