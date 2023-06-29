import asyncio
import datetime
import enum
import voluptuous as vol
from . import block_async_io as block_async_io, loader as loader, util as util
from .auth import AuthManager as AuthManager
from .backports.enum import StrEnum as StrEnum
from .components.http import ApiConfig as ApiConfig, HomeAssistantHTTP as HomeAssistantHTTP
from .config_entries import ConfigEntries as ConfigEntries
from .const import ATTR_DOMAIN as ATTR_DOMAIN, ATTR_FRIENDLY_NAME as ATTR_FRIENDLY_NAME, ATTR_SERVICE as ATTR_SERVICE, ATTR_SERVICE_DATA as ATTR_SERVICE_DATA, COMPRESSED_STATE_ATTRIBUTES as COMPRESSED_STATE_ATTRIBUTES, COMPRESSED_STATE_CONTEXT as COMPRESSED_STATE_CONTEXT, COMPRESSED_STATE_LAST_CHANGED as COMPRESSED_STATE_LAST_CHANGED, COMPRESSED_STATE_LAST_UPDATED as COMPRESSED_STATE_LAST_UPDATED, COMPRESSED_STATE_STATE as COMPRESSED_STATE_STATE, EVENT_CALL_SERVICE as EVENT_CALL_SERVICE, EVENT_CORE_CONFIG_UPDATE as EVENT_CORE_CONFIG_UPDATE, EVENT_HOMEASSISTANT_CLOSE as EVENT_HOMEASSISTANT_CLOSE, EVENT_HOMEASSISTANT_FINAL_WRITE as EVENT_HOMEASSISTANT_FINAL_WRITE, EVENT_HOMEASSISTANT_START as EVENT_HOMEASSISTANT_START, EVENT_HOMEASSISTANT_STARTED as EVENT_HOMEASSISTANT_STARTED, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, EVENT_SERVICE_REGISTERED as EVENT_SERVICE_REGISTERED, EVENT_SERVICE_REMOVED as EVENT_SERVICE_REMOVED, EVENT_STATE_CHANGED as EVENT_STATE_CHANGED, LENGTH_METERS as LENGTH_METERS, MATCH_ALL as MATCH_ALL, MAX_LENGTH_EVENT_EVENT_TYPE as MAX_LENGTH_EVENT_EVENT_TYPE, MAX_LENGTH_STATE_STATE as MAX_LENGTH_STATE_STATE, __version__ as __version__
from .exceptions import HomeAssistantError as HomeAssistantError, InvalidEntityFormatError as InvalidEntityFormatError, InvalidStateError as InvalidStateError, MaxLengthExceeded as MaxLengthExceeded, ServiceNotFound as ServiceNotFound, Unauthorized as Unauthorized
from .helpers.aiohttp_compat import restore_original_aiohttp_cancel_behavior as restore_original_aiohttp_cancel_behavior
from .helpers.json import json_dumps as json_dumps
from .helpers.storage import Store as Store
from .util import location as location
from .util.async_ import cancelling as cancelling, run_callback_threadsafe as run_callback_threadsafe, shutdown_run_callback_threadsafe as shutdown_run_callback_threadsafe
from .util.json import JsonObjectType as JsonObjectType
from .util.read_only_dict import ReadOnlyDict as ReadOnlyDict
from .util.timeout import TimeoutManager as TimeoutManager
from .util.ulid import ulid as ulid, ulid_at_time as ulid_at_time
from .util.unit_system import METRIC_SYSTEM as METRIC_SYSTEM, UnitSystem as UnitSystem, _CONF_UNIT_SYSTEM_IMPERIAL as _CONF_UNIT_SYSTEM_IMPERIAL, _CONF_UNIT_SYSTEM_US_CUSTOMARY as _CONF_UNIT_SYSTEM_US_CUSTOMARY, get_unit_system as get_unit_system
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable, Collection, Coroutine, Iterable, Mapping
from contextvars import ContextVar
from typing import Any, Generic, NamedTuple, TypeVar, overload
from typing_extensions import Self

