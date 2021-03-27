from homeassistant.components import http as http
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.loader import bind_hass as bind_hass
from homeassistant.util.network import is_ip_address as is_ip_address, is_loopback as is_loopback, normalize_url as normalize_url

TYPE_URL_INTERNAL: str
TYPE_URL_EXTERNAL: str

class NoURLAvailableError(HomeAssistantError): ...

def is_internal_request(hass: HomeAssistant) -> bool: ...
def get_url(hass: HomeAssistant, *, require_current_request: bool=..., require_ssl: bool=..., require_standard_port: bool=..., allow_internal: bool=..., allow_external: bool=..., allow_cloud: bool=..., allow_ip: bool=..., prefer_external: bool=..., prefer_cloud: bool=...) -> str: ...
