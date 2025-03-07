import logging
from . import BluetoothChange as BluetoothChange, BluetoothScanningMode as BluetoothScanningMode, BluetoothServiceInfoBleak as BluetoothServiceInfoBleak
from .passive_update_coordinator import PassiveBluetoothDataUpdateCoordinator as PassiveBluetoothDataUpdateCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.debounce import Debouncer as Debouncer
from homeassistant.util.dt import monotonic_time_coarse as monotonic_time_coarse
from typing import Any, Generic, TypeVar

POLL_DEFAULT_COOLDOWN: int
POLL_DEFAULT_IMMEDIATE: bool
_T = TypeVar('_T')

class ActiveBluetoothDataUpdateCoordinator(PassiveBluetoothDataUpdateCoordinator, Generic[_T]):
    data: Incomplete
    _needs_poll_method: Incomplete
    _poll_method: Incomplete
    _last_poll: Incomplete
    last_poll_successful: bool
    _last_service_info: Incomplete
    _debounced_poll: Incomplete
    def __init__(self, hass: HomeAssistant, logger: logging.Logger, *, address: str, mode: BluetoothScanningMode, needs_poll_method: Callable[[BluetoothServiceInfoBleak, float | None], bool], poll_method: Callable[[BluetoothServiceInfoBleak], Coroutine[Any, Any, _T]] | None = ..., poll_debouncer: Debouncer[Coroutine[Any, Any, None]] | None = ..., connectable: bool = ...) -> None: ...
    def needs_poll(self, service_info: BluetoothServiceInfoBleak) -> bool: ...
    async def _async_poll_data(self, last_service_info: BluetoothServiceInfoBleak) -> _T: ...
    async def _async_poll(self) -> None: ...
    def _async_handle_bluetooth_poll(self) -> None: ...
    def _async_handle_bluetooth_event(self, service_info: BluetoothServiceInfoBleak, change: BluetoothChange) -> None: ...
    def _async_stop(self) -> None: ...