STAGE_1_SHUTDOWN_TIMEOUT: int
STAGE_2_SHUTDOWN_TIMEOUT: int
STAGE_3_SHUTDOWN_TIMEOUT: int
_T = TypeVar('_T')
_R = TypeVar('_R')
_R_co = TypeVar('_R_co', covariant=True)
_P: Incomplete
_UNDEF: dict[Any, Any]
_CallableT = TypeVar('_CallableT', bound=Callable[..., Any])
CALLBACK_TYPE = Callable[[], None]
CORE_STORAGE_KEY: str
CORE_STORAGE_VERSION: int
CORE_STORAGE_MINOR_VERSION: int
DOMAIN: str
BLOCK_LOG_TIMEOUT: int
ServiceResponse: Incomplete

class ConfigSource(StrEnum):
    DEFAULT: str
    DISCOVERED: str
    STORAGE: str
    YAML: str

SOURCE_DISCOVERED: Incomplete
SOURCE_STORAGE: Incomplete
SOURCE_YAML: Incomplete
TIMEOUT_EVENT_START: int
MAX_EXPECTED_ENTITY_IDS: int
_LOGGER: Incomplete
_cv_hass: ContextVar[HomeAssistant]

def split_entity_id(entity_id: str) -> tuple[str, str]: ...

_OBJECT_ID: str
_DOMAIN: Incomplete
VALID_DOMAIN: Incomplete
VALID_ENTITY_ID: Incomplete

def valid_domain(domain: str) -> bool: ...
def valid_entity_id(entity_id: str) -> bool: ...
def callback(func: _CallableT) -> _CallableT: ...
def is_callback(func: Callable[..., Any]) -> bool: ...
def async_get_hass() -> HomeAssistant: ...

class HassJobType(enum.Enum):
    Coroutinefunction: int
    Callback: int
    Executor: int

class HassJob(Generic[_P, _R_co]):
    __slots__: Incomplete
    target: Incomplete
    name: Incomplete
    job_type: Incomplete
    _cancel_on_shutdown: Incomplete
    def __init__(self, target: Callable[_P, _R_co], name: str | None = ..., *, cancel_on_shutdown: bool | None = ...) -> None: ...
    @property
    def cancel_on_shutdown(self) -> bool | None: ...
    def __repr__(self) -> str: ...

def _get_hassjob_callable_job_type(target: Callable[..., Any]) -> HassJobType: ...

class CoreState(enum.Enum):
    not_running: str
    starting: str
    running: str
    stopping: str
    final_write: str
    stopped: str
    def __str__(self) -> str: ...

