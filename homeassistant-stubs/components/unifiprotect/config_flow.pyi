from .const import CONF_ALL_UPDATES as CONF_ALL_UPDATES, CONF_DISABLE_RTSP as CONF_DISABLE_RTSP, CONF_OVERRIDE_CHOST as CONF_OVERRIDE_CHOST, DEFAULT_PORT as DEFAULT_PORT, DEFAULT_VERIFY_SSL as DEFAULT_VERIFY_SSL, DOMAIN as DOMAIN, MIN_REQUIRED_PROTECT_V as MIN_REQUIRED_PROTECT_V, OUTDATED_LOG_MESSAGE as OUTDATED_LOG_MESSAGE
from .discovery import async_start_discovery as async_start_discovery
from .utils import _async_resolve as _async_resolve, _async_short_mac as _async_short_mac, _async_unifi_mac_from_hass as _async_unifi_mac_from_hass
from homeassistant import config_entries as config_entries
from homeassistant.components import dhcp as dhcp, ssdp as ssdp
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_ID as CONF_ID, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_USERNAME as CONF_USERNAME, CONF_VERIFY_SSL as CONF_VERIFY_SSL
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.aiohttp_client import async_create_clientsession as async_create_clientsession
from homeassistant.helpers.typing import DiscoveryInfoType as DiscoveryInfoType
from homeassistant.loader import async_get_integration as async_get_integration
from homeassistant.util.network import is_ip_address as is_ip_address
from pyunifiprotect.data.nvr import NVR as NVR
from typing import Any

_LOGGER: Any

async def async_local_user_documentation_url(hass: HomeAssistant) -> str: ...
def _host_is_direct_connect(host: str) -> bool: ...

class ProtectFlowHandler(config_entries.ConfigFlow):
    VERSION: int
    entry: Any
    _discovered_device: Any
    def __init__(self) -> None: ...
    async def async_step_dhcp(self, discovery_info: dhcp.DhcpServiceInfo) -> FlowResult: ...
    async def async_step_ssdp(self, discovery_info: ssdp.SsdpServiceInfo) -> FlowResult: ...
    async def _async_discovery_handoff(self) -> FlowResult: ...
    async def async_step_discovery(self, discovery_info: DiscoveryInfoType) -> FlowResult: ...
    async def async_step_discovery_confirm(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    @staticmethod
    def async_get_options_flow(config_entry: config_entries.ConfigEntry) -> config_entries.OptionsFlow: ...
    def _async_create_entry(self, title: str, data: dict[str, Any]) -> FlowResult: ...
    async def _async_get_nvr_data(self, user_input: dict[str, Any]) -> tuple[Union[NVR, None], dict[str, str]]: ...
    async def async_step_reauth(self, user_input: dict[str, Any]) -> FlowResult: ...
    async def async_step_reauth_confirm(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...

class OptionsFlowHandler(config_entries.OptionsFlow):
    config_entry: Any
    def __init__(self, config_entry: config_entries.ConfigEntry) -> None: ...
    async def async_step_init(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
