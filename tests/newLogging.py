#
# import logging
# import pytest
# from setup_logger import logger
#
#
#
# #def __init__(self):
# #    self.logger = logging.getLogger('Thanos.Superman.Batman')
# #    print(self.logger.parent)
# #    self.logger.info('creating an instance of Auxiliary')
#
# LOGGER = logging.getLogger(__name__)
#
#
#
# #class Class1(object):
#  #   def do_something(self):
#  #      logger.info('Class1: doing something')
# @pytest.fixture()
# def logger():
#
#     logging.basicConfig(
#         level=logging.DEBUG,
#         format='%(asctime)s [%(name)s]: %(levelname)s: %(message)s',
#         handlers=[
#             logging.FileHandler("test_logger.log", 'w')
#         ]
#     )
#     logger.setLevel(logging.DEBUG)
#     logging.getLogger(logger.debug())
#
#     return logger
#
