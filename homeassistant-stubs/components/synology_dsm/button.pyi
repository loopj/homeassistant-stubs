from . import SynoApi as SynoApi
from .const import DOMAIN as DOMAIN
from .models import SynologyDSMData as SynologyDSMData
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any, Final

LOGGER: Incomplete

class SynologyDSMbuttonDescriptionMixin:
    press_action: Callable[[SynoApi], Callable[[], Coroutine[Any, Any, None]]]
    def __init__(self, press_action) -> None: ...
    def __mypy-replace(*, press_action) -> None: ...

class SynologyDSMbuttonDescription(ButtonEntityDescription, SynologyDSMbuttonDescriptionMixin):
    def __init__(self, press_action, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...
    def __mypy-replace(*, press_action, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

BUTTONS: Final[Incomplete]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SynologyDSMButton(ButtonEntity):
    entity_description: SynologyDSMbuttonDescription
    syno_api: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, api: SynoApi, description: SynologyDSMbuttonDescription) -> None: ...
    async def async_press(self) -> None: ...
