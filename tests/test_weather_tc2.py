import time
from loggingFile import logger
import pytest
from RoverFile import Rover
from modules.Weather.WeatherMain import WeatherMain


@pytest.mark.parametrize("Shortsleep,LongSleep", [
    pytest.param(
        2, 35, marks=pytest.mark.tags("TC-1"),
    )

])
def test_give(logger,Shortsleep, LongSleep):
    """ Module should not make a new measurement if previous was done less than 30 seconds ago  """
    logger.info("LOGGER_MESSAGE")
    rover = Rover()
    rover.weather_core.get_weather()
    #time_before = before.date_measurement()
    date_old = rover.weather_core.date_measurement
    print(date_old)

    time.sleep(Shortsleep)

    rover.weather_core.get_weather()
    date_new = rover.weather_core.date_measurement
    print(date_new)
    assert date_old == date_new


    #time_after = after.date_measurement()

    #assert before.get_weather.date_measurement() == after.get_weather.date_measurement()
    #assert time_before == time_after
    #assert float(str(before.date_measurement)) == float(str(after.date_measurement))
