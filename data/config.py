import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))

DATABASE = str(os.getenv("DATABASE"))
PGUSER = str(os.getenv("PGUSER"))
PGPASSWORD = str(os.getenv("PGPASSWORD"))

TEH_DEP_CHANNEL_ID = str(os.getenv("TEH_DEP_CHANNEL_ID"))
SET_DEP_CHANNEL_ID = str(os.getenv("SET_DEP_CHANNEL_ID"))
CALL_CENTER_CHANNEL_ID = str(os.getenv("CALL_CENTER_CHANNEL_ID"))

admins = [
    os.getenv("ADMIN_ID"),
]

ip = os.getenv("ip")

SQLITE_URI = ''

POSTGRES_URI = f"postgresql://{PGUSER}:{PGPASSWORD}@{ip}/{DATABASE}"