import RFXtrx as rfxtrxmod
from . import DOMAIN as DOMAIN, DeviceTuple as DeviceTuple, RfxtrxCommandEntity as RfxtrxCommandEntity, async_setup_platform_entry as async_setup_platform_entry, get_pt2262_cmd as get_pt2262_cmd
from .const import COMMAND_OFF_LIST as COMMAND_OFF_LIST, COMMAND_ON_LIST as COMMAND_ON_LIST, CONF_DATA_BITS as CONF_DATA_BITS, DEVICE_PACKET_TYPE_LIGHTING4 as DEVICE_PACKET_TYPE_LIGHTING4
from _typeshed import Incomplete
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_COMMAND_OFF as CONF_COMMAND_OFF, CONF_COMMAND_ON as CONF_COMMAND_ON, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

DATA_SWITCH: Incomplete
_LOGGER: Incomplete

def supported(event: rfxtrxmod.RFXtrxEvent) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RfxtrxSwitch(RfxtrxCommandEntity, SwitchEntity):
    _data_bits: Incomplete
    _cmd_on: Incomplete
    _cmd_off: Incomplete
    def __init__(self, device: rfxtrxmod.RFXtrxDevice, device_id: DeviceTuple, data_bits: int | None = ..., cmd_on: int | None = ..., cmd_off: int | None = ..., event: rfxtrxmod.RFXtrxEvent | None = ...) -> None: ...
    _attr_is_on: Incomplete
    async def async_added_to_hass(self) -> None: ...
    def _apply_event_lighting4(self, event: rfxtrxmod.RFXtrxEvent) -> None: ...
    def _apply_event_standard(self, event: rfxtrxmod.RFXtrxEvent) -> None: ...
    def _apply_event(self, event: rfxtrxmod.RFXtrxEvent) -> None: ...
    def _handle_event(self, event: rfxtrxmod.RFXtrxEvent, device_id: DeviceTuple) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
