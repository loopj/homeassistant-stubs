from _typeshed import Incomplete
from ipaddress import IPv4Address, IPv6Address

LOOPBACK_NETWORKS: Incomplete
PRIVATE_NETWORKS: Incomplete
LINK_LOCAL_NETWORKS: Incomplete

def is_loopback(address: IPv4Address | IPv6Address) -> bool: ...
def is_private(address: IPv4Address | IPv6Address) -> bool: ...
def is_link_local(address: IPv4Address | IPv6Address) -> bool: ...
def is_local(address: IPv4Address | IPv6Address) -> bool: ...
def is_invalid(address: IPv4Address | IPv6Address) -> bool: ...
def is_ip_address(address: str) -> bool: ...
def is_ipv4_address(address: str) -> bool: ...
def is_ipv6_address(address: str) -> bool: ...
def is_host_valid(host: str) -> bool: ...
def normalize_url(address: str) -> str: ...
