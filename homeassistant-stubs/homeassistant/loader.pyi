import pathlib
from awesomeversion import AwesomeVersion
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.generated.dhcp import DHCP as DHCP
from homeassistant.generated.mqtt import MQTT as MQTT
from homeassistant.generated.ssdp import SSDP as SSDP
from homeassistant.generated.zeroconf import HOMEKIT as HOMEKIT, ZEROCONF as ZEROCONF
from types import ModuleType
from typing import Any, Callable, Dict, List, Optional, Set, TypeVar, TypedDict, Union

CALLABLE_T = TypeVar('CALLABLE_T', bound=Callable[..., Any])
DATA_COMPONENTS: str
DATA_INTEGRATIONS: str
DATA_CUSTOM_COMPONENTS: str
PACKAGE_CUSTOM_COMPONENTS: str
PACKAGE_BUILTIN: str
CUSTOM_WARNING: str
CUSTOM_WARNING_VERSION_MISSING: str
CUSTOM_WARNING_VERSION_TYPE: str
MAX_LOAD_CONCURRENTLY: int

class Manifest(TypedDict):
    name: str
    disabled: str
    domain: str
    dependencies: List[str]
    after_dependencies: List[str]
    requirements: List[str]
    config_flow: bool
    documentation: str
    issue_tracker: str
    quality_scale: str
    mqtt: List[str]
    ssdp: List[Dict[str, str]]
    zeroconf: List[Union[str, Dict[str, str]]]
    dhcp: List[Dict[str, str]]
    homekit: Dict[str, List[str]]
    is_built_in: bool
    version: str
    codeowners: List[str]

def manifest_from_legacy_module(domain: str, module: ModuleType) -> Manifest: ...
async def async_get_custom_components(hass: HomeAssistant) -> Dict[str, Integration]: ...
async def async_get_config_flows(hass: HomeAssistant) -> Set[str]: ...
async def async_get_zeroconf(hass: HomeAssistant) -> Dict[str, List[Dict[str, str]]]: ...
async def async_get_dhcp(hass: HomeAssistant) -> List[Dict[str, str]]: ...
async def async_get_homekit(hass: HomeAssistant) -> Dict[str, str]: ...
async def async_get_ssdp(hass: HomeAssistant) -> Dict[str, List[Dict[str, str]]]: ...
async def async_get_mqtt(hass: HomeAssistant) -> Dict[str, List[str]]: ...

class Integration:
    @classmethod
    def resolve_from_root(cls: Any, hass: HomeAssistant, root_module: ModuleType, domain: str) -> Optional[Integration]: ...
    @classmethod
    def resolve_legacy(cls: Any, hass: HomeAssistant, domain: str) -> Optional[Integration]: ...
    hass: Any = ...
    pkg_path: Any = ...
    file_path: Any = ...
    manifest: Any = ...
    def __init__(self, hass: HomeAssistant, pkg_path: str, file_path: pathlib.Path, manifest: Manifest) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def disabled(self) -> Optional[str]: ...
    @property
    def domain(self) -> str: ...
    @property
    def dependencies(self) -> List[str]: ...
    @property
    def after_dependencies(self) -> List[str]: ...
    @property
    def requirements(self) -> List[str]: ...
    @property
    def config_flow(self) -> bool: ...
    @property
    def documentation(self) -> Optional[str]: ...
    @property
    def issue_tracker(self) -> Optional[str]: ...
    @property
    def quality_scale(self) -> Optional[str]: ...
    @property
    def mqtt(self) -> Optional[List[str]]: ...
    @property
    def ssdp(self) -> Optional[List[Dict[str, str]]]: ...
    @property
    def zeroconf(self) -> Optional[List[Union[str, Dict[str, str]]]]: ...
    @property
    def dhcp(self) -> Optional[List[Dict[str, str]]]: ...
    @property
    def homekit(self) -> Optional[Dict[str, List[str]]]: ...
    @property
    def is_built_in(self) -> bool: ...
    @property
    def version(self) -> Optional[AwesomeVersion]: ...
    @property
    def all_dependencies(self) -> Set[str]: ...
    @property
    def all_dependencies_resolved(self) -> bool: ...
    async def resolve_dependencies(self) -> bool: ...
    def get_component(self) -> ModuleType: ...
    def get_platform(self, platform_name: str) -> ModuleType: ...

async def async_get_integration(hass: HomeAssistant, domain: str) -> Integration: ...

class LoaderError(Exception): ...

class IntegrationNotFound(LoaderError):
    domain: Any = ...
    def __init__(self, domain: str) -> None: ...

class CircularDependency(LoaderError):
    from_domain: Any = ...
    to_domain: Any = ...
    def __init__(self, from_domain: str, to_domain: str) -> None: ...

class ModuleWrapper:
    def __init__(self, hass: HomeAssistant, module: ModuleType) -> None: ...
    def __getattr__(self, attr: str) -> Any: ...

class Components:
    def __init__(self, hass: HomeAssistant) -> None: ...
    def __getattr__(self, comp_name: str) -> ModuleWrapper: ...

class Helpers:
    def __init__(self, hass: HomeAssistant) -> None: ...
    def __getattr__(self, helper_name: str) -> ModuleWrapper: ...

def bind_hass(func: CALLABLE_T) -> CALLABLE_T: ...
def validate_custom_integration_version(version: str) -> bool: ...
def custom_integration_warning(integration: Integration) -> None: ...
