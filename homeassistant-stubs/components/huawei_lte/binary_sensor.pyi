from . import HuaweiLteBaseEntityWithDevice as HuaweiLteBaseEntityWithDevice
from .const import DOMAIN as DOMAIN, KEY_MONITORING_CHECK_NOTIFICATIONS as KEY_MONITORING_CHECK_NOTIFICATIONS, KEY_MONITORING_STATUS as KEY_MONITORING_STATUS, KEY_WLAN_WIFI_FEATURE_SWITCH as KEY_WLAN_WIFI_FEATURE_SWITCH
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class HuaweiLteBaseBinarySensor(HuaweiLteBaseEntityWithDevice, BinarySensorEntity):
    key: str
    item: str
    _raw_state: str | None
    @property
    def entity_registry_enabled_default(self) -> bool: ...
    @property
    def _device_unique_id(self) -> str: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    _available: bool
    async def async_update(self) -> None: ...
    def __init__(self, router) -> None: ...

CONNECTION_STATE_ATTRIBUTES: Incomplete

class HuaweiLteMobileConnectionBinarySensor(HuaweiLteBaseBinarySensor):
    _attr_name: str
    key: Incomplete
    item: str
    def __post_init__(self) -> None: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def assumed_state(self) -> bool: ...
    @property
    def icon(self) -> str: ...
    @property
    def entity_registry_enabled_default(self) -> bool: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any] | None: ...
    def __init__(self, router) -> None: ...

class HuaweiLteBaseWifiStatusBinarySensor(HuaweiLteBaseBinarySensor):
    @property
    def is_on(self) -> bool: ...
    @property
    def assumed_state(self) -> bool: ...
    @property
    def icon(self) -> str: ...

class HuaweiLteWifiStatusBinarySensor(HuaweiLteBaseWifiStatusBinarySensor):
    _attr_name: str
    key: Incomplete
    item: str
    def __post_init__(self) -> None: ...
    def __init__(self, router) -> None: ...

class HuaweiLteWifi24ghzStatusBinarySensor(HuaweiLteBaseWifiStatusBinarySensor):
    _attr_name: str
    key: Incomplete
    item: str
    def __post_init__(self) -> None: ...
    def __init__(self, router) -> None: ...

class HuaweiLteWifi5ghzStatusBinarySensor(HuaweiLteBaseWifiStatusBinarySensor):
    _attr_name: str
    key: Incomplete
    item: str
    def __post_init__(self) -> None: ...
    def __init__(self, router) -> None: ...

class HuaweiLteSmsStorageFullBinarySensor(HuaweiLteBaseBinarySensor):
    _attr_name: str
    key: Incomplete
    item: str
    def __post_init__(self) -> None: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def assumed_state(self) -> bool: ...
    @property
    def icon(self) -> str: ...
    def __init__(self, router) -> None: ...
