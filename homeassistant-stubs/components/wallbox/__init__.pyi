from ...helpers.entity import DeviceInfo
from .const import CONF_CURRENT_VERSION_KEY as CONF_CURRENT_VERSION_KEY, CONF_DATA_KEY as CONF_DATA_KEY, CONF_LOCKED_UNLOCKED_KEY as CONF_LOCKED_UNLOCKED_KEY, CONF_MAX_CHARGING_CURRENT_KEY as CONF_MAX_CHARGING_CURRENT_KEY, CONF_NAME_KEY as CONF_NAME_KEY, CONF_PART_NUMBER_KEY as CONF_PART_NUMBER_KEY, CONF_SERIAL_NUMBER_KEY as CONF_SERIAL_NUMBER_KEY, CONF_SOFTWARE_KEY as CONF_SOFTWARE_KEY, CONF_STATION as CONF_STATION, DOMAIN as DOMAIN
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, HomeAssistantError as HomeAssistantError
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any
from wallbox import Wallbox

_LOGGER: Any
PLATFORMS: Any
UPDATE_INTERVAL: int

class WallboxCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    _station: Any
    _wallbox: Any
    def __init__(self, station: str, wallbox: Wallbox, hass: HomeAssistant) -> None: ...
    def _authenticate(self) -> None: ...
    def _validate(self) -> None: ...
    async def async_validate_input(self) -> None: ...
    def _get_data(self) -> dict[str, Any]: ...
    async def _async_update_data(self) -> dict[str, Any]: ...
    def _set_charging_current(self, charging_current: float) -> None: ...
    async def async_set_charging_current(self, charging_current: float) -> None: ...
    def _set_lock_unlock(self, lock: bool) -> None: ...
    async def async_set_lock_unlock(self, lock: bool) -> None: ...

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class InvalidAuth(HomeAssistantError): ...

class WallboxEntity(CoordinatorEntity[WallboxCoordinator]):
    @property
    def device_info(self) -> DeviceInfo: ...
