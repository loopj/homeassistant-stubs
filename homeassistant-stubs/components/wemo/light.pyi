from . import async_wemo_dispatcher_connect as async_wemo_dispatcher_connect
from .entity import WemoBinaryStateEntity as WemoBinaryStateEntity, WemoEntity as WemoEntity
from .wemo_device import DeviceCoordinator as DeviceCoordinator
from _typeshed import Incomplete
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_COLOR_TEMP as ATTR_COLOR_TEMP, ATTR_HS_COLOR as ATTR_HS_COLOR, ATTR_TRANSITION as ATTR_TRANSITION, ColorMode as ColorMode, LightEntity as LightEntity, LightEntityFeature as LightEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import CONNECTION_ZIGBEE as CONNECTION_ZIGBEE
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pywemo import BridgeLight as BridgeLight, Dimmer as Dimmer
from typing import Any

WEMO_OFF: int

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def async_setup_bridge(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback, coordinator: DeviceCoordinator) -> None: ...

class WemoLight(WemoEntity, LightEntity):
    _attr_supported_features: Incomplete
    light: Incomplete
    _unique_id: Incomplete
    _model_name: Incomplete
    def __init__(self, coordinator: DeviceCoordinator, light: BridgeLight) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def available(self) -> bool: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    @property
    def brightness(self) -> int: ...
    @property
    def xy_color(self) -> tuple[float, float] | None: ...
    @property
    def color_temp(self) -> int | None: ...
    @property
    def color_mode(self) -> ColorMode: ...
    @property
    def supported_color_modes(self) -> set[ColorMode]: ...
    @property
    def is_on(self) -> bool: ...
    def turn_on(self, **kwargs: Any) -> None: ...
    def turn_off(self, **kwargs: Any) -> None: ...

class WemoDimmer(WemoBinaryStateEntity, LightEntity):
    _attr_supported_color_modes: Incomplete
    _attr_color_mode: Incomplete
    wemo: Dimmer
    @property
    def brightness(self) -> int: ...
    def turn_on(self, **kwargs: Any) -> None: ...
    def turn_off(self, **kwargs: Any) -> None: ...
