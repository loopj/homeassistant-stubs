import re
import voluptuous as vol
from . import template as template_helper
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Hashable
from datetime import date as date_sys, datetime as datetime_sys, time as time_sys, timedelta
from enum import Enum
from homeassistant.const import ATTR_AREA_ID as ATTR_AREA_ID, ATTR_DEVICE_ID as ATTR_DEVICE_ID, ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_ABOVE as CONF_ABOVE, CONF_ALIAS as CONF_ALIAS, CONF_ATTRIBUTE as CONF_ATTRIBUTE, CONF_BELOW as CONF_BELOW, CONF_CHOOSE as CONF_CHOOSE, CONF_CONDITION as CONF_CONDITION, CONF_CONDITIONS as CONF_CONDITIONS, CONF_CONTINUE_ON_ERROR as CONF_CONTINUE_ON_ERROR, CONF_CONTINUE_ON_TIMEOUT as CONF_CONTINUE_ON_TIMEOUT, CONF_COUNT as CONF_COUNT, CONF_DEFAULT as CONF_DEFAULT, CONF_DELAY as CONF_DELAY, CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_DOMAIN as CONF_DOMAIN, CONF_ELSE as CONF_ELSE, CONF_ENABLED as CONF_ENABLED, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_ENTITY_NAMESPACE as CONF_ENTITY_NAMESPACE, CONF_ERROR as CONF_ERROR, CONF_EVENT as CONF_EVENT, CONF_EVENT_DATA as CONF_EVENT_DATA, CONF_EVENT_DATA_TEMPLATE as CONF_EVENT_DATA_TEMPLATE, CONF_FOR as CONF_FOR, CONF_FOR_EACH as CONF_FOR_EACH, CONF_ID as CONF_ID, CONF_IF as CONF_IF, CONF_MATCH as CONF_MATCH, CONF_PARALLEL as CONF_PARALLEL, CONF_PLATFORM as CONF_PLATFORM, CONF_REPEAT as CONF_REPEAT, CONF_RESPONSE_VARIABLE as CONF_RESPONSE_VARIABLE, CONF_SCAN_INTERVAL as CONF_SCAN_INTERVAL, CONF_SCENE as CONF_SCENE, CONF_SEQUENCE as CONF_SEQUENCE, CONF_SERVICE as CONF_SERVICE, CONF_SERVICE_DATA as CONF_SERVICE_DATA, CONF_SERVICE_DATA_TEMPLATE as CONF_SERVICE_DATA_TEMPLATE, CONF_SERVICE_TEMPLATE as CONF_SERVICE_TEMPLATE, CONF_STATE as CONF_STATE, CONF_STOP as CONF_STOP, CONF_TARGET as CONF_TARGET, CONF_THEN as CONF_THEN, CONF_TIMEOUT as CONF_TIMEOUT, CONF_UNTIL as CONF_UNTIL, CONF_VALUE_TEMPLATE as CONF_VALUE_TEMPLATE, CONF_VARIABLES as CONF_VARIABLES, CONF_WAIT_FOR_TRIGGER as CONF_WAIT_FOR_TRIGGER, CONF_WAIT_TEMPLATE as CONF_WAIT_TEMPLATE, CONF_WHILE as CONF_WHILE, ENTITY_MATCH_ALL as ENTITY_MATCH_ALL, ENTITY_MATCH_ANY as ENTITY_MATCH_ANY, ENTITY_MATCH_NONE as ENTITY_MATCH_NONE, SUN_EVENT_SUNRISE as SUN_EVENT_SUNRISE, SUN_EVENT_SUNSET as SUN_EVENT_SUNSET, UnitOfTemperature as UnitOfTemperature, WEEKDAYS as WEEKDAYS
from homeassistant.core import HomeAssistant as HomeAssistant, async_get_hass as async_get_hass, split_entity_id as split_entity_id, valid_entity_id as valid_entity_id
from homeassistant.exceptions import TemplateError as TemplateError
from homeassistant.generated import currencies as currencies
from homeassistant.generated.countries import COUNTRIES as COUNTRIES
from homeassistant.generated.languages import LANGUAGES as LANGUAGES
from homeassistant.util import raise_if_invalid_path as raise_if_invalid_path
from typing import Any, TypeVar, overload

TIME_PERIOD_ERROR: str
byte: Incomplete
small_float: Incomplete
positive_int: Incomplete
positive_float: Incomplete
latitude: Incomplete
longitude: Incomplete
gps: Incomplete
sun_event: Incomplete
port: Incomplete
_T = TypeVar('_T')

