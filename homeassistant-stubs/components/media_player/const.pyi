from _typeshed import Incomplete
from enum import IntEnum

CONTENT_AUTH_EXPIRY_TIME: Incomplete
ATTR_APP_ID: str
ATTR_APP_NAME: str
ATTR_ENTITY_PICTURE_LOCAL: str
ATTR_GROUP_MEMBERS: str
ATTR_INPUT_SOURCE: str
ATTR_INPUT_SOURCE_LIST: str
ATTR_MEDIA_ALBUM_ARTIST: str
ATTR_MEDIA_ALBUM_NAME: str
ATTR_MEDIA_ARTIST: str
ATTR_MEDIA_CHANNEL: str
ATTR_MEDIA_CONTENT_ID: str
ATTR_MEDIA_CONTENT_TYPE: str
ATTR_MEDIA_DURATION: str
ATTR_MEDIA_ENQUEUE: str
ATTR_MEDIA_EXTRA: str
ATTR_MEDIA_EPISODE: str
ATTR_MEDIA_PLAYLIST: str
ATTR_MEDIA_POSITION: str
ATTR_MEDIA_POSITION_UPDATED_AT: str
ATTR_MEDIA_REPEAT: str
ATTR_MEDIA_SEASON: str
ATTR_MEDIA_SEEK_POSITION: str
ATTR_MEDIA_SERIES_TITLE: str
ATTR_MEDIA_SHUFFLE: str
ATTR_MEDIA_TITLE: str
ATTR_MEDIA_TRACK: str
ATTR_MEDIA_VOLUME_LEVEL: str
ATTR_MEDIA_VOLUME_MUTED: str
ATTR_SOUND_MODE: str
ATTR_SOUND_MODE_LIST: str
DOMAIN: str
MEDIA_CLASS_ALBUM: str
MEDIA_CLASS_APP: str
MEDIA_CLASS_ARTIST: str
MEDIA_CLASS_CHANNEL: str
MEDIA_CLASS_COMPOSER: str
MEDIA_CLASS_CONTRIBUTING_ARTIST: str
MEDIA_CLASS_DIRECTORY: str
MEDIA_CLASS_EPISODE: str
MEDIA_CLASS_GAME: str
MEDIA_CLASS_GENRE: str
MEDIA_CLASS_IMAGE: str
MEDIA_CLASS_MOVIE: str
MEDIA_CLASS_MUSIC: str
MEDIA_CLASS_PLAYLIST: str
MEDIA_CLASS_PODCAST: str
MEDIA_CLASS_SEASON: str
MEDIA_CLASS_TRACK: str
MEDIA_CLASS_TV_SHOW: str
MEDIA_CLASS_URL: str
MEDIA_CLASS_VIDEO: str
MEDIA_TYPE_ALBUM: str
MEDIA_TYPE_APP: str
MEDIA_TYPE_APPS: str
MEDIA_TYPE_ARTIST: str
MEDIA_TYPE_CHANNEL: str
MEDIA_TYPE_CHANNELS: str
MEDIA_TYPE_COMPOSER: str
MEDIA_TYPE_CONTRIBUTING_ARTIST: str
MEDIA_TYPE_EPISODE: str
MEDIA_TYPE_GAME: str
MEDIA_TYPE_GENRE: str
MEDIA_TYPE_IMAGE: str
MEDIA_TYPE_MOVIE: str
MEDIA_TYPE_MUSIC: str
MEDIA_TYPE_PLAYLIST: str
MEDIA_TYPE_PODCAST: str
MEDIA_TYPE_SEASON: str
MEDIA_TYPE_TRACK: str
MEDIA_TYPE_TVSHOW: str
MEDIA_TYPE_URL: str
MEDIA_TYPE_VIDEO: str
SERVICE_CLEAR_PLAYLIST: str
SERVICE_JOIN: str
SERVICE_PLAY_MEDIA: str
SERVICE_SELECT_SOUND_MODE: str
SERVICE_SELECT_SOURCE: str
SERVICE_UNJOIN: str
REPEAT_MODE_ALL: str
REPEAT_MODE_OFF: str
REPEAT_MODE_ONE: str
REPEAT_MODES: Incomplete

class MediaPlayerEntityFeature(IntEnum):
    PAUSE: int
    SEEK: int
    VOLUME_SET: int
    VOLUME_MUTE: int
    PREVIOUS_TRACK: int
    NEXT_TRACK: int
    TURN_ON: int
    TURN_OFF: int
    PLAY_MEDIA: int
    VOLUME_STEP: int
    SELECT_SOURCE: int
    STOP: int
    CLEAR_PLAYLIST: int
    PLAY: int
    SHUFFLE_SET: int
    SELECT_SOUND_MODE: int
    BROWSE_MEDIA: int
    REPEAT_SET: int
    GROUPING: int

SUPPORT_PAUSE: int
SUPPORT_SEEK: int
SUPPORT_VOLUME_SET: int
SUPPORT_VOLUME_MUTE: int
SUPPORT_PREVIOUS_TRACK: int
SUPPORT_NEXT_TRACK: int
SUPPORT_TURN_ON: int
SUPPORT_TURN_OFF: int
SUPPORT_PLAY_MEDIA: int
SUPPORT_VOLUME_STEP: int
SUPPORT_SELECT_SOURCE: int
SUPPORT_STOP: int
SUPPORT_CLEAR_PLAYLIST: int
SUPPORT_PLAY: int
SUPPORT_SHUFFLE_SET: int
SUPPORT_SELECT_SOUND_MODE: int
SUPPORT_BROWSE_MEDIA: int
SUPPORT_REPEAT_SET: int
SUPPORT_GROUPING: int
