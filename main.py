from textSummarizer.pipeline.data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.data_validation import DataValidationTrainingPipeline

from textSummarizer.logging import logger 


STAGE_NAME = 'Data Ingestion stage'
try:
    logger.info(f'>>>>>> Starting {STAGE_NAME}. <<<<<<')
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.main()
    logger.info(f'>>>>>> Stage {STAGE_NAME} completed. <<<<<<')
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = 'Data Validation stage'
try:
    logger.info(f'>>>>>> Starting {STAGE_NAME}. <<<<<<')
    data_validation_pipeline = DataValidationTrainingPipeline()
    data_validation_pipeline.main()
    logger.info(f'>>>>>> Stage {STAGE_NAME} completed. <<<<<<')
except Exception as e:
    logger.exception(e)
    raise e