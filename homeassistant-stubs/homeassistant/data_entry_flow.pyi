import abc
import voluptuous as vol
from .core import HomeAssistant as HomeAssistant, callback as callback
from .exceptions import HomeAssistantError as HomeAssistantError
from typing import Any, Dict, List, Optional

RESULT_TYPE_FORM: str
RESULT_TYPE_CREATE_ENTRY: str
RESULT_TYPE_ABORT: str
RESULT_TYPE_EXTERNAL_STEP: str
RESULT_TYPE_EXTERNAL_STEP_DONE: str
RESULT_TYPE_SHOW_PROGRESS: str
RESULT_TYPE_SHOW_PROGRESS_DONE: str
EVENT_DATA_ENTRY_FLOW_PROGRESSED: str

class FlowError(HomeAssistantError): ...
class UnknownHandler(FlowError): ...
class UnknownFlow(FlowError): ...
class UnknownStep(FlowError): ...

class AbortFlow(FlowError):
    reason: Any = ...
    description_placeholders: Any = ...
    def __init__(self, reason: str, description_placeholders: Optional[Dict]=...) -> None: ...

class FlowManager(abc.ABC, metaclass=abc.ABCMeta):
    hass: Any = ...
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def async_wait_init_flow_finish(self, handler: str) -> None: ...
    @abc.abstractmethod
    async def async_create_flow(self, handler_key: Any, *, context: Optional[Dict[str, Any]]=..., data: Optional[Dict[str, Any]]=...) -> FlowHandler: ...
    @abc.abstractmethod
    async def async_finish_flow(self, flow: FlowHandler, result: Dict[str, Any]) -> Dict[str, Any]: ...
    async def async_post_init(self, flow: FlowHandler, result: Dict[str, Any]) -> None: ...
    def async_progress(self) -> List[Dict]: ...
    async def async_init(self, handler: str, *, context: Optional[Dict]=..., data: Any=...) -> Any: ...
    async def async_configure(self, flow_id: str, user_input: Optional[Dict]=...) -> Any: ...
    def async_abort(self, flow_id: str) -> None: ...

class FlowHandler:
    cur_step: Optional[Dict[str, str]] = ...
    flow_id: str = ...
    hass: HomeAssistant = ...
    handler: str = ...
    context: Dict = ...
    init_step: str = ...
    VERSION: int = ...
    @property
    def source(self) -> Optional[str]: ...
    @property
    def show_advanced_options(self) -> bool: ...
    def async_show_form(self, step_id: str, *, data_schema: vol.Schema=..., errors: Optional[Dict]=..., description_placeholders: Optional[Dict]=...) -> Dict[str, Any]: ...
    def async_create_entry(self, title: str, data: Dict, *, description: Optional[str]=..., description_placeholders: Optional[Dict]=...) -> Dict[str, Any]: ...
    def async_abort(self, reason: str, *, description_placeholders: Optional[Dict]=...) -> Dict[str, Any]: ...
    def async_external_step(self, step_id: str, url: str, *, description_placeholders: Optional[Dict]=...) -> Dict[str, Any]: ...
    def async_external_step_done(self, next_step_id: str) -> Dict[str, Any]: ...
    def async_show_progress(self, step_id: str, progress_action: str, *, description_placeholders: Optional[Dict]=...) -> Dict[str, Any]: ...
    def async_show_progress_done(self, next_step_id: str) -> Dict[str, Any]: ...
