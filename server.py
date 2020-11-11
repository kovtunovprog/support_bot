import asyncio
import json

import aiogram
import aiohttp_jinja2
import jinja2
import socketio
import logging

from aiogram.utils.exceptions import ChatIdIsEmpty
from aiohttp import web

from data import config
from handlers import dp
from utils.db_api.db_gino import start_connection
from utils.db_api.quick_commands import add_message, select_chat_messages, get_operator_id, delete_chat_history_from_user
from utils.send_to_channel import send_first_msg, send_message_to_operator

logging.basicConfig(level=logging.DEBUG)

routes = web.RouteTableDef()
server = web.Application()
sio = socketio.AsyncServer(async_mode='aiohttp')
sio.attach(server)

aiohttp_jinja2.setup(server, loader=jinja2.FileSystemLoader('template'))


@routes.get('/')
@aiohttp_jinja2.template('index.html')
async def index(request):
    return {}


@routes.get('/api/operator')
class ApiOperatorView(web.View):
    async def get(self):
        response = self.request.json
        data = await self.request.json()
        print(data)
        await send_user_message(web_chat_id=data['web_chat_id'], msg=data['msg'])
        return 200


@sio.on('user message')
async def user_message(sid, data):
    web_chat_id = data['data']['chat_id']
    msg = data['data']['message']
    full_name = data['data']['full_name']
    support_group = data['data']['support_group']
    await start_connection(dp)
    await add_message(
        web_chat_id=web_chat_id,
        support_chat=1,
        msg=msg,
        full_name=full_name
    )

    chat = await select_chat_messages(web_chat_id=web_chat_id)
    if len(list(chat)) < 2:
        # Отправляет только первое сообщение в чат
        await send_first_msg(dp=dp, support_group=support_group, web_chat_id=web_chat_id, msg=msg, full_name=full_name)
        return
    else:
        operator_id = await get_operator_id(web_chat_id=web_chat_id)
        await send_message_to_operator(dp=dp, chat_id=operator_id, msg=msg)
        return


@sio.on('')
async def send_user_message(web_chat_id: str, msg: str):
    await sio.emit(
        'operator message', {
            'data': {
                "web_chat_id": web_chat_id,
                "message": msg
            }},
    )


@sio.on('close')
async def test_connect(sid, data):
    print(data)
    web_chat_id = data['data']['web_chat_id']
    message = 'Пользователь вышел из чата'
    await start_connection(dp)
    try:
        operator_id = await get_operator_id(web_chat_id=web_chat_id)
        await send_message_to_operator(dp=dp, chat_id=operator_id, msg=message)
    except ChatIdIsEmpty:
        pass
    await delete_chat_history_from_user(web_chat_id)


server.add_routes(routes)


if __name__ == '__main__':
    web.run_app(server)
