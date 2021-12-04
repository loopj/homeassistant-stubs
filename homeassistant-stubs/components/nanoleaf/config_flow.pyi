from .const import DOMAIN as DOMAIN
from homeassistant import config_entries as config_entries
from homeassistant.components import ssdp as ssdp, zeroconf as zeroconf
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_TOKEN as CONF_TOKEN
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.util.json import load_json as load_json, save_json as save_json
from typing import Any, Final

_LOGGER: Any
CONFIG_FILE: Final[str]
USER_SCHEMA: Final[Any]

class ConfigFlow(config_entries.ConfigFlow):
    reauth_entry: Union[config_entries.ConfigEntry, None]
    VERSION: int
    nanoleaf: Any
    discovery_conf: Any
    device_id: Any
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_reauth(self, data: dict[str, str]) -> FlowResult: ...
    async def async_step_zeroconf(self, discovery_info: zeroconf.ZeroconfServiceInfo) -> FlowResult: ...
    async def async_step_homekit(self, discovery_info: zeroconf.ZeroconfServiceInfo) -> FlowResult: ...
    async def _async_homekit_zeroconf_discovery_handler(self, discovery_info: zeroconf.ZeroconfServiceInfo) -> FlowResult: ...
    async def async_step_ssdp(self, discovery_info: ssdp.SsdpServiceInfo) -> FlowResult: ...
    async def _async_discovery_handler(self, host: str, name: str, device_id: str) -> FlowResult: ...
    async def async_step_link(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_import(self, config: dict[str, Any]) -> FlowResult: ...
    async def async_setup_finish(self, discovery_integration_import: bool = ...) -> FlowResult: ...
