from .const import CONF_DSMR_VERSION as CONF_DSMR_VERSION, CONF_PROTOCOL as CONF_PROTOCOL, CONF_SERIAL_ID as CONF_SERIAL_ID, CONF_SERIAL_ID_GAS as CONF_SERIAL_ID_GAS, CONF_TIME_BETWEEN_UPDATE as CONF_TIME_BETWEEN_UPDATE, DEFAULT_TIME_BETWEEN_UPDATE as DEFAULT_TIME_BETWEEN_UPDATE, DOMAIN as DOMAIN, DSMR_PROTOCOL as DSMR_PROTOCOL, DSMR_VERSIONS as DSMR_VERSIONS, LOGGER as LOGGER, RFXTRX_DSMR_PROTOCOL as RFXTRX_DSMR_PROTOCOL
from _typeshed import Incomplete
from dsmr_parser.objects import DSMRObject as DSMRObject
from homeassistant import config_entries as config_entries, core as core, exceptions as exceptions
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT, CONF_TYPE as CONF_TYPE
from homeassistant.core import callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from typing import Any

CONF_MANUAL_PATH: str

class DSMRConnection:
    _host: Incomplete
    _port: Incomplete
    _dsmr_version: Incomplete
    _protocol: Incomplete
    _telegram: Incomplete
    _equipment_identifier: Incomplete
    def __init__(self, host: str | None, port: int, dsmr_version: str, protocol: str) -> None: ...
    def equipment_identifier(self) -> str | None: ...
    def equipment_identifier_gas(self) -> str | None: ...
    async def validate_connect(self, hass: core.HomeAssistant) -> bool: ...

async def _validate_dsmr_connection(hass: core.HomeAssistant, data: dict[str, Any], protocol: str) -> dict[str, str | None]: ...

class DSMRFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION: int
    _dsmr_version: str | None
    @staticmethod
    def async_get_options_flow(config_entry: ConfigEntry) -> DSMROptionFlowHandler: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_setup_network(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_setup_serial(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_setup_serial_manual_path(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_validate_dsmr(self, input_data: dict[str, Any], errors: dict[str, str]) -> dict[str, Any]: ...

class DSMROptionFlowHandler(config_entries.OptionsFlow):
    entry: Incomplete
    def __init__(self, entry: ConfigEntry) -> None: ...
    async def async_step_init(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...

def get_serial_by_id(dev_path: str) -> str: ...

class CannotConnect(exceptions.HomeAssistantError): ...
class CannotCommunicate(exceptions.HomeAssistantError): ...
