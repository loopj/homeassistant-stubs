from .const import API_TIMEOUT as API_TIMEOUT, DOMAIN as DOMAIN, LOGGER as LOGGER, UPDATE_INTERVAL_CLOUD as UPDATE_INTERVAL_CLOUD, UPDATE_INTERVAL_LOCAL as UPDATE_INTERVAL_LOCAL
from _typeshed import Incomplete
from aiohttp import ClientSession as ClientSession
from datetime import timedelta
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN, CONF_HOST as CONF_HOST, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from python_awair.air_data import AirData as AirData
from python_awair.devices import AwairBaseDevice as AwairBaseDevice, AwairLocalDevice as AwairLocalDevice

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
async def _async_update_listener(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
async def async_unload_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...

class AwairResult:
    device: AwairBaseDevice
    air_data: AirData
    def __init__(self, device, air_data) -> None: ...
    def __mypy-replace(*, device, air_data) -> None: ...

class AwairDataUpdateCoordinator(DataUpdateCoordinator[dict[str, AwairResult]]):
    _config_entry: Incomplete
    title: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry, update_interval: timedelta | None) -> None: ...
    async def _fetch_air_data(self, device: AwairBaseDevice) -> AwairResult: ...

class AwairCloudDataUpdateCoordinator(AwairDataUpdateCoordinator):
    _awair: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry, session: ClientSession) -> None: ...
    async def _async_update_data(self) -> dict[str, AwairResult]: ...

class AwairLocalDataUpdateCoordinator(AwairDataUpdateCoordinator):
    _device: AwairLocalDevice | None
    _awair: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry, session: ClientSession) -> None: ...
    async def _async_update_data(self) -> dict[str, AwairResult]: ...
