
from loggingFile import logger
import pytest
from UAC_rover.power_control.SolarPanels import SolarPanels


@pytest.mark.parametrize("conditions, IntOutput",[
    pytest.param(b'\x00\x10',0.006274509803921569 , marks=[pytest.mark.tags("TC-1")]
    ),
])

def test_charge(logger, conditions, IntOutput):
    logger.info("LOGGER_MESSAGE")
    charge_output = SolarPanels.charge(conditions)
    assert float(str(charge_output)[:5]) == float(str(IntOutput)[:5])