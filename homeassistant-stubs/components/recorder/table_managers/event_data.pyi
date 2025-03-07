from . import BaseLRUTableManager as BaseLRUTableManager
from ..const import SQLITE_MAX_BIND_VARS as SQLITE_MAX_BIND_VARS
from ..core import Recorder as Recorder
from ..db_schema import EventData as EventData
from ..queries import get_shared_event_datas as get_shared_event_datas
from ..util import chunked as chunked, execute_stmt_lambda_element as execute_stmt_lambda_element
from _typeshed import Incomplete
from collections.abc import Iterable
from homeassistant.core import Event as Event
from homeassistant.util.json import JSON_ENCODE_EXCEPTIONS as JSON_ENCODE_EXCEPTIONS
from sqlalchemy.orm.session import Session as Session

CACHE_SIZE: int
_LOGGER: Incomplete

class EventDataManager(BaseLRUTableManager[EventData]):
    active: bool
    def __init__(self, recorder: Recorder) -> None: ...
    def serialize_from_event(self, event: Event) -> bytes | None: ...
    def load(self, events: list[Event], session: Session) -> None: ...
    def get(self, shared_data: str, data_hash: int, session: Session) -> int | None: ...
    def get_many(self, shared_data_data_hashs: Iterable[tuple[str, int]], session: Session) -> dict[str, int | None]: ...
    def _load_from_hashes(self, hashes: Iterable[int], session: Session) -> dict[str, int | None]: ...
    def add_pending(self, db_event_data: EventData) -> None: ...
    def post_commit_pending(self) -> None: ...
    def evict_purged(self, data_ids: set[int]) -> None: ...
