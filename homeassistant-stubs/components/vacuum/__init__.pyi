import asyncio
from _typeshed import Incomplete
from collections.abc import Mapping
from enum import IntFlag
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_BATTERY_LEVEL as ATTR_BATTERY_LEVEL, ATTR_COMMAND as ATTR_COMMAND, SERVICE_TOGGLE as SERVICE_TOGGLE, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON, STATE_IDLE as STATE_IDLE, STATE_ON as STATE_ON, STATE_PAUSED as STATE_PAUSED
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.config_validation import PLATFORM_SCHEMA as PLATFORM_SCHEMA, PLATFORM_SCHEMA_BASE as PLATFORM_SCHEMA_BASE, make_entity_service_schema as make_entity_service_schema
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription, ToggleEntity as ToggleEntity, ToggleEntityDescription as ToggleEntityDescription
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.entity_platform import EntityPlatform as EntityPlatform
from homeassistant.helpers.icon import icon_for_battery_level as icon_for_battery_level
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.loader import bind_hass as bind_hass
from typing import Any

_LOGGER: Incomplete
DOMAIN: str
ENTITY_ID_FORMAT: Incomplete
SCAN_INTERVAL: Incomplete
ATTR_BATTERY_ICON: str
ATTR_CLEANED_AREA: str
ATTR_FAN_SPEED: str
ATTR_FAN_SPEED_LIST: str
ATTR_PARAMS: str
ATTR_STATUS: str
SERVICE_CLEAN_SPOT: str
SERVICE_LOCATE: str
SERVICE_RETURN_TO_BASE: str
SERVICE_SEND_COMMAND: str
SERVICE_SET_FAN_SPEED: str
SERVICE_START_PAUSE: str
SERVICE_START: str
SERVICE_PAUSE: str
SERVICE_STOP: str
STATE_CLEANING: str
STATE_DOCKED: str
STATE_RETURNING: str
STATE_ERROR: str
STATES: Incomplete
DEFAULT_NAME: str

class VacuumEntityFeature(IntFlag):
    TURN_ON: int
    TURN_OFF: int
    PAUSE: int
    STOP: int
    RETURN_HOME: int
    FAN_SPEED: int
    BATTERY: int
    STATUS: int
    SEND_COMMAND: int
    LOCATE: int
    CLEAN_SPOT: int
    MAP: int
    STATE: int
    START: int

SUPPORT_TURN_ON: int
SUPPORT_TURN_OFF: int
SUPPORT_PAUSE: int
SUPPORT_STOP: int
SUPPORT_RETURN_HOME: int
SUPPORT_FAN_SPEED: int
SUPPORT_BATTERY: int
SUPPORT_STATUS: int
SUPPORT_SEND_COMMAND: int
SUPPORT_LOCATE: int
SUPPORT_CLEAN_SPOT: int
SUPPORT_MAP: int
SUPPORT_STATE: int
SUPPORT_START: int

def is_on(hass: HomeAssistant, entity_id: str) -> bool: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class _BaseVacuum(Entity):
    _attr_battery_icon: str
    _attr_battery_level: int | None
    _attr_fan_speed: str | None
    _attr_fan_speed_list: list[str]
    _attr_supported_features: VacuumEntityFeature
    @property
    def supported_features(self) -> VacuumEntityFeature: ...
    @property
    def battery_level(self) -> int | None: ...
    @property
    def battery_icon(self) -> str: ...
    @property
    def fan_speed(self) -> str | None: ...
    @property
    def fan_speed_list(self) -> list[str]: ...
    @property
    def capability_attributes(self) -> Mapping[str, Any] | None: ...
    @property
    def state_attributes(self) -> dict[str, Any]: ...
    def stop(self, **kwargs: Any) -> None: ...
    async def async_stop(self, **kwargs: Any) -> None: ...
    def return_to_base(self, **kwargs: Any) -> None: ...
    async def async_return_to_base(self, **kwargs: Any) -> None: ...
    def clean_spot(self, **kwargs: Any) -> None: ...
    async def async_clean_spot(self, **kwargs: Any) -> None: ...
    def locate(self, **kwargs: Any) -> None: ...
    async def async_locate(self, **kwargs: Any) -> None: ...
    def set_fan_speed(self, fan_speed: str, **kwargs: Any) -> None: ...
    async def async_set_fan_speed(self, fan_speed: str, **kwargs: Any) -> None: ...
    def send_command(self, command: str, params: dict[str, Any] | list[Any] | None = ..., **kwargs: Any) -> None: ...
    async def async_send_command(self, command: str, params: dict[str, Any] | list[Any] | None = ..., **kwargs: Any) -> None: ...

class VacuumEntityDescription(ToggleEntityDescription):
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...
    def __mypy-replace(*, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

class VacuumEntity(_BaseVacuum, ToggleEntity):
    def add_to_platform_start(self, hass: HomeAssistant, platform: EntityPlatform, parallel_updates: asyncio.Semaphore | None) -> None: ...
    entity_description: VacuumEntityDescription
    _attr_status: str | None
    @property
    def status(self) -> str | None: ...
    @property
    def battery_icon(self) -> str: ...
    @property
    def state_attributes(self) -> dict[str, Any]: ...
    def turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    def turn_off(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    def start_pause(self, **kwargs: Any) -> None: ...
    async def async_start_pause(self, **kwargs: Any) -> None: ...

class StateVacuumEntityDescription(EntityDescription):
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...
    def __mypy-replace(*, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

class StateVacuumEntity(_BaseVacuum):
    entity_description: StateVacuumEntityDescription
    _attr_state: str | None
    @property
    def state(self) -> str | None: ...
    @property
    def battery_icon(self) -> str: ...
    def start(self) -> None: ...
    async def async_start(self) -> None: ...
    def pause(self) -> None: ...
    async def async_pause(self) -> None: ...
