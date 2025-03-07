import abc
from . import start as start
from .entity import Entity as Entity
from .event import async_track_time_interval as async_track_time_interval
from .frame import report as report
from .json import JSONEncoder as JSONEncoder
from .storage import Store as Store
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from datetime import datetime
from homeassistant.const import ATTR_RESTORED as ATTR_RESTORED, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import HomeAssistant as HomeAssistant, State as State, callback as callback, valid_entity_id as valid_entity_id
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from typing import Any, Self

DATA_RESTORE_STATE: str
_LOGGER: Incomplete
STORAGE_KEY: str
STORAGE_VERSION: int
STATE_DUMP_INTERVAL: Incomplete
STATE_EXPIRATION: Incomplete

class ExtraStoredData(ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def as_dict(self) -> dict[str, Any]: ...

class RestoredExtraData(ExtraStoredData):
    json_dict: Incomplete
    def __init__(self, json_dict: dict[str, Any]) -> None: ...
    def as_dict(self) -> dict[str, Any]: ...

class StoredState:
    extra_data: Incomplete
    last_seen: Incomplete
    state: Incomplete
    def __init__(self, state: State, extra_data: ExtraStoredData | None, last_seen: datetime) -> None: ...
    def as_dict(self) -> dict[str, Any]: ...
    @classmethod
    def from_dict(cls, json_dict: dict) -> Self: ...

async def async_load(hass: HomeAssistant) -> None: ...
def async_get(hass: HomeAssistant) -> RestoreStateData: ...

class RestoreStateData:
    @classmethod
    async def async_save_persistent_states(cls, hass: HomeAssistant) -> None: ...
    @classmethod
    async def async_get_instance(cls, hass: HomeAssistant) -> RestoreStateData: ...
    hass: Incomplete
    store: Incomplete
    last_states: Incomplete
    entities: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def async_setup(self) -> None: ...
    async def async_load(self) -> None: ...
    def async_get_stored_states(self) -> list[StoredState]: ...
    async def async_dump_states(self) -> None: ...
    def async_setup_dump(self, *args: Any) -> None: ...
    def async_restore_entity_added(self, entity: RestoreEntity) -> None: ...
    def async_restore_entity_removed(self, entity_id: str, extra_data: ExtraStoredData | None) -> None: ...

def _encode(value: Any) -> Any: ...
def _encode_complex(value: Any) -> Any: ...

class RestoreEntity(Entity):
    async def async_internal_added_to_hass(self) -> None: ...
    async def async_internal_will_remove_from_hass(self) -> None: ...
    def _async_get_restored_data(self) -> StoredState | None: ...
    async def async_get_last_state(self) -> State | None: ...
    async def async_get_last_extra_data(self) -> ExtraStoredData | None: ...
    @property
    def extra_restore_state_data(self) -> ExtraStoredData | None: ...
