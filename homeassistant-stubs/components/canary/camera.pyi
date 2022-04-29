from .const import CONF_FFMPEG_ARGUMENTS as CONF_FFMPEG_ARGUMENTS, DATA_COORDINATOR as DATA_COORDINATOR, DEFAULT_FFMPEG_ARGUMENTS as DEFAULT_FFMPEG_ARGUMENTS, DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER
from .coordinator import CanaryDataUpdateCoordinator as CanaryDataUpdateCoordinator
from _typeshed import Incomplete
from aiohttp.web import Request as Request, StreamResponse as StreamResponse
from canary.api import Device as Device, Location as Location
from canary.live_stream_api import LiveStreamSession as LiveStreamSession
from homeassistant.components import ffmpeg as ffmpeg
from homeassistant.components.camera import Camera as Camera
from homeassistant.components.ffmpeg import FFmpegManager as FFmpegManager, get_ffmpeg_manager as get_ffmpeg_manager
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_aiohttp_proxy_stream as async_aiohttp_proxy_stream
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from homeassistant.util import Throttle as Throttle
from typing import Final

MIN_TIME_BETWEEN_SESSION_RENEW: Final[Incomplete]
PLATFORM_SCHEMA: Final[Incomplete]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class CanaryCamera(CoordinatorEntity[CanaryDataUpdateCoordinator], Camera):
    _ffmpeg: Incomplete
    _ffmpeg_arguments: Incomplete
    _location_id: Incomplete
    _device: Incomplete
    _live_stream_session: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, hass: HomeAssistant, coordinator: CanaryDataUpdateCoordinator, location_id: str, device: Device, ffmpeg_args: str) -> None: ...
    @property
    def location(self) -> Location: ...
    @property
    def is_recording(self) -> bool: ...
    @property
    def motion_detection_enabled(self) -> bool: ...
    async def async_camera_image(self, width: Union[int, None] = ..., height: Union[int, None] = ...) -> Union[bytes, None]: ...
    async def handle_async_mjpeg_stream(self, request: Request) -> Union[StreamResponse, None]: ...
    def renew_live_stream_session(self) -> None: ...
