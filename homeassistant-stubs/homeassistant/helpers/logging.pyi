import logging
from typing import Any, Mapping, MutableMapping, Optional, Tuple

class KeywordMessage:
    def __init__(self, fmt: Any, args: Any, kwargs: Mapping[str, Any]) -> None: ...

class KeywordStyleAdapter(logging.LoggerAdapter):
    def __init__(self, logger: logging.Logger, extra: Optional[Mapping[str, Any]]=...) -> None: ...
    def log(self, level: int, msg: Any, *args: Any, **kwargs: Any) -> None: ...
    def process(self, msg: Any, kwargs: MutableMapping[str, Any]) -> Tuple[Any, MutableMapping[str, Any]]: ...
