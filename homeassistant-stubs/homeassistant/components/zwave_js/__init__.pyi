import asyncio
from .addon import AddonError as AddonError, AddonManager as AddonManager, get_addon_manager as get_addon_manager
from .api import async_register_api as async_register_api
from .const import ATTR_COMMAND_CLASS as ATTR_COMMAND_CLASS, ATTR_COMMAND_CLASS_NAME as ATTR_COMMAND_CLASS_NAME, ATTR_DEVICE_ID as ATTR_DEVICE_ID, ATTR_ENDPOINT as ATTR_ENDPOINT, ATTR_HOME_ID as ATTR_HOME_ID, ATTR_LABEL as ATTR_LABEL, ATTR_NODE_ID as ATTR_NODE_ID, ATTR_PARAMETERS as ATTR_PARAMETERS, ATTR_PROPERTY as ATTR_PROPERTY, ATTR_PROPERTY_KEY as ATTR_PROPERTY_KEY, ATTR_PROPERTY_KEY_NAME as ATTR_PROPERTY_KEY_NAME, ATTR_PROPERTY_NAME as ATTR_PROPERTY_NAME, ATTR_TYPE as ATTR_TYPE, ATTR_VALUE as ATTR_VALUE, ATTR_VALUE_RAW as ATTR_VALUE_RAW, CONF_INTEGRATION_CREATED_ADDON as CONF_INTEGRATION_CREATED_ADDON, CONF_NETWORK_KEY as CONF_NETWORK_KEY, CONF_USB_PATH as CONF_USB_PATH, CONF_USE_ADDON as CONF_USE_ADDON, DATA_CLIENT as DATA_CLIENT, DATA_UNSUBSCRIBE as DATA_UNSUBSCRIBE, DOMAIN as DOMAIN, EVENT_DEVICE_ADDED_TO_REGISTRY as EVENT_DEVICE_ADDED_TO_REGISTRY, LOGGER as LOGGER, PLATFORMS as PLATFORMS, ZWAVE_JS_EVENT as ZWAVE_JS_EVENT
from .discovery import async_discover_values as async_discover_values
from .helpers import get_device_id as get_device_id
from .migrate import async_migrate_discovered_value as async_migrate_discovered_value
from .services import ZWaveServices as ZWaveServices
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_DOMAIN as ATTR_DOMAIN, CONF_URL as CONF_URL, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import device_registry as device_registry, entity_registry as entity_registry
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from zwave_js_server.client import Client as ZwaveClient
from zwave_js_server.model.node import Node as ZwaveNode
from zwave_js_server.model.notification import Notification as Notification
from zwave_js_server.model.value import ValueNotification as ValueNotification

CONNECT_TIMEOUT: int
DATA_CLIENT_LISTEN_TASK: str
DATA_START_PLATFORM_TASK: str
DATA_CONNECT_FAILED_LOGGED: str
DATA_INVALID_SERVER_VERSION_LOGGED: str

async def async_setup(hass: HomeAssistant, config: dict) -> bool: ...
def register_node_in_dev_reg(hass: HomeAssistant, entry: ConfigEntry, dev_reg: device_registry.DeviceRegistry, client: ZwaveClient, node: ZwaveNode) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def client_listen(hass: HomeAssistant, entry: ConfigEntry, client: ZwaveClient, driver_ready: asyncio.Event) -> None: ...
async def disconnect_client(hass: HomeAssistant, entry: ConfigEntry, client: ZwaveClient, listen_task: asyncio.Task, platform_task: asyncio.Task) -> None: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_remove_entry(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
async def async_ensure_addon_running(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
def async_ensure_addon_updated(hass: HomeAssistant) -> None: ...
