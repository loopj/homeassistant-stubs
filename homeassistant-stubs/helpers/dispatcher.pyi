from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from homeassistant.core import HassJob as HassJob, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.loader import bind_hass as bind_hass
from homeassistant.util.async_ import run_callback_threadsafe as run_callback_threadsafe
from homeassistant.util.logging import catch_log_exception as catch_log_exception
from typing import Any

_LOGGER: Incomplete
DATA_DISPATCHER: str

def dispatcher_connect(hass: HomeAssistant, signal: str, target: Callable[..., None]) -> Callable[[], None]: ...
def async_dispatcher_connect(hass: HomeAssistant, signal: str, target: Callable[..., Any]) -> Callable[[], None]: ...
def dispatcher_send(hass: HomeAssistant, signal: str, *args: Any) -> None: ...
def _generate_job(signal: str, target: Callable[..., Any]) -> HassJob[..., None | Coroutine[Any, Any, None]]: ...
def async_dispatcher_send(hass: HomeAssistant, signal: str, *args: Any) -> None: ...
