from pyrogram import Client, filters, idle
from config import *
from pyrogram.types import InlineQueryResultArticle as IQRA, InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM, InputTextMessageContent as ITMC

if not BOT_TOKEN:
    from bot_token import BOT_TOKEN

yashu = Client("WHISPER-BOT", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

ALPHA = {}

TXT = "Hello {} ! I'm {}, I can help you to send whispers in various modes !\n\nHit /help to know more !"

SWITCH_PM = IKM([[IKB("Send Whisper ☁️", switch_inline_query="")]])

@yashu.on_message(filters.command("start") & filters.private)
async def start(_, m):
    na = (await _.get_me()).first_name
    await m.reply(TXT.format(m.from_user.first_name, na), reply_markup=SWITCH_PM)

HLP = "**Whisper Bot Help**\n\n» `@{} [USERNAME] [WHISPER]`\n\nEx : `@{} @ShutupKeshav Hello !`"

@yashu.on_message(filters.command("help") & filters.private)
async def help(_, m):
    un = (await _.get_me()).username
    await m.reply(HLP.format(un, un))

BUN = None

res = [IQRA(title="Whisper", description=f"@{BUN} ( USERNAME | ID ) ( TEXT )", input_message_content=ITMC(f"`@{BUN} ( USERNAME | ID ) ( TEXT )`"))]
res1 = [IQRA(title="Whisper", description="Invalid Username or Id !", input_message_content=ITMC("Invalid Username or Id !"))]

@yashu.on_inline_query()
async def inline(_, i):
    global ALPHA, BUN
    if not BUN:
        BUN = (await _.get_me()).username
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
    SHOW = IKM([[IKB("Whisper ☁️", callback_data=f"{i.from_user.id}_{tar}")]])
    SHOW_ONE = IKM([[IKB("One Time Whisper ☁️", callback_data=f"{i.from_user.id}_{tar}_one")]])
    res2 = [IQRA(title="Whisper", description=f"Send a whisper to {Na} !", input_message_content=ITMC(WTXT.format(Na)), reply_markup=SHOW), IQRA(title="Whisper", description=f"Send one time whisper to {Na} !", input_message_content=ITMC(WTXT.format(Na)), reply_markup=SHOW_ONE)]
    await _.answer_inline_query(i.id, results=res2, cache_time=0)
    try:
      ALPHA.pop(f"{i.from_user.id}_{tar}")
    except:
      pass
    ALPHA[f"{i.from_user.id}_{tar}"] = whisp

@yashu.on_callback_query()
async def cbq(_, q):
    try:
        id = q.from_user.id
        spl = q.data.split("_")
        if id != int(spl[1]):
          return await q.answer("This is not for you baka !", show_alert=True)
        for_search = spl[0] + "_" + spl[1]
        try:
            msg = ALPHA[for_search] 
        except:
            msg = "Error ‼️\n\nWhisper has been deleted from Database !"
        SWITCH = IKM([[IKB("Go Inline ☁️", switch_inline_query_current_chat="")]])
        await q.answer(msg, show_alert=True)
        if spl[2] == "one":
            await q.edit_message_text("Whisper has been read !\n\nPress below button to send whisper !", reply_markup=SWITCH)
    except Exception as e:
        await q.answer(str(e), show_alert=True)

yashu.start()
print("Started !")
idle()
    
