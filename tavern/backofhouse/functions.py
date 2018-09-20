import logging
import os
from .storeroom import settings

def setup_logging():
    logging.basicConfig(filename=os.path.join(settings.TVRN_FREEZER, 'old-meat.log'), level=settings.LOG_LEVEL, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filemode='a')
