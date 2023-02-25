import logging
import pytest


@pytest.fixture()
def logger(request):
    """ logging config"""

    name = request.node.name
    logger = logging.getLogger(name)

    return logger
