from . import AUTH_PROVIDERS as AUTH_PROVIDERS, AUTH_PROVIDER_SCHEMA as AUTH_PROVIDER_SCHEMA, AuthProvider as AuthProvider, LoginFlow as LoginFlow
from ..models import Credentials as Credentials, UserMeta as UserMeta
from homeassistant.core import callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from typing import Any, Dict, Optional

USER_SCHEMA: Any
CONFIG_SCHEMA: Any

class InvalidAuthError(HomeAssistantError): ...

class ExampleAuthProvider(AuthProvider):
    async def async_login_flow(self, context: Optional[Dict]) -> LoginFlow: ...
    def async_validate_login(self, username: str, password: str) -> None: ...
    async def async_get_or_create_credentials(self, flow_result: Dict[str, str]) -> Credentials: ...
    async def async_user_meta_for_credentials(self, credentials: Credentials) -> UserMeta: ...

class ExampleLoginFlow(LoginFlow):
    async def async_step_init(self, user_input: Optional[Dict[str, str]]=...) -> Dict[str, Any]: ...
