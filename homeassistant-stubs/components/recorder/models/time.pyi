from _typeshed import Incomplete
from datetime import datetime
from typing import overload

_LOGGER: Incomplete
DB_TIMEZONE: str
EMPTY_JSON_OBJECT: str


@overload
def process_timestamp(ts: None) -> None: ...
@overload
def process_timestamp(ts: datetime) -> datetime: ...
@overload
def process_timestamp_to_utc_isoformat(ts: None) -> None: ...
@overload
def process_timestamp_to_utc_isoformat(ts: datetime) -> str: ...
def process_datetime_to_timestamp(ts: datetime) -> float: ...
def datetime_to_timestamp_or_none(dt: datetime | None) -> float | None: ...
def timestamp_to_datetime_or_none(ts: float | None) -> datetime | None: ...
