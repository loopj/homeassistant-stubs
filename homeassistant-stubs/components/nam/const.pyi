from .model import SensorDescription as SensorDescription
from homeassistant.components.sensor import ATTR_STATE_CLASS as ATTR_STATE_CLASS, STATE_CLASS_MEASUREMENT as STATE_CLASS_MEASUREMENT
from homeassistant.const import ATTR_DEVICE_CLASS as ATTR_DEVICE_CLASS, ATTR_ICON as ATTR_ICON, CONCENTRATION_MICROGRAMS_PER_CUBIC_METER as CONCENTRATION_MICROGRAMS_PER_CUBIC_METER, DEVICE_CLASS_HUMIDITY as DEVICE_CLASS_HUMIDITY, DEVICE_CLASS_PRESSURE as DEVICE_CLASS_PRESSURE, DEVICE_CLASS_SIGNAL_STRENGTH as DEVICE_CLASS_SIGNAL_STRENGTH, DEVICE_CLASS_TEMPERATURE as DEVICE_CLASS_TEMPERATURE, DEVICE_CLASS_TIMESTAMP as DEVICE_CLASS_TIMESTAMP, PERCENTAGE as PERCENTAGE, PRESSURE_HPA as PRESSURE_HPA, SIGNAL_STRENGTH_DECIBELS_MILLIWATT as SIGNAL_STRENGTH_DECIBELS_MILLIWATT, TEMP_CELSIUS as TEMP_CELSIUS
from typing import Any, Final

ATTR_BME280_HUMIDITY: Final[str]
ATTR_BME280_PRESSURE: Final[str]
ATTR_BME280_TEMPERATURE: Final[str]
ATTR_BMP280_PRESSURE: Final[str]
ATTR_BMP280_TEMPERATURE: Final[str]
ATTR_DHT22_HUMIDITY: Final[str]
ATTR_DHT22_TEMPERATURE: Final[str]
ATTR_HECA_HUMIDITY: Final[str]
ATTR_HECA_TEMPERATURE: Final[str]
ATTR_MHZ14A_CARBON_DIOXIDE: Final[str]
ATTR_SHT3X_HUMIDITY: Final[str]
ATTR_SHT3X_TEMPERATURE: Final[str]
ATTR_SIGNAL_STRENGTH: Final[str]
ATTR_SPS30_P0: Final[str]
ATTR_SPS30_P4: Final[str]
ATTR_UPTIME: Final[str]
ATTR_ENABLED: Final[str]
ATTR_LABEL: Final[str]
ATTR_UNIT: Final[str]
DEFAULT_NAME: Final[str]
DEFAULT_UPDATE_INTERVAL: Final[Any]
DOMAIN: Final[str]
MANUFACTURER: Final[str]
SUFFIX_P1: Final[str]
SUFFIX_P2: Final[str]
AIR_QUALITY_SENSORS: Final[dict[str, str]]
SENSORS: Final[dict[str, SensorDescription]]
