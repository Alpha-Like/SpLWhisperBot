from pyrogram import Client, filters, idle
from config import *
from pyrogram.types import InlineQueryResultArticle as IQRA, InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM, InputTextMessageContent as ITMC

yashu = Client("WHISPER-BOT", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

ALPHA = {}

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

res = [IQRA(title="Whisper", input_message_content=ITMC("[USERNAME | ID] [WHISPER]"))]
res1 = [IQRA(title="Whisper", input_message_content=ITMC("Invalid Username or Id !"))]

@yashu.on_inline_query()
async def inline(_, i):
    global ALPHA
    txt = i.query
    if not len(txt.split(None, 1)) == 2:
        await _.answer_inline_query(i.id, results=res, cache_time=0)
    try:
        tar = int(txt.split()[0])
    except:
        try:
            tar = (await _.get_users(txt.split()[0])).id
        except:
            await _.answer_inline_query(i.id, results=res1, cache_time=0)
    Na = (await _.get_users(tar)).first_name
    whisp = txt.split(None, 1)[1]
    WTXT = "A whisper has been sent to {}.\n\nOnly he / she can open it."
    SHOW = IKM([[IKB("Whisper ☁️", callback_data=f"{i.from_user.id}_{id}")]])
    res2 = [IQRA(title="Whisper", input_message_content=ITMC(WTXT.format(Na)), reply_markup=SHOW)]
    await _.answer_inline_query(i.id, results=res2, cache_time=0)
    ALPHA[[tar, i.from_user.id]] = whisp

@yashu.on_callback_query()
async def cbq(_, q):
    id = q.from_user.id
    mid = q.message.from_user.id
    if q.data != f"{mid}_{id}":
        return await q.answer("This is not for you baka !", show_alert=True)
    try:
        msg = ALPHA[[id, mid]]
    except:
        msg = "Whisper has been deleted from Database !"
    await q.answer(msg, show_alert=True)

yashu.start()
print("Started !")
idle()
    
