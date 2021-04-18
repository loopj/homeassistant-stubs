import logging
from .trace import TraceElement as TraceElement, async_trace_path as async_trace_path, trace_append_element as trace_append_element, trace_id_get as trace_id_get, trace_path as trace_path, trace_path_get as trace_path_get, trace_set_result as trace_set_result, trace_stack_cv as trace_stack_cv, trace_stack_pop as trace_stack_pop, trace_stack_push as trace_stack_push
from homeassistant import exceptions as exceptions
from homeassistant.components import device_automation as device_automation, scene as scene
from homeassistant.components.logger import LOGSEVERITY as LOGSEVERITY
from homeassistant.const import ATTR_AREA_ID as ATTR_AREA_ID, ATTR_DEVICE_ID as ATTR_DEVICE_ID, ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_ALIAS as CONF_ALIAS, CONF_CHOOSE as CONF_CHOOSE, CONF_CONDITION as CONF_CONDITION, CONF_CONDITIONS as CONF_CONDITIONS, CONF_CONTINUE_ON_TIMEOUT as CONF_CONTINUE_ON_TIMEOUT, CONF_COUNT as CONF_COUNT, CONF_DEFAULT as CONF_DEFAULT, CONF_DELAY as CONF_DELAY, CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_DOMAIN as CONF_DOMAIN, CONF_EVENT as CONF_EVENT, CONF_EVENT_DATA as CONF_EVENT_DATA, CONF_EVENT_DATA_TEMPLATE as CONF_EVENT_DATA_TEMPLATE, CONF_MODE as CONF_MODE, CONF_REPEAT as CONF_REPEAT, CONF_SCENE as CONF_SCENE, CONF_SEQUENCE as CONF_SEQUENCE, CONF_SERVICE as CONF_SERVICE, CONF_TARGET as CONF_TARGET, CONF_TIMEOUT as CONF_TIMEOUT, CONF_UNTIL as CONF_UNTIL, CONF_VARIABLES as CONF_VARIABLES, CONF_WAIT_FOR_TRIGGER as CONF_WAIT_FOR_TRIGGER, CONF_WAIT_TEMPLATE as CONF_WAIT_TEMPLATE, CONF_WHILE as CONF_WHILE, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, SERVICE_TURN_ON as SERVICE_TURN_ON
from homeassistant.core import Context as Context, HassJob as HassJob, HomeAssistant as HomeAssistant, SERVICE_CALL_LIMIT as SERVICE_CALL_LIMIT, callback as callback
from homeassistant.helpers import condition as condition, service as service, template as template
from homeassistant.helpers.condition import trace_condition_function as trace_condition_function
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect, async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.event import async_call_later as async_call_later, async_track_template as async_track_template
from homeassistant.helpers.script_variables import ScriptVariables as ScriptVariables
from homeassistant.helpers.trace import script_execution_set as script_execution_set
from homeassistant.helpers.trigger import async_initialize_triggers as async_initialize_triggers, async_validate_trigger_config as async_validate_trigger_config
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util import slugify as slugify
from homeassistant.util.dt import utcnow as utcnow
from types import MappingProxyType
from typing import Any, Callable, Dict, Optional, Sequence, Union

SCRIPT_MODE_PARALLEL: str
SCRIPT_MODE_QUEUED: str
SCRIPT_MODE_RESTART: str
SCRIPT_MODE_SINGLE: str
SCRIPT_MODE_CHOICES: Any
DEFAULT_SCRIPT_MODE = SCRIPT_MODE_SINGLE
CONF_MAX: str
DEFAULT_MAX: int
CONF_MAX_EXCEEDED: str
_MAX_EXCEEDED_CHOICES: Any
DEFAULT_MAX_EXCEEDED: str
ATTR_CUR: str
ATTR_MAX: str
DATA_SCRIPTS: str
DATA_SCRIPT_BREAKPOINTS: str
RUN_ID_ANY: str
NODE_ANY: str
_LOGGER: Any
_LOG_EXCEPTION: Any
_TIMEOUT_MSG: str
_SHUTDOWN_MAX_WAIT: int
ACTION_TRACE_NODE_MAX_LEN: int
SCRIPT_BREAKPOINT_HIT: str
SCRIPT_DEBUG_CONTINUE_STOP: str
SCRIPT_DEBUG_CONTINUE_ALL: str

def action_trace_append(variables: Any, path: Any): ...
async def trace_action(hass: Any, script_run: Any, stop: Any, variables: Any) -> None: ...
def make_script_schema(schema: Any, default_script_mode: Any, extra: Any = ...): ...

STATIC_VALIDATION_ACTION_TYPES: Any

async def async_validate_actions_config(hass: HomeAssistant, actions: list[ConfigType]) -> list[ConfigType]: ...
async def async_validate_action_config(hass: HomeAssistant, config: ConfigType) -> ConfigType: ...

class _StopScript(Exception): ...

