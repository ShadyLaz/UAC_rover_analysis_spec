from loggingFile import logger
import pytest
from power_control.SolarPanels import SolarPanels


@pytest.mark.parametrize("conditions, IntOutput", [
    pytest.param(b'\x00\x10', 0.006274509803921569
                 ),
])
def test_charge(logger, conditions, IntOutput):
    """ checks if byte output is equal to int output """

    logger.info("LOGGER_MESSAGE")
    charge_output = SolarPanels.charge(conditions)
    # assert float(str(charge_output)[:5]) == float(str(IntOutput)[:5])
    # Better way to write this function
    assert float(str(charge_output)) == pytest.approx(float(str(IntOutput)))
