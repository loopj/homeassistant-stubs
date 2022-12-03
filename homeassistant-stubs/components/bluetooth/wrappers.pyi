from . import models as models
from .models import HaBluetoothConnector as HaBluetoothConnector
from _typeshed import Incomplete
from bleak import BleakClient
from bleak.backends.client import BaseBleakClient as BaseBleakClient
from bleak.backends.device import BLEDevice
from bleak.backends.scanner import AdvertisementDataCallback as AdvertisementDataCallback, BaseBleakScanner
from collections.abc import Callable as Callable
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE
from homeassistant.helpers.frame import report as report
from typing import Any, Final

FILTER_UUIDS: Final[str]
_LOGGER: Incomplete

class _HaWrappedBleakBackend:
    device: BLEDevice
    client: type[BaseBleakClient]
    def __init__(self, device, client) -> None: ...

class HaBleakScannerWrapper(BaseBleakScanner):
    _detection_cancel: Incomplete
    _mapped_filters: Incomplete
    _advertisement_data_callback: Incomplete
    def __init__(self, *args: Any, detection_callback: Union[AdvertisementDataCallback, None] = ..., service_uuids: Union[list[str], None] = ..., **kwargs: Any) -> None: ...
    @classmethod
    async def discover(cls, timeout: float = ..., **kwargs: Any) -> list[BLEDevice]: ...
    async def stop(self, *args: Any, **kwargs: Any) -> None: ...
    async def start(self, *args: Any, **kwargs: Any) -> None: ...
    def _map_filters(self, *args: Any, **kwargs: Any) -> bool: ...
    def set_scanning_filter(self, *args: Any, **kwargs: Any) -> None: ...
    def _cancel_callback(self) -> None: ...
    @property
    def discovered_devices(self) -> list[BLEDevice]: ...
    def register_detection_callback(self, callback: Union[AdvertisementDataCallback, None]) -> None: ...
    def _setup_detection_callback(self) -> None: ...
    def __del__(self) -> None: ...

class HaBleakClientWrapper(BleakClient):
    __address: Incomplete
    __disconnected_callback: Incomplete
    __timeout: Incomplete
    _backend: Incomplete
    def __init__(self, address_or_ble_device: Union[str, BLEDevice], disconnected_callback: Union[Callable[[BleakClient], None], None] = ..., *args: Any, timeout: float = ..., **kwargs: Any) -> None: ...
    @property
    def is_connected(self) -> bool: ...
    def set_disconnected_callback(self, callback: Union[Callable[[BleakClient], None], None], **kwargs: Any) -> None: ...
    async def connect(self, **kwargs: Any) -> bool: ...
    def _async_get_backend_for_ble_device(self, ble_device: BLEDevice) -> Union[_HaWrappedBleakBackend, None]: ...
    def _async_get_best_available_backend_and_device(self) -> _HaWrappedBleakBackend: ...
    async def disconnect(self) -> bool: ...