class _ScriptRun:
    _hass: Any = ...
    _script: Any = ...
    _variables: Any = ...
    _context: Any = ...
    _log_exceptions: Any = ...
    _step: int = ...
    _action: Any = ...
    _stop: Any = ...
    _stopped: Any = ...
    def __init__(self, hass: HomeAssistant, script: Script, variables: dict[str, Any], context: Union[Context, None], log_exceptions: bool) -> None: ...
    def _changed(self) -> None: ...
    async def _async_get_condition(self, config: Any): ...
    def _log(self, msg: str, *args: Any, level: int=..., **kwargs: Any) -> None: ...
    def _step_log(self, default_message: Any, timeout: Optional[Any] = ...) -> None: ...
    async def async_run(self) -> None: ...
    async def _async_step(self, log_exceptions: Any) -> None: ...
    def _finish(self) -> None: ...
    async def async_stop(self) -> None: ...
    def _log_exception(self, exception: Any) -> None: ...
    def _get_pos_time_period_template(self, key: Any): ...
    async def _async_delay_step(self) -> None: ...
    async def _async_wait_template_step(self) -> None: ...
    async def _async_run_long_action(self, long_task: Any) -> None: ...
    async def _async_call_service_step(self) -> None: ...
    async def _async_device_step(self) -> None: ...
    async def _async_scene_step(self) -> None: ...
    async def _async_event_step(self) -> None: ...
    async def _async_condition_step(self) -> None: ...
    def _test_conditions(self, conditions: Any, name: Any, condition_path: Optional[Any] = ...): ...
    async def _async_repeat_step(self) -> None: ...
    async def _async_choose_step(self) -> None: ...
    async def _async_wait_for_trigger_step(self) -> None: ...
    async def _async_variables_step(self) -> None: ...
    async def _async_run_script(self, script: Any) -> None: ...

class _QueuedScriptRun(_ScriptRun):
    lock_acquired: bool = ...
    async def async_run(self) -> None: ...
    def _finish(self) -> None: ...

async def _async_stop_scripts_after_shutdown(hass: Any, point_in_time: Any) -> None: ...
async def _async_stop_scripts_at_shutdown(hass: Any, event: Any) -> None: ...
_VarsType = Union[Dict[str, Any], MappingProxyType]

def _referenced_extract_ids(data: dict[str, Any], key: str, found: set[str]) -> None: ...

class Script:
    _top_level: Any = ...
    _hass: Any = ...
    sequence: Any = ...
    name: Any = ...
    domain: Any = ...
    running_description: Any = ...
    _change_listener: Any = ...
    _change_listener_job: Any = ...
    script_mode: Any = ...
    _log_exceptions: Any = ...
    last_action: Any = ...
    last_triggered: Any = ...
    _runs: Any = ...
    max_runs: Any = ...
    _max_exceeded: Any = ...
    _queue_lck: Any = ...
    _config_cache: Any = ...
    _repeat_script: Any = ...
    _choose_data: Any = ...
    _referenced_entities: Any = ...
    _referenced_devices: Any = ...
    _referenced_areas: Any = ...
    variables: Any = ...
    _variables_dynamic: Any = ...
    def __init__(self, hass: HomeAssistant, sequence: Sequence[dict[str, Any]], name: str, domain: str, *, running_description: Union[str, None]=..., change_listener: Union[Callable[..., Any], None]=..., script_mode: str=..., max_runs: int=..., max_exceeded: str=..., logger: Union[logging.Logger, None]=..., log_exceptions: bool=..., top_level: bool=..., variables: Union[ScriptVariables, None]=...) -> None: ...
    @property
    def change_listener(self) -> Union[Callable[..., Any], None]: ...
    @change_listener.setter
    def change_listener(self, change_listener: Callable[..., Any]) -> None: ...
    _logger: Any = ...
    def _set_logger(self, logger: Union[logging.Logger, None]=...) -> None: ...
    def update_logger(self, logger: Union[logging.Logger, None]=...) -> None: ...
    def _changed(self) -> None: ...
    def _chain_change_listener(self, sub_script: Any) -> None: ...
    @property
    def is_running(self) -> bool: ...
    @property
    def runs(self) -> int: ...
    @property
    def supports_max(self) -> bool: ...
    @property
    def referenced_areas(self): ...
    @property
    def referenced_devices(self): ...
    @property
    def referenced_entities(self): ...
    def run(self, variables: Union[_VarsType, None]=..., context: Union[Context, None]=...) -> None: ...
    async def async_run(self, run_variables: Union[_VarsType, None]=..., context: Union[Context, None]=..., started_action: Union[Callable[..., Any], None]=...) -> None: ...
    async def _async_stop(self, update_state: Any, spare: Optional[Any] = ...) -> None: ...
    async def async_stop(self, update_state: bool=..., spare: Union[_ScriptRun, None]=...) -> None: ...
    async def _async_get_condition(self, config: Any): ...
    def _prep_repeat_script(self, step: Any): ...
    def _get_repeat_script(self, step: Any): ...
    async def _async_prep_choose_data(self, step: Any): ...
    async def _async_get_choose_data(self, step: Any): ...
    def _log(self, msg: str, *args: Any, level: int=..., **kwargs: Any) -> None: ...

def breakpoint_clear(hass: Any, key: Any, run_id: Any, node: Any) -> None: ...
def breakpoint_clear_all(hass: Any) -> None: ...
def breakpoint_set(hass: Any, key: Any, run_id: Any, node: Any) -> None: ...
def breakpoint_list(hass: Any): ...
def debug_continue(hass: Any, key: Any, run_id: Any) -> None: ...
def debug_step(hass: Any, key: Any, run_id: Any) -> None: ...
def debug_stop(hass: Any, key: Any, run_id: Any) -> None: ...
