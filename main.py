from textSummarizer.pipeline.data_ingestion import DataIngestionTraininPipeline
from textSummarizer.logging import logger 


STAGE_NAME = 'Data Ingestion stage'
try:
    logger.info(f'>>>>>> Starting {STAGE_NAME}. <<<<<<')
    data_ingestion_pipeline = DataIngestionTraininPipeline()
    data_ingestion_pipeline.main()
    logger.info(f'>>>>>> Stage {STAGE_NAME} completed. <<<<<<')
except Exception as e:
    logger.exception(e)
    raise e