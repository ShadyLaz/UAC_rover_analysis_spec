from loggingFile import logger
import pytest
from power_control.SolarPanels import SolarPanels


@pytest.mark.parametrize("temp, eff", [
    pytest.param(
        14, 0.7, marks=[pytest.mark.tags("TC-1", "MarkXfail"),
                        pytest.mark.xfail()]
    ),
    pytest.param(
        14, 1, marks=pytest.mark.tags("TC-2", "OPTIMAL")
    ),
    pytest.param(
        14.444444444, 1, marks=[pytest.mark.tags("TC-4", "FLOAT_NON_OPTIMAL"),
                                  pytest.mark.xfail()]
    ),
    pytest.param(
        14.444444444, 0.7, marks=[pytest.mark.tags("TC-4", "FLOAT_NON_OPTIMAL"),
                                  pytest.mark.xfail()]
    ),
    pytest.param(
        "14", 1, marks=[pytest.mark.tags("TC-5", "STRING_OPTIMAL"),
                        pytest.mark.xfail()]
    ),
    pytest.param(
        "14", 1, marks=[pytest.mark.tags("TC-6", "STRING_NON_OPTIMAl"),
                        pytest.mark.xfail()]
    ),
])
def test_InOptimalTempFail(temp, eff, logger):
    """ checks if efficiency is optimal  """

    logger.info("TESTING---------------------------------------------")
    assert SolarPanels.calc_efficiency(temp) == eff
