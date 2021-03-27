import types
from ..auth_store import AuthStore as AuthStore
from ..const import MFA_SESSION_EXPIRATION as MFA_SESSION_EXPIRATION
from ..models import Credentials as Credentials, RefreshToken as RefreshToken, User as User, UserMeta as UserMeta
from homeassistant import data_entry_flow as data_entry_flow, requirements as requirements
from homeassistant.const import CONF_ID as CONF_ID, CONF_NAME as CONF_NAME, CONF_TYPE as CONF_TYPE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.util.decorator import Registry as Registry
from typing import Any, Dict, List, Optional

DATA_REQS: str
AUTH_PROVIDERS: Any
AUTH_PROVIDER_SCHEMA: Any

class AuthProvider:
    DEFAULT_TITLE: str = ...
    hass: Any = ...
    store: Any = ...
    config: Any = ...
    def __init__(self, hass: HomeAssistant, store: AuthStore, config: Dict[str, Any]) -> None: ...
    @property
    def id(self) -> Optional[str]: ...
    @property
    def type(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def support_mfa(self) -> bool: ...
    async def async_credentials(self) -> List[Credentials]: ...
    def async_create_credentials(self, data: Dict[str, str]) -> Credentials: ...
    async def async_login_flow(self, context: Optional[Dict]) -> LoginFlow: ...
    async def async_get_or_create_credentials(self, flow_result: Dict[str, str]) -> Credentials: ...
    async def async_user_meta_for_credentials(self, credentials: Credentials) -> UserMeta: ...
    async def async_initialize(self) -> None: ...
    def async_validate_refresh_token(self, refresh_token: RefreshToken, remote_ip: Optional[str]=...) -> None: ...

async def auth_provider_from_config(hass: HomeAssistant, store: AuthStore, config: Dict[str, Any]) -> AuthProvider: ...
async def load_auth_provider_module(hass: HomeAssistant, provider: str) -> types.ModuleType: ...

class LoginFlow(data_entry_flow.FlowHandler):
    available_mfa_modules: Any = ...
    created_at: Any = ...
    invalid_mfa_times: int = ...
    user: Any = ...
    credential: Any = ...
    def __init__(self, auth_provider: AuthProvider) -> None: ...
    async def async_step_init(self, user_input: Optional[Dict[str, str]]=...) -> Dict[str, Any]: ...
    async def async_step_select_mfa_module(self, user_input: Optional[Dict[str, str]]=...) -> Dict[str, Any]: ...
    async def async_step_mfa(self, user_input: Optional[Dict[str, str]]=...) -> Dict[str, Any]: ...
    async def async_finish(self, flow_result: Any) -> Dict: ...
