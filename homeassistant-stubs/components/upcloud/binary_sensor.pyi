from . import CONF_SERVERS as CONF_SERVERS, DATA_UPCLOUD as DATA_UPCLOUD, UpCloudServerEntity as UpCloudServerEntity
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, PLATFORM_SCHEMA as PLATFORM_SCHEMA
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class UpCloudBinarySensor(UpCloudServerEntity, BinarySensorEntity): ...
