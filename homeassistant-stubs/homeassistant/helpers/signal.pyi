from homeassistant.const import RESTART_EXIT_CODE as RESTART_EXIT_CODE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.loader import bind_hass as bind_hass
from types import FrameType as FrameType

def async_register_signal_handling(hass: HomeAssistant) -> None: ...
