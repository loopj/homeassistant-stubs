import av
from . import redact_credentials as redact_credentials
from .const import ATTR_SETTINGS as ATTR_SETTINGS, AUDIO_CODECS as AUDIO_CODECS, DOMAIN as DOMAIN, MAX_MISSING_DTS as MAX_MISSING_DTS, MAX_TIMESTAMP_GAP as MAX_TIMESTAMP_GAP, PACKETS_TO_WAIT_FOR_AUDIO as PACKETS_TO_WAIT_FOR_AUDIO, SEGMENT_CONTAINER_FORMAT as SEGMENT_CONTAINER_FORMAT, SOURCE_TIMEOUT as SOURCE_TIMEOUT
from .core import Part as Part, Segment as Segment, StreamOutput as StreamOutput, StreamSettings as StreamSettings
from collections.abc import Callable as Callable, Generator, Iterator, Mapping
from homeassistant.core import HomeAssistant as HomeAssistant
from io import BytesIO
from threading import Event
from typing import Any

_LOGGER: Any

class SegmentBuffer:
    _stream_id: int
    _hass: Any
    _outputs_callback: Any
    _sequence: int
    _segment_start_dts: Any
    _memory_file: Any
    _av_output: Any
    _input_video_stream: Any
    _input_audio_stream: Any
    _output_video_stream: Any
    _output_audio_stream: Any
    _segment: Any
    _memory_file_pos: Any
    _part_start_dts: Any
    _part_has_keyframe: bool
    _stream_settings: Any
    _start_time: Any
    def __init__(self, hass: HomeAssistant, outputs_callback: Callable[[], Mapping[str, StreamOutput]]) -> None: ...
    def make_new_av(self, memory_file: BytesIO, sequence: int, input_vstream: av.video.VideoStream) -> av.container.OutputContainer: ...
    def set_streams(self, video_stream: av.video.VideoStream, audio_stream: Any) -> None: ...
    def reset(self, video_dts: int) -> None: ...
    def mux_packet(self, packet: av.Packet) -> None: ...
    def check_flush_part(self, packet: av.Packet) -> None: ...
    def flush(self, packet: av.Packet, last_part: bool) -> None: ...
    def discontinuity(self) -> None: ...
    def close(self) -> None: ...

class PeekIterator(Iterator):
    _iterator: Any
    _buffer: Any
    _next: Any
    def __init__(self, iterator: Iterator[av.Packet]) -> None: ...
    def __iter__(self) -> Iterator: ...
    def __next__(self) -> av.Packet: ...
    def replace_underlying_iterator(self, new_iterator: Iterator) -> None: ...
    def _pop_buffer(self) -> av.Packet: ...
    def peek(self) -> Generator[av.Packet, None, None]: ...

class TimestampValidator:
    _last_dts: Any
    _missing_dts: int
    def __init__(self): ...
    def is_valid(self, packet: av.Packet) -> bool: ...

def is_keyframe(packet: av.Packet) -> Any: ...
def unsupported_audio(packets: Iterator[av.Packet], audio_stream: Any) -> bool: ...
def stream_worker(source: str, options: dict[str, str], segment_buffer: SegmentBuffer, quit_event: Event) -> None: ...
