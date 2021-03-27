from homeassistant.const import ATTR_LATITUDE as ATTR_LATITUDE, ATTR_LONGITUDE as ATTR_LONGITUDE
from homeassistant.core import State as State
from homeassistant.helpers.typing import HomeAssistantType as HomeAssistantType
from typing import Optional, Sequence

def has_location(state: State) -> bool: ...
def closest(latitude: float, longitude: float, states: Sequence[State]) -> Optional[State]: ...
def find_coordinates(hass: HomeAssistantType, entity_id: str, recursion_history: Optional[list]=...) -> Optional[str]: ...
