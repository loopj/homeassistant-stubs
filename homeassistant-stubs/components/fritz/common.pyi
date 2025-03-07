from .const import CONF_OLD_DISCOVERY as CONF_OLD_DISCOVERY, DEFAULT_CONF_OLD_DISCOVERY as DEFAULT_CONF_OLD_DISCOVERY, DEFAULT_DEVICE_NAME as DEFAULT_DEVICE_NAME, DEFAULT_HOST as DEFAULT_HOST, DEFAULT_PORT as DEFAULT_PORT, DEFAULT_USERNAME as DEFAULT_USERNAME, DOMAIN as DOMAIN, FRITZ_EXCEPTIONS as FRITZ_EXCEPTIONS, MeshRoles as MeshRoles, SERVICE_CLEANUP as SERVICE_CLEANUP, SERVICE_REBOOT as SERVICE_REBOOT, SERVICE_RECONNECT as SERVICE_RECONNECT, SERVICE_SET_GUEST_WIFI_PW as SERVICE_SET_GUEST_WIFI_PW
from _typeshed import Incomplete
from collections.abc import Callable, ValuesView
from datetime import datetime
from fritzconnection.lib.fritzstatus import FritzStatus
from homeassistant.components.device_tracker import CONF_CONSIDER_HOME as CONF_CONSIDER_HOME, DEFAULT_CONSIDER_HOME as DEFAULT_CONSIDER_HOME
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import entity_registry as er, update_coordinator as update_coordinator
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, EntityDescription as EntityDescription
from homeassistant.helpers.typing import StateType as StateType
from types import MappingProxyType
from typing import Any, TypedDict

_LOGGER: Incomplete

def _is_tracked(mac: str, current_devices: ValuesView) -> bool: ...
def device_filter_out_from_trackers(mac: str, device: FritzDevice, current_devices: ValuesView) -> bool: ...
def _cleanup_entity_filter(device: er.RegistryEntry) -> bool: ...
def _ha_is_stopping(activity: str) -> None: ...

class ClassSetupMissing(Exception):
    def __init__(self) -> None: ...

class Device:
    connected: bool
    connected_to: str
    connection_type: str
    ip_address: str
    name: str
    ssid: str | None
    wan_access: bool | None
    def __init__(self, connected, connected_to, connection_type, ip_address, name, ssid, wan_access) -> None: ...
    def __mypy-replace(*, connected, connected_to, connection_type, ip_address, name, ssid, wan_access) -> None: ...

class Interface(TypedDict):
    device: str
    mac: str
    op_mode: str
    ssid: str | None
    type: str

HostAttributes = TypedDict('HostAttributes', {'Index': int, 'IPAddress': str, 'MACAddress': str, 'Active': bool, 'HostName': str, 'InterfaceType': str, 'X_AVM-DE_Port': int, 'X_AVM-DE_Speed': int, 'X_AVM-DE_UpdateAvailable': bool, 'X_AVM-DE_UpdateSuccessful': str, 'X_AVM-DE_InfoURL': str | None, 'X_AVM-DE_MACAddressList': str | None, 'X_AVM-DE_Model': str | None, 'X_AVM-DE_URL': str | None, 'X_AVM-DE_Guest': bool, 'X_AVM-DE_RequestClient': str, 'X_AVM-DE_VPN': bool, 'X_AVM-DE_WANAccess': str, 'X_AVM-DE_Disallow': bool, 'X_AVM-DE_IsMeshable': str, 'X_AVM-DE_Priority': str, 'X_AVM-DE_FriendlyName': str, 'X_AVM-DE_FriendlyNameIsWriteable': str})

class HostInfo(TypedDict):
    mac: str
    name: str
    ip: str
    status: bool

class UpdateCoordinatorDataType(TypedDict):
    call_deflections: dict[int, dict]
    entity_states: dict[str, StateType | bool]

class FritzBoxTools(update_coordinator.DataUpdateCoordinator[UpdateCoordinatorDataType]):
    _devices: Incomplete
    _options: Incomplete
    _unique_id: Incomplete
    connection: Incomplete
    fritz_guest_wifi: Incomplete
    fritz_hosts: Incomplete
    fritz_status: Incomplete
    hass: Incomplete
    host: Incomplete
    mesh_role: Incomplete
    device_conn_type: Incomplete
    device_is_router: bool
    password: Incomplete
    port: Incomplete
    username: Incomplete
    has_call_deflections: bool
    _model: Incomplete
    _current_firmware: Incomplete
    _latest_firmware: Incomplete
    _update_available: bool
    _release_url: Incomplete
    _entity_update_functions: Incomplete
    def __init__(self, hass: HomeAssistant, password: str, username: str = ..., host: str = ..., port: int = ...) -> None: ...
    async def async_setup(self, options: MappingProxyType[str, Any] | None = ...) -> None: ...
    def setup(self) -> None: ...
    def register_entity_updates(self, key: str, update_fn: Callable[[FritzStatus, StateType], Any]) -> Callable[[], None]: ...
    async def _async_update_data(self) -> UpdateCoordinatorDataType: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def model(self) -> str: ...
    @property
    def current_firmware(self) -> str: ...
    @property
    def latest_firmware(self) -> str | None: ...
    @property
    def update_available(self) -> bool: ...
    @property
    def release_url(self) -> str | None: ...
    @property
    def mac(self) -> str: ...
    @property
    def devices(self) -> dict[str, FritzDevice]: ...
    @property
    def signal_device_new(self) -> str: ...
    @property
    def signal_device_update(self) -> str: ...
    async def _async_get_wan_access(self, ip_address: str) -> bool | None: ...
    async def _async_update_hosts_info(self) -> dict[str, Device]: ...
    def _update_device_info(self) -> tuple[bool, str | None, str | None]: ...
    async def _async_update_device_info(self) -> tuple[bool, str | None, str | None]: ...
    async def async_update_call_deflections(self) -> dict[int, dict[str, Any]]: ...
    def manage_device_info(self, dev_info: Device, dev_mac: str, consider_home: bool) -> bool: ...
    async def async_send_signal_device_update(self, new_device: bool) -> None: ...
    async def async_scan_devices(self, now: datetime | None = ...) -> None: ...
    async def async_trigger_firmware_update(self) -> bool: ...
    async def async_trigger_reboot(self) -> None: ...
    async def async_trigger_reconnect(self) -> None: ...
    async def async_trigger_set_guest_password(self, password: str | None, length: int) -> None: ...
    async def async_trigger_cleanup(self, config_entry: ConfigEntry | None = ...) -> None: ...
    def _async_remove_empty_devices(self, entity_reg: er.EntityRegistry, config_entry: ConfigEntry) -> None: ...
    async def service_fritzbox(self, service_call: ServiceCall, config_entry: ConfigEntry) -> None: ...