class HomeAssistant:
    auth: AuthManager
    http: HomeAssistantHTTP
    config_entries: ConfigEntries
    def __new__(cls) -> HomeAssistant: ...
    loop: Incomplete
    _tasks: Incomplete
    _background_tasks: Incomplete
    bus: Incomplete
    services: Incomplete
    states: Incomplete
    config: Incomplete
    components: Incomplete
    helpers: Incomplete
    data: Incomplete
    state: Incomplete
    exit_code: int
    _stopped: Incomplete
    timeout: Incomplete
    _stop_future: Incomplete
    def __init__(self) -> None: ...
    @property
    def is_running(self) -> bool: ...
    @property
    def is_stopping(self) -> bool: ...
    def start(self) -> int: ...
    async def async_run(self, *, attach_signals: bool = ...) -> int: ...
    async def async_start(self) -> None: ...
    def add_job(self, target: Callable[..., Any] | Coroutine[Any, Any, Any], *args: Any) -> None: ...
    @overload
    def async_add_job(self, target: Callable[..., Coroutine[Any, Any, _R]], *args: Any) -> asyncio.Future[_R] | None: ...
    @overload
    def async_add_job(self, target: Callable[..., Coroutine[Any, Any, _R] | _R], *args: Any) -> asyncio.Future[_R] | None: ...
    @overload
    def async_add_job(self, target: Coroutine[Any, Any, _R], *args: Any) -> asyncio.Future[_R] | None: ...
    @overload
    def async_add_hass_job(self, hassjob: HassJob[..., Coroutine[Any, Any, _R]], *args: Any) -> asyncio.Future[_R] | None: ...
    @overload
    def async_add_hass_job(self, hassjob: HassJob[..., Coroutine[Any, Any, _R] | _R], *args: Any) -> asyncio.Future[_R] | None: ...
    def create_task(self, target: Coroutine[Any, Any, Any], name: str | None = ...) -> None: ...
    def async_create_task(self, target: Coroutine[Any, Any, _R], name: str | None = ...) -> asyncio.Task[_R]: ...
    def async_create_background_task(self, target: Coroutine[Any, Any, _R], name: str) -> asyncio.Task[_R]: ...
    def async_add_executor_job(self, target: Callable[..., _T], *args: Any) -> asyncio.Future[_T]: ...
    @overload
    def async_run_hass_job(self, hassjob: HassJob[..., Coroutine[Any, Any, _R]], *args: Any) -> asyncio.Future[_R] | None: ...
    @overload
    def async_run_hass_job(self, hassjob: HassJob[..., Coroutine[Any, Any, _R] | _R], *args: Any) -> asyncio.Future[_R] | None: ...
    @overload
    def async_run_job(self, target: Callable[..., Coroutine[Any, Any, _R]], *args: Any) -> asyncio.Future[_R] | None: ...
    @overload
    def async_run_job(self, target: Callable[..., Coroutine[Any, Any, _R] | _R], *args: Any) -> asyncio.Future[_R] | None: ...
    @overload
    def async_run_job(self, target: Coroutine[Any, Any, _R], *args: Any) -> asyncio.Future[_R] | None: ...
    def block_till_done(self) -> None: ...
    async def async_block_till_done(self) -> None: ...
    async def _await_and_log_pending(self, pending: Collection[Awaitable[Any]]) -> None: ...
    def stop(self) -> None: ...
    async def async_stop(self, exit_code: int = ..., *, force: bool = ...) -> None: ...
    def _cancel_cancellable_timers(self) -> None: ...
    def _async_log_running_tasks(self, stage: int) -> None: ...

class Context:
    __slots__: Incomplete
    id: Incomplete
    user_id: Incomplete
    parent_id: Incomplete
    origin_event: Incomplete
    _as_dict: Incomplete
    def __init__(self, user_id: str | None = ..., parent_id: str | None = ..., id: str | None = ...) -> None: ...
    def __eq__(self, other: Any) -> bool: ...
    def as_dict(self) -> ReadOnlyDict[str, str | None]: ...

class EventOrigin(enum.Enum):
    local: str
    remote: str
    def __str__(self) -> str: ...

class Event:
    __slots__: Incomplete
    event_type: Incomplete
    data: Incomplete
    origin: Incomplete
    time_fired: Incomplete
    context: Incomplete
    _as_dict: Incomplete
    def __init__(self, event_type: str, data: dict[str, Any] | None = ..., origin: EventOrigin = ..., time_fired: datetime.datetime | None = ..., context: Context | None = ...) -> None: ...
    def as_dict(self) -> ReadOnlyDict[str, Any]: ...
    def __repr__(self) -> str: ...

class _FilterableJob(NamedTuple):
    job: HassJob[[Event], Coroutine[Any, Any, None] | None]
    event_filter: Callable[[Event], bool] | None
    run_immediately: bool

