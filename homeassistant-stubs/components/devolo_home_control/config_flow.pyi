from . import configure_mydevolo as configure_mydevolo
from .const import CONF_MYDEVOLO as CONF_MYDEVOLO, DEFAULT_MYDEVOLO as DEFAULT_MYDEVOLO, DOMAIN as DOMAIN, SUPPORTED_MODEL_TYPES as SUPPORTED_MODEL_TYPES
from .exceptions import CredentialsInvalid as CredentialsInvalid, UuidChanged as UuidChanged
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant import config_entries as config_entries
from homeassistant.components import zeroconf as zeroconf
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from typing import Any

class DevoloHomeControlFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION: int
    data_schema: Incomplete
    _reauth_entry: Incomplete
    _url: Incomplete
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_zeroconf(self, discovery_info: zeroconf.ZeroconfServiceInfo) -> FlowResult: ...
    async def async_step_zeroconf_confirm(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> FlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def _connect_mydevolo(self, user_input: dict[str, Any]) -> FlowResult: ...
    def _show_form(self, step_id: str, errors: dict[str, str] | None = ...) -> FlowResult: ...
