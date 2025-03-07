from .const import DATA_DISCOVERY as DATA_DISCOVERY, DOMAIN as DOMAIN
from .utils import async_discover_devices as async_discover_devices
from homeassistant import config_entries as config_entries
from homeassistant.data_entry_flow import FlowResult as FlowResult
from typing import Any

class SwitcherFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    async def async_step_import(self, import_config: dict[str, Any]) -> FlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_confirm(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
