import ifaddr
from .const import MDNS_TARGET_IP as MDNS_TARGET_IP
from .models import Adapter as Adapter, IPv4ConfiguredAddress as IPv4ConfiguredAddress, IPv6ConfiguredAddress as IPv6ConfiguredAddress
from _typeshed import Incomplete
from homeassistant.core import callback as callback
from ipaddress import IPv4Address, IPv6Address

_LOGGER: Incomplete

async def async_load_adapters() -> list[Adapter]: ...
def enable_adapters(adapters: list[Adapter], enabled_interfaces: list[str]) -> bool: ...
def enable_auto_detected_adapters(adapters: list[Adapter]) -> None: ...
def _adapter_has_external_address(adapter: Adapter) -> bool: ...
def _has_external_address(ip_str: str) -> bool: ...
def _ip_address_is_external(ip_addr: Union[IPv4Address, IPv6Address]) -> bool: ...
def _reset_enabled_adapters(adapters: list[Adapter]) -> None: ...
def _ifaddr_adapter_to_ha(adapter: ifaddr.Adapter, next_hop_address: Union[None, IPv4Address, IPv6Address]) -> Adapter: ...
def _ip_v6_from_adapter(ip_config: ifaddr.IP) -> IPv6ConfiguredAddress: ...
def _ip_v4_from_adapter(ip_config: ifaddr.IP) -> IPv4ConfiguredAddress: ...
def async_get_source_ip(target_ip: str) -> Union[str, None]: ...
