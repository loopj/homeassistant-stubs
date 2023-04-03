from .base_scanner import BaseHaScanner as BaseHaScanner, BluetoothScannerDevice as BluetoothScannerDevice
from .const import DATA_MANAGER as DATA_MANAGER
from .manager import BluetoothManager as BluetoothManager
from .match import BluetoothCallbackMatcher as BluetoothCallbackMatcher
from .models import BluetoothCallback as BluetoothCallback, BluetoothChange as BluetoothChange, BluetoothScanningMode as BluetoothScanningMode, ProcessAdvertisementCallback as ProcessAdvertisementCallback
from .wrappers import HaBleakScannerWrapper as HaBleakScannerWrapper
from bleak.backends.device import BLEDevice as BLEDevice
from collections.abc import Callable as Callable, Iterable
from home_assistant_bluetooth import BluetoothServiceInfoBleak as BluetoothServiceInfoBleak
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant

def _get_manager(hass: HomeAssistant) -> BluetoothManager: ...
def async_get_scanner(hass: HomeAssistant) -> HaBleakScannerWrapper: ...
def async_scanner_by_source(hass: HomeAssistant, source: str) -> BaseHaScanner | None: ...
def async_scanner_count(hass: HomeAssistant, connectable: bool = ...) -> int: ...
def async_discovered_service_info(hass: HomeAssistant, connectable: bool = ...) -> Iterable[BluetoothServiceInfoBleak]: ...
def async_last_service_info(hass: HomeAssistant, address: str, connectable: bool = ...) -> BluetoothServiceInfoBleak | None: ...
def async_ble_device_from_address(hass: HomeAssistant, address: str, connectable: bool = ...) -> BLEDevice | None: ...
def async_scanner_devices_by_address(hass: HomeAssistant, address: str, connectable: bool = ...) -> list[BluetoothScannerDevice]: ...
def async_address_present(hass: HomeAssistant, address: str, connectable: bool = ...) -> bool: ...
def async_register_callback(hass: HomeAssistant, callback: BluetoothCallback, match_dict: BluetoothCallbackMatcher | None, mode: BluetoothScanningMode) -> Callable[[], None]: ...
async def async_process_advertisements(hass: HomeAssistant, callback: ProcessAdvertisementCallback, match_dict: BluetoothCallbackMatcher, mode: BluetoothScanningMode, timeout: int) -> BluetoothServiceInfoBleak: ...
def async_track_unavailable(hass: HomeAssistant, callback: Callable[[BluetoothServiceInfoBleak], None], address: str, connectable: bool = ...) -> Callable[[], None]: ...
def async_rediscover_address(hass: HomeAssistant, address: str) -> None: ...
def async_register_scanner(hass: HomeAssistant, scanner: BaseHaScanner, connectable: bool, connection_slots: int | None = ...) -> CALLBACK_TYPE: ...
def async_get_advertisement_callback(hass: HomeAssistant) -> Callable[[BluetoothServiceInfoBleak], None]: ...
