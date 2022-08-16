#!/usr/src/env python
# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy import Boolean, Column, String, MetaData, Table

meta = MetaData()

settings = Table(
    "settings", meta,
    Column("id", String, primary_key=True),
    Column("key", String, nullable=False, unique=True),
    Column("value", String),
    Column("status", Boolean),
)

containers = Table(
    "containers", meta,
    Column("id", String, primary_key=True),
    Column("name", String, nullable=False, unique=True),
    Column("image", String),
    Column("status", String),
    Column("ports", String),
    Column("created", String),
    Column("started", String),
    Column("finished", String),
    Column("duration", String),
    Column("command", String),
    Column("args", String),
    Column("env", String),
    Column("volumes", String),
    Column("networks", String),
)

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    echo=True,
    connect_args={"check_same_thread": False}
)


def get_table(table_name: str) -> Table:
    return Table(table_name, meta, autoload=True, autoload_with=engine)
