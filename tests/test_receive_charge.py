

from loggingFile import logg
import pytest
from UAC_rover.power_control.PowerControl import PowerControl


@pytest.mark.parametrize("val, bat_lvl", [
    pytest.param(
        10, 10, marks=pytest.mark.tags("TC-1", "MarkXfail")
    ),
    pytest.param(
        14, 10, marks=[pytest.mark.tags("TC-1", "MarkXfail"), pytest.mark.xfail()]
    ),
])
def test_receive(logg, val, bat_lvl):
    logg.info("LOGGER_MESSAGE")
    assert PowerControl.receive_charge() == bat_lvl + val
