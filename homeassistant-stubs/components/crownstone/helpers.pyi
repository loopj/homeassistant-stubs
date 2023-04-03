from .const import DONT_USE_USB as DONT_USE_USB, MANUAL_PATH as MANUAL_PATH, REFRESH_LIST as REFRESH_LIST
from homeassistant.components import usb as usb
from serial.tools.list_ports_common import ListPortInfo as ListPortInfo

def list_ports_as_str(serial_ports: list[ListPortInfo], no_usb_option: bool = ...) -> list[str]: ...
def get_port(dev_path: str) -> str | None: ...
def map_from_to(val: int, in_min: int, in_max: int, out_min: int, out_max: int) -> int: ...
