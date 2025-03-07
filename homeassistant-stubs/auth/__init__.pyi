from . import auth_store as auth_store, jwt_wrapper as jwt_wrapper, models as models
from .const import ACCESS_TOKEN_EXPIRATION as ACCESS_TOKEN_EXPIRATION, GROUP_ID_ADMIN as GROUP_ID_ADMIN
from .mfa_modules import MultiFactorAuthModule as MultiFactorAuthModule, auth_mfa_module_from_config as auth_mfa_module_from_config
from .providers import AuthProvider as AuthProvider, LoginFlow as LoginFlow, auth_provider_from_config as auth_provider_from_config
from _typeshed import Incomplete
from datetime import timedelta
from homeassistant import data_entry_flow as data_entry_flow
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from typing import Any

EVENT_USER_ADDED: str
EVENT_USER_UPDATED: str
EVENT_USER_REMOVED: str
_MfaModuleDict = dict[str, MultiFactorAuthModule]
_ProviderKey: Incomplete
_ProviderDict = dict[_ProviderKey, AuthProvider]

class InvalidAuthError(Exception): ...
class InvalidProvider(Exception): ...

async def auth_manager_from_config(hass: HomeAssistant, provider_configs: list[dict[str, Any]], module_configs: list[dict[str, Any]]) -> AuthManager: ...

class AuthManagerFlowManager(data_entry_flow.FlowManager):
    auth_manager: Incomplete
    def __init__(self, hass: HomeAssistant, auth_manager: AuthManager) -> None: ...
    async def async_create_flow(self, handler_key: str, *, context: dict[str, Any] | None = ..., data: dict[str, Any] | None = ...) -> data_entry_flow.FlowHandler: ...
    async def async_finish_flow(self, flow: data_entry_flow.FlowHandler, result: FlowResult) -> FlowResult: ...

class AuthManager:
    hass: Incomplete
    _store: Incomplete
    _providers: Incomplete
    _mfa_modules: Incomplete
    login_flow: Incomplete
    _revoke_callbacks: Incomplete
    def __init__(self, hass: HomeAssistant, store: auth_store.AuthStore, providers: _ProviderDict, mfa_modules: _MfaModuleDict) -> None: ...
    @property
    def auth_providers(self) -> list[AuthProvider]: ...
    @property
    def auth_mfa_modules(self) -> list[MultiFactorAuthModule]: ...
    def get_auth_provider(self, provider_type: str, provider_id: str | None) -> AuthProvider | None: ...
    def get_auth_providers(self, provider_type: str) -> list[AuthProvider]: ...
    def get_auth_mfa_module(self, module_id: str) -> MultiFactorAuthModule | None: ...
    async def async_get_users(self) -> list[models.User]: ...
    async def async_get_user(self, user_id: str) -> models.User | None: ...
    async def async_get_owner(self) -> models.User | None: ...
    async def async_get_group(self, group_id: str) -> models.Group | None: ...
    async def async_get_user_by_credentials(self, credentials: models.Credentials) -> models.User | None: ...
    async def async_create_system_user(self, name: str, *, group_ids: list[str] | None = ..., local_only: bool | None = ...) -> models.User: ...
    async def async_create_user(self, name: str, *, group_ids: list[str] | None = ..., local_only: bool | None = ...) -> models.User: ...
    async def async_get_or_create_user(self, credentials: models.Credentials) -> models.User: ...
    async def async_link_user(self, user: models.User, credentials: models.Credentials) -> None: ...
    async def async_remove_user(self, user: models.User) -> None: ...
    async def async_update_user(self, user: models.User, name: str | None = ..., is_active: bool | None = ..., group_ids: list[str] | None = ..., local_only: bool | None = ...) -> None: ...
    async def async_activate_user(self, user: models.User) -> None: ...
    async def async_deactivate_user(self, user: models.User) -> None: ...
    async def async_remove_credentials(self, credentials: models.Credentials) -> None: ...
    async def async_enable_user_mfa(self, user: models.User, mfa_module_id: str, data: Any) -> None: ...
    async def async_disable_user_mfa(self, user: models.User, mfa_module_id: str) -> None: ...
    async def async_get_enabled_mfa(self, user: models.User) -> dict[str, str]: ...
    async def async_create_refresh_token(self, user: models.User, client_id: str | None = ..., client_name: str | None = ..., client_icon: str | None = ..., token_type: str | None = ..., access_token_expiration: timedelta = ..., credential: models.Credentials | None = ...) -> models.RefreshToken: ...
    async def async_get_refresh_token(self, token_id: str) -> models.RefreshToken | None: ...
    async def async_get_refresh_token_by_token(self, token: str) -> models.RefreshToken | None: ...
    async def async_remove_refresh_token(self, refresh_token: models.RefreshToken) -> None: ...
    def async_register_revoke_token_callback(self, refresh_token_id: str, revoke_callback: CALLBACK_TYPE) -> CALLBACK_TYPE: ...
    def async_create_access_token(self, refresh_token: models.RefreshToken, remote_ip: str | None = ...) -> str: ...
    def _async_resolve_provider(self, refresh_token: models.RefreshToken) -> AuthProvider | None: ...
    def async_validate_refresh_token(self, refresh_token: models.RefreshToken, remote_ip: str | None = ...) -> None: ...
    async def async_validate_access_token(self, token: str) -> models.RefreshToken | None: ...
    def _async_get_auth_provider(self, credentials: models.Credentials) -> AuthProvider | None: ...
    async def _user_should_be_owner(self) -> bool: ...
