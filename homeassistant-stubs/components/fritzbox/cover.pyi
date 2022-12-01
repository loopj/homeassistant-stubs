from . import FritzBoxDeviceEntity as FritzBoxDeviceEntity, FritzboxDataUpdateCoordinator as FritzboxDataUpdateCoordinator
from .const import CONF_COORDINATOR as CONF_COORDINATOR
from _typeshed import Incomplete
from homeassistant.components.cover import ATTR_POSITION as ATTR_POSITION, CoverDeviceClass as CoverDeviceClass, CoverEntity as CoverEntity, CoverEntityFeature as CoverEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FritzboxCover(FritzBoxDeviceEntity, CoverEntity):
    _attr_device_class: Incomplete
    _attr_supported_features: Incomplete
    @property
    def current_cover_position(self) -> Union[int, None]: ...
    @property
    def is_closed(self) -> Union[bool, None]: ...
    async def async_open_cover(self, **kwargs: Any) -> None: ...
    async def async_close_cover(self, **kwargs: Any) -> None: ...
    async def async_set_cover_position(self, **kwargs: Any) -> None: ...
    async def async_stop_cover(self, **kwargs: Any) -> None: ...
