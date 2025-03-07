from .const import DOMAIN as DOMAIN, HA_FAN_TO_ISY as HA_FAN_TO_ISY, HA_HVAC_TO_ISY as HA_HVAC_TO_ISY, ISY_HVAC_MODES as ISY_HVAC_MODES, UOM_FAN_MODES as UOM_FAN_MODES, UOM_HVAC_ACTIONS as UOM_HVAC_ACTIONS, UOM_HVAC_MODE_GENERIC as UOM_HVAC_MODE_GENERIC, UOM_HVAC_MODE_INSTEON as UOM_HVAC_MODE_INSTEON, UOM_ISYV4_NONE as UOM_ISYV4_NONE, UOM_ISY_CELSIUS as UOM_ISY_CELSIUS, UOM_ISY_FAHRENHEIT as UOM_ISY_FAHRENHEIT, UOM_TO_STATES as UOM_TO_STATES, _LOGGER as _LOGGER
from .entity import ISYNodeEntity as ISYNodeEntity
from .helpers import convert_isy_value_to_hass as convert_isy_value_to_hass
from _typeshed import Incomplete
from homeassistant.components.climate import ATTR_TARGET_TEMP_HIGH as ATTR_TARGET_TEMP_HIGH, ATTR_TARGET_TEMP_LOW as ATTR_TARGET_TEMP_LOW, ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, FAN_AUTO as FAN_AUTO, FAN_OFF as FAN_OFF, FAN_ON as FAN_ON, HVACAction as HVACAction, HVACMode as HVACMode
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, PRECISION_TENTHS as PRECISION_TENTHS, Platform as Platform, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util.enum import try_parse_enum as try_parse_enum
from pyisy.nodes import Node as Node
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ISYThermostatEntity(ISYNodeEntity, ClimateEntity):
    _attr_hvac_modes = ISY_HVAC_MODES
    _attr_precision = PRECISION_TENTHS
    _attr_supported_features: Incomplete
    _uom: Incomplete
    _hvac_action: Incomplete
    _hvac_mode: Incomplete
    _fan_mode: Incomplete
    _temp_unit: Incomplete
    _current_humidity: int
    _target_temp_low: int
    _target_temp_high: int
    def __init__(self, node: Node, device_info: DeviceInfo | None = ...) -> None: ...
    @property
    def temperature_unit(self) -> str: ...
    @property
    def current_humidity(self) -> int | None: ...
    @property
    def hvac_mode(self) -> HVACMode: ...
    @property
    def hvac_action(self) -> HVACAction | None: ...
    @property
    def current_temperature(self) -> float | None: ...
    @property
    def target_temperature_step(self) -> float | None: ...
    @property
    def target_temperature(self) -> float | None: ...
    @property
    def target_temperature_high(self) -> float | None: ...
    @property
    def target_temperature_low(self) -> float | None: ...
    @property
    def fan_modes(self) -> list[str]: ...
    @property
    def fan_mode(self) -> str: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    async def async_set_fan_mode(self, fan_mode: str) -> None: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
