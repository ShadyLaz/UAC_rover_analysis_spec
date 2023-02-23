import logging
import pytest


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s [%(name)s]: %(levelname)s: %(message)s',
        handlers=[
            logging.FileHandler("test.log", 'w'),
            logging.StreamHandler()
        ]
    )
    pytest.main(["-v", "tests/"])
