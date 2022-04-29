from _typeshed import Incomplete
from homeassistant.backports.enum import StrEnum as StrEnum
from homeassistant.const import Platform as Platform
from typing import Literal

class MeshRoles(StrEnum):
    NONE: str
    MASTER: str
    SLAVE: str

DOMAIN: str
PLATFORMS: Incomplete
CONF_OLD_DISCOVERY: str
DEFAULT_CONF_OLD_DISCOVERY: bool
DATA_FRITZ: str
DSL_CONNECTION: Literal['dsl']
DEFAULT_DEVICE_NAME: str
DEFAULT_HOST: str
DEFAULT_PORT: int
DEFAULT_USERNAME: str
ERROR_AUTH_INVALID: str
ERROR_CANNOT_CONNECT: str
ERROR_UPNP_NOT_CONFIGURED: str
ERROR_UNKNOWN: str
FRITZ_SERVICES: str
SERVICE_REBOOT: str
SERVICE_RECONNECT: str
SERVICE_CLEANUP: str
SERVICE_SET_GUEST_WIFI_PW: str
SWITCH_TYPE_DEFLECTION: str
SWITCH_TYPE_PORTFORWARD: str
SWITCH_TYPE_PROFILE: str
SWITCH_TYPE_WIFINETWORK: str
UPTIME_DEVIATION: int
FRITZ_EXCEPTIONS: Incomplete
WIFI_STANDARD: Incomplete
