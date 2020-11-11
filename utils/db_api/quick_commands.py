from utils.db_api.schemas.message import Message


async def add_message(web_chat_id: str, support_chat: int, msg: str, operator_id: int = None, full_name: str = None):
    """Добавляет сообщение в историю чата"""
    if full_name is None:
        user_name = 'anonymous user'
    message = Message(web_chat_id=web_chat_id, support_chat=support_chat, msg=msg, operator_id=operator_id,
                      full_name=full_name)
    await message.create()


async def select_chat_messages(web_chat_id: str):
    """Выборка сообщений по конкретному"""
    messages = await Message.query.where(Message.web_chat_id == web_chat_id).gino.all()
    return messages


async def get_web_chat_id(operator_id: int):
    """Получить айди чата"""
    message = await Message.query.where(Message.operator_id == operator_id).gino.first()
    return message.web_chat_id


async def get_operator_id(web_chat_id: str):
    """Получить айди оператора"""
    message = await Message.query.where(Message.web_chat_id == web_chat_id).gino.first()
    return message.operator_id


async def delete_chat_history_from_user(web_chat_id: str):
    """Удаление истории чата пользователем"""
    await Message.delete.where(Message.web_chat_id == web_chat_id).gino.all()


async def delete_chat_history_from_operator(operator_id: int):
    """Удаление истории чата оператором"""
    await Message.delete.where(Message.operator_id == operator_id).gino.all()