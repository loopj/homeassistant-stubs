from .common import FritzBoxTools as FritzBoxTools
from .const import DEFAULT_HOST as DEFAULT_HOST, DEFAULT_PORT as DEFAULT_PORT, DOMAIN as DOMAIN, ERROR_AUTH_INVALID as ERROR_AUTH_INVALID, ERROR_CANNOT_CONNECT as ERROR_CANNOT_CONNECT, ERROR_UNKNOWN as ERROR_UNKNOWN
from homeassistant.components import ssdp as ssdp
from homeassistant.components.device_tracker.const import CONF_CONSIDER_HOME as CONF_CONSIDER_HOME, DEFAULT_CONSIDER_HOME as DEFAULT_CONSIDER_HOME
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, OptionsFlow as OptionsFlow
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from typing import Any
from urllib.parse import ParseResult as ParseResult

_LOGGER: Any

class FritzBoxToolsFlowHandler(ConfigFlow):
    VERSION: int
    @staticmethod
    def async_get_options_flow(config_entry: ConfigEntry) -> OptionsFlow: ...
    _host: Any
    _entry: Any
    _name: Any
    _password: Any
    _port: Any
    _username: Any
    fritz_tools: Any
    def __init__(self) -> None: ...
    async def fritz_tools_init(self) -> Union[str, None]: ...
    async def async_check_configured_entry(self) -> Union[ConfigEntry, None]: ...
    def _async_create_entry(self) -> FlowResult: ...
    async def async_step_ssdp(self, discovery_info: ssdp.SsdpServiceInfo) -> FlowResult: ...
    async def async_step_confirm(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    def _show_setup_form_init(self, errors: Union[dict[str, str], None] = ...) -> FlowResult: ...
    def _show_setup_form_confirm(self, errors: Union[dict[str, str], None] = ...) -> FlowResult: ...
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_reauth(self, data: dict[str, Any]) -> FlowResult: ...
    def _show_setup_form_reauth_confirm(self, user_input: dict[str, Any], errors: Union[dict[str, str], None] = ...) -> FlowResult: ...
    async def async_step_reauth_confirm(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_import(self, import_config: dict[str, Any]) -> FlowResult: ...

class FritzBoxToolsOptionsFlowHandler(OptionsFlow):
    config_entry: Any
    def __init__(self, config_entry: ConfigEntry) -> None: ...
    async def async_step_init(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
