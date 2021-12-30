
import asyncio

from pyrogram.types import Message

from config import SUDO_USERS
from datetime import datetime
from sys import version_info
from time import time

from config import (
    ALIVE_IMG,
    ALIVE_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
from program import __version__
from driver.filters import command, other_filters
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""✨ **Merhabalar {message.from_user.mention()} !**\n
💭 [{BOT_NAME}](https://t.me/{BOT_USERNAME}) **botu ve asistanı gruba ekleyip güzel flim izleyebilir şarkılar dinleyebilirsiniz**
MERHABA ARKADAŞLAR HOŞGELDİNİZ 
KURUCU => @Mubtezell
ÜYE EKLEME REKALM VE İŞ BİRLİĞİ İÇİN BOT SAHİBİ İLE İLETİŞİME GEÇİNİZ
Daha fazla bilgi için aşağıdaki butonları kullanın👇
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Add me to your Group ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("❓ Basit bilgi", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("❤️ Sahip", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                 InlineKeyboardButton("BayKaosbio", url=f"https://t.me/@baykosbio "),
                ],
                [
                    InlineKeyboardButton(
                        "👥 Official Group", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "📣 Official Channel", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "🌐 Özel bot yapımı", url="https://t.me/Mubtezell"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_message(
    command(["alive", f"alive@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def alive(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("✨ Group", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton(
                    "📣 kanal", url=f"https://t.me/{UPDATES_CHANNEL}"
                ),
            ]
        ]
    )

    alive = f"**Merhaba {message.from_user.mention()}, ben {BOT_NAME}**\n\n✨ Bot normal çalışıyor\n🍀 Ustam: [{ALIVE_NAME}](https://t.me/{OWNER_NAME}) \n✨ Bot Sürümü: `v{__version__}`\n🍀 Pyrogram Sürümü: `{pyrover}`\n✨ Python Sürümü: `{__python_version__}`\n🍀 PyTgCalls sürümü: `{pytover.__version__}`\n✨ Çalışma Süresi Durumu: `{uptime}`\n\n**Beni buraya eklediğiniz, Grup görüntülü sohbetinizde video ve müzik oynattığınız için teşekkürler** ❤"

    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )



@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("🏓 `PONG!!`\n" f"⚡️ `{delta_ping * 1000:.3f} ms`")


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🤖 bot status:\n"
        f"• **çalışma süresi :** `{uptime}`\n"
        f"• **başlangıç saati:** `{START_TIME_ISO}`"
    )
@Client.on_message(filters.command("help") & ~filters.private & ~filters.channel)
async def ghelp(_, message: Message):
    await message.reply_text(
        """ Özel bot yapmak için iletişim=> @Mubtezell

» /oynat => istediğin şarkıyı direk dinletir
» /izlet => istedigin filmi indirip izletir
» /ara => video indirir
» /indir => music indirir 

NOT : /izlet ve /oynat komutu kendinize ait music ve videoları da oynatır

» /durdur - seste botu durdurur
» /devam - durdurulan botu başlatır
» /atla - şarkı ve video atlar
» /son - sesten düşer herşeyi durdurur
» /reload - botu yeniden başlatıp admin listesi yeniler
» /gel - gruba katılır
» /git - gruptan çıkar """
        )
