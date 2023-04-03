from .const import DEFAULT_CHANNEL as DEFAULT_CHANNEL, DOMAIN as DOMAIN
from .util import get_allowed_channel as get_allowed_channel
from _typeshed import Incomplete
from homeassistant.components.hassio import HassioServiceInfo as HassioServiceInfo
from homeassistant.components.thread import async_get_preferred_dataset as async_get_preferred_dataset
from homeassistant.config_entries import ConfigFlow as ConfigFlow, SOURCE_HASSIO as SOURCE_HASSIO
from homeassistant.const import CONF_URL as CONF_URL
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

_LOGGER: Incomplete

class OTBRConfigFlow(ConfigFlow):
    VERSION: int
    async def _connect_and_set_dataset(self, otbr_url: str) -> None: ...
    async def async_step_user(self, user_input: dict[str, str] | None = ...) -> FlowResult: ...
    async def async_step_hassio(self, discovery_info: HassioServiceInfo) -> FlowResult: ...
