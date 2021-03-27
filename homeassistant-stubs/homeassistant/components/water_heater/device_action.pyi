from . import DOMAIN as DOMAIN
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_DOMAIN as CONF_DOMAIN, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_TYPE as CONF_TYPE, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON
from homeassistant.core import Context as Context, HomeAssistant as HomeAssistant
from homeassistant.helpers import entity_registry as entity_registry
from typing import Any, List, Optional

ACTION_TYPES: Any
ACTION_SCHEMA: Any

async def async_get_actions(hass: HomeAssistant, device_id: str) -> List[dict]: ...
async def async_call_action_from_config(hass: HomeAssistant, config: dict, variables: dict, context: Optional[Context]) -> None: ...
