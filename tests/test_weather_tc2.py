from loggingFile import logger
import pytest
from power_control.PowerControl import PowerControl
from RoverFile import Rover
import time
from modules.Weather.WeatherMain import WeatherMain


@pytest.mark.parametrize("Shortsleep,LongSleep", [
    pytest.param(
        2, 31, marks=pytest.mark.tags("TC-1"),
    )

])
def test_give(logger,Shortsleep, LongSleep):
    """ Module should not make a new measurement if previous was done less than 30 seconds ago  """
    rover = Rover()
    before = rover.weather_core.get_weather()
    #time_before = before.date_measurement()

    time.sleep(LongSleep)

    after = rover.weather_core.get_weather()
    assert before == after


    #time_after = after.date_measurement()

    #assert before.get_weather.date_measurement() == after.get_weather.date_measurement()
    #assert time_before == time_after
    #assert float(str(before.date_measurement)) == float(str(after.date_measurement))
