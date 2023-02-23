from loggingFile import logger
import pytest
from power_control.PowerControl import PowerControl


@pytest.mark.parametrize("bat_lvl, val, ,full_bat", [
    pytest.param(
        10, 0, 10, marks=pytest.mark.tags("TC-1"),
    )

])
def test_give(logger, val, bat_lvl, full_bat):
    """ checks if battery level is equal to battery level after receiving charge  """
    logger.info("LOGGER_MESSAGE")
    controlCharge = PowerControl()
    controlCharge.battery_level = bat_lvl
    controlCharge.receive_charge(val)
    assert controlCharge.battery_level == full_bat
