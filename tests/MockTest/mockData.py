
import pytest

@pytest.mark.parametrize("a",[
    pytest.param(b'\x00\x10'
    ),
])


def load_data(a):
    # This should be mocked as it is a dependency, this function converts byte data to float value
    return float(str(a))


def dummy_function():
    # This is the desired function we are testing
    return load_data()
