# Credits: @STUPID_FAMILY
# FROM File-Sharing-Man <https://github.com/Gultomganteng/File-Sharing-Man/>
# t.me/CARI_TEMAN_SLEEPCALL & t.me/bahagiaslaluu

from pyrogram.types import InlineKeyboardButton

class Data:
    HELP = """
<b> ❏ Perintah untuk Pengguna BOT
 ├ /start - Mulai Bot
 ├ /about - Tentang Bot ini
 ├ /help - Bantuan Perintah Bot ini
 ├ /ping - Untuk mengecek bot hidup
 └ /uptime - Untuk melihat status bot 
 
 ❏ Perintah Untuk Admin BOT
 ├ /logs - Untuk melihat logs bot
 ├ /setvar - Untuk mengatur var dengan command dibot
 ├ /delvar - Untuk menghapus var dengan command dibot
 ├ /getvar - Untuk melihat salah satu var dengan command dibot
 ├ /users - Untuk melihat statistik pengguna bot
 ├ /batch - Untuk membuat link lebih dari satu file
 ├ /speedtest - Untuk Mengetes kecepatan server bot
 └ /broadcast - Untuk mengirim pesan broadcast ke pengguna bot

👨‍💻 Develoved by </b><a href='https://t.me/bahagiaslaluu/101'>@bahagiaslaluu</a>
"""

    close = [
        [InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")]
    ]

    mbuttons = [
        [
            InlineKeyboardButton("ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
            InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")
        ],
    ]

    buttons = [
        [
            InlineKeyboardButton("ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ", callback_data="about"),
            InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")
        ],
    ]

    ABOUT = """
<b>Tentang Bot ini:

@{} adalah Bot Telegram untuk menonton video bokep yang viral-viral.

 • Creator: @{}
 • Ch owner: <a href='https://t.me/bahagiaslaluu'>Join lah</a>
 • Grup Mutualan: <a href='https://t.me/CARI_TEMAN_SLEEPCALL'>Join lah</a>

👨‍💻 Develoved by </b><a href='https://t.me/bahagiaslaluu/101'>@bahagiaslaluu</a>
"""
