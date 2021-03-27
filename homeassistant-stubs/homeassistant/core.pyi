import asyncio
import datetime
import enum
import voluptuous as vol
from homeassistant import block_async_io as block_async_io, loader as loader, util as util
from homeassistant.auth import AuthManager as AuthManager
from homeassistant.components.http import HomeAssistantHTTP as HomeAssistantHTTP
from homeassistant.config_entries import ConfigEntries as ConfigEntries
from homeassistant.const import ATTR_DOMAIN as ATTR_DOMAIN, ATTR_FRIENDLY_NAME as ATTR_FRIENDLY_NAME, ATTR_NOW as ATTR_NOW, ATTR_SECONDS as ATTR_SECONDS, ATTR_SERVICE as ATTR_SERVICE, ATTR_SERVICE_DATA as ATTR_SERVICE_DATA, CONF_UNIT_SYSTEM_IMPERIAL as CONF_UNIT_SYSTEM_IMPERIAL, EVENT_CALL_SERVICE as EVENT_CALL_SERVICE, EVENT_CORE_CONFIG_UPDATE as EVENT_CORE_CONFIG_UPDATE, EVENT_HOMEASSISTANT_CLOSE as EVENT_HOMEASSISTANT_CLOSE, EVENT_HOMEASSISTANT_FINAL_WRITE as EVENT_HOMEASSISTANT_FINAL_WRITE, EVENT_HOMEASSISTANT_START as EVENT_HOMEASSISTANT_START, EVENT_HOMEASSISTANT_STARTED as EVENT_HOMEASSISTANT_STARTED, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, EVENT_SERVICE_REGISTERED as EVENT_SERVICE_REGISTERED, EVENT_SERVICE_REMOVED as EVENT_SERVICE_REMOVED, EVENT_STATE_CHANGED as EVENT_STATE_CHANGED, EVENT_TIMER_OUT_OF_SYNC as EVENT_TIMER_OUT_OF_SYNC, EVENT_TIME_CHANGED as EVENT_TIME_CHANGED, LENGTH_METERS as LENGTH_METERS, MATCH_ALL as MATCH_ALL
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, InvalidEntityFormatError as InvalidEntityFormatError, InvalidStateError as InvalidStateError, ServiceNotFound as ServiceNotFound, Unauthorized as Unauthorized
from homeassistant.util import location as location
from homeassistant.util.async_ import fire_coroutine_threadsafe as fire_coroutine_threadsafe, run_callback_threadsafe as run_callback_threadsafe, shutdown_run_callback_threadsafe as shutdown_run_callback_threadsafe
from homeassistant.util.timeout import TimeoutManager as TimeoutManager
from homeassistant.util.unit_system import IMPERIAL_SYSTEM as IMPERIAL_SYSTEM, METRIC_SYSTEM as METRIC_SYSTEM, UnitSystem as UnitSystem
from typing import Any, Awaitable, Callable, Coroutine, Dict, Iterable, List, Mapping, Optional, TypeVar, Union

T = TypeVar('T')
CALLABLE_T = TypeVar('CALLABLE_T', bound=Callable)
CALLBACK_TYPE = Callable[[], None]
CORE_STORAGE_KEY: str
CORE_STORAGE_VERSION: int
DOMAIN: str
BLOCK_LOG_TIMEOUT: int
SERVICE_CALL_LIMIT: int
SOURCE_DISCOVERED: str
SOURCE_STORAGE: str
SOURCE_YAML: str
TIMEOUT_EVENT_START: int

def split_entity_id(entity_id: str) -> List[str]: ...

VALID_ENTITY_ID: Any

def valid_entity_id(entity_id: str) -> bool: ...
def valid_state(state: str) -> bool: ...
def callback(func: CALLABLE_T) -> CALLABLE_T: ...
def is_callback(func: Callable[..., Any]) -> bool: ...

class HassJobType(enum.Enum):
    Coroutinefunction: int = ...
    Callback: int = ...
    Executor: int = ...

class HassJob:
    target: Any = ...
    job_type: Any = ...
    def __init__(self, target: Callable) -> None: ...

class CoreState(enum.Enum):
    not_running: str = ...
    starting: str = ...
    running: str = ...
    stopping: str = ...
    final_write: str = ...
    stopped: str = ...

