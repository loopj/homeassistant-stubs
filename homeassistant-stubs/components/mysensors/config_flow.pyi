from . import CONF_RETAIN as CONF_RETAIN, CONF_VERSION as CONF_VERSION, DEFAULT_VERSION as DEFAULT_VERSION
from .const import CONF_BAUD_RATE as CONF_BAUD_RATE, CONF_GATEWAY_TYPE as CONF_GATEWAY_TYPE, CONF_GATEWAY_TYPE_ALL as CONF_GATEWAY_TYPE_ALL, CONF_GATEWAY_TYPE_MQTT as CONF_GATEWAY_TYPE_MQTT, CONF_GATEWAY_TYPE_SERIAL as CONF_GATEWAY_TYPE_SERIAL, CONF_GATEWAY_TYPE_TCP as CONF_GATEWAY_TYPE_TCP, CONF_PERSISTENCE_FILE as CONF_PERSISTENCE_FILE, CONF_TCP_PORT as CONF_TCP_PORT, CONF_TOPIC_IN_PREFIX as CONF_TOPIC_IN_PREFIX, CONF_TOPIC_OUT_PREFIX as CONF_TOPIC_OUT_PREFIX, ConfGatewayType as ConfGatewayType, DOMAIN as DOMAIN
from .gateway import MQTT_COMPONENT as MQTT_COMPONENT, is_serial_port as is_serial_port, is_socket_address as is_socket_address, try_connect as try_connect
from homeassistant import config_entries as config_entries
from homeassistant.components.mqtt import valid_publish_topic as valid_publish_topic, valid_subscribe_topic as valid_subscribe_topic
from homeassistant.components.mysensors import CONF_DEVICE as CONF_DEVICE, DEFAULT_BAUD_RATE as DEFAULT_BAUD_RATE, DEFAULT_TCP_PORT as DEFAULT_TCP_PORT, is_persistence_file as is_persistence_file
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from typing import Any

_LOGGER: Any

def _get_schema_common(user_input: dict[str, str]) -> dict: ...
def _validate_version(version: str) -> dict[str, str]: ...
def _is_same_device(gw_type: ConfGatewayType, user_input: dict[str, Any], entry: ConfigEntry) -> bool: ...

class MySensorsConfigFlowHandler(config_entries.ConfigFlow):
    _gw_type: Any
    def __init__(self) -> None: ...
    async def async_step_import(self, user_input: dict[str, Any]) -> FlowResult: ...
    async def async_step_user(self, user_input: Union[dict[str, str], None] = ...) -> FlowResult: ...
    async def async_step_gw_serial(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_gw_tcp(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    def _check_topic_exists(self, topic: str) -> bool: ...
    async def async_step_gw_mqtt(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    def _async_create_entry(self, user_input: dict[str, Any]) -> FlowResult: ...
    def _normalize_persistence_file(self, path: str) -> str: ...
    async def validate_common(self, gw_type: ConfGatewayType, errors: dict[str, str], user_input: dict[str, Any]) -> dict[str, str]: ...
