from homeassistant.components.recorder.filters import Filters as Filters
from homeassistant.helpers.entityfilter import EntityFilter as EntityFilter

class HistoryConfig:
    sqlalchemy_filter: Filters | None
    entity_filter: EntityFilter | None
    def __init__(self, sqlalchemy_filter, entity_filter) -> None: ...