def path(value: Any) -> str: ...
def has_at_least_one_key(*keys: Any) -> Callable[[dict], dict]: ...
def has_at_most_one_key(*keys: Any) -> Callable[[dict], dict]: ...
def boolean(value: Any) -> bool: ...

_WS: Incomplete

def whitespace(value: Any) -> str: ...
def isdevice(value: Any) -> str: ...
def matches_regex(regex: str) -> Callable[[Any], str]: ...
def is_regex(value: Any) -> re.Pattern[Any]: ...
def isfile(value: Any) -> str: ...
def isdir(value: Any) -> str: ...
@overload
def ensure_list(value: None) -> list[Any]: ...
@overload
def ensure_list(value: list[_T]) -> list[_T]: ...
@overload
def ensure_list(value: list[_T] | _T) -> list[_T]: ...
def entity_id(value: Any) -> str: ...
def entity_id_or_uuid(value: Any) -> str: ...
def _entity_ids(value: str | list, allow_uuid: bool) -> list[str]: ...
def entity_ids(value: str | list) -> list[str]: ...
def entity_ids_or_uuids(value: str | list) -> list[str]: ...

comp_entity_ids: Incomplete
comp_entity_ids_or_uuids: Incomplete

def entity_domain(domain: str | list[str]) -> Callable[[Any], str]: ...
def entities_domain(domain: str | list[str]) -> Callable[[str | list], list[str]]: ...
def enum(enumClass: type[Enum]) -> vol.All: ...
def icon(value: Any) -> str: ...

_TIME_PERIOD_DICT_KEYS: Incomplete
time_period_dict: Incomplete

def time(value: Any) -> time_sys: ...
def date(value: Any) -> date_sys: ...
def time_period_str(value: str) -> timedelta: ...
def time_period_seconds(value: float | str) -> timedelta: ...

time_period: Incomplete

def match_all(value: _T) -> _T: ...
def positive_timedelta(value: timedelta) -> timedelta: ...

positive_time_period_dict: Incomplete
positive_time_period: Incomplete

def remove_falsy(value: list[_T]) -> list[_T]: ...
def service(value: Any) -> str: ...
def slug(value: Any) -> str: ...
def schema_with_slug_keys(value_schema: _T | Callable, *, slug_validator: Callable[[Any], str] = ...) -> Callable: ...
def slugify(value: Any) -> str: ...
def string(value: Any) -> str: ...
def string_with_no_html(value: Any) -> str: ...
def temperature_unit(value: Any) -> UnitOfTemperature: ...
def template(value: Any | None) -> template_helper.Template: ...
def dynamic_template(value: Any | None) -> template_helper.Template: ...
def template_complex(value: Any) -> Any: ...
def _positive_time_period_template_complex(value: Any) -> Any: ...

positive_time_period_template: Incomplete

def datetime(value: Any) -> datetime_sys: ...
def time_zone(value: str) -> str: ...

weekdays: Incomplete

def socket_timeout(value: Any | None) -> object: ...
def url(value: Any) -> str: ...
def url_no_path(value: Any) -> str: ...
def x10_address(value: str) -> str: ...
def uuid4_hex(value: Any) -> str: ...

_FAKE_UUID_4_HEX: Incomplete

def fake_uuid4_hex(value: Any) -> str: ...
def ensure_list_csv(value: Any) -> list: ...

class multi_select:
    options: Incomplete
    def __init__(self, options: dict | list) -> None: ...
    def __call__(self, selected: list) -> list: ...

def _deprecated_or_removed(key: str, replacement_key: str | None, default: Any | None, raise_if_present: bool, option_removed: bool) -> Callable[[dict], dict]: ...
def deprecated(key: str, replacement_key: str | None = ..., default: Any | None = ..., raise_if_present: bool | None = ...) -> Callable[[dict], dict]: ...
def removed(key: str, default: Any | None = ..., raise_if_present: bool | None = ...) -> Callable[[dict], dict]: ...
def key_value_schemas(key: str, value_schemas: dict[Hashable, vol.Schema], default_schema: vol.Schema | None = ..., default_description: str | None = ...) -> Callable[[Any], dict[Hashable, Any]]: ...
def key_dependency(key: Hashable, dependency: Hashable) -> Callable[[dict[Hashable, Any]], dict[Hashable, Any]]: ...
def custom_serializer(schema: Any) -> Any: ...
def expand_condition_shorthand(value: Any | None) -> Any: ...
def empty_config_schema(domain: str) -> Callable[[dict], dict]: ...
def _no_yaml_config_schema(domain: str, issue_base: str, translation_key: str, translation_placeholders: dict[str, str]) -> Callable[[dict], dict]: ...
def config_entry_only_config_schema(domain: str) -> Callable[[dict], dict]: ...
def platform_only_config_schema(domain: str) -> Callable[[dict], dict]: ...

