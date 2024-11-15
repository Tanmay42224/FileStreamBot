from pyrogram import Client
from ..vars import Var

StreamBot = Client(
    "Web Streamer",  # Session name as the first argument
    api_id=Var.API_ID,
    api_hash=Var.API_HASH,
    bot_token=Var.BOT_TOKEN,
    sleep_threshold=Var.SLEEP_THRESHOLD,
    workers=Var.WORKERS
)
