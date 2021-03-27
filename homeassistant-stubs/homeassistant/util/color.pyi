from typing import Any, List, Optional, Tuple

COLORS: Any

class XYPoint:
    x: float = ...
    y: float = ...
    def __init__(self, x: Any, y: Any) -> None: ...
    def __lt__(self, other: Any) -> Any: ...
    def __le__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def __ge__(self, other: Any) -> Any: ...

class GamutType:
    red: XYPoint = ...
    green: XYPoint = ...
    blue: XYPoint = ...
    def __init__(self, red: Any, green: Any, blue: Any) -> None: ...
    def __lt__(self, other: Any) -> Any: ...
    def __le__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def __ge__(self, other: Any) -> Any: ...

def color_name_to_rgb(color_name: str) -> Tuple[int, int, int]: ...
def color_RGB_to_xy(iR: int, iG: int, iB: int, Gamut: Optional[GamutType]=...) -> Tuple[float, float]: ...
def color_RGB_to_xy_brightness(iR: int, iG: int, iB: int, Gamut: Optional[GamutType]=...) -> Tuple[float, float, int]: ...
def color_xy_to_RGB(vX: float, vY: float, Gamut: Optional[GamutType]=...) -> Tuple[int, int, int]: ...
def color_xy_brightness_to_RGB(vX: float, vY: float, ibrightness: int, Gamut: Optional[GamutType]=...) -> Tuple[int, int, int]: ...
def color_hsb_to_RGB(fH: float, fS: float, fB: float) -> Tuple[int, int, int]: ...
def color_RGB_to_hsv(iR: float, iG: float, iB: float) -> Tuple[float, float, float]: ...
def color_RGB_to_hs(iR: float, iG: float, iB: float) -> Tuple[float, float]: ...
def color_hsv_to_RGB(iH: float, iS: float, iV: float) -> Tuple[int, int, int]: ...
def color_hs_to_RGB(iH: float, iS: float) -> Tuple[int, int, int]: ...
def color_xy_to_hs(vX: float, vY: float, Gamut: Optional[GamutType]=...) -> Tuple[float, float]: ...
def color_hs_to_xy(iH: float, iS: float, Gamut: Optional[GamutType]=...) -> Tuple[float, float]: ...
def color_rgb_to_rgbw(r: int, g: int, b: int) -> Tuple[int, int, int, int]: ...
def color_rgbw_to_rgb(r: int, g: int, b: int, w: int) -> Tuple[int, int, int]: ...
def color_rgb_to_hex(r: int, g: int, b: int) -> str: ...
def rgb_hex_to_rgb_list(hex_string: str) -> List[int]: ...
def color_temperature_to_hs(color_temperature_kelvin: float) -> Tuple[float, float]: ...
def color_temperature_to_rgb(color_temperature_kelvin: float) -> Tuple[float, float, float]: ...
def color_temperature_mired_to_kelvin(mired_temperature: float) -> float: ...
def color_temperature_kelvin_to_mired(kelvin_temperature: float) -> float: ...
def cross_product(p1: XYPoint, p2: XYPoint) -> float: ...
def get_distance_between_two_points(one: XYPoint, two: XYPoint) -> float: ...
def get_closest_point_to_line(A: XYPoint, B: XYPoint, P: XYPoint) -> XYPoint: ...
def get_closest_point_to_point(xy_tuple: Tuple[float, float], Gamut: GamutType) -> Tuple[float, float]: ...
def check_point_in_lamps_reach(p: Tuple[float, float], Gamut: GamutType) -> bool: ...
def check_valid_gamut(Gamut: GamutType) -> bool: ...
