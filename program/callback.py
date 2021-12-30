# Copyright (C) 2021 By VeezMusicProject

from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Hoşgeldin [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
💭 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) yeni Telegram'ın görüntülü sohbetleri aracılığıyla gruplarda müzik ve video oynatmanıza olanak tanır!**

💡 **📚 Komutlar düğmesini tıklayarak Bot'un tüm komutlarını ve nasıl çalıştıklarını öğrenin!**

🔖 **Bu botun nasıl kullanılacağını öğrenmek için lütfen tıklayın » ❓ Basit Komutlar!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Add me to your Group ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("❓ Basit komutlar", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton(" Sahibi ", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "👥 Official Group", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "📣 Official Kanal", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
    f"""
» /oynat => istediğin şarkıyı direk dinletir
» /izlet => istedigin filmi indirip izletir
» /ara => video indirir
» /indir => music indirir 
» /durdur - seste botu durdurur
» /devam - durdurulan botu başlatır
» /atla - şarkı ve video atlar
» /son - sesten düşer herşeyi durdurur
» /reload - botu yeniden başlatıp admin listesi yeniler
» /Gel - gruba katılır
» /git - gruptan çıkar
NOT : /izlet ve /oynat komutu kendinize ait music ve videoları da oynatır 

⚡ __Powered by {BOT_NAME} A.I__""",
    )

@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    await query.message.delete()
