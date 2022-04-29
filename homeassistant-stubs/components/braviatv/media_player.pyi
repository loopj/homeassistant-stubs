from . import BraviaTVCoordinator as BraviaTVCoordinator
from .const import ATTR_MANUFACTURER as ATTR_MANUFACTURER, DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.media_player import MediaPlayerDeviceClass as MediaPlayerDeviceClass, MediaPlayerEntity as MediaPlayerEntity, MediaPlayerEntityFeature as MediaPlayerEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import STATE_OFF as STATE_OFF, STATE_PAUSED as STATE_PAUSED, STATE_PLAYING as STATE_PLAYING
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BraviaTVMediaPlayer(CoordinatorEntity[BraviaTVCoordinator], MediaPlayerEntity):
    _attr_device_class: Incomplete
    _attr_supported_features: Incomplete
    _attr_device_info: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: BraviaTVCoordinator, name: str, unique_id: str, device_info: DeviceInfo) -> None: ...
    @property
    def state(self) -> Union[str, None]: ...
    @property
    def source(self) -> Union[str, None]: ...
    @property
    def source_list(self) -> list[str]: ...
    @property
    def volume_level(self) -> Union[float, None]: ...
    @property
    def is_volume_muted(self) -> bool: ...
    @property
    def media_title(self) -> Union[str, None]: ...
    @property
    def media_content_id(self) -> Union[str, None]: ...
    @property
    def media_duration(self) -> Union[int, None]: ...
    async def async_turn_on(self) -> None: ...
    async def async_turn_off(self) -> None: ...
    async def async_set_volume_level(self, volume: float) -> None: ...
    async def async_volume_up(self) -> None: ...
    async def async_volume_down(self) -> None: ...
    async def async_mute_volume(self, mute: bool) -> None: ...
    async def async_select_source(self, source: str) -> None: ...
    async def async_media_play(self) -> None: ...
    async def async_media_pause(self) -> None: ...
    async def async_media_stop(self) -> None: ...
    async def async_media_next_track(self) -> None: ...
    async def async_media_previous_track(self) -> None: ...
