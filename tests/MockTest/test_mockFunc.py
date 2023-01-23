
from mockData import dummy_function
import pytest
import os


@pytest.mark.parametrize("n",[
    pytest.param(10
    ),
])

def test_mocking_function(mocker, n):

    mocker.patch("mockData.load_data", return_value=n)
    assert dummy_function() == n, f"{n} is the new mocked value"
