import threading
from .const import DB_WORKER_PREFIX as DB_WORKER_PREFIX
from _typeshed import Incomplete
from homeassistant.helpers.frame import report as report
from sqlalchemy.pool import NullPool, SingletonThreadPool, StaticPool
from typing import Any

_LOGGER: Incomplete
DEBUG_MUTEX_POOL: bool
DEBUG_MUTEX_POOL_TRACE: bool
POOL_SIZE: int

class RecorderPool(SingletonThreadPool, NullPool):
    def __init__(self, *args: Any, **kw: Any) -> None: ...
    @property
    def recorder_or_dbworker(self) -> bool: ...
    def _do_return_conn(self, conn: Any) -> Any: ...
    def shutdown(self) -> None: ...
    def dispose(self) -> None: ...
    def _do_get(self) -> Any: ...

class MutexPool(StaticPool):
    _reference_counter: int
    pool_lock: threading.RLock
    def _do_return_conn(self, conn: Any) -> None: ...
    def _do_get(self) -> Any: ...
