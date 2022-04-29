from .bridge import SamsungTVBridge as SamsungTVBridge, SamsungTVWSBridge as SamsungTVWSBridge
from .const import CONF_MANUFACTURER as CONF_MANUFACTURER, CONF_ON_ACTION as CONF_ON_ACTION, CONF_SSDP_RENDERING_CONTROL_LOCATION as CONF_SSDP_RENDERING_CONTROL_LOCATION, DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from async_upnp_client.client import UpnpDevice as UpnpDevice, UpnpService as UpnpService, UpnpStateVariable as UpnpStateVariable
from collections.abc import Sequence
from homeassistant.components.media_player import MediaPlayerDeviceClass as MediaPlayerDeviceClass, MediaPlayerEntity as MediaPlayerEntity, MediaPlayerEntityFeature as MediaPlayerEntityFeature
from homeassistant.components.media_player.const import MEDIA_TYPE_APP as MEDIA_TYPE_APP, MEDIA_TYPE_CHANNEL as MEDIA_TYPE_CHANNEL
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_REAUTH as SOURCE_REAUTH
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_MAC as CONF_MAC, CONF_MODEL as CONF_MODEL, CONF_NAME as CONF_NAME, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import entity_component as entity_component
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.script import Script as Script
from typing import Any

SOURCES: Incomplete
SUPPORT_SAMSUNGTV: Incomplete
SCAN_INTERVAL_PLUS_OFF_TIME: Incomplete
APP_LIST_DELAY: int

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SamsungTVDevice(MediaPlayerEntity):
    _attr_source_list: list[str]
    _config_entry: Incomplete
    _host: Incomplete
    _mac: Incomplete
    _ssdp_rendering_control_location: Incomplete
    _on_script: Incomplete
    _playing: bool
    _attr_name: Incomplete
    _attr_state: Incomplete
    _attr_unique_id: Incomplete
    _attr_is_volume_muted: bool
    _attr_device_class: Incomplete
    _app_list: Incomplete
    _app_list_event: Incomplete
    _attr_supported_features: Incomplete
    _attr_device_info: Incomplete
    _end_of_power_off: Incomplete
    _bridge: Incomplete
    _auth_failed: bool
    _dmr_device: Incomplete
    _upnp_server: Incomplete
    def __init__(self, bridge: SamsungTVBridge, config_entry: ConfigEntry, on_script: Union[Script, None]) -> None: ...
    def _update_sources(self) -> None: ...
    def _app_list_callback(self, app_list: dict[str, str]) -> None: ...
    def access_denied(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    async def async_update(self) -> None: ...
    _attr_volume_level: Incomplete
    def _update_from_upnp(self) -> bool: ...
    async def _async_startup_app_list(self) -> None: ...
    async def _async_startup_dmr(self) -> None: ...
    async def _async_resubscribe_dmr(self) -> None: ...
    async def _async_shutdown_dmr(self) -> None: ...
    def _on_upnp_event(self, service: UpnpService, state_variables: Sequence[UpnpStateVariable]) -> None: ...
    async def _async_launch_app(self, app_id: str) -> None: ...
    async def _async_send_keys(self, keys: list[str]) -> None: ...
    def _power_off_in_progress(self) -> bool: ...
    @property
    def available(self) -> bool: ...
    async def async_turn_off(self) -> None: ...
    async def async_set_volume_level(self, volume: float) -> None: ...
    async def async_volume_up(self) -> None: ...
    async def async_volume_down(self) -> None: ...
    async def async_mute_volume(self, mute: bool) -> None: ...
    async def async_media_play_pause(self) -> None: ...
    async def async_media_play(self) -> None: ...
    async def async_media_pause(self) -> None: ...
    async def async_media_next_track(self) -> None: ...
    async def async_media_previous_track(self) -> None: ...
    async def async_play_media(self, media_type: str, media_id: str, **kwargs: Any) -> None: ...
    def _wake_on_lan(self) -> None: ...
    async def async_turn_on(self) -> None: ...
    async def async_select_source(self, source: str) -> None: ...
