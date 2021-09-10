# By @Purushottam-6668

from .worker import *


async def up(event):
    if not event.is_private:
        return
    stt = dt.now()
    ed = dt.now()
    v = ts(int((ed - uptime).seconds) * 1000)
    ms = (ed - stt).microseconds / 1000
    p = f"இᏢing = {ms}ms"
    await event.reply(v + "\n" + p)


async def start(event):
    ok = await event.client(GetFullUserRequest(event.sender_id))
    await event.reply(
        f"Hi `{ok.user.first_name}`\nᎢhis is Ꭺ ᏞiʙᏟᴏʍᴩrᴇssᴏrᏴᴏᴛ Ꮃhiᴄh Ꮯᴀn Ꭼnᴄᴏdᴇ Ꮩidᴇᴏs.\nᏒᴇduᴄᴇ Ꮪizᴇ ᴏf Ꮩidᴇᴏs Ꮃiᴛh Nᴇgligiʙlᴇ Ꭷuᴀliᴛy Ꮯhᴀngᴇ.\nᎩᴏu ᴄᴀn Ꮐᴇnᴇrᴀᴛᴇ Ꮪᴀʍᴩlᴇs ᴀnd sᴄrᴇᴇnshᴏᴛs ᴛᴏᴏ..",
        buttons=[
            [Button.inline("⌜ Ꮋᴇlᴩ  ⌟", data="ihelp")],
            [
                Button.url("⌜ Ꮜᴩdᴀᴛᴇs ⌟", url="https://t.me/AVBotz/5"),
                Button.url("⌜ Ꭰᴇvᴇlᴏᴩᴇr ⌟", url="t.me/Purushottam_6668"),
            ],
        ],
    )


async def help(event):
    await event.reply(
        "**Ꭺ Ꮲᴇrfᴇᴄᴛ Ꭺnd Ꮀᴀsᴛᴇr.....! ᏟᴏʍᴩrᴇssᴏrᏴᴏᴛ.**\n\n+Ꭲhis Ᏼᴏᴛ Ꮯᴏʍᴩrᴇss Ꮩidᴇᴏs Ꮃiᴛh Nᴇgligiʙlᴇ Ꭷuᴀliᴛy Ꮯhᴀngᴇ\n+Ꮐᴇnᴇrᴀᴛᴇ Ꮪᴀʍᴩlᴇ Ꮯᴏʍᴩrᴇssᴇd Ꮩidᴇᴏ\n+Ꭼᴀsy Ꭲᴏ Ꮜsᴇ\n-DᎠuᴇ Ꭲᴏ Ꭷuᴀliᴛy Ꮪᴇᴛᴛings Ᏼᴏᴛ Ꭲᴀᴋᴇs Ꮪᴏʍᴇ Ꭲiʍᴇ Ꭲᴏ Ꮯᴏʍᴩrᴇss.\nᏚᴏ Ᏼᴇ Ꮲᴀᴛiᴇnᴄᴇ Ꭺnd Ꮪᴇnd Ꮩidᴇᴏs Ꮻnᴇ Ᏼy Ꮻnᴇ Ꭺfᴛᴇr Ꮯᴏʍᴩlᴇᴛing..\nᎠᴏnᴛ Ꮪᴩᴀʍ Ᏼᴏᴛ.\n\nᎫusᴛ Ꮀᴏrwᴀrd Ꮩidᴇᴏ Ꭲᴏ Ꮐᴇᴛ Ꮻᴩᴛiᴏns"
    )


async def ihelp(event):
    await event.edit(
        "**Ꭺ Ꮲᴇrfᴇᴄᴛ Ꭺnd Ꮀᴀsᴛᴇr.....! ᏟᴏʍᴩrᴇssᴏrᏴᴏᴛ.**\n\n+Ꭲhis Ᏼᴏᴛ Ꮯᴏʍᴩrᴇss Ꮩidᴇᴏs Ꮃiᴛh Nᴇgligiʙlᴇ Ꭷuᴀliᴛy Ꮯhᴀngᴇ\n+Ꮐᴇnᴇrᴀᴛᴇ Ꮪᴀʍᴩlᴇ Ꮯᴏʍᴩrᴇssᴇd Ꮩidᴇᴏ\n+Ꮪᴄrᴇᴇnshᴏᴛs Ꭲᴏᴏ\n+Ꭼᴀsy Ꭲᴏ Ꮜsᴇ\n-DᎠuᴇ Ꭲᴏ Ꭷuᴀliᴛy Ꮪᴇᴛᴛings Ᏼᴏᴛ Ꭲᴀᴋᴇs Ꮪᴏʍᴇ Ꭲiʍᴇ Ꭲᴏ Ꮯᴏʍᴩrᴇss.\nᏚᴏ Ᏼᴇ Ꮲᴀᴛiᴇnᴄᴇ Ꭺnd Ꮪᴇnd Ꮩidᴇᴏs Ꮻnᴇ Ᏼy Ꮻnᴇ Ꭺfᴛᴇr Ꮯᴏʍᴩlᴇᴛing.\nᎠᴏnᴛ Ꮪᴩᴀʍ Ᏼᴏᴛ.\n\nᎫusᴛ Ꮀᴏrwᴀrd Ꮩidᴇᴏ Ꭲᴏ Ꮐᴇᴛ Ꮻᴩᴛiᴏns",
        buttons=[Button.inline("BACK", data="beck")],
    )