class EventBus:
    _listeners: Incomplete
    _match_all_listeners: Incomplete
    _hass: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    def async_listeners(self) -> dict[str, int]: ...
    @property
    def listeners(self) -> dict[str, int]: ...
    def fire(self, event_type: str, event_data: dict[str, Any] | None = ..., origin: EventOrigin = ..., context: Context | None = ...) -> None: ...
    def async_fire(self, event_type: str, event_data: dict[str, Any] | None = ..., origin: EventOrigin = ..., context: Context | None = ..., time_fired: datetime.datetime | None = ...) -> None: ...
    def listen(self, event_type: str, listener: Callable[[Event], Coroutine[Any, Any, None] | None]) -> CALLBACK_TYPE: ...
    def async_listen(self, event_type: str, listener: Callable[[Event], Coroutine[Any, Any, None] | None], event_filter: Callable[[Event], bool] | None = ..., run_immediately: bool = ...) -> CALLBACK_TYPE: ...
    def _async_listen_filterable_job(self, event_type: str, filterable_job: _FilterableJob) -> CALLBACK_TYPE: ...
    def listen_once(self, event_type: str, listener: Callable[[Event], Coroutine[Any, Any, None] | None]) -> CALLBACK_TYPE: ...
    def async_listen_once(self, event_type: str, listener: Callable[[Event], Coroutine[Any, Any, None] | None]) -> CALLBACK_TYPE: ...
    def _async_remove_listener(self, event_type: str, filterable_job: _FilterableJob) -> None: ...

class State:
    __slots__: Incomplete
    entity_id: Incomplete
    state: Incomplete
    attributes: Incomplete
    last_updated: Incomplete
    last_changed: Incomplete
    context: Incomplete
    _as_dict: Incomplete
    _as_dict_json: Incomplete
    _as_compressed_state_json: Incomplete
    def __init__(self, entity_id: str, state: str, attributes: Mapping[str, Any] | None = ..., last_changed: datetime.datetime | None = ..., last_updated: datetime.datetime | None = ..., context: Context | None = ..., validate_entity_id: bool | None = ...) -> None: ...
    @property
    def name(self) -> str: ...
    def as_dict(self) -> ReadOnlyDict[str, Collection[Any]]: ...
    def as_dict_json(self) -> str: ...
    def as_compressed_state(self) -> dict[str, Any]: ...
    def as_compressed_state_json(self) -> str: ...
    @classmethod
    def from_dict(cls, json_dict: dict[str, Any]) -> Self | None: ...
    def expire(self) -> None: ...
    def __repr__(self) -> str: ...

class StateMachine:
    _states: Incomplete
    _reservations: Incomplete
    _bus: Incomplete
    _loop: Incomplete
    def __init__(self, bus: EventBus, loop: asyncio.events.AbstractEventLoop) -> None: ...
    def entity_ids(self, domain_filter: str | None = ...) -> list[str]: ...
    def async_entity_ids(self, domain_filter: str | Iterable[str] | None = ...) -> list[str]: ...
    def async_entity_ids_count(self, domain_filter: str | Iterable[str] | None = ...) -> int: ...
    def all(self, domain_filter: str | Iterable[str] | None = ...) -> list[State]: ...
    def async_all(self, domain_filter: str | Iterable[str] | None = ...) -> list[State]: ...
    def get(self, entity_id: str) -> State | None: ...
    def is_state(self, entity_id: str, state: str) -> bool: ...
    def remove(self, entity_id: str) -> bool: ...
    def async_remove(self, entity_id: str, context: Context | None = ...) -> bool: ...
    def set(self, entity_id: str, new_state: str, attributes: Mapping[str, Any] | None = ..., force_update: bool = ..., context: Context | None = ...) -> None: ...
    def async_reserve(self, entity_id: str) -> None: ...
    def async_available(self, entity_id: str) -> bool: ...
    def async_set(self, entity_id: str, new_state: str, attributes: Mapping[str, Any] | None = ..., force_update: bool = ..., context: Context | None = ...) -> None: ...

class SupportsResponse(StrEnum):
    NONE: str
    OPTIONAL: str
    ONLY: str

class Service:
    __slots__: Incomplete
    job: Incomplete
    schema: Incomplete
    supports_response: Incomplete
    def __init__(self, func: Callable[[ServiceCall], Coroutine[Any, Any, ServiceResponse] | None], schema: vol.Schema | None, domain: str, service: str, context: Context | None = ..., supports_response: SupportsResponse = ...) -> None: ...

