from . import debug_info as debug_info
from .. import mqtt as mqtt
from .const import DEFAULT_QOS as DEFAULT_QOS
from .models import MessageCallbackType as MessageCallbackType
from collections.abc import Callable as Callable, Coroutine
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

class EntitySubscription:
    hass: HomeAssistant
    topic: str | None
    message_callback: MessageCallbackType
    subscribe_task: Coroutine[Any, Any, Callable[[], None]] | None
    unsubscribe_callback: Callable[[], None] | None
    qos: int
    encoding: str
    def resubscribe_if_necessary(self, hass: HomeAssistant, other: EntitySubscription | None) -> None: ...
    async def subscribe(self) -> None: ...
    def _should_resubscribe(self, other: EntitySubscription | None) -> bool: ...
    def __init__(self, hass, topic, message_callback, subscribe_task, unsubscribe_callback, qos, encoding) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

def async_prepare_subscribe_topics(hass: HomeAssistant, new_state: dict[str, EntitySubscription] | None, topics: dict[str, Any]) -> dict[str, EntitySubscription]: ...
async def async_subscribe_topics(hass: HomeAssistant, sub_state: dict[str, EntitySubscription]) -> None: ...
def async_unsubscribe_topics(hass: HomeAssistant, sub_state: dict[str, EntitySubscription] | None) -> dict[str, EntitySubscription]: ...
