import datetime
from typing import List

from aiogram import Dispatcher
from gino import Gino
from sqlalchemy import Table, inspect, Column, DateTime

from data import config

db = Gino()


class BaseModel(db.Model):
    __abstract__ = True

    def __str__(self):
        model = self.__class__.__name__
        table: Table = inspect(self.__class__)
        primary_key_columns: List[Column] = table.primary_key.columns
        values = {
            column.name: getattr(self, self._column_name_map[column.name])
            for column in primary_key_columns
        }

        values_str = " ".join(f"{name}={value!r}" for name, value in values.items())
        return f"<{model} {values_str}>"


async def start_connection(dispatcher: Dispatcher):
    print('Устанавливаю связи с PostgreSQL')
    await db.set_bind(config.POSTGRES_URI)
