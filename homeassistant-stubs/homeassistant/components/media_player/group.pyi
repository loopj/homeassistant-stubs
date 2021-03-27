from homeassistant.components.group import GroupIntegrationRegistry as GroupIntegrationRegistry
from homeassistant.const import STATE_IDLE as STATE_IDLE, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON, STATE_PAUSED as STATE_PAUSED, STATE_PLAYING as STATE_PLAYING
from homeassistant.core import callback as callback
from homeassistant.helpers.typing import HomeAssistantType as HomeAssistantType

def async_describe_on_off_states(hass: HomeAssistantType, registry: GroupIntegrationRegistry) -> None: ...
