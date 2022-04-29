from . import SynoApi as SynoApi
from .const import CONF_DEVICE_TOKEN as CONF_DEVICE_TOKEN, DOMAIN as DOMAIN, SYNO_API as SYNO_API, SYSTEM_LOADED as SYSTEM_LOADED
from _typeshed import Incomplete
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from synology_dsm.api.surveillance_station.camera import SynoCamera as SynoCamera

TO_REDACT: Incomplete

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: ConfigEntry) -> dict: ...
