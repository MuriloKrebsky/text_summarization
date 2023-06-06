from textSummarizer.logging import logger
from textSummarizer.pipeline.data_ingestion import \
    DataIngestionTrainingPipeline
from textSummarizer.pipeline.data_transformation import \
    DataTransformationTrainingPipeline
from textSummarizer.pipeline.data_validation import \
    DataValidationTrainingPipeline
from textSummarizer.pipeline.model_trainer import ModelTrainerTrainingPipeline
from textSummarizer.pipeline.model_evaluation import ModelEvaluationTrainingPipeline


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

STAGE_NAME = 'Data Transformation stage'
try:
    logger.info(f'>>>>>> Starting {STAGE_NAME}. <<<<<<')
    data_transformation_pipeline = DataTransformationTrainingPipeline()
    data_transformation_pipeline.main()
    logger.info(f'>>>>>> Stage {STAGE_NAME} completed. <<<<<<')
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Model Trainer stage'
try:
    logger.info(f'>>>>>> Starting {STAGE_NAME}. <<<<<<')
    model_trainer_pipeline = ModelTrainerTrainingPipeline()
    model_trainer_pipeline.main()
    logger.info(f'>>>>>> Stage {STAGE_NAME} completed. <<<<<<')
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Model Evaluation stage'
try:
    logger.info(f'>>>>>> Starting {STAGE_NAME}. <<<<<<')
    model_evaluation_pipeline = ModelEvaluationTrainingPipeline()
    model_evaluation_pipeline.main()
    logger.info(f'>>>>>> Stage {STAGE_NAME} completed. <<<<<<')
except Exception as e:
    logger.exception(e)
    raise e