
import pytest


@pytest.mark.parametrize("n", [2, 4, 6])
def test_even_number(n):
    assert not n % 2, f"{n} is not an even number"

@pytest.mark.parametrize(["n", "expected_output"], [(1, 3), (2, 6)])
def test_multiplication(n, expected_output):
    assert n * 3 == expected_output, "Check multiplication"