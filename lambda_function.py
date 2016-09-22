import logging

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.info('Loading deploy-poc-lambda.')

def lambda_handler(event, context):
    return {"Version": "feature 1g"}


if __name__ == "__main__":
    lambda_handler(None, None)