class AvmWrapper(FritzBoxTools):
    async def _async_service_call(self, service_name: str, service_suffix: str, action_name: str, **kwargs: Any) -> dict: ...
    async def async_get_upnp_configuration(self) -> dict[str, Any]: ...
    async def async_get_wan_link_properties(self) -> dict[str, Any]: ...
    async def async_ipv6_active(self) -> bool: ...
    async def async_get_connection_info(self) -> ConnectionInfo: ...
    async def async_get_num_port_mapping(self, con_type: str) -> dict[str, Any]: ...
    async def async_get_port_mapping(self, con_type: str, index: int) -> dict[str, Any]: ...
    async def async_get_wlan_configuration(self, index: int) -> dict[str, Any]: ...
    async def async_set_wlan_configuration(self, index: int, turn_on: bool) -> dict[str, Any]: ...
    async def async_set_deflection_enable(self, index: int, turn_on: bool) -> dict[str, Any]: ...
    async def async_add_port_mapping(self, con_type: str, port_mapping: Any) -> dict[str, Any]: ...
    async def async_set_allow_wan_access(self, ip_address: str, turn_on: bool) -> dict[str, Any]: ...

class FritzData:
    tracked: dict
    profile_switches: dict
    def __init__(self, tracked, profile_switches) -> None: ...
    def __mypy-replace(*, tracked, profile_switches) -> None: ...

class FritzDeviceBase(update_coordinator.CoordinatorEntity[AvmWrapper]):
    _avm_wrapper: Incomplete
    _mac: Incomplete
    _name: Incomplete
    def __init__(self, avm_wrapper: AvmWrapper, device: FritzDevice) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def ip_address(self) -> str | None: ...
    @property
    def mac_address(self) -> str: ...
    @property
    def hostname(self) -> str | None: ...
    async def async_process_update(self) -> None: ...
    async def async_on_demand_update(self) -> None: ...

class FritzDevice:
    _connected: bool
    _connected_to: Incomplete
    _connection_type: Incomplete
    _ip_address: Incomplete
    _last_activity: Incomplete
    _mac: Incomplete
    _name: Incomplete
    _ssid: Incomplete
    _wan_access: bool
    def __init__(self, mac: str, name: str) -> None: ...
    def update(self, dev_info: Device, consider_home: float) -> None: ...
    @property
    def connected_to(self) -> str | None: ...
    @property
    def connection_type(self) -> str | None: ...
    @property
    def is_connected(self) -> bool: ...
    @property
    def mac_address(self) -> str: ...
    @property
    def hostname(self) -> str: ...
    @property
    def ip_address(self) -> str | None: ...
    @property
    def last_activity(self) -> datetime | None: ...
    @property
    def ssid(self) -> str | None: ...
    @property
    def wan_access(self) -> bool | None: ...

class SwitchInfo(TypedDict):
    description: str
    friendly_name: str
    icon: str
    type: str
    callback_update: Callable
    callback_switch: Callable

class FritzBoxBaseEntity:
    _avm_wrapper: Incomplete
    _device_name: Incomplete
    def __init__(self, avm_wrapper: AvmWrapper, device_name: str) -> None: ...
    @property
    def mac_address(self) -> str: ...
    @property
    def device_info(self) -> DeviceInfo: ...

class FritzRequireKeysMixin:
    value_fn: Callable[[FritzStatus, Any], Any]
    def __init__(self, value_fn) -> None: ...
    def __mypy-replace(*, value_fn) -> None: ...

class FritzEntityDescription(EntityDescription, FritzRequireKeysMixin):
    def __init__(self, value_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...
    def __mypy-replace(*, value_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

class FritzBoxBaseCoordinatorEntity(update_coordinator.CoordinatorEntity[AvmWrapper]):
    entity_description: FritzEntityDescription
    _attr_has_entity_name: bool
    _device_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, avm_wrapper: AvmWrapper, device_name: str, description: FritzEntityDescription) -> None: ...
    @property
    def device_info(self) -> DeviceInfo: ...

class ConnectionInfo:
    connection: str
    mesh_role: MeshRoles
    wan_enabled: bool
    ipv6_active: bool
    def __init__(self, connection, mesh_role, wan_enabled, ipv6_active) -> None: ...
    def __mypy-replace(*, connection, mesh_role, wan_enabled, ipv6_active) -> None: ...
