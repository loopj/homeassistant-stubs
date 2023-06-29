import aiohttp
import asyncio
from . import alexa_config as alexa_config, google_config as google_config
from .const import DISPATCHER_REMOTE_UPDATE as DISPATCHER_REMOTE_UPDATE, DOMAIN as DOMAIN
from .prefs import CloudPreferences as CloudPreferences
from _typeshed import Incomplete
from hass_nabucasa.client import CloudClient as Interface
from homeassistant.components import google_assistant as google_assistant, persistent_notification as persistent_notification, webhook as webhook
from homeassistant.core import Context as Context, HassJob as HassJob, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.event import async_call_later as async_call_later
from homeassistant.util.aiohttp import MockRequest as MockRequest, serialize_response as serialize_response
from pathlib import Path
from typing import Any

class CloudClient(Interface):
    _hass: Incomplete
    _prefs: Incomplete
    _websession: Incomplete
    google_user_config: Incomplete
    alexa_user_config: Incomplete
    _alexa_config: Incomplete
    _google_config: Incomplete
    _alexa_config_init_lock: Incomplete
    _google_config_init_lock: Incomplete
    _relayer_region: Incomplete
    def __init__(self, hass: HomeAssistant, prefs: CloudPreferences, websession: aiohttp.ClientSession, alexa_user_config: dict[str, Any], google_user_config: dict[str, Any]) -> None: ...
    @property
    def base_path(self) -> Path: ...
    @property
    def prefs(self) -> CloudPreferences: ...
    @property
    def loop(self) -> asyncio.AbstractEventLoop: ...
    @property
    def websession(self) -> aiohttp.ClientSession: ...
    @property
    def aiohttp_runner(self) -> aiohttp.web.AppRunner | None: ...
    @property
    def cloudhooks(self) -> dict[str, dict[str, str | bool]]: ...
    @property
    def remote_autostart(self) -> bool: ...
    @property
    def relayer_region(self) -> str | None: ...
    async def get_alexa_config(self) -> alexa_config.CloudAlexaConfig: ...
    async def get_google_config(self) -> google_config.CloudGoogleConfig: ...
    async def cloud_connected(self) -> None: ...
    async def cloud_disconnected(self) -> None: ...
    async def cloud_started(self) -> None: ...
    async def cloud_stopped(self) -> None: ...
    async def logout_cleanups(self) -> None: ...
    def user_message(self, identifier: str, title: str, message: str) -> None: ...
    def dispatcher_message(self, identifier: str, data: Any = ...) -> None: ...
    async def async_cloud_connect_update(self, connect: bool) -> None: ...
    async def async_cloud_connection_info(self, payload: dict[str, Any]) -> dict[str, Any]: ...
    async def async_alexa_message(self, payload: dict[Any, Any]) -> dict[Any, Any]: ...
    async def async_google_message(self, payload: dict[Any, Any]) -> dict[Any, Any]: ...
    async def async_webhook_message(self, payload: dict[Any, Any]) -> dict[Any, Any]: ...
    async def async_system_message(self, payload: dict[Any, Any] | None) -> None: ...
    async def async_cloudhooks_update(self, data: dict[str, dict[str, str | bool]]) -> None: ...
