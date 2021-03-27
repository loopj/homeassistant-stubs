from aiohttp import web
from homeassistant.components.http import HomeAssistantView as HomeAssistantView
from homeassistant.components.media_player.const import ATTR_MEDIA_CONTENT_ID as ATTR_MEDIA_CONTENT_ID, ATTR_MEDIA_CONTENT_TYPE as ATTR_MEDIA_CONTENT_TYPE, MEDIA_TYPE_MUSIC as MEDIA_TYPE_MUSIC, SERVICE_PLAY_MEDIA as SERVICE_PLAY_MEDIA
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_NAME as CONF_NAME, CONF_PLATFORM as CONF_PLATFORM, HTTP_BAD_REQUEST as HTTP_BAD_REQUEST, HTTP_NOT_FOUND as HTTP_NOT_FOUND
from homeassistant.core import callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import config_per_platform as config_per_platform, discovery as discovery
from homeassistant.helpers.network import get_url as get_url
from homeassistant.helpers.service import async_set_service_schema as async_set_service_schema
from homeassistant.helpers.typing import HomeAssistantType as HomeAssistantType
from homeassistant.loader import async_get_integration as async_get_integration
from homeassistant.setup import async_prepare_setup_platform as async_prepare_setup_platform
from homeassistant.util.yaml import load_yaml as load_yaml
from typing import Any, Optional

ATTR_CACHE: str
ATTR_LANGUAGE: str
ATTR_MESSAGE: str
ATTR_OPTIONS: str
ATTR_PLATFORM: str
BASE_URL_KEY: str
CONF_BASE_URL: str
CONF_CACHE: str
CONF_CACHE_DIR: str
CONF_LANG: str
CONF_SERVICE_NAME: str
CONF_TIME_MEMORY: str
CONF_DESCRIPTION: str
CONF_FIELDS: str
DEFAULT_CACHE: bool
DEFAULT_CACHE_DIR: str
DEFAULT_TIME_MEMORY: int
DOMAIN: str
MEM_CACHE_FILENAME: str
MEM_CACHE_VOICE: str
SERVICE_CLEAR_CACHE: str
SERVICE_SAY: str
KEY_PATTERN: str
PLATFORM_SCHEMA: Any
PLATFORM_SCHEMA_BASE: Any
SCHEMA_SERVICE_SAY: Any
SCHEMA_SERVICE_CLEAR_CACHE: Any

async def async_setup(hass: Any, config: Any): ...

class SpeechManager:
    hass: Any = ...
    providers: Any = ...
    use_cache: Any = ...
    cache_dir: Any = ...
    time_memory: Any = ...
    base_url: Any = ...
    file_cache: Any = ...
    mem_cache: Any = ...
    def __init__(self, hass: Any) -> None: ...
    async def async_init_cache(self, use_cache: Any, cache_dir: Any, time_memory: Any, base_url: Any) -> None: ...
    async def async_clear_cache(self) -> None: ...
    def async_register_engine(self, engine: Any, provider: Any, config: Any) -> None: ...
    async def async_get_url_path(self, engine: Any, message: Any, cache: Optional[Any] = ..., language: Optional[Any] = ..., options: Optional[Any] = ...): ...
    async def async_get_tts_audio(self, engine: Any, key: Any, message: Any, cache: Any, language: Any, options: Any): ...
    async def async_save_tts_audio(self, key: Any, filename: Any, data: Any) -> None: ...
    async def async_file_to_mem(self, key: Any): ...
    async def async_read_tts(self, filename: Any): ...
    @staticmethod
    def write_tags(filename: Any, data: Any, provider: Any, message: Any, language: Any, options: Any): ...

class Provider:
    hass: Optional[HomeAssistantType] = ...
    name: Optional[str] = ...
    @property
    def default_language(self) -> None: ...
    @property
    def supported_languages(self) -> None: ...
    @property
    def supported_options(self) -> None: ...
    @property
    def default_options(self) -> None: ...
    def get_tts_audio(self, message: Any, language: Any, options: Optional[Any] = ...) -> None: ...
    async def async_get_tts_audio(self, message: Any, language: Any, options: Optional[Any] = ...): ...

class TextToSpeechUrlView(HomeAssistantView):
    requires_auth: bool = ...
    url: str = ...
    name: str = ...
    tts: Any = ...
    def __init__(self, tts: Any) -> None: ...
    async def post(self, request: web.Request) -> web.Response: ...

class TextToSpeechView(HomeAssistantView):
    requires_auth: bool = ...
    url: str = ...
    name: str = ...
    tts: Any = ...
    def __init__(self, tts: Any) -> None: ...
    async def get(self, request: web.Request, filename: str) -> web.Response: ...

def get_base_url(hass: Any): ...
