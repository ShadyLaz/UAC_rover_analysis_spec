from loggingFile import logger
import pytest
from UAC_rover.power_control.SolarPanels import SolarPanels


@pytest.mark.tags("TC-1", "Normal", "unit-test")
def test_InOptimalTempFail(logger):
    logger.info("LOGGER_MESSAGE")
    assert SolarPanels.calc_efficiency(14) == 0.7


def test_InOptimalTempPass():
    assert SolarPanels.calc_efficiency(14) == 1


@pytest.mark.tag("TC-3", "Border", "unit-test")
@pytest.mark.xfail()
def test_float():
    assert SolarPanels.calc_efficiency(13.33333333333333) == 1

#[["tag1", "tag2", "tag3"], ["tag1", "tag2", "tag3"]]
@pytest.mark.xfail()
def test_StringInput_1():
    assert SolarPanels.calc_efficiency("String") == 1


@pytest.mark.xfail()
def test_StringInput_2():
    assert SolarPanels.calc_efficiency("String") == 0.7