class HomeAssistant:
    auth: AuthManager
    http: HomeAssistantHTTP = ...
    config_entries: ConfigEntries = ...
    loop: Any = ...
    bus: Any = ...
    services: Any = ...
    states: Any = ...
    config: Any = ...
    components: Any = ...
    helpers: Any = ...
    data: Any = ...
    state: Any = ...
    exit_code: int = ...
    timeout: Any = ...
    def __init__(self) -> None: ...
    @property
    def is_running(self) -> bool: ...
    @property
    def is_stopping(self) -> bool: ...
    def start(self) -> int: ...
    async def async_run(self, *, attach_signals: bool=...) -> int: ...
    async def async_start(self) -> None: ...
    def add_job(self, target: Callable[..., Any], *args: Any) -> None: ...
    def async_add_job(self, target: Callable[..., Any], *args: Any) -> Optional[asyncio.Future]: ...
    def async_add_hass_job(self, hassjob: HassJob, *args: Any) -> Optional[asyncio.Future]: ...
    def async_create_task(self, target: Coroutine) -> asyncio.tasks.Task: ...
    def async_add_executor_job(self, target: Callable[..., T], *args: Any) -> Awaitable[T]: ...
    def async_track_tasks(self) -> None: ...
    def async_stop_track_tasks(self) -> None: ...
    def async_run_hass_job(self, hassjob: HassJob, *args: Any) -> Optional[asyncio.Future]: ...
    def async_run_job(self, target: Callable[..., Union[None, Awaitable]], *args: Any) -> Optional[asyncio.Future]: ...
    def block_till_done(self) -> None: ...
    async def async_block_till_done(self) -> None: ...
    def stop(self) -> None: ...
    async def async_stop(self, exit_code: int=..., *, force: bool=...) -> None: ...

class Context:
    user_id: str = ...
    parent_id: Optional[str] = ...
    id: str = ...
    def as_dict(self) -> Dict[str, Optional[str]]: ...
    def __init__(self, user_id: Any, parent_id: Any, id: Any) -> None: ...
    def __lt__(self, other: Any) -> Any: ...
    def __le__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def __ge__(self, other: Any) -> Any: ...

class EventOrigin(enum.Enum):
    local: str = ...
    remote: str = ...

class Event:
    event_type: Any = ...
    data: Any = ...
    origin: Any = ...
    time_fired: Any = ...
    context: Any = ...
    def __init__(self, event_type: str, data: Optional[Dict[str, Any]]=..., origin: EventOrigin=..., time_fired: Optional[datetime.datetime]=..., context: Optional[Context]=...) -> None: ...
    def __hash__(self) -> int: ...
    def as_dict(self) -> Dict[str, Any]: ...
    def __eq__(self, other: Any) -> bool: ...

class EventBus:
    def __init__(self, hass: HomeAssistant) -> None: ...
    def async_listeners(self) -> Dict[str, int]: ...
    @property
    def listeners(self) -> Dict[str, int]: ...
    def fire(self, event_type: str, event_data: Optional[Dict]=..., origin: EventOrigin=..., context: Optional[Context]=...) -> None: ...
    def async_fire(self, event_type: str, event_data: Optional[Dict[str, Any]]=..., origin: EventOrigin=..., context: Optional[Context]=..., time_fired: Optional[datetime.datetime]=...) -> None: ...
    def listen(self, event_type: str, listener: Callable) -> CALLBACK_TYPE: ...
    def async_listen(self, event_type: str, listener: Callable, event_filter: Optional[Callable]=...) -> CALLBACK_TYPE: ...
    def listen_once(self, event_type: str, listener: Callable) -> CALLBACK_TYPE: ...
    def async_listen_once(self, event_type: str, listener: Callable) -> CALLBACK_TYPE: ...

class State:
    entity_id: Any = ...
    state: Any = ...
    attributes: Any = ...
    last_updated: Any = ...
    last_changed: Any = ...
    context: Any = ...
    def __init__(self, entity_id: str, state: str, attributes: Optional[Mapping[str, Any]]=..., last_changed: Optional[datetime.datetime]=..., last_updated: Optional[datetime.datetime]=..., context: Optional[Context]=..., validate_entity_id: Optional[bool]=...) -> None: ...
    @property
    def name(self) -> str: ...
    def as_dict(self) -> Dict: ...
    @classmethod
    def from_dict(cls: Any, json_dict: Dict) -> Any: ...
    def __eq__(self, other: Any) -> bool: ...

