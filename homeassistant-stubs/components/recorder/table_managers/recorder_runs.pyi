from ..db_schema import RecorderRuns as RecorderRuns
from ..models import process_timestamp as process_timestamp
from _typeshed import Incomplete
from datetime import datetime
from sqlalchemy.orm.session import Session as Session

def _find_recorder_run_for_start_time(run_history: _RecorderRunsHistory, start: datetime) -> RecorderRuns | None: ...

class _RecorderRunsHistory:
    run_timestamps: list[int]
    runs_by_timestamp: dict[int, RecorderRuns]
    def __init__(self, run_timestamps, runs_by_timestamp) -> None: ...
    def __mypy-replace(*, run_timestamps, runs_by_timestamp) -> None: ...

class RecorderRunsManager:
    _recording_start: Incomplete
    _current_run_info: Incomplete
    _run_history: Incomplete
    def __init__(self) -> None: ...
    @property
    def recording_start(self) -> datetime: ...
    @property
    def first(self) -> RecorderRuns: ...
    @property
    def current(self) -> RecorderRuns: ...
    @property
    def active(self) -> bool: ...
    def get(self, start: datetime) -> RecorderRuns | None: ...
    def start(self, session: Session) -> None: ...
    def reset(self) -> None: ...
    def end(self, session: Session) -> None: ...
    def load_from_db(self, session: Session) -> None: ...
    def clear(self) -> None: ...