PLATFORM_SCHEMA: Incomplete
PLATFORM_SCHEMA_BASE: Incomplete
ENTITY_SERVICE_FIELDS: Incomplete
TARGET_SERVICE_FIELDS: Incomplete

def make_entity_service_schema(schema: dict, *, extra: int = ...) -> vol.Schema: ...

SCRIPT_VARIABLES_SCHEMA: Incomplete

def script_action(value: Any) -> dict: ...

SCRIPT_SCHEMA: Incomplete
SCRIPT_ACTION_BASE_SCHEMA: Incomplete
EVENT_SCHEMA: Incomplete
SERVICE_SCHEMA: Incomplete
NUMERIC_STATE_THRESHOLD_SCHEMA: Incomplete
CONDITION_BASE_SCHEMA: Incomplete
NUMERIC_STATE_CONDITION_SCHEMA: Incomplete
STATE_CONDITION_BASE_SCHEMA: Incomplete
STATE_CONDITION_STATE_SCHEMA: Incomplete
STATE_CONDITION_ATTRIBUTE_SCHEMA: Incomplete

def STATE_CONDITION_SCHEMA(value: Any) -> dict: ...

SUN_CONDITION_SCHEMA: Incomplete
TEMPLATE_CONDITION_SCHEMA: Incomplete
TIME_CONDITION_SCHEMA: Incomplete
TRIGGER_CONDITION_SCHEMA: Incomplete
ZONE_CONDITION_SCHEMA: Incomplete
AND_CONDITION_SCHEMA: Incomplete
AND_CONDITION_SHORTHAND_SCHEMA: Incomplete
OR_CONDITION_SCHEMA: Incomplete
OR_CONDITION_SHORTHAND_SCHEMA: Incomplete
NOT_CONDITION_SCHEMA: Incomplete
NOT_CONDITION_SHORTHAND_SCHEMA: Incomplete
DEVICE_CONDITION_BASE_SCHEMA: Incomplete
DEVICE_CONDITION_SCHEMA: Incomplete
dynamic_template_condition_action: Incomplete
CONDITION_SHORTHAND_SCHEMA: Incomplete
CONDITION_SCHEMA: vol.Schema
CONDITIONS_SCHEMA: Incomplete
CONDITION_ACTION_SCHEMA: vol.Schema
TRIGGER_BASE_SCHEMA: Incomplete
_base_trigger_validator_schema: Incomplete

def _base_trigger_validator(value: Any) -> Any: ...

TRIGGER_SCHEMA: Incomplete
_SCRIPT_DELAY_SCHEMA: Incomplete
_SCRIPT_WAIT_TEMPLATE_SCHEMA: Incomplete
DEVICE_ACTION_BASE_SCHEMA: Incomplete
DEVICE_ACTION_SCHEMA: Incomplete
_SCRIPT_SCENE_SCHEMA: Incomplete
_SCRIPT_REPEAT_SCHEMA: Incomplete
_SCRIPT_CHOOSE_SCHEMA: Incomplete
_SCRIPT_WAIT_FOR_TRIGGER_SCHEMA: Incomplete
_SCRIPT_IF_SCHEMA: Incomplete
_SCRIPT_SET_SCHEMA: Incomplete
_SCRIPT_STOP_SCHEMA: Incomplete
_SCRIPT_PARALLEL_SEQUENCE: Incomplete
_parallel_sequence_action: Incomplete
_SCRIPT_PARALLEL_SCHEMA: Incomplete
SCRIPT_ACTION_DELAY: str
SCRIPT_ACTION_WAIT_TEMPLATE: str
SCRIPT_ACTION_CHECK_CONDITION: str
SCRIPT_ACTION_FIRE_EVENT: str
SCRIPT_ACTION_CALL_SERVICE: str
SCRIPT_ACTION_DEVICE_AUTOMATION: str
SCRIPT_ACTION_ACTIVATE_SCENE: str
SCRIPT_ACTION_REPEAT: str
SCRIPT_ACTION_CHOOSE: str
SCRIPT_ACTION_WAIT_FOR_TRIGGER: str
SCRIPT_ACTION_VARIABLES: str
SCRIPT_ACTION_STOP: str
SCRIPT_ACTION_IF: str
SCRIPT_ACTION_PARALLEL: str

def determine_script_action(action: dict[str, Any]) -> str: ...

ACTION_TYPE_SCHEMAS: dict[str, Callable[[Any], dict]]
currency: Incomplete
historic_currency: Incomplete
country: Incomplete
language: Incomplete
