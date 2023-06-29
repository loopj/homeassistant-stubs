from .entity import EsphomeEntity as EsphomeEntity, esphome_state_property as esphome_state_property, platform_async_setup_entry as platform_async_setup_entry
from _typeshed import Incomplete
from aioesphomeapi import EntityInfo as EntityInfo, LightColorCapability, LightInfo, LightState
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_COLOR_TEMP_KELVIN as ATTR_COLOR_TEMP_KELVIN, ATTR_EFFECT as ATTR_EFFECT, ATTR_FLASH as ATTR_FLASH, ATTR_RGBWW_COLOR as ATTR_RGBWW_COLOR, ATTR_RGBW_COLOR as ATTR_RGBW_COLOR, ATTR_RGB_COLOR as ATTR_RGB_COLOR, ATTR_TRANSITION as ATTR_TRANSITION, ATTR_WHITE as ATTR_WHITE, ColorMode as ColorMode, FLASH_LONG as FLASH_LONG, FLASH_SHORT as FLASH_SHORT, LightEntity as LightEntity, LightEntityFeature as LightEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

FLASH_LENGTHS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

_COLOR_MODE_MAPPING: Incomplete

def _mired_to_kelvin(mired_temperature: float) -> int: ...
def _color_mode_to_ha(mode: int) -> str: ...
def _filter_color_modes(supported: list[int], features: LightColorCapability) -> list[int]: ...

class EsphomeLight(EsphomeEntity[LightInfo, LightState], LightEntity):
    _native_supported_color_modes: list[int]
    _supports_color_mode: bool
    @property
    def is_on(self) -> bool | None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @property
    def brightness(self) -> int | None: ...
    @property
    def color_mode(self) -> str | None: ...
    @property
    def rgb_color(self) -> tuple[int, int, int] | None: ...
    @property
    def rgbw_color(self) -> tuple[int, int, int, int] | None: ...
    @property
    def rgbww_color(self) -> tuple[int, int, int, int, int] | None: ...
    @property
    def color_temp_kelvin(self) -> int: ...
    @property
    def effect(self) -> str | None: ...
    _attr_supported_features: Incomplete
    _attr_supported_color_modes: Incomplete
    _attr_effect_list: Incomplete
    _attr_min_mireds: Incomplete
    _attr_max_mireds: Incomplete
    _attr_min_color_temp_kelvin: Incomplete
    _attr_max_color_temp_kelvin: Incomplete
    def _on_static_info_update(self, static_info: EntityInfo) -> None: ...
