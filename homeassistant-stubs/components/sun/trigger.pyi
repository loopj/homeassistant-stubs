from _typeshed import Incomplete
from homeassistant.const import CONF_EVENT as CONF_EVENT, CONF_OFFSET as CONF_OFFSET, CONF_PLATFORM as CONF_PLATFORM, SUN_EVENT_SUNRISE as SUN_EVENT_SUNRISE
from homeassistant.core import HassJob as HassJob, callback as callback
from homeassistant.helpers.event import async_track_sunrise as async_track_sunrise, async_track_sunset as async_track_sunset

TRIGGER_SCHEMA: Incomplete

async def async_attach_trigger(hass, config, action, automation_info): ...
