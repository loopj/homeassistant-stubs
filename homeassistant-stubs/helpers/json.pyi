import json
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from functools import partial as partial
from homeassistant.util.file import write_utf8_file as write_utf8_file, write_utf8_file_atomic as write_utf8_file_atomic
from homeassistant.util.json import JSON_DECODE_EXCEPTIONS as JSON_DECODE_EXCEPTIONS, JSON_ENCODE_EXCEPTIONS as JSON_ENCODE_EXCEPTIONS, SerializationError as SerializationError, format_unserializable_data as format_unserializable_data, json_loads as json_loads
from typing import Any, Final

_LOGGER: Incomplete

class JSONEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any: ...

def json_encoder_default(obj: Any) -> Any: ...
def json_bytes(obj: Any) -> bytes: ...

class ExtendedJSONEncoder(JSONEncoder):
    def default(self, o: Any) -> Any: ...

def _strip_null(obj: Any) -> Any: ...
def json_bytes_strip_null(data: Any) -> bytes: ...
def json_dumps(data: Any) -> str: ...
def json_dumps_sorted(data: Any) -> str: ...

JSON_DUMP: Final[Incomplete]

def _orjson_default_encoder(data: Any) -> str: ...
def save_json(filename: str, data: list | dict, private: bool = ..., *, encoder: type[json.JSONEncoder] | None = ..., atomic_writes: bool = ...) -> None: ...
def find_paths_unserializable_data(bad_data: Any, *, dump: Callable[[Any], str] = ...) -> dict[str, Any]: ...
