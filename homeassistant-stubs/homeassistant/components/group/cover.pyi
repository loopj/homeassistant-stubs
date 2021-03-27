from . import GroupEntity as GroupEntity
from homeassistant.components.cover import ATTR_CURRENT_POSITION as ATTR_CURRENT_POSITION, ATTR_CURRENT_TILT_POSITION as ATTR_CURRENT_TILT_POSITION, ATTR_POSITION as ATTR_POSITION, ATTR_TILT_POSITION as ATTR_TILT_POSITION, CoverEntity as CoverEntity, DOMAIN as DOMAIN, PLATFORM_SCHEMA as PLATFORM_SCHEMA, SERVICE_CLOSE_COVER as SERVICE_CLOSE_COVER, SERVICE_CLOSE_COVER_TILT as SERVICE_CLOSE_COVER_TILT, SERVICE_OPEN_COVER as SERVICE_OPEN_COVER, SERVICE_OPEN_COVER_TILT as SERVICE_OPEN_COVER_TILT, SERVICE_SET_COVER_POSITION as SERVICE_SET_COVER_POSITION, SERVICE_SET_COVER_TILT_POSITION as SERVICE_SET_COVER_TILT_POSITION, SERVICE_STOP_COVER as SERVICE_STOP_COVER, SERVICE_STOP_COVER_TILT as SERVICE_STOP_COVER_TILT, SUPPORT_CLOSE as SUPPORT_CLOSE, SUPPORT_CLOSE_TILT as SUPPORT_CLOSE_TILT, SUPPORT_OPEN as SUPPORT_OPEN, SUPPORT_OPEN_TILT as SUPPORT_OPEN_TILT, SUPPORT_SET_POSITION as SUPPORT_SET_POSITION, SUPPORT_SET_TILT_POSITION as SUPPORT_SET_TILT_POSITION, SUPPORT_STOP as SUPPORT_STOP, SUPPORT_STOP_TILT as SUPPORT_STOP_TILT
from homeassistant.const import ATTR_ASSUMED_STATE as ATTR_ASSUMED_STATE, ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_SUPPORTED_FEATURES as ATTR_SUPPORTED_FEATURES, CONF_ENTITIES as CONF_ENTITIES, CONF_NAME as CONF_NAME, STATE_CLOSING as STATE_CLOSING, STATE_OPEN as STATE_OPEN, STATE_OPENING as STATE_OPENING
from homeassistant.core import CoreState as CoreState, State as State
from homeassistant.helpers.event import async_track_state_change_event as async_track_state_change_event
from typing import Any, Optional

KEY_OPEN_CLOSE: str
KEY_STOP: str
KEY_POSITION: str
DEFAULT_NAME: str

async def async_setup_platform(hass: Any, config: Any, async_add_entities: Any, discovery_info: Optional[Any] = ...) -> None: ...

class CoverGroup(GroupEntity, CoverEntity):
    def __init__(self, name: Any, entities: Any) -> None: ...
    async def async_update_supported_features(self, entity_id: str, new_state: Optional[State], update_state: bool=...) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @property
    def name(self): ...
    @property
    def assumed_state(self): ...
    @property
    def supported_features(self): ...
    @property
    def is_closed(self): ...
    @property
    def is_opening(self): ...
    @property
    def is_closing(self): ...
    @property
    def current_cover_position(self) -> Optional[int]: ...
    @property
    def current_cover_tilt_position(self): ...
    @property
    def device_state_attributes(self): ...
    async def async_open_cover(self, **kwargs: Any) -> None: ...
    async def async_close_cover(self, **kwargs: Any) -> None: ...
    async def async_stop_cover(self, **kwargs: Any) -> None: ...
    async def async_set_cover_position(self, **kwargs: Any) -> None: ...
    async def async_open_cover_tilt(self, **kwargs: Any) -> None: ...
    async def async_close_cover_tilt(self, **kwargs: Any) -> None: ...
    async def async_stop_cover_tilt(self, **kwargs: Any) -> None: ...
    async def async_set_cover_tilt_position(self, **kwargs: Any) -> None: ...
    async def async_update(self) -> None: ...
