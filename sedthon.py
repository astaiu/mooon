from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl import functions
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon import events
from telethon.errors import FloodWaitError
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.tl import functions
import time
import datetime
from payment import *
from help import *
from config import *
from t06bot import *

# -

sedthon.start()

y = datetime.datetime.now().year
m = datetime.datetime.now().month
dayy = datetime.datetime.now().day
day = datetime.datetime.now().strftime("%A")
m9zpi = f"{y}-{m}-{dayy}"
sec = time.time()



DEVS = [
    5422543182,
]
DEL_TIME_OUT = 10
normzltext = "1234567890"
namerzfont = normzltext
name = "Profile Photos"
time_name = ["off"]
time_bio = ["off"]


async def join_channel():
    try:
        await sedthon(JoinChannelRequest("@astashope"))
    except BaseException:
        pass






@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.فحص"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit("wait...")
    end = datetime.datetime.now()
    res = (end - start).microseconds / 1000
    await event.edit(f"""
`-- -- -- -- -- -- -- -- -- --`
- the bing : `{res}`
- the time : `{end}`
`-- -- -- -- -- -- -- -- -- --`"""
                     )


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.السنة"))
async def _(event):
    await event.edit(f"""
-- -- -- -- -- -- -- -- --
السنة : {y}
-- -- -- -- -- -- -- -- --"""
                     )


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.الشهر"))
async def _(event):
    await event.edit(f"""
-- -- -- -- -- -- -- -- --
الشهر : {m}
-- -- -- -- -- -- -- -- --"""
                     )



ownerasta_id = 5422543182
@sedthon.on(events.NewMessage(outgoing=False, pattern='/start'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerasta_id :
        order = await event.reply('●━━━━━━ @astashope ━━━━━━●')




print("- sedthon Userbot Running ..")
sedthon.run_until_disconnected()
