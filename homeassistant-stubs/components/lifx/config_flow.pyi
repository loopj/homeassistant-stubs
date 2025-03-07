from .const import CONF_SERIAL as CONF_SERIAL, DEFAULT_ATTEMPTS as DEFAULT_ATTEMPTS, DOMAIN as DOMAIN, OVERALL_TIMEOUT as OVERALL_TIMEOUT, TARGET_ANY as TARGET_ANY, _LOGGER as _LOGGER
from .discovery import async_discover_devices as async_discover_devices
from .util import async_entry_is_legacy as async_entry_is_legacy, async_get_legacy_entry as async_get_legacy_entry, async_multi_execute_lifx_with_retries as async_multi_execute_lifx_with_retries, formatted_serial as formatted_serial, lifx_features as lifx_features, mac_matches_serial_number as mac_matches_serial_number
from _typeshed import Incomplete
from aiolifx.aiolifx import Light as Light
from homeassistant import config_entries as config_entries
from homeassistant.components import zeroconf as zeroconf
from homeassistant.components.dhcp import DhcpServiceInfo as DhcpServiceInfo
from homeassistant.const import CONF_DEVICE as CONF_DEVICE, CONF_HOST as CONF_HOST
from homeassistant.core import callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.typing import DiscoveryInfoType as DiscoveryInfoType
from typing import Any

class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION: int
    _discovered_devices: Incomplete
    _discovered_device: Incomplete
    def __init__(self) -> None: ...
    async def async_step_dhcp(self, discovery_info: DhcpServiceInfo) -> FlowResult: ...
    async def async_step_homekit(self, discovery_info: zeroconf.ZeroconfServiceInfo) -> FlowResult: ...
    async def async_step_integration_discovery(self, discovery_info: DiscoveryInfoType) -> FlowResult: ...
    async def _async_handle_discovery(self, host: str, serial: str | None = ...) -> FlowResult: ...
    def _async_discovered_pending_migration(self) -> bool: ...
    async def async_step_discovery_confirm(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_pick_device(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    def _async_create_entry_from_device(self, device: Light) -> FlowResult: ...
    async def _async_try_connect(self, host: str, serial: str | None = ..., raise_on_progress: bool = ...) -> Light | None: ...
