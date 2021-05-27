from .model import SensorDescription as SensorDescription
from homeassistant.components.weather import ATTR_CONDITION_CLEAR_NIGHT as ATTR_CONDITION_CLEAR_NIGHT, ATTR_CONDITION_CLOUDY as ATTR_CONDITION_CLOUDY, ATTR_CONDITION_EXCEPTIONAL as ATTR_CONDITION_EXCEPTIONAL, ATTR_CONDITION_FOG as ATTR_CONDITION_FOG, ATTR_CONDITION_HAIL as ATTR_CONDITION_HAIL, ATTR_CONDITION_LIGHTNING as ATTR_CONDITION_LIGHTNING, ATTR_CONDITION_LIGHTNING_RAINY as ATTR_CONDITION_LIGHTNING_RAINY, ATTR_CONDITION_PARTLYCLOUDY as ATTR_CONDITION_PARTLYCLOUDY, ATTR_CONDITION_POURING as ATTR_CONDITION_POURING, ATTR_CONDITION_RAINY as ATTR_CONDITION_RAINY, ATTR_CONDITION_SNOWY as ATTR_CONDITION_SNOWY, ATTR_CONDITION_SNOWY_RAINY as ATTR_CONDITION_SNOWY_RAINY, ATTR_CONDITION_SUNNY as ATTR_CONDITION_SUNNY, ATTR_CONDITION_WINDY as ATTR_CONDITION_WINDY
from homeassistant.const import ATTR_DEVICE_CLASS as ATTR_DEVICE_CLASS, ATTR_ICON as ATTR_ICON, CONCENTRATION_PARTS_PER_CUBIC_METER as CONCENTRATION_PARTS_PER_CUBIC_METER, DEVICE_CLASS_TEMPERATURE as DEVICE_CLASS_TEMPERATURE, LENGTH_FEET as LENGTH_FEET, LENGTH_INCHES as LENGTH_INCHES, LENGTH_METERS as LENGTH_METERS, LENGTH_MILLIMETERS as LENGTH_MILLIMETERS, PERCENTAGE as PERCENTAGE, SPEED_KILOMETERS_PER_HOUR as SPEED_KILOMETERS_PER_HOUR, SPEED_MILES_PER_HOUR as SPEED_MILES_PER_HOUR, TEMP_CELSIUS as TEMP_CELSIUS, TEMP_FAHRENHEIT as TEMP_FAHRENHEIT, TIME_HOURS as TIME_HOURS, UV_INDEX as UV_INDEX
from typing import Final

API_IMPERIAL: Final[str]
API_METRIC: Final[str]
ATTRIBUTION: Final[str]
ATTR_ENABLED: Final[str]
ATTR_FORECAST: Final[str]
ATTR_LABEL: Final[str]
ATTR_UNIT_IMPERIAL: Final[str]
ATTR_UNIT_METRIC: Final[str]
CONF_FORECAST: Final[str]
COORDINATOR: Final[str]
DOMAIN: Final[str]
MANUFACTURER: Final[str]
MAX_FORECAST_DAYS: Final[int]
NAME: Final[str]
UNDO_UPDATE_LISTENER: Final[str]
CONDITION_CLASSES: Final[dict[str, list[int]]]
FORECAST_SENSOR_TYPES: Final[dict[str, SensorDescription]]
SENSOR_TYPES: Final[dict[str, SensorDescription]]