async def beck(event):
    ok = await event.client(GetFullUserRequest(event.sender_id))
    await event.edit(
        f"Hi `{ok.user.first_name}`\nᎢhis is Ꭺ ᏞiʙᏟᴏʍᴩrᴇssᴏrᏴᴏᴛ Ꮃhiᴄh Ꮯᴀn Ꭼnᴄᴏdᴇ Ꮩidᴇᴏs.\nᏒᴇduᴄᴇ Ꮪizᴇ ᴏf Ꮩidᴇᴏs Ꮃiᴛh Nᴇgligiʙlᴇ Ꭷuᴀliᴛy Ꮯhᴀngᴇ.\nᎩᴏu ᴄᴀn Ꮐᴇnᴇrᴀᴛᴇ Ꮪᴀʍᴩlᴇs ᴀnd sᴄrᴇᴇnshᴏᴛs ᴛᴏᴏ.",
        buttons=[
            [Button.inline("⌜ Ꮋᴇlᴩ  ⌟", data="ihelp")],
            [
                Button.url("⌜ Ꮜᴩdᴀᴛᴇs ⌟", url="https://t.me/AVBotz/5/"),
                Button.url("⌜ Ꭰᴇvᴇlᴏᴩᴇr ⌟", url="http://t.me/Purushottam_6668/"),
            ],
        ],
    )


async def sencc(e):
    key = e.pattern_match.group(1).decode("ᏌᎢᎰ - ８")
    await e.edit(
        "Choose Mode",
        buttons=[
            [
                Button.inline("⌜ Ꭰᴇfᴀulᴛ Ꮯᴏʍᴩrᴇss ⌟", data=f"encc{key}"),
                Button.inline("⌜ Ꮯusᴛᴏʍ Ꮯᴏʍᴩrᴇss ⌟", data=f"ccom{key}"),
            ],
            [Button.inline("⌜ Ᏼᴀᴄᴋ ⌟", data=f"back{key}")],
        ],
    )


async def back(e):
    key = e.pattern_match.group(1).decode("ᏌᎢᎰ - ８")
    await e.edit(
        "  🤔**Nᴏw  Ꮃhᴀᴛ Ꭲᴏ Ꭰᴏ?** 🤔",
        buttons=[
            [
                Button.inline("⌜ Ꮐᴇnᴇrᴀᴛᴇ Ꮪᴀʍᴩlᴇ ⌟", data=f"gsmpl{key}"),
                Button.inline("⌜ Ꮪᴄrᴇᴇnshᴏᴛs ⌟", data=f"sshot{key}"),
            ],
            [Button.inline("⌜ Ꮯᴏʍᴩrᴇss? ⌟", data=f"sencc{key}")],
        ],
    )


async def ccom(e):
    await e.edit("Ꮪᴇnd Ꮜr Ꮯusᴛᴏʍ Nᴀʍᴇ Ꮀᴏr Ꭲhᴀᴛ Ꮀilᴇ")
    wah = e.pattern_match.group(1).decode("ᏌᎢᎰ - ８")
    wh = decode(wah)
    out, dl, thum, dtime = wh.split(";")
    chat = e.sender_id
    async with e.client.conversation(chat) as cv:
        reply = cv.wait_event(events.NewMessage(from_users=chat))
        repl = await reply
        if "." in repl.text:
            q = repl.text.split(".")[-1]
            g = repl.text.replace(q, "mkv")
        else:
            g = repl.text + ".mkv"
        outt = f"encode/{chat}/{g}"
        x = await repl.reply(
            f"Ꮯusᴛᴏʍ Nᴀʍᴇ Ꮀᴏr Ꭲhᴀᴛ Ꮀilᴇ : {g}\n\nᏚᴇnd Ꭲhuʍʙnᴀil Ꮲiᴄᴛurᴇ Ꮀᴏr iᴛ."
        )
        replyy = cv.wait_event(events.NewMessage(from_users=chat))
        rep = await replyy
        if rep.media:
            tb = await e.client.download_media(rep.media, f"thumb/{chat}.jpg")
        elif rep.text and not (rep.text).startswith("/"):
            url = rep.text
            os.system(f"wget {url}")
            tb = url.replace("https://telegra.ph/file/", "")
        else:
            tb = thum
        omk = await rep.reply(f"Ꭲhuʍʙnᴀil {tb} Ꮪᴇᴛᴛᴇd Ꮪuᴄᴄᴇssfully")
        hehe = f"{outt};{dl};{tb};{dtime}"
        key = code(hehe)
        await customenc(omk, key)
