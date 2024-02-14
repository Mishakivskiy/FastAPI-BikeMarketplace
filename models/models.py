import datetime
from sqlalchemy import MetaData, Integer, String, ForeignKey, Table, Column, JSON, TIMESTAMP

metadata = MetaData()

roles = Table(
    "roles",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('permissions', JSON),
)

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("first_name", String, nullable=False),
    Column("last_name", String, nullable=False),
    Column("email", String, nullable=False),
    Column("password", String, nullable=False),
    Column("register_at", TIMESTAMP, default=datetime.datetime.utcnow),
    Column('role_id', Integer, ForeignKey('roles.id')),
)
