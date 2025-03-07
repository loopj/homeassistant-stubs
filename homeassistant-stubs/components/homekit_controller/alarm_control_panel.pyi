from . import KNOWN_DEVICES as KNOWN_DEVICES
from .connection import HKDevice as HKDevice
from .entity import HomeKitEntity as HomeKitEntity
from _typeshed import Incomplete
from aiohomekit.model.services import Service as Service
from homeassistant.components.alarm_control_panel import AlarmControlPanelEntity as AlarmControlPanelEntity, AlarmControlPanelEntityFeature as AlarmControlPanelEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_BATTERY_LEVEL as ATTR_BATTERY_LEVEL, Platform as Platform, STATE_ALARM_ARMED_AWAY as STATE_ALARM_ARMED_AWAY, STATE_ALARM_ARMED_HOME as STATE_ALARM_ARMED_HOME, STATE_ALARM_ARMED_NIGHT as STATE_ALARM_ARMED_NIGHT, STATE_ALARM_DISARMED as STATE_ALARM_DISARMED, STATE_ALARM_TRIGGERED as STATE_ALARM_TRIGGERED
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

CURRENT_STATE_MAP: Incomplete
TARGET_STATE_MAP: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class HomeKitAlarmControlPanelEntity(HomeKitEntity, AlarmControlPanelEntity):
    _attr_icon: str
    _attr_supported_features: Incomplete
    def get_characteristic_types(self) -> list[str]: ...
    @property
    def state(self) -> str: ...
    async def async_alarm_disarm(self, code: str | None = ...) -> None: ...
    async def async_alarm_arm_away(self, code: str | None = ...) -> None: ...
    async def async_alarm_arm_home(self, code: str | None = ...) -> None: ...
    async def async_alarm_arm_night(self, code: str | None = ...) -> None: ...
    async def set_alarm_state(self, state: str, code: str | None = ...) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any] | None: ...
