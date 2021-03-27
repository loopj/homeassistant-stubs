from .core import Context as Context
from typing import Any, Generator, Optional, Sequence

class HomeAssistantError(Exception): ...
class InvalidEntityFormatError(HomeAssistantError): ...
class NoEntitySpecifiedError(HomeAssistantError): ...

class TemplateError(HomeAssistantError):
    def __init__(self, exception: Exception) -> None: ...

class ConditionError(HomeAssistantError):
    type: str = ...
    def output(self, indent: int) -> Generator: ...
    def __init__(self, type: Any) -> None: ...
    def __lt__(self, other: Any) -> Any: ...
    def __le__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def __ge__(self, other: Any) -> Any: ...

class ConditionErrorMessage(ConditionError):
    message: str = ...
    def output(self, indent: int) -> Generator: ...
    def __init__(self, type: Any, message: Any) -> None: ...
    def __lt__(self, other: Any) -> Any: ...
    def __le__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def __ge__(self, other: Any) -> Any: ...

class ConditionErrorIndex(ConditionError):
    index: int = ...
    total: int = ...
    error: ConditionError = ...
    def output(self, indent: int) -> Generator: ...
    def __init__(self, type: Any, index: Any, total: Any, error: Any) -> None: ...
    def __lt__(self, other: Any) -> Any: ...
    def __le__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def __ge__(self, other: Any) -> Any: ...

class ConditionErrorContainer(ConditionError):
    errors: Sequence[ConditionError] = ...
    def output(self, indent: int) -> Generator: ...
    def __init__(self, type: Any, errors: Any) -> None: ...
    def __lt__(self, other: Any) -> Any: ...
    def __le__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def __ge__(self, other: Any) -> Any: ...

class PlatformNotReady(HomeAssistantError): ...
class ConfigEntryNotReady(HomeAssistantError): ...
class InvalidStateError(HomeAssistantError): ...

class Unauthorized(HomeAssistantError):
    context: Any = ...
    user_id: Any = ...
    entity_id: Any = ...
    config_entry_id: Any = ...
    perm_category: Any = ...
    permission: Any = ...
    def __init__(self, context: Optional[Context]=..., user_id: Optional[str]=..., entity_id: Optional[str]=..., config_entry_id: Optional[str]=..., perm_category: Optional[str]=..., permission: Optional[str]=...) -> None: ...

class UnknownUser(Unauthorized): ...

class ServiceNotFound(HomeAssistantError):
    domain: Any = ...
    service: Any = ...
    def __init__(self, domain: str, service: str) -> None: ...
