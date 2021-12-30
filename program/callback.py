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
                        "➕ Gruba Ekle➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("❓ Basit komutlar", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("📚 Komutlar", callback_data="cbcmds"),
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
        f"""❓ **Bu botu kullanmak için temel anlatım:**
1.) **Önce beni grubunuza ekleyin.**
2.) **O zaman beni yönetici olarak yükselt ve Anonim Yönetici hariç tüm izinleri ver.**
3.) **Beni terfi ettirdikten sonra, yönetici verilerini yenilemek için /reload  yazın.**
3.) **Grubunuza @{ASSISTANT_NAME} ekleyin veya onu davet etmek için /gel yazın.**
4.) **Video/müzik oynatmaya başlamadan önce görüntülü sohbeti açın.**
5.) **Bazen /reload komutunu kullanarak botu yeniden yüklemek bazı sorunları çözmenize yardımcı olabilir.**
💡 **Bu bot hakkında takip eden bir sorunuz varsa, bunu buradaki destek sohbetimde iletebilirsiniz. @burakizm**
⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Geri", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Merhaba [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**
⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("👷🏻 Admin komut", callback_data="cbadmin"),
                    InlineKeyboardButton("🧙🏻 sahip ", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("📚 Basit komut", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("🔙 geri", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 basit komutlar:
» /oynat => istediğin şarkıyı direk dinletir
» /izlet => istedigin videoyu direk oynatır
» /ara => video indirir
» /indir => musik indirir 
NOT : /izlet ve /oynat komutu kendinize ait musik ve videoları da oynatır 
⚡️ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 geri", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 admin komutları:
» /durdur - seste botu durdurur
» /devam - durdurulan botu başlatır
» /atla - şarkı ve video atlar
» /son - sesten düşer herşeyi durdurur
» /reload - botu yeniden başlatıp admin listesi yeniler
» /gel - gruba katılır
» /git - gruptan çıkar
⚡️ __{BOT_NAME} tarafından güçlendirildi__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Geri", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮
Üzgünüm bu komutları sadece bot sahibi kullanabilir sen de kendine ait bir bot istiyorsan @burakizm 'e yazabilirsin...
⚡ __{BOT_NAME}tarafından güçlendirildi__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Geri", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    await query.message.delete()
