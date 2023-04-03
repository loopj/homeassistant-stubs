import voluptuous as vol
from .const import ATTR_ATTRIBUTES as ATTR_ATTRIBUTES, ATTR_BATTERY as ATTR_BATTERY, ATTR_CONSIDER_HOME as ATTR_CONSIDER_HOME, ATTR_DEV_ID as ATTR_DEV_ID, ATTR_GPS as ATTR_GPS, ATTR_HOST_NAME as ATTR_HOST_NAME, ATTR_LOCATION_NAME as ATTR_LOCATION_NAME, ATTR_MAC as ATTR_MAC, ATTR_SOURCE_TYPE as ATTR_SOURCE_TYPE, CONF_CONSIDER_HOME as CONF_CONSIDER_HOME, CONF_NEW_DEVICE_DEFAULTS as CONF_NEW_DEVICE_DEFAULTS, CONF_SCAN_INTERVAL as CONF_SCAN_INTERVAL, CONF_TRACK_NEW as CONF_TRACK_NEW, DEFAULT_CONSIDER_HOME as DEFAULT_CONSIDER_HOME, DEFAULT_TRACK_NEW as DEFAULT_TRACK_NEW, DOMAIN as DOMAIN, LOGGER as LOGGER, PLATFORM_TYPE_LEGACY as PLATFORM_TYPE_LEGACY, SCAN_INTERVAL as SCAN_INTERVAL, SourceType as SourceType
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine, Sequence
from datetime import datetime, timedelta
from homeassistant import util as util
from homeassistant.components import zone as zone
from homeassistant.config import async_log_exception as async_log_exception, load_yaml_config_file as load_yaml_config_file
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_GPS_ACCURACY as ATTR_GPS_ACCURACY, ATTR_ICON as ATTR_ICON, ATTR_LATITUDE as ATTR_LATITUDE, ATTR_LONGITUDE as ATTR_LONGITUDE, ATTR_NAME as ATTR_NAME, CONF_ICON as CONF_ICON, CONF_MAC as CONF_MAC, CONF_NAME as CONF_NAME, DEVICE_DEFAULT_NAME as DEVICE_DEFAULT_NAME, STATE_HOME as STATE_HOME, STATE_NOT_HOME as STATE_NOT_HOME
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import config_per_platform as config_per_platform, discovery as discovery
from homeassistant.helpers.event import async_track_time_interval as async_track_time_interval, async_track_utc_time_change as async_track_utc_time_change
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.typing import ConfigType as ConfigType, GPSType as GPSType, StateType as StateType
from homeassistant.setup import async_prepare_setup_platform as async_prepare_setup_platform, async_start_setup as async_start_setup
from homeassistant.util.yaml import dump as dump
from types import ModuleType
from typing import Any, Final, Protocol

SERVICE_SEE: Final[str]
SOURCE_TYPES: Incomplete
NEW_DEVICE_DEFAULTS_SCHEMA: Incomplete
PLATFORM_SCHEMA: Final[Incomplete]
PLATFORM_SCHEMA_BASE: Final[vol.Schema]
SERVICE_SEE_PAYLOAD_SCHEMA: Final[vol.Schema]
YAML_DEVICES: Final[str]
EVENT_NEW_DEVICE: Final[str]

class SeeCallback(Protocol):
    def __call__(self, mac: str | None = ..., dev_id: str | None = ..., host_name: str | None = ..., location_name: str | None = ..., gps: GPSType | None = ..., gps_accuracy: int | None = ..., battery: int | None = ..., attributes: dict[str, Any] | None = ..., source_type: SourceType | str = ..., picture: str | None = ..., icon: str | None = ..., consider_home: timedelta | None = ...) -> None: ...

class AsyncSeeCallback(Protocol):
    async def __call__(self, mac: str | None = ..., dev_id: str | None = ..., host_name: str | None = ..., location_name: str | None = ..., gps: GPSType | None = ..., gps_accuracy: int | None = ..., battery: int | None = ..., attributes: dict[str, Any] | None = ..., source_type: SourceType | str = ..., picture: str | None = ..., icon: str | None = ..., consider_home: timedelta | None = ...) -> None: ...

def see(hass: HomeAssistant, mac: str | None = ..., dev_id: str | None = ..., host_name: str | None = ..., location_name: str | None = ..., gps: GPSType | None = ..., gps_accuracy: int | None = ..., battery: int | None = ..., attributes: dict[str, Any] | None = ...) -> None: ...
async def async_setup_integration(hass: HomeAssistant, config: ConfigType) -> None: ...

