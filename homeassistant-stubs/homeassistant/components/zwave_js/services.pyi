from . import const as const
from .helpers import async_get_node_from_device_id as async_get_node_from_device_id, async_get_node_from_entity_id as async_get_node_from_entity_id
from homeassistant.const import ATTR_DEVICE_ID as ATTR_DEVICE_ID, ATTR_ENTITY_ID as ATTR_ENTITY_ID
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.entity_registry import EntityRegistry as EntityRegistry
from typing import Any, Dict, Union

def parameter_name_does_not_need_bitmask(val: Dict[str, Union[int, str]]) -> Dict[str, Union[int, str]]: ...

BITMASK_SCHEMA: Any

class ZWaveServices:
    def __init__(self, hass: HomeAssistant, ent_reg: EntityRegistry) -> None: ...
    def async_register(self) -> None: ...
    async def async_set_config_parameter(self, service: ServiceCall) -> None: ...
    async def async_poll_value(self, service: ServiceCall) -> None: ...
