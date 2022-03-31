from .const import DOMAIN as DOMAIN, EXCLUDE_FROM_BACKUP as EXCLUDE_FROM_BACKUP, LOGGER as LOGGER
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import integration_platform as integration_platform
from homeassistant.util import dt as dt
from pathlib import Path
from typing import Any

class Backup:
    slug: str
    name: str
    date: str
    path: Path
    size: float
    def as_dict(self) -> dict: ...
    def __init__(self, slug, name, date, path, size) -> None: ...

class BackupPlatformProtocol:
    async def async_pre_backup(self, hass: HomeAssistant) -> None: ...
    async def async_post_backup(self, hass: HomeAssistant) -> None: ...

class BackupManager:
    hass: Any
    backup_dir: Any
    backing_up: bool
    backups: Any
    platforms: Any
    loaded_backups: bool
    loaded_platforms: bool
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def _add_platform(self, hass: HomeAssistant, integration_domain: str, platform: BackupPlatformProtocol) -> None: ...
    async def load_backups(self) -> None: ...
    async def load_platforms(self) -> None: ...
    def _read_backups(self) -> dict[str, Backup]: ...
    async def get_backups(self) -> dict[str, Backup]: ...
    async def get_backup(self, slug: str) -> Union[Backup, None]: ...
    async def remove_backup(self, slug: str) -> None: ...
    async def generate_backup(self) -> Backup: ...
    def _generate_backup_contents(self, tar_file_path: Path, backup_data: dict[str, Any]) -> None: ...

def _generate_slug(date: str, name: str) -> str: ...
