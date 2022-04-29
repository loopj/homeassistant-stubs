from . import async_wait_for_elk_to_sync as async_wait_for_elk_to_sync
from .const import CONF_AUTO_CONFIGURE as CONF_AUTO_CONFIGURE, DISCOVER_SCAN_TIMEOUT as DISCOVER_SCAN_TIMEOUT, DOMAIN as DOMAIN, LOGIN_TIMEOUT as LOGIN_TIMEOUT
from .discovery import _short_mac as _short_mac, async_discover_device as async_discover_device, async_discover_devices as async_discover_devices, async_update_entry_from_discovery as async_update_entry_from_discovery
from _typeshed import Incomplete
from elkm1_lib.discovery import ElkSystem
from homeassistant import config_entries as config_entries, exceptions as exceptions
from homeassistant.components import dhcp as dhcp
from homeassistant.const import CONF_ADDRESS as CONF_ADDRESS, CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_PREFIX as CONF_PREFIX, CONF_PROTOCOL as CONF_PROTOCOL, CONF_USERNAME as CONF_USERNAME
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.typing import DiscoveryInfoType as DiscoveryInfoType
from homeassistant.util import slugify as slugify
from homeassistant.util.network import is_ip_address as is_ip_address
from typing import Any

CONF_DEVICE: str
NON_SECURE_PORT: int
SECURE_PORT: int
STANDARD_PORTS: Incomplete
_LOGGER: Incomplete
PROTOCOL_MAP: Incomplete
VALIDATE_TIMEOUT: int
BASE_SCHEMA: Incomplete
SECURE_PROTOCOLS: Incomplete
ALL_PROTOCOLS: Incomplete
DEFAULT_SECURE_PROTOCOL: str
DEFAULT_NON_SECURE_PROTOCOL: str
PORT_PROTOCOL_MAP: Incomplete

async def validate_input(data: dict[str, str], mac: Union[str, None]) -> dict[str, str]: ...
def _address_from_discovery(device: ElkSystem) -> str: ...
def _make_url_from_data(data: dict[str, str]) -> str: ...
def _placeholders_from_device(device: ElkSystem) -> dict[str, str]: ...

class ConfigFlow(config_entries.ConfigFlow):
    VERSION: int
    _discovered_device: Incomplete
    _discovered_devices: Incomplete
    def __init__(self) -> None: ...
    async def async_step_dhcp(self, discovery_info: dhcp.DhcpServiceInfo) -> FlowResult: ...
    async def async_step_integration_discovery(self, discovery_info: DiscoveryInfoType) -> FlowResult: ...
    async def _async_handle_discovery(self) -> FlowResult: ...
    async def async_step_discovery_confirm(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def _async_create_or_error(self, user_input: dict[str, Any], importing: bool) -> tuple[Union[dict[str, str], None], Union[FlowResult, None]]: ...
    async def async_step_discovered_connection(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_manual_connection(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_import(self, user_input: dict[str, Any]) -> FlowResult: ...
    def _url_already_configured(self, url: str) -> bool: ...

class InvalidAuth(exceptions.HomeAssistantError): ...
