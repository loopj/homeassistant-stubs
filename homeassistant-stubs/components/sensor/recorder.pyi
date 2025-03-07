import datetime
from .const import ATTR_LAST_RESET as ATTR_LAST_RESET, ATTR_OPTIONS as ATTR_OPTIONS, ATTR_STATE_CLASS as ATTR_STATE_CLASS, DOMAIN as DOMAIN, SensorStateClass as SensorStateClass
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Iterable
from homeassistant.components.recorder import get_instance as get_instance, history as history, statistics as statistics
from homeassistant.components.recorder.models import StatisticData as StatisticData, StatisticMetaData as StatisticMetaData, StatisticResult as StatisticResult
from homeassistant.const import ATTR_UNIT_OF_MEASUREMENT as ATTR_UNIT_OF_MEASUREMENT, REVOLUTIONS_PER_MINUTE as REVOLUTIONS_PER_MINUTE, UnitOfIrradiance as UnitOfIrradiance, UnitOfSoundPressure as UnitOfSoundPressure, UnitOfVolume as UnitOfVolume
from homeassistant.core import HomeAssistant as HomeAssistant, State as State, callback as callback, split_entity_id as split_entity_id
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity import entity_sources as entity_sources
from homeassistant.util.enum import try_parse_enum as try_parse_enum
from sqlalchemy.orm.session import Session as Session
from typing import Any

_LOGGER: Incomplete
DEFAULT_STATISTICS: Incomplete
EQUIVALENT_UNITS: Incomplete
SEEN_DIP: str
WARN_DIP: str
WARN_NEGATIVE: str
WARN_UNSUPPORTED_UNIT: str
WARN_UNSTABLE_UNIT: str
LINK_DEV_STATISTICS: str

def _get_sensor_states(hass: HomeAssistant) -> list[State]: ...
def _time_weighted_average(fstates: list[tuple[float, State]], start: datetime.datetime, end: datetime.datetime) -> float: ...
def _get_units(fstates: list[tuple[float, State]]) -> set[str | None]: ...
def _equivalent_units(units: set[str | None]) -> bool: ...
def _parse_float(state: str) -> float: ...
def _float_or_none(state: str) -> float | None: ...
def _entity_history_to_float_and_state(entity_history: Iterable[State]) -> list[tuple[float, State]]: ...
def _normalize_states(hass: HomeAssistant, old_metadatas: dict[str, tuple[int, StatisticMetaData]], fstates: list[tuple[float, State]], entity_id: str) -> tuple[str | None, list[tuple[float, State]]]: ...
def _suggest_report_issue(hass: HomeAssistant, entity_id: str) -> str: ...
def warn_dip(hass: HomeAssistant, entity_id: str, state: State, previous_fstate: float) -> None: ...
def warn_negative(hass: HomeAssistant, entity_id: str, state: State) -> None: ...
def reset_detected(hass: HomeAssistant, entity_id: str, fstate: float, previous_fstate: float | None, state: State) -> bool: ...
def _wanted_statistics(sensor_states: list[State]) -> dict[str, set[str]]: ...
def _last_reset_as_utc_isoformat(last_reset_s: Any, entity_id: str) -> str | None: ...
def _timestamp_to_isoformat_or_none(timestamp: float | None) -> str | None: ...
def compile_statistics(hass: HomeAssistant, start: datetime.datetime, end: datetime.datetime) -> statistics.PlatformCompiledStatistics: ...
def _compile_statistics(hass: HomeAssistant, session: Session, start: datetime.datetime, end: datetime.datetime) -> statistics.PlatformCompiledStatistics: ...
def list_statistic_ids(hass: HomeAssistant, statistic_ids: list[str] | tuple[str] | None = ..., statistic_type: str | None = ...) -> dict: ...
def validate_statistics(hass: HomeAssistant) -> dict[str, list[statistics.ValidationIssue]]: ...
def exclude_attributes(hass: HomeAssistant) -> set[str]: ...
