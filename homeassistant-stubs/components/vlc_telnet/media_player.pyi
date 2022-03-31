from .const import DATA_AVAILABLE as DATA_AVAILABLE, DATA_VLC as DATA_VLC, DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN, LOGGER as LOGGER
from aiovlc.client import Client as Client
from collections.abc import Awaitable as Awaitable, Callable as Callable, Coroutine
from datetime import datetime
from homeassistant.components import media_source as media_source
from homeassistant.components.media_player import BrowseMedia as BrowseMedia, MediaPlayerEntity as MediaPlayerEntity, async_process_play_media_url as async_process_play_media_url
from homeassistant.components.media_player.const import MEDIA_TYPE_MUSIC as MEDIA_TYPE_MUSIC, SUPPORT_BROWSE_MEDIA as SUPPORT_BROWSE_MEDIA, SUPPORT_CLEAR_PLAYLIST as SUPPORT_CLEAR_PLAYLIST, SUPPORT_NEXT_TRACK as SUPPORT_NEXT_TRACK, SUPPORT_PAUSE as SUPPORT_PAUSE, SUPPORT_PLAY as SUPPORT_PLAY, SUPPORT_PLAY_MEDIA as SUPPORT_PLAY_MEDIA, SUPPORT_PREVIOUS_TRACK as SUPPORT_PREVIOUS_TRACK, SUPPORT_SEEK as SUPPORT_SEEK, SUPPORT_SHUFFLE_SET as SUPPORT_SHUFFLE_SET, SUPPORT_STOP as SUPPORT_STOP, SUPPORT_VOLUME_MUTE as SUPPORT_VOLUME_MUTE, SUPPORT_VOLUME_SET as SUPPORT_VOLUME_SET
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_HASSIO as SOURCE_HASSIO
from homeassistant.const import CONF_NAME as CONF_NAME, STATE_IDLE as STATE_IDLE, STATE_PAUSED as STATE_PAUSED, STATE_PLAYING as STATE_PLAYING
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any, TypeVar
from typing_extensions import Concatenate as Concatenate

MAX_VOLUME: int
SUPPORT_VLC: Any
_T = TypeVar('_T', bound='VlcDevice')
_P: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def catch_vlc_errors(func: Callable[Concatenate[_T, _P], Awaitable[None]]) -> Callable[Concatenate[_T, _P], Coroutine[Any, Any, None]]: ...

class VlcDevice(MediaPlayerEntity):
    _config_entry: Any
    _name: Any
    _volume: Any
    _muted: Any
    _state: Any
    _media_position_updated_at: Any
    _media_position: Any
    _media_duration: Any
    _vlc: Any
    _available: Any
    _volume_bkp: float
    _media_artist: Any
    _media_title: Any
    _attr_unique_id: Any
    _attr_device_info: Any
    _using_addon: Any
    def __init__(self, config_entry: ConfigEntry, vlc: Client, name: str, available: bool) -> None: ...
    async def async_update(self) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def state(self) -> Union[str, None]: ...
    @property
    def available(self) -> bool: ...
    @property
    def volume_level(self) -> Union[float, None]: ...
    @property
    def is_volume_muted(self) -> Union[bool, None]: ...
    @property
    def supported_features(self) -> int: ...
    @property
    def media_content_type(self) -> str: ...
    @property
    def media_duration(self) -> Union[int, None]: ...
    @property
    def media_position(self) -> Union[int, None]: ...
    @property
    def media_position_updated_at(self) -> Union[datetime, None]: ...
    @property
    def media_title(self) -> Union[str, None]: ...
    @property
    def media_artist(self) -> Union[str, None]: ...
    async def async_media_seek(self, position: float) -> None: ...
    async def async_mute_volume(self, mute: bool) -> None: ...
    async def async_set_volume_level(self, volume: float) -> None: ...
    async def async_media_play(self) -> None: ...
    async def async_media_pause(self) -> None: ...
    async def async_media_stop(self) -> None: ...
    async def async_play_media(self, media_type: str, media_id: str, **kwargs: Any) -> None: ...
    async def async_media_previous_track(self) -> None: ...
    async def async_media_next_track(self) -> None: ...
    async def async_clear_playlist(self) -> None: ...
    async def async_set_shuffle(self, shuffle: bool) -> None: ...
    async def async_browse_media(self, media_content_type: Union[str, None] = ..., media_content_id: Union[str, None] = ...) -> BrowseMedia: ...
