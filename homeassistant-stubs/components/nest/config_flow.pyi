import logging
from . import api as api
from .const import CONF_CLOUD_PROJECT_ID as CONF_CLOUD_PROJECT_ID, CONF_PROJECT_ID as CONF_PROJECT_ID, CONF_SUBSCRIBER_ID as CONF_SUBSCRIBER_ID, DATA_NEST_CONFIG as DATA_NEST_CONFIG, DATA_SDM as DATA_SDM, DOMAIN as DOMAIN, OAUTH2_AUTHORIZE as OAUTH2_AUTHORIZE, SDM_SCOPES as SDM_SCOPES
from _typeshed import Incomplete
from collections.abc import Iterable, Mapping
from google_nest_sdm.structure import Structure as Structure
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_REAUTH as SOURCE_REAUTH
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers import config_entry_oauth2_flow as config_entry_oauth2_flow
from homeassistant.util import get_random_string as get_random_string
from typing import Any

DATA_FLOW_IMPL: str
SUBSCRIPTION_FORMAT: str
SUBSCRIPTION_RAND_LENGTH: int
MORE_INFO_URL: str
CLOUD_CONSOLE_URL: str
SDM_API_URL: str
PUBSUB_API_URL: str
DEVICE_ACCESS_CONSOLE_URL: str
DEVICE_ACCESS_CONSOLE_EDIT_URL: str
_LOGGER: Incomplete

def _generate_subscription_id(cloud_project_id: str) -> str: ...
def generate_config_title(structures: Iterable[Structure]) -> str | None: ...

class NestFlowHandler(config_entry_oauth2_flow.AbstractOAuth2FlowHandler, domain=DOMAIN):
    DOMAIN = DOMAIN
    VERSION: int
    _data: Incomplete
    _structure_config_title: Incomplete
    def __init__(self) -> None: ...
    def _async_reauth_entry(self) -> ConfigEntry | None: ...
    @property
    def logger(self) -> logging.Logger: ...
    @property
    def extra_authorize_data(self) -> dict[str, str]: ...
    async def async_generate_authorize_url(self) -> str: ...
    async def async_oauth_create_entry(self, data: dict[str, Any]) -> FlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> FlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_create_cloud_project(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_cloud_project(self, user_input: dict | None = ...) -> FlowResult: ...
    async def async_step_device_project(self, user_input: dict | None = ...) -> FlowResult: ...
    async def async_step_pubsub(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_finish(self, data: dict[str, Any] | None = ...) -> FlowResult: ...
