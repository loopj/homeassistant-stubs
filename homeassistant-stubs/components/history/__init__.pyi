from _typeshed import Incomplete
from aiohttp import web
from collections.abc import Iterable
from datetime import datetime as dt
from homeassistant.components import frontend as frontend, websocket_api as websocket_api
from homeassistant.components.http import HomeAssistantView as HomeAssistantView
from homeassistant.components.recorder import get_instance as get_instance, history as history, models as history_models
from homeassistant.components.recorder.statistics import list_statistic_ids as list_statistic_ids, statistics_during_period as statistics_during_period
from homeassistant.components.recorder.util import session_scope as session_scope
from homeassistant.const import CONF_DOMAINS as CONF_DOMAINS, CONF_ENTITIES as CONF_ENTITIES, CONF_EXCLUDE as CONF_EXCLUDE, CONF_INCLUDE as CONF_INCLUDE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.deprecation import deprecated_class as deprecated_class, deprecated_function as deprecated_function
from homeassistant.helpers.entityfilter import CONF_ENTITY_GLOBS as CONF_ENTITY_GLOBS, INCLUDE_EXCLUDE_BASE_FILTER_SCHEMA as INCLUDE_EXCLUDE_BASE_FILTER_SCHEMA
from homeassistant.helpers.typing import ConfigType as ConfigType

_LOGGER: Incomplete
DOMAIN: str
CONF_ORDER: str
GLOB_TO_SQL_CHARS: Incomplete
CONFIG_SCHEMA: Incomplete

def get_significant_states(hass, *args, **kwargs): ...
def state_changes_during_period(hass, start_time, end_time: Incomplete | None = ..., entity_id: Incomplete | None = ...): ...
def get_last_state_changes(hass, number_of_states, entity_id): ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...

class LazyState(history_models.LazyState): ...

async def ws_get_statistics_during_period(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict) -> None: ...
async def ws_get_list_statistic_ids(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict) -> None: ...

class HistoryPeriodView(HomeAssistantView):
    url: str
    name: str
    extra_urls: Incomplete
    filters: Incomplete
    use_include_order: Incomplete
    def __init__(self, filters: Union[Filters, None], use_include_order: bool) -> None: ...
    async def get(self, request: web.Request, datetime: Union[str, None] = ...) -> web.Response: ...
    def _sorted_significant_states_json(self, hass, start_time, end_time, entity_ids, include_start_time_state, significant_changes_only, minimal_response, no_attributes): ...

def sqlalchemy_filter_from_include_exclude_conf(conf: ConfigType) -> Union[Filters, None]: ...

class Filters:
    excluded_entities: Incomplete
    excluded_domains: Incomplete
    excluded_entity_globs: Incomplete
    included_entities: Incomplete
    included_domains: Incomplete
    included_entity_globs: Incomplete
    def __init__(self) -> None: ...
    def apply(self, query): ...
    @property
    def has_config(self): ...
    def bake(self, baked_query): ...
    def entity_filter(self): ...

def _glob_to_like(glob_str): ...
def _entities_may_have_state_changes_after(hass: HomeAssistant, entity_ids: Iterable, start_time: dt) -> bool: ...
