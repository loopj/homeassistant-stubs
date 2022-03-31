from .const import CALL_TYPE_COIL as CALL_TYPE_COIL, CALL_TYPE_DISCRETE as CALL_TYPE_DISCRETE, CALL_TYPE_REGISTER_HOLDING as CALL_TYPE_REGISTER_HOLDING, CALL_TYPE_REGISTER_INPUT as CALL_TYPE_REGISTER_INPUT, CALL_TYPE_X_COILS as CALL_TYPE_X_COILS, CALL_TYPE_X_REGISTER_HOLDINGS as CALL_TYPE_X_REGISTER_HOLDINGS, CONF_BAUDRATE as CONF_BAUDRATE, CONF_BYTESIZE as CONF_BYTESIZE, CONF_CLIMATES as CONF_CLIMATES, CONF_CLOSE_COMM_ON_ERROR as CONF_CLOSE_COMM_ON_ERROR, CONF_DATA_TYPE as CONF_DATA_TYPE, CONF_FANS as CONF_FANS, CONF_INPUT_TYPE as CONF_INPUT_TYPE, CONF_LAZY_ERROR as CONF_LAZY_ERROR, CONF_MAX_TEMP as CONF_MAX_TEMP, CONF_MIN_TEMP as CONF_MIN_TEMP, CONF_MSG_WAIT as CONF_MSG_WAIT, CONF_PARITY as CONF_PARITY, CONF_PRECISION as CONF_PRECISION, CONF_RETRIES as CONF_RETRIES, CONF_RETRY_ON_EMPTY as CONF_RETRY_ON_EMPTY, CONF_SCALE as CONF_SCALE, CONF_SLAVE_COUNT as CONF_SLAVE_COUNT, CONF_STATE_CLOSED as CONF_STATE_CLOSED, CONF_STATE_CLOSING as CONF_STATE_CLOSING, CONF_STATE_OFF as CONF_STATE_OFF, CONF_STATE_ON as CONF_STATE_ON, CONF_STATE_OPEN as CONF_STATE_OPEN, CONF_STATE_OPENING as CONF_STATE_OPENING, CONF_STATUS_REGISTER as CONF_STATUS_REGISTER, CONF_STATUS_REGISTER_TYPE as CONF_STATUS_REGISTER_TYPE, CONF_STEP as CONF_STEP, CONF_STOPBITS as CONF_STOPBITS, CONF_SWAP as CONF_SWAP, CONF_SWAP_BYTE as CONF_SWAP_BYTE, CONF_SWAP_NONE as CONF_SWAP_NONE, CONF_SWAP_WORD as CONF_SWAP_WORD, CONF_SWAP_WORD_BYTE as CONF_SWAP_WORD_BYTE, CONF_TARGET_TEMP as CONF_TARGET_TEMP, CONF_VERIFY as CONF_VERIFY, CONF_WRITE_TYPE as CONF_WRITE_TYPE, DEFAULT_HUB as DEFAULT_HUB, DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL, DEFAULT_TEMP_UNIT as DEFAULT_TEMP_UNIT, DataType as DataType, RTUOVERTCP as RTUOVERTCP, SERIAL as SERIAL, TCP as TCP, UDP as UDP
from .modbus import ModbusHub as ModbusHub, async_modbus_setup as async_modbus_setup
from .validators import duplicate_entity_validator as duplicate_entity_validator, duplicate_modbus_validator as duplicate_modbus_validator, number_validator as number_validator, scan_interval_validator as scan_interval_validator, struct_validator as struct_validator
from homeassistant.components.sensor import CONF_STATE_CLASS as CONF_STATE_CLASS
from homeassistant.const import CONF_ADDRESS as CONF_ADDRESS, CONF_BINARY_SENSORS as CONF_BINARY_SENSORS, CONF_COMMAND_OFF as CONF_COMMAND_OFF, CONF_COMMAND_ON as CONF_COMMAND_ON, CONF_COUNT as CONF_COUNT, CONF_COVERS as CONF_COVERS, CONF_DELAY as CONF_DELAY, CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_HOST as CONF_HOST, CONF_LIGHTS as CONF_LIGHTS, CONF_METHOD as CONF_METHOD, CONF_NAME as CONF_NAME, CONF_OFFSET as CONF_OFFSET, CONF_PORT as CONF_PORT, CONF_SCAN_INTERVAL as CONF_SCAN_INTERVAL, CONF_SENSORS as CONF_SENSORS, CONF_SLAVE as CONF_SLAVE, CONF_STRUCTURE as CONF_STRUCTURE, CONF_SWITCHES as CONF_SWITCHES, CONF_TEMPERATURE_UNIT as CONF_TEMPERATURE_UNIT, CONF_TIMEOUT as CONF_TIMEOUT, CONF_TYPE as CONF_TYPE, CONF_UNIQUE_ID as CONF_UNIQUE_ID, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

_LOGGER: Any
BASE_SCHEMA: Any
BASE_COMPONENT_SCHEMA: Any
BASE_STRUCT_SCHEMA: Any
BASE_SWITCH_SCHEMA: Any
CLIMATE_SCHEMA: Any
COVERS_SCHEMA: Any
SWITCH_SCHEMA: Any
LIGHT_SCHEMA: Any
FAN_SCHEMA: Any
SENSOR_SCHEMA: Any
BINARY_SENSOR_SCHEMA: Any
MODBUS_SCHEMA: Any
SERIAL_SCHEMA: Any
ETHERNET_SCHEMA: Any
CONFIG_SCHEMA: Any

def get_hub(hass: HomeAssistant, name: str) -> ModbusHub: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_reset_platform(hass: HomeAssistant, integration_name: str) -> None: ...
