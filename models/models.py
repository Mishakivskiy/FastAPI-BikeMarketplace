import datetime
from sqlalchemy import MetaData, Integer, String, Table, Column, TIMESTAMP, Boolean

metadata = MetaData()

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("first_name", String, nullable=False),
    Column("last_name", String, nullable=False),
    Column("email", String, nullable=False),
    Column("hashed_password", String, nullable=False),
    Column("register_at", TIMESTAMP, default=datetime.datetime.utcnow),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False),
)
