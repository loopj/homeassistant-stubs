from .common import FritzBoxBaseEntity as FritzBoxBaseEntity, FritzBoxTools as FritzBoxTools
from .const import DOMAIN as DOMAIN, DSL_CONNECTION as DSL_CONNECTION, UPTIME_DEVIATION as UPTIME_DEVIATION
from collections.abc import Callable as Callable
from datetime import datetime
from fritzconnection.lib.fritzstatus import FritzStatus as FritzStatus
from homeassistant.components.sensor import STATE_CLASS_MEASUREMENT as STATE_CLASS_MEASUREMENT, STATE_CLASS_TOTAL_INCREASING as STATE_CLASS_TOTAL_INCREASING, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import DATA_GIGABYTES as DATA_GIGABYTES, DATA_RATE_KILOBITS_PER_SECOND as DATA_RATE_KILOBITS_PER_SECOND, DATA_RATE_KILOBYTES_PER_SECOND as DATA_RATE_KILOBYTES_PER_SECOND, DEVICE_CLASS_TIMESTAMP as DEVICE_CLASS_TIMESTAMP, ENTITY_CATEGORY_DIAGNOSTIC as ENTITY_CATEGORY_DIAGNOSTIC, SIGNAL_STRENGTH_DECIBELS as SIGNAL_STRENGTH_DECIBELS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util.dt import utcnow as utcnow
from typing import Any, Literal

_LOGGER: Any

def _uptime_calculation(seconds_uptime: float, last_value: Union[datetime, None]) -> datetime: ...
def _retrieve_device_uptime_state(status: FritzStatus, last_value: datetime) -> datetime: ...
def _retrieve_connection_uptime_state(status: FritzStatus, last_value: Union[datetime, None]) -> datetime: ...
def _retrieve_external_ip_state(status: FritzStatus, last_value: str) -> str: ...
def _retrieve_kb_s_sent_state(status: FritzStatus, last_value: str) -> float: ...
def _retrieve_kb_s_received_state(status: FritzStatus, last_value: str) -> float: ...
def _retrieve_max_kb_s_sent_state(status: FritzStatus, last_value: str) -> float: ...
def _retrieve_max_kb_s_received_state(status: FritzStatus, last_value: str) -> float: ...
def _retrieve_gb_sent_state(status: FritzStatus, last_value: str) -> float: ...
def _retrieve_gb_received_state(status: FritzStatus, last_value: str) -> float: ...
def _retrieve_link_kb_s_sent_state(status: FritzStatus, last_value: str) -> float: ...
def _retrieve_link_kb_s_received_state(status: FritzStatus, last_value: str) -> float: ...
def _retrieve_link_noise_margin_sent_state(status: FritzStatus, last_value: str) -> float: ...
def _retrieve_link_noise_margin_received_state(status: FritzStatus, last_value: str) -> float: ...
def _retrieve_link_attenuation_sent_state(status: FritzStatus, last_value: str) -> float: ...
def _retrieve_link_attenuation_received_state(status: FritzStatus, last_value: str) -> float: ...

class FritzRequireKeysMixin:
    value_fn: Callable[[FritzStatus, Any], Any]

class FritzSensorEntityDescription(SensorEntityDescription, FritzRequireKeysMixin):
    connection_type: Union[Literal[dsl], None]

SENSOR_TYPES: tuple[FritzSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FritzBoxSensor(FritzBoxBaseEntity, SensorEntity):
    entity_description: FritzSensorEntityDescription
    _last_device_value: Any
    _attr_available: bool
    _attr_name: Any
    _attr_unique_id: Any
    def __init__(self, fritzbox_tools: FritzBoxTools, device_friendly_name: str, description: FritzSensorEntityDescription) -> None: ...
    _attr_native_value: Any
    def update(self) -> None: ...
