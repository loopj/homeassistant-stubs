from .const import CONF_APP_KEY as CONF_APP_KEY, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.const import CONF_API_KEY as CONF_API_KEY
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers import aiohttp_client as aiohttp_client

class AmbientStationFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION: int
    data_schema: Incomplete
    def __init__(self) -> None: ...
    async def _show_form(self, errors: dict | None = ...) -> FlowResult: ...
    async def async_step_user(self, user_input: dict | None = ...) -> FlowResult: ...
