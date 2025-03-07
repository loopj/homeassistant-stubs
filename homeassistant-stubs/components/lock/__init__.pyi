import re
from _typeshed import Incomplete
from enum import IntFlag
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_CODE as ATTR_CODE, ATTR_CODE_FORMAT as ATTR_CODE_FORMAT, SERVICE_LOCK as SERVICE_LOCK, SERVICE_OPEN as SERVICE_OPEN, SERVICE_UNLOCK as SERVICE_UNLOCK, STATE_JAMMED as STATE_JAMMED, STATE_LOCKED as STATE_LOCKED, STATE_LOCKING as STATE_LOCKING, STATE_UNLOCKED as STATE_UNLOCKED, STATE_UNLOCKING as STATE_UNLOCKING
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.helpers.config_validation import PLATFORM_SCHEMA as PLATFORM_SCHEMA, PLATFORM_SCHEMA_BASE as PLATFORM_SCHEMA_BASE, make_entity_service_schema as make_entity_service_schema
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.service import remove_entity_service_fields as remove_entity_service_fields
from homeassistant.helpers.typing import ConfigType as ConfigType, StateType as StateType
from typing import Any

_LOGGER: Incomplete
ATTR_CHANGED_BY: str
CONF_DEFAULT_CODE: str
DOMAIN: str
SCAN_INTERVAL: Incomplete
ENTITY_ID_FORMAT: Incomplete
MIN_TIME_BETWEEN_SCANS: Incomplete
LOCK_SERVICE_SCHEMA: Incomplete

class LockEntityFeature(IntFlag):
    OPEN: int

SUPPORT_OPEN: int
PROP_TO_ATTR: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def _async_lock(entity: LockEntity, service_call: ServiceCall) -> None: ...
async def _async_unlock(entity: LockEntity, service_call: ServiceCall) -> None: ...
async def _async_open(entity: LockEntity, service_call: ServiceCall) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class LockEntityDescription(EntityDescription):
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...
    def __mypy-replace(*, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

class LockEntity(Entity):
    entity_description: LockEntityDescription
    _attr_changed_by: str | None
    _attr_code_format: str | None
    _attr_is_locked: bool | None
    _attr_is_locking: bool | None
    _attr_is_unlocking: bool | None
    _attr_is_jammed: bool | None
    _attr_state: None
    _attr_supported_features: LockEntityFeature
    _lock_option_default_code: str
    __code_format_cmp: re.Pattern[str] | None
    @property
    def changed_by(self) -> str | None: ...
    @property
    def code_format(self) -> str | None: ...
    @property
    def code_format_cmp(self) -> re.Pattern[str] | None: ...
    @property
    def is_locked(self) -> bool | None: ...
    @property
    def is_locking(self) -> bool | None: ...
    @property
    def is_unlocking(self) -> bool | None: ...
    @property
    def is_jammed(self) -> bool | None: ...
    def lock(self, **kwargs: Any) -> None: ...
    async def async_lock(self, **kwargs: Any) -> None: ...
    def unlock(self, **kwargs: Any) -> None: ...
    async def async_unlock(self, **kwargs: Any) -> None: ...
    def open(self, **kwargs: Any) -> None: ...
    async def async_open(self, **kwargs: Any) -> None: ...
    @property
    def state_attributes(self) -> dict[str, StateType]: ...
    @property
    def state(self) -> str | None: ...
    @property
    def supported_features(self) -> LockEntityFeature: ...
    async def async_internal_added_to_hass(self) -> None: ...
    def async_registry_entry_updated(self) -> None: ...
    def _async_read_entity_options(self) -> None: ...