class ServiceCall:
    __slots__: Incomplete
    domain: Incomplete
    service: Incomplete
    data: Incomplete
    context: Incomplete
    return_response: Incomplete
    def __init__(self, domain: str, service: str, data: dict[str, Any] | None = ..., context: Context | None = ..., return_response: bool = ...) -> None: ...
    def __repr__(self) -> str: ...

class ServiceRegistry:
    _services: Incomplete
    _hass: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    @property
    def services(self) -> dict[str, dict[str, Service]]: ...
    def async_services(self) -> dict[str, dict[str, Service]]: ...
    def has_service(self, domain: str, service: str) -> bool: ...
    def supports_response(self, domain: str, service: str) -> SupportsResponse: ...
    def register(self, domain: str, service: str, service_func: Callable[[ServiceCall], Coroutine[Any, Any, ServiceResponse] | None], schema: vol.Schema | None = ...) -> None: ...
    def async_register(self, domain: str, service: str, service_func: Callable[[ServiceCall], Coroutine[Any, Any, ServiceResponse] | None], schema: vol.Schema | None = ..., supports_response: SupportsResponse = ...) -> None: ...
    def remove(self, domain: str, service: str) -> None: ...
    def async_remove(self, domain: str, service: str) -> None: ...
    def call(self, domain: str, service: str, service_data: dict[str, Any] | None = ..., blocking: bool = ..., context: Context | None = ..., target: dict[str, Any] | None = ..., return_response: bool = ...) -> ServiceResponse: ...
    async def async_call(self, domain: str, service: str, service_data: dict[str, Any] | None = ..., blocking: bool = ..., context: Context | None = ..., target: dict[str, Any] | None = ..., return_response: bool = ...) -> ServiceResponse: ...
    def _run_service_in_background(self, coro_or_task: Coroutine[Any, Any, Any] | asyncio.Task[Any], service_call: ServiceCall) -> None: ...
    async def _execute_service(self, handler: Service, service_call: ServiceCall) -> ServiceResponse: ...

class Config:
    hass: Incomplete
    _store: Incomplete
    latitude: int
    longitude: int
    elevation: int
    location_name: str
    time_zone: str
    units: Incomplete
    internal_url: Incomplete
    external_url: Incomplete
    currency: str
    country: Incomplete
    language: str
    config_source: Incomplete
    skip_pip: bool
    skip_pip_packages: Incomplete
    components: Incomplete
    api: Incomplete
    config_dir: Incomplete
    allowlist_external_dirs: Incomplete
    allowlist_external_urls: Incomplete
    media_dirs: Incomplete
    safe_mode: bool
    legacy_templates: bool
    def __init__(self, hass: HomeAssistant) -> None: ...
    def distance(self, lat: float, lon: float) -> float | None: ...
    def path(self, *path: str) -> str: ...
    def is_allowed_external_url(self, url: str) -> bool: ...
    def is_allowed_path(self, path: str) -> bool: ...
    def as_dict(self) -> dict[str, Any]: ...
    def set_time_zone(self, time_zone_str: str) -> None: ...
    def _update(self, *, source: ConfigSource, latitude: float | None = ..., longitude: float | None = ..., elevation: int | None = ..., unit_system: str | None = ..., location_name: str | None = ..., time_zone: str | None = ..., external_url: str | dict[Any, Any] | None = ..., internal_url: str | dict[Any, Any] | None = ..., currency: str | None = ..., country: str | dict[Any, Any] | None = ..., language: str | None = ...) -> None: ...
    async def async_update(self, **kwargs: Any) -> None: ...
    async def async_load(self) -> None: ...
    async def _async_store(self) -> None: ...
    class _ConfigStore(Store[dict[str, Any]]):
        _original_unit_system: Incomplete
        def __init__(self, hass: HomeAssistant) -> None: ...
        async def _async_migrate_func(self, old_major_version: int, old_minor_version: int, old_data: dict[str, Any]) -> dict[str, Any]: ...
        async def async_save(self, data: dict[str, Any]) -> None: ...
