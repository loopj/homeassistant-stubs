from .const import DOMAIN as DOMAIN
from homeassistant.components.hassio import HassioServiceInfo as HassioServiceInfo
from homeassistant.config_entries import ConfigFlow as ConfigFlow
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_SSL as CONF_SSL, CONF_USERNAME as CONF_USERNAME, CONF_VERIFY_SSL as CONF_VERIFY_SSL
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from typing import Any

class AdGuardHomeFlowHandler(ConfigFlow):
    VERSION: int
    _hassio_discovery: Union[dict[str, Any], None]
    async def _show_setup_form(self, errors: Union[dict[str, str], None] = ...) -> FlowResult: ...
    async def _show_hassio_form(self, errors: Union[dict[str, str], None] = ...) -> FlowResult: ...
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_hassio(self, discovery_info: HassioServiceInfo) -> FlowResult: ...
    async def async_step_hassio_confirm(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
