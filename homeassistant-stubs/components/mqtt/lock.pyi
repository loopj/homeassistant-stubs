import voluptuous as vol
from . import subscription as subscription
from .config import MQTT_RW_SCHEMA as MQTT_RW_SCHEMA
from .const import CONF_COMMAND_TOPIC as CONF_COMMAND_TOPIC, CONF_ENCODING as CONF_ENCODING, CONF_QOS as CONF_QOS, CONF_RETAIN as CONF_RETAIN, CONF_STATE_TOPIC as CONF_STATE_TOPIC
from .debug_info import log_messages as log_messages
from .mixins import MQTT_ENTITY_COMMON_SCHEMA as MQTT_ENTITY_COMMON_SCHEMA, MqttEntity as MqttEntity, async_setup_entry_helper as async_setup_entry_helper, warn_for_legacy_schema as warn_for_legacy_schema
from .models import MqttValueTemplate as MqttValueTemplate, ReceiveMessage as ReceiveMessage, ReceivePayloadType as ReceivePayloadType
from .util import get_mqtt_data as get_mqtt_data
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components import lock as lock
from homeassistant.components.lock import LockEntity as LockEntity, LockEntityFeature as LockEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_OPTIMISTIC as CONF_OPTIMISTIC, CONF_VALUE_TEMPLATE as CONF_VALUE_TEMPLATE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

CONF_PAYLOAD_LOCK: str
CONF_PAYLOAD_UNLOCK: str
CONF_PAYLOAD_OPEN: str
CONF_STATE_LOCKED: str
CONF_STATE_UNLOCKED: str
DEFAULT_NAME: str
DEFAULT_OPTIMISTIC: bool
DEFAULT_PAYLOAD_LOCK: str
DEFAULT_PAYLOAD_UNLOCK: str
DEFAULT_PAYLOAD_OPEN: str
DEFAULT_STATE_LOCKED: str
DEFAULT_STATE_UNLOCKED: str
MQTT_LOCK_ATTRIBUTES_BLOCKED: Incomplete
PLATFORM_SCHEMA_MODERN: Incomplete
PLATFORM_SCHEMA: Incomplete
DISCOVERY_SCHEMA: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
async def _async_setup_entity(hass: HomeAssistant, async_add_entities: AddEntitiesCallback, config: ConfigType, config_entry: ConfigEntry, discovery_data: Union[DiscoveryInfoType, None] = ...) -> None: ...

class MqttLock(MqttEntity, LockEntity):
    _entity_id_format: Incomplete
    _attributes_extra_blocked: Incomplete
    _optimistic: bool
    _value_template: Callable[[ReceivePayloadType], ReceivePayloadType]
    _attr_is_locked: bool
    def __init__(self, hass: HomeAssistant, config: ConfigType, config_entry: ConfigEntry, discovery_data: Union[DiscoveryInfoType, None]) -> None: ...
    @staticmethod
    def config_schema() -> vol.Schema: ...
    _attr_supported_features: Incomplete
    def _setup_from_config(self, config: ConfigType) -> None: ...
    _sub_state: Incomplete
    def _prepare_subscribe_topics(self) -> None: ...
    async def _subscribe_topics(self) -> None: ...
    @property
    def assumed_state(self) -> bool: ...
    async def async_lock(self, **kwargs: Any) -> None: ...
    async def async_unlock(self, **kwargs: Any) -> None: ...
    async def async_open(self, **kwargs: Any) -> None: ...
