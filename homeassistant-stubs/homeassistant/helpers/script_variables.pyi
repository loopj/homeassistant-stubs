from . import template as template
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from typing import Any, Dict, Mapping, Optional

class ScriptVariables:
    variables: Any = ...
    def __init__(self, variables: Dict[str, Any]) -> None: ...
    def async_render(self, hass: HomeAssistant, run_variables: Optional[Mapping[str, Any]], *, render_as_defaults: bool=..., limited: bool=...) -> Dict[str, Any]: ...
    def as_dict(self) -> dict: ...
