import datetime
from _typeshed import Incomplete
from homeassistant.components.calendar import CalendarEntity as CalendarEntity, CalendarEvent as CalendarEvent
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType

def setup_platform(hass: HomeAssistant, config: ConfigType, add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = ...) -> None: ...
def calendar_data_future() -> CalendarEvent: ...
def calendar_data_current() -> CalendarEvent: ...

class DemoCalendar(CalendarEntity):
    _event: Incomplete
    _attr_name: Incomplete
    def __init__(self, event: CalendarEvent, name: str) -> None: ...
    @property
    def event(self) -> CalendarEvent: ...
    async def async_get_events(self, hass: HomeAssistant, start_date: datetime.datetime, end_date: datetime.datetime) -> list[CalendarEvent]: ...
