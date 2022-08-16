#!/usr/src/env python
# -*- coding: utf-8 -*-
from typing import Any

import sqlalchemy

from logger import logger
from sql_app.database import engine, meta, get_table
from sqlalchemy import select, Table

table_name: str = "settings"
settings_data: Table = get_table(table_name)


def check_table_settings() -> bool:
    try:
        response: bool = sqlalchemy.inspect(engine).has_table(table_name)
        if response:
            logger.debug(f'table {table_name} exists')
        else:
            logger.debug(f'table {table_name} does not exist')
            create_table_settings()
        return response
    except Exception as e:
        logger.error(e)
        return False
    finally:
        engine.dispose()


def create_table_settings():
    connection = engine.connect()
    try:
        logger.debug(f'Creating table settings')
        meta.create_all(engine)
        query = select([settings_data])
        result = connection.execute(query)
        result_set = result.fetchall()
        logger.info(f"Database version: {result_set}")
    except Exception as e:
        logger.error(e)
    finally:
        connection.close()
        engine.dispose()


def insert_settings(parameter, value, status):
    connection = engine.connect()
    try:
        query = settings_data.insert().values(parameter=parameter, value=value, status=status)
        result = connection.execute(query)
        logger.info(f"Inserted {result.rowcount} row(s)")
    except Exception as e:
        logger.error(e)
    finally:
        connection.close()
        engine.dispose()


def find_all():
    connection = engine.connect()
    try:
        query = select([settings_data])
        result = connection.execute(query)
        result_set = result.fetchall()
        logger.info(f"Settings: {result_set}")
    except Exception as e:
        logger.error(e)
    finally:
        connection.close()
        engine.dispose()


def find_one(parameter) -> Any or None:
    connection = engine.connect()
    try:
        query = select([settings_data]).where(settings_data.c.parameter == parameter)
        result = connection.execute(query)
        result_set = result.fetchall()
        logger.info(f"Setting: {result_set}")
        return result_set[0]
    except Exception as e:
        logger.error(e)
        return None
    finally:
        connection.close()
        engine.dispose()