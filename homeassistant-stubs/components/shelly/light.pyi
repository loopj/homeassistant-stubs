from . import BlockDeviceWrapper as BlockDeviceWrapper, RpcDeviceWrapper as RpcDeviceWrapper
from .const import BLOCK as BLOCK, DATA_CONFIG_ENTRY as DATA_CONFIG_ENTRY, DOMAIN as DOMAIN, DUAL_MODE_LIGHT_MODELS as DUAL_MODE_LIGHT_MODELS, FIRMWARE_PATTERN as FIRMWARE_PATTERN, KELVIN_MAX_VALUE as KELVIN_MAX_VALUE, KELVIN_MIN_VALUE_COLOR as KELVIN_MIN_VALUE_COLOR, KELVIN_MIN_VALUE_WHITE as KELVIN_MIN_VALUE_WHITE, LIGHT_TRANSITION_MIN_FIRMWARE_DATE as LIGHT_TRANSITION_MIN_FIRMWARE_DATE, MAX_TRANSITION_TIME as MAX_TRANSITION_TIME, MODELS_SUPPORTING_LIGHT_TRANSITION as MODELS_SUPPORTING_LIGHT_TRANSITION, RGBW_MODELS as RGBW_MODELS, RPC as RPC, SHBLB_1_RGB_EFFECTS as SHBLB_1_RGB_EFFECTS, STANDARD_RGB_EFFECTS as STANDARD_RGB_EFFECTS
from .entity import ShellyBlockEntity as ShellyBlockEntity, ShellyRpcEntity as ShellyRpcEntity
from .utils import async_remove_shelly_entity as async_remove_shelly_entity, get_device_entry_gen as get_device_entry_gen, get_rpc_key_ids as get_rpc_key_ids, is_block_channel_type_light as is_block_channel_type_light, is_rpc_channel_type_light as is_rpc_channel_type_light
from aioshelly.block_device import Block as Block
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_COLOR_TEMP as ATTR_COLOR_TEMP, ATTR_EFFECT as ATTR_EFFECT, ATTR_RGBW_COLOR as ATTR_RGBW_COLOR, ATTR_RGB_COLOR as ATTR_RGB_COLOR, ATTR_TRANSITION as ATTR_TRANSITION, COLOR_MODE_BRIGHTNESS as COLOR_MODE_BRIGHTNESS, COLOR_MODE_COLOR_TEMP as COLOR_MODE_COLOR_TEMP, COLOR_MODE_ONOFF as COLOR_MODE_ONOFF, COLOR_MODE_RGB as COLOR_MODE_RGB, COLOR_MODE_RGBW as COLOR_MODE_RGBW, LightEntity as LightEntity, SUPPORT_EFFECT as SUPPORT_EFFECT, SUPPORT_TRANSITION as SUPPORT_TRANSITION, brightness_supported as brightness_supported
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util.color import color_temperature_kelvin_to_mired as color_temperature_kelvin_to_mired, color_temperature_mired_to_kelvin as color_temperature_mired_to_kelvin
from typing import Any, Final

_LOGGER: Final[Any]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
async def async_setup_block_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
async def async_setup_rpc_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BlockShellyLight(ShellyBlockEntity, LightEntity):
    control_result: Any
    _supported_color_modes: Any
    _supported_features: int
    _min_kelvin: Any
    _max_kelvin: Any
    def __init__(self, wrapper: BlockDeviceWrapper, block: Block) -> None: ...
    @property
    def supported_features(self) -> int: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def mode(self) -> str: ...
    @property
    def brightness(self) -> int: ...
    @property
    def color_mode(self) -> str: ...
    @property
    def rgb_color(self) -> tuple[int, int, int]: ...
    @property
    def rgbw_color(self) -> tuple[int, int, int, int]: ...
    @property
    def color_temp(self) -> int: ...
    @property
    def min_mireds(self) -> int: ...
    @property
    def max_mireds(self) -> int: ...
    @property
    def supported_color_modes(self) -> Union[set, None]: ...
    @property
    def effect_list(self) -> Union[list[str], None]: ...
    @property
    def effect(self) -> Union[str, None]: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    def _update_callback(self) -> None: ...

class RpcShellyLight(ShellyRpcEntity, LightEntity):
    _id: Any
    def __init__(self, wrapper: RpcDeviceWrapper, id_: int) -> None: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
