from .const import DOMAIN as DOMAIN
from .coordinator import SleepIQData as SleepIQData
from .entity import SleepIQBedEntity as SleepIQBedEntity
from asyncsleepiq import SleepIQBed as SleepIQBed, SleepIQPreset as SleepIQPreset
from homeassistant.components.select import SelectEntity as SelectEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SleepIQSelectEntity(SleepIQBedEntity, SelectEntity):
    _attr_options: Any
    preset: Any
    _attr_name: Any
    _attr_unique_id: Any
    def __init__(self, coordinator: DataUpdateCoordinator, bed: SleepIQBed, preset: SleepIQPreset) -> None: ...
    _attr_current_option: Any
    def _async_update_attrs(self) -> None: ...
    async def async_select_option(self, option: str) -> None: ...
