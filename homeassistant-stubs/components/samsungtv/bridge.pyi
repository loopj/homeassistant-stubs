import abc
from .const import CONF_DESCRIPTION as CONF_DESCRIPTION, LEGACY_PORT as LEGACY_PORT, LOGGER as LOGGER, METHOD_LEGACY as METHOD_LEGACY, METHOD_WEBSOCKET as METHOD_WEBSOCKET, RESULT_AUTH_MISSING as RESULT_AUTH_MISSING, RESULT_CANNOT_CONNECT as RESULT_CANNOT_CONNECT, RESULT_NOT_SUPPORTED as RESULT_NOT_SUPPORTED, RESULT_SUCCESS as RESULT_SUCCESS, TIMEOUT_REQUEST as TIMEOUT_REQUEST, TIMEOUT_WEBSOCKET as TIMEOUT_WEBSOCKET, VALUE_CONF_ID as VALUE_CONF_ID, VALUE_CONF_NAME as VALUE_CONF_NAME, WEBSOCKET_PORTS as WEBSOCKET_PORTS
from abc import ABC, abstractmethod
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_ID as CONF_ID, CONF_METHOD as CONF_METHOD, CONF_NAME as CONF_NAME, CONF_PORT as CONF_PORT, CONF_TIMEOUT as CONF_TIMEOUT, CONF_TOKEN as CONF_TOKEN
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import format_mac as format_mac
from samsungctl import Remote
from typing import Any

def mac_from_device_info(info: dict[str, Any]) -> Union[str, None]: ...
async def async_get_device_info(hass: HomeAssistant, bridge: Union[SamsungTVWSBridge, SamsungTVLegacyBridge, None], host: str) -> tuple[Union[int, None], Union[str, None], Union[dict[str, Any], None]]: ...
def _get_device_info(bridge: Union[SamsungTVWSBridge, SamsungTVLegacyBridge], host: str) -> tuple[Union[int, None], Union[str, None], Union[dict[str, Any], None]]: ...

class SamsungTVBridge(ABC, metaclass=abc.ABCMeta):
    @staticmethod
    def get_bridge(method: str, host: str, port: Union[int, None] = ..., token: Union[str, None] = ...) -> Union[SamsungTVLegacyBridge, SamsungTVWSBridge]: ...
    port: Any
    method: Any
    host: Any
    token: Any
    _remote: Any
    _reauth_callback: Any
    _new_token_callback: Any
    def __init__(self, method: str, host: str, port: Union[int, None] = ...) -> None: ...
    def register_reauth_callback(self, func: CALLBACK_TYPE) -> None: ...
    def register_new_token_callback(self, func: CALLBACK_TYPE) -> None: ...
    @abstractmethod
    def try_connect(self) -> Union[str, None]: ...
    @abstractmethod
    def device_info(self) -> Union[dict[str, Any], None]: ...
    @abstractmethod
    def mac_from_device(self) -> Union[str, None]: ...
    def is_on(self) -> bool: ...
    def send_key(self, key: str) -> None: ...
    @abstractmethod
    def _send_key(self, key: str) -> None: ...
    @abstractmethod
    def _get_remote(self, avoid_open: bool = ...) -> Remote: ...
    def close_remote(self) -> None: ...
    def _notify_reauth_callback(self) -> None: ...
    def _notify_new_token_callback(self) -> None: ...

class SamsungTVLegacyBridge(SamsungTVBridge):
    config: Any
    def __init__(self, method: str, host: str, port: Union[int, None]) -> None: ...
    def mac_from_device(self) -> None: ...
    def try_connect(self) -> str: ...
    def device_info(self) -> None: ...
    _remote: Any
    def _get_remote(self, avoid_open: bool = ...) -> Remote: ...
    def _send_key(self, key: str) -> None: ...
    def stop(self) -> None: ...

class SamsungTVWSBridge(SamsungTVBridge):
    token: Any
    def __init__(self, method: str, host: str, port: Union[int, None] = ..., token: Union[str, None] = ...) -> None: ...
    def mac_from_device(self) -> Union[str, None]: ...
    def try_connect(self) -> str: ...
    def device_info(self) -> Union[dict[str, Any], None]: ...
    def _send_key(self, key: str) -> None: ...
    _remote: Any
    def _get_remote(self, avoid_open: bool = ...) -> Remote: ...
    def stop(self) -> None: ...
