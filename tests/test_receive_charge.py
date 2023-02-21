from loggingFile import logger
import pytest
from power_control.PowerControl import PowerControl


@pytest.mark.parametrize("val, bat_lvl", [
    pytest.param(
        10, 10, marks=[pytest.mark.tags("TC-1"), pytest.mark.xfail()]
    ),
    pytest.param(
        14, 10, marks=[pytest.mark.tags("TC-1"), pytest.mark.xfail()]
    ),
])
def test_receive(logger, val, bat_lvl):
    """ checks if battery level is equal to battery level after receiving charge  """
    controlCharge = PowerControl()
    controlCharge.receive_charge(val)

    logger.info("LOGGER_MESSAGE")
    assert controlCharge.battery_level == (bat_lvl + val)
