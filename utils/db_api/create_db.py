import asyncio

from data import config
from utils.db_api import quick_commands
from utils.db_api.db_gino import db


async def test():
    await db.set_bind(bind=config.POSTGRES_URI)
    await db.gino.drop_all()
    await db.gino.create_all()


loop = asyncio.get_event_loop()
loop.run_until_complete(test())