class DeviceTrackerPlatform:
    LEGACY_SETUP: Final[tuple[str, ...]]
    name: str
    platform: ModuleType
    config: dict
    @property
    def type(self) -> str | None: ...
    async def async_setup_legacy(self, hass: HomeAssistant, tracker: DeviceTracker, discovery_info: dict[str, Any] | None = ...) -> None: ...
    def __init__(self, name, platform, config) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

async def async_extract_config(hass: HomeAssistant, config: ConfigType) -> list[DeviceTrackerPlatform]: ...
async def async_create_platform_type(hass: HomeAssistant, config: ConfigType, p_type: str, p_config: dict) -> DeviceTrackerPlatform | None: ...
def async_setup_scanner_platform(hass: HomeAssistant, config: ConfigType, scanner: DeviceScanner, async_see_device: Callable[..., Coroutine[None, None, None]], platform: str) -> None: ...
async def get_tracker(hass: HomeAssistant, config: ConfigType) -> DeviceTracker: ...

class DeviceTracker:
    hass: Incomplete
    devices: Incomplete
    mac_to_dev: Incomplete
    consider_home: Incomplete
    track_new: Incomplete
    defaults: Incomplete
    _is_updating: Incomplete
    def __init__(self, hass: HomeAssistant, consider_home: timedelta, track_new: bool, defaults: dict[str, Any], devices: Sequence[Device]) -> None: ...
    def see(self, mac: str | None = ..., dev_id: str | None = ..., host_name: str | None = ..., location_name: str | None = ..., gps: GPSType | None = ..., gps_accuracy: int | None = ..., battery: int | None = ..., attributes: dict[str, Any] | None = ..., source_type: SourceType | str = ..., picture: str | None = ..., icon: str | None = ..., consider_home: timedelta | None = ...) -> None: ...
    async def async_see(self, mac: str | None = ..., dev_id: str | None = ..., host_name: str | None = ..., location_name: str | None = ..., gps: GPSType | None = ..., gps_accuracy: int | None = ..., battery: int | None = ..., attributes: dict[str, Any] | None = ..., source_type: SourceType | str = ..., picture: str | None = ..., icon: str | None = ..., consider_home: timedelta | None = ...) -> None: ...
    async def async_update_config(self, path: str, dev_id: str, device: Device) -> None: ...
    def async_update_stale(self, now: datetime) -> None: ...
    async def async_setup_tracked_device(self) -> None: ...

class Device(RestoreEntity):
    host_name: str | None
    location_name: str | None
    gps: GPSType | None
    gps_accuracy: int
    last_seen: datetime | None
    battery: int | None
    attributes: dict | None
    last_update_home: bool
    _state: str
    hass: Incomplete
    entity_id: Incomplete
    consider_home: Incomplete
    dev_id: Incomplete
    mac: Incomplete
    track: Incomplete
    config_name: Incomplete
    config_picture: Incomplete
    _icon: Incomplete
    source_type: Incomplete
    _attributes: Incomplete
    def __init__(self, hass: HomeAssistant, consider_home: timedelta, track: bool, dev_id: str, mac: str | None, name: str | None = ..., picture: str | None = ..., gravatar: str | None = ..., icon: str | None = ...) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def state(self) -> str: ...
    @property
    def entity_picture(self) -> str | None: ...
    @property
    def state_attributes(self) -> dict[str, StateType]: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    @property
    def icon(self) -> str | None: ...
    async def async_seen(self, host_name: str | None = ..., location_name: str | None = ..., gps: GPSType | None = ..., gps_accuracy: int | None = ..., battery: int | None = ..., attributes: dict[str, Any] | None = ..., source_type: SourceType | str = ..., consider_home: timedelta | None = ...) -> None: ...
    def stale(self, now: datetime | None = ...) -> bool: ...
    def mark_stale(self) -> None: ...
    async def async_update(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...

class DeviceScanner:
    hass: HomeAssistant | None
    def scan_devices(self) -> list[str]: ...
    async def async_scan_devices(self) -> list[str]: ...
    def get_device_name(self, device: str) -> str | None: ...
    async def async_get_device_name(self, device: str) -> str | None: ...
    def get_extra_attributes(self, device: str) -> dict: ...
    async def async_get_extra_attributes(self, device: str) -> dict: ...

async def async_load_config(path: str, hass: HomeAssistant, consider_home: timedelta) -> list[Device]: ...
def update_config(path: str, dev_id: str, device: Device) -> None: ...
def get_gravatar_for_email(email: str) -> str: ...
