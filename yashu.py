from pyrogram import Client, filters, idle
from config import *

yashu = Client("WHISPER-BOT", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


TXT = "Hello {} ! I'm {}, I can help you to send whispers in various modes !\n\Hit /help to know more !"

@yashu.on_message(filters.command("start") & filters.private)
async def start(_, m):
    na = (await _.get_me()).first_name
    await m.reply(TXT.format(m.from_user.first_name, na))

HLP = "**Whisper Bot**\n\n» @{} [USERNAME] [WHISPER]\n\nEx : `@{} @ShutupKeshav Hello !`"

@yashu.on_message(filters.command("help") & filters.private)
async def help(_, m):
    un = (await _.get_me()).username
    await m.reply(HLP.format(un, un))

