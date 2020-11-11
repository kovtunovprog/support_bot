from sqlalchemy import Column, BigInteger, String, Integer, Text, sql

from utils.db_api.db_gino import BaseModel


class Message(BaseModel):
    __tablename__ = 'temp_chat_history'
    id = Column(BigInteger, unique=True, primary_key=True)
    web_chat_id = Column(String(100), unique=False)
    full_name = Column(String(100), unique=False)
    operator_id = Column(Integer, nullable=True)
    support_chat = Column(Integer)
    msg = Column(Text)

    query: sql
