import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery, Message, InputMediaPhoto

from helper.database import madflixbotz
from config import Config, Txt  

@Client.on_message(filters.private & filters.command("start"))
async def start(client, message):
    user = message.from_user
    await madflixbotz.add_user(client, message)                
    button = InlineKeyboardMarkup([[
      InlineKeyboardButton('♨ 𝐔𝐏𝐃𝐀𝐓𝐄𝐒 ♨', url='https://t.me/pcott'),
      InlineKeyboardButton('🚨 𝐀𝐃𝐌𝐈𝐍 🚨', url='https://t.me/PCADMINOFFICIALBOT')
    ],[
      InlineKeyboardButton('🔥 𝐇𝐄𝐋𝐏 🔥', callback_data='help'),
      InlineKeyboardButton('⚡ 𝐀𝐁𝐎𝐔𝐓 ⚡', callback_data='about')
    ],[
        InlineKeyboardButton("🧑‍💻 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 🧑‍💻", url='https://t.me/PCADMINOFFICIALBOT')
    ]])
    if Config.START_PIC:
        await message.reply_photo(Config.START_PIC, caption=Txt.START_TXT.format(user.mention), reply_markup=button)       
    else:
        await message.reply_text(text=Txt.START_TXT.format(user.mention), reply_markup=button, disable_web_page_preview=True)   

@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data 
    user_id = query.from_user.id  
    
    if data == "home":
        await query.message.edit_text(
            text=Txt.START_TXT.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
      InlineKeyboardButton('♨ 𝐔𝐏𝐃𝐀𝐓𝐄𝐒 ♨', url='https://t.me/pcott'),
      InlineKeyboardButton('🚨 𝐀𝐃𝐌𝐈𝐍 🚨', url='https://t.me/PCADMINOFFICIALBOT')
    ],[
      InlineKeyboardButton('🔥 𝐇𝐄𝐋𝐏 🔥', callback_data='help'),
      InlineKeyboardButton('⚡ 𝐀𝐁𝐎𝐔𝐓 ⚡', callback_data='about')
    ],[
        InlineKeyboardButton("🧑‍💻 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 🧑‍💻", url='https://t.me/PCADMINOFFICIALBOT')
    ]])
        )
    elif data == "caption":
        await query.message.edit_text(
            text=Txt.CAPTION_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("⚠ 𝐂𝐥𝐨𝐬𝐞 ⚠", callback_data="close"),
                InlineKeyboardButton("🚦 𝐁𝐚𝐜𝐤 🚦", callback_data="help")
            ]])            
        )
    elif data == "help":
        await query.message.edit_text(
            text=Txt.HELP_TXT.format(client.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("✨ 𝐒𝐞𝐭𝐮𝐩 𝐀𝐮𝐭𝐨𝐑𝐞𝐧𝐚𝐦𝐞 𝐅𝐨𝐫𝐦𝐚𝐭 ✨", callback_data='file_names')
                ],[
                InlineKeyboardButton('🎆 𝐓𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 🎆', callback_data='thumbnail'),
                InlineKeyboardButton('🧩 𝐂𝐚𝐩𝐭𝐢𝐨𝐧 🧩', callback_data='caption')
                ],[
                InlineKeyboardButton('💢 𝐇𝐨𝐦𝐞 💢', callback_data='home'),
                InlineKeyboardButton('💵 𝐃𝐨𝐧𝐚𝐭𝐞 💵', callback_data='donate')
                ]])
        )
    elif data == "donate":
        await query.message.edit_text(
            text=Txt.DONATE_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("⚠ 𝐂𝐥𝐨𝐬𝐞 ⚠", callback_data="close"),
                InlineKeyboardButton("🚦 𝐁𝐚𝐜𝐤 🚦", callback_data="help")
            ]])          
        )
    
    elif data == "file_names":
        format_template = await madflixbotz.get_format_template(user_id)
        await query.message.edit_text(
            text=Txt.FILE_NAME_TXT.format(format_template=format_template),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("⚠ 𝐂𝐥𝐨𝐬𝐞 ⚠", callback_data="close"),
                InlineKeyboardButton("🚦 𝐁𝐚𝐜𝐤 🚦", callback_data="help")
            ]])
        )      
    
    elif data == "thumbnail":
        await query.message.edit_caption(
            caption=Txt.THUMBNAIL_TXT,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("⚠ 𝐂𝐥𝐨𝐬𝐞 ⚠", callback_data="close"),
                InlineKeyboardButton("🚦 𝐁𝐚𝐜𝐤 🚦", callback_data="help"),
            ]]),
        )

    elif data == "about":
        await query.message.edit_text(
            text=Txt.ABOUT_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("⚠ 𝐂𝐥𝐨𝐬𝐞 ⚠", callback_data="close"),
                InlineKeyboardButton("🚦 𝐁𝐚𝐜𝐤 🚦", callback_data="home")
            ]])          
        )
    
    
    elif data == "close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
            await query.message.continue_propagation()
        except:
            await query.message.delete()
            await query.message.continue_propagation()





