import datetime
from _typeshed import Incomplete
from aiohttp import web
from homeassistant.components import frontend as frontend, http as http
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import STATE_OFF as STATE_OFF, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.config_validation import PLATFORM_SCHEMA as PLATFORM_SCHEMA, PLATFORM_SCHEMA_BASE as PLATFORM_SCHEMA_BASE, time_period_str as time_period_str
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.template import DATE_STR_FORMAT as DATE_STR_FORMAT
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util import dt as dt
from typing import Any

_LOGGER: Incomplete
DOMAIN: str
ENTITY_ID_FORMAT: Incomplete
SCAN_INTERVAL: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
def get_date(date: dict[str, Any]) -> datetime.datetime: ...

class CalendarEvent:
    start: Union[datetime.date, datetime.datetime]
    end: Union[datetime.date, datetime.datetime]
    summary: str
    description: Union[str, None]
    location: Union[str, None]
    @property
    def start_datetime_local(self) -> datetime.datetime: ...
    @property
    def end_datetime_local(self) -> datetime.datetime: ...
    @property
    def all_day(self) -> bool: ...
    def as_dict(self) -> dict[str, Any]: ...
    def __init__(self, start, end, summary, description, location) -> None: ...

def _get_datetime_local(dt_or_d: Union[datetime.datetime, datetime.date]) -> datetime.datetime: ...
def _get_api_date(dt_or_d: Union[datetime.datetime, datetime.date]) -> dict[str, str]: ...
def normalize_event(event: dict[str, Any]) -> dict[str, Any]: ...
def extract_offset(summary: str, offset_prefix: str) -> tuple[str, datetime.timedelta]: ...
def is_offset_reached(start: datetime.datetime, offset_time: datetime.timedelta) -> bool: ...

class CalendarEventDevice(Entity):
    def __init_subclass__(cls, **kwargs: Any) -> None: ...
    @property
    def event(self) -> Union[dict[str, Any], None]: ...
    @property
    def state_attributes(self) -> Union[dict[str, Any], None]: ...
    @property
    def state(self) -> Union[str, None]: ...
    async def async_get_events(self, hass: HomeAssistant, start_date: datetime.datetime, end_date: datetime.datetime) -> list[dict[str, Any]]: ...

class CalendarEntity(Entity):
    @property
    def event(self) -> Union[CalendarEvent, None]: ...
    @property
    def state_attributes(self) -> Union[dict[str, Any], None]: ...
    @property
    def state(self) -> Union[str, None]: ...
    async def async_get_events(self, hass: HomeAssistant, start_date: datetime.datetime, end_date: datetime.datetime) -> list[CalendarEvent]: ...

class CalendarEventView(http.HomeAssistantView):
    url: str
    name: str
    component: Incomplete
    def __init__(self, component: EntityComponent) -> None: ...
    async def get(self, request: web.Request, entity_id: str) -> web.Response: ...

class CalendarListView(http.HomeAssistantView):
    url: str
    name: str
    component: Incomplete
    def __init__(self, component: EntityComponent) -> None: ...
    async def get(self, request: web.Request) -> web.Response: ...
