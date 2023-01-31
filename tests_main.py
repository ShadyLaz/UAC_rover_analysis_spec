import os
import pytest


def main():
    """Something"""

    arr = os.listdir("tests")
    out = []
    for file_test in arr:
        if "test" in file_test[0:4] and ".py" in file_test:
            out.append(f"tests/{file_test}")

    print(out)

    return out


if __name__ == "__main__":
    files = main()
    for file in files:
        pytest.main(["-v", file])