class StateMachine:
    def __init__(self, bus: EventBus, loop: asyncio.events.AbstractEventLoop) -> None: ...
    def entity_ids(self, domain_filter: Optional[str]=...) -> List[str]: ...
    def async_entity_ids(self, domain_filter: Optional[Union[str, Iterable]]=...) -> List[str]: ...
    def async_entity_ids_count(self, domain_filter: Optional[Union[str, Iterable]]=...) -> int: ...
    def all(self, domain_filter: Optional[Union[str, Iterable]]=...) -> List[State]: ...
    def async_all(self, domain_filter: Optional[Union[str, Iterable]]=...) -> List[State]: ...
    def get(self, entity_id: str) -> Optional[State]: ...
    def is_state(self, entity_id: str, state: str) -> bool: ...
    def remove(self, entity_id: str) -> bool: ...
    def async_remove(self, entity_id: str, context: Optional[Context]=...) -> bool: ...
    def set(self, entity_id: str, new_state: str, attributes: Optional[Mapping[str, Any]]=..., force_update: bool=..., context: Optional[Context]=...) -> None: ...
    def async_reserve(self, entity_id: str) -> None: ...
    def async_available(self, entity_id: str) -> bool: ...
    def async_set(self, entity_id: str, new_state: str, attributes: Optional[Mapping[str, Any]]=..., force_update: bool=..., context: Optional[Context]=...) -> None: ...

class Service:
    job: Any = ...
    schema: Any = ...
    def __init__(self, func: Callable, schema: Optional[vol.Schema], context: Optional[Context]=...) -> None: ...

class ServiceCall:
    domain: Any = ...
    service: Any = ...
    data: Any = ...
    context: Any = ...
    def __init__(self, domain: str, service: str, data: Optional[Dict]=..., context: Optional[Context]=...) -> None: ...

class ServiceRegistry:
    def __init__(self, hass: HomeAssistant) -> None: ...
    @property
    def services(self) -> Dict[str, Dict[str, Service]]: ...
    def async_services(self) -> Dict[str, Dict[str, Service]]: ...
    def has_service(self, domain: str, service: str) -> bool: ...
    def register(self, domain: str, service: str, service_func: Callable, schema: Optional[vol.Schema]=...) -> None: ...
    def async_register(self, domain: str, service: str, service_func: Callable, schema: Optional[vol.Schema]=...) -> None: ...
    def remove(self, domain: str, service: str) -> None: ...
    def async_remove(self, domain: str, service: str) -> None: ...
    def call(self, domain: str, service: str, service_data: Optional[Dict]=..., blocking: bool=..., context: Optional[Context]=..., limit: Optional[float]=..., target: Optional[Dict]=...) -> Optional[bool]: ...
    async def async_call(self, domain: str, service: str, service_data: Optional[Dict]=..., blocking: bool=..., context: Optional[Context]=..., limit: Optional[float]=..., target: Optional[Dict]=...) -> Optional[bool]: ...

class Config:
    hass: Any = ...
    latitude: int = ...
    longitude: int = ...
    elevation: int = ...
    location_name: str = ...
    time_zone: Any = ...
    units: Any = ...
    internal_url: Any = ...
    external_url: Any = ...
    config_source: str = ...
    skip_pip: bool = ...
    components: Any = ...
    api: Any = ...
    config_dir: Any = ...
    allowlist_external_dirs: Any = ...
    allowlist_external_urls: Any = ...
    media_dirs: Any = ...
    safe_mode: bool = ...
    legacy_templates: bool = ...
    def __init__(self, hass: HomeAssistant) -> None: ...
    def distance(self, lat: float, lon: float) -> Optional[float]: ...
    def path(self, *path: str) -> str: ...
    def is_allowed_external_url(self, url: str) -> bool: ...
    def is_allowed_path(self, path: str) -> bool: ...
    def as_dict(self) -> Dict: ...
    def set_time_zone(self, time_zone_str: str) -> None: ...
    async def async_update(self, **kwargs: Any) -> None: ...
    async def async_load(self) -> None: ...
    async def async_store(self) -> None: ...
