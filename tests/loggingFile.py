
import logging
import pytest


def __init__(self):
    # To use later
    self.logger = logging.getLogger(__name__)
    print(self.logger.parent)


@pytest.fixture()
def logger():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s [%(name)s]: %(levelname)s: %(message)s',
        handlers=[
            logging.FileHandler("test_logger.log", 'w')
        ]
    )

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    return logger
