from sqlalchemy.orm.session import Session as Session

def db_size_bytes(session: Session, database_name: str) -> float | None: ...
