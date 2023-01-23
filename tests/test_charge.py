# from loggingFile import logg
import pytest
from UAC_rover.power_control.SolarPanels import SolarPanels


@pytest.mark.parametrize("conditions, IntOutput", [
    pytest.param(b'\x00\x10', 0.006274509803921569
                 ),
])
def test_charge(logg, conditions, IntOutput):
    logg.info("LOGGER_MESSAGE")
    charge_output = SolarPanels.charge(conditions)
    # assert float(str(charge_output)[:5]) == float(str(IntOutput)[:5])
    # Better way to write this function
    assert float(str(charge_output)) == pytest.approx(float(str(IntOutput)))
