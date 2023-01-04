
import logging
import pytest

LOGGER = logging.getLogger(__name__)

def __init__(self):
    self.logger = logging.getLogger('Thanos.Superman.Batman')
    print(self.logger.parent)
    self.logger.info('creating an instance of Auxiliary')


@pytest.fixture()
def logger():

    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s [%(name)s]: %(levelname)s: %(message)s',
        handlers=[
            logging.FileHandler("test_logger.log", 'w')
        ]
    )
    logger = logging.getLogger('Some.Logger')
    logger.setLevel(logging.DEBUG)

    return logger
