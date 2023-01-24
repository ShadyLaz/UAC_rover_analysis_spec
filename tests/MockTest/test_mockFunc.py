# import os
from mockData import dummy_function
import pytest


@pytest.mark.parametrize("n", [
    pytest.param(10
                 ),
])
def test_mocking_function(mocker, a, n):
    """changes return value from a to n """

    mocker.patch("mockData.load_data", return_value=n)
    assert dummy_function(a) == n, f"{n} is the new mocked value"
