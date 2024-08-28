from pyrogram import filters, Client
import asyncio
from .. import JN
from pyrogram.enums import ParseMode
from pyrogram.errors import UserNotParticipant, ChatWriteForbidden, ChatAdminRequired
from config import *
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from ..database import collection, add_refer_balance, add_default_balance, is_new_user


# Force join handler

@JN.on_message(filters.command("start") & filters.private)

async def must_join_channel(bot: Client, msg):
    
    SUPPORT_GRP2=int(-1002007552392)
    user_id=msg.from_user.id
    
    try:
        user_status = await bot.get_chat_member(SUPPORT_GRP2, msg.from_user.id)
        if user_status.status == "left":
            print("hello")
    except UserNotParticipant:
        print(hii)
    
                
                
    if not UPDATE_CHNL and not SUPPORT_GRP:
        return
    try:
        try:
            await bot.get_chat_member(UPDATE_CHNL, msg.from_user.id)
            await bot.get_chat_member(SUPPORT_GRP, msg.from_user.id)
            
            caption = f"Hello {msg.from_user.mention}, \nI'm {JN.mention}\n\nɪ'ᴍ ᴘᴏᴡᴇʀꜰᴜʟ ʀᴇꜰᴇʀ ᴀɴᴅ ᴇᴀʀɴ ʙᴏᴛ, ʜᴇʀᴇ ʏᴏᴜ ᴄᴀɴ  ᴇᴀʀɴ ʙʏ ʀᴇꜰᴇʀ ʏᴏᴜʀ ꜰʀɪᴇɴᴅꜱ ᴀɴᴅ ᴀʟꜱᴏ ʏᴏᴜ ᴄᴀɴ ᴇᴀʀɴ ʙʏ ʙᴇᴛꜱ .\n\nMaintained by:<a href='https://t.me/JN_dev/'>JN Dev</a>"
            caption2 = f"Hello {msg.from_user.mention},\n\n ʜᴇʏ ʟᴏᴏᴋ ʟɪᴋᴇ ʏᴏᴜ ᴀʀᴇ ɴᴇᴡ ʜᴇʀᴇ ᴏɴᴇ ʟɪᴛᴛʟᴇ ɢɪꜰᴛ ꜰʀᴏᴍ ᴍᴇ ʏᴏᴜ ᴊᴜꜱᴛ ɢᴏᴛ +1 ₹ ᴀꜱ ʙᴏɴᴜꜱ.\n Maintained by:<a href='https://t.me/JN_dev/'>JN Dev</a>"

            if is_new_user(msg.from_user.id):
                add_default_balance(msg.from_user.id)

                j=await msg.reply_sticker("CAACAgUAAxkDAAIIImYMPfDBC9C0hwEdm34oVxFYbAYLAAJrDgACIHkgVAjUFXHyK3urHgQ")
                await asyncio.sleep(1)
                await j.delete()
                await JN.send_photo(msg.chat.id, photo=start_img2, caption=caption, reply_markup=main_button)
                await JN.send_message(msg.chat.id, text="Hey you just got +1₹ in your acount as new user bonus  ")
                await JN.send_message(log_channel, text=f"🦋 #newuser 🦋,\n\n**ID** : `{msg.from_user.id}`\n**Name**: {msg.from_user.first_name}\n **refer by:**No one    ")
            else:
                j=await msg.reply_sticker("CAACAgUAAxkBAAECPc9mA9nqb8a0d0ziqad0mrNlleIXXAAC0w4AAudpIVTD64tNd-x1Xx4E")
                await asyncio.sleep(1)
                await j.delete()
                j=await msg.reply_sticker("CAACAgUAAxkBAAECPcpmA9bYkPLWQz9DGg0KL5tShE3QRwACrQ8AAutgIVRELBWrQpHOux4E")
                await asyncio.sleep(1)
                await j.delete()
                await JN.send_photo(msg.chat.id, photo=start_img2, caption=caption, reply_markup=main_button)
                
        except UserNotParticipant:
            if UPDATE_CHNL.isalpha() and SUPPORT_GRP.isalpha():
                link = "https://t.me/" + UPDATE_CHNL
                link2 = "https://t.me/" + SUPPORT_GRP
            else:
                chat_info = await bot.get_chat(UPDATE_CHNL)
                link = chat_info.invite_link
                chat_info = await bot.get_chat(SUPPORT_GRP)
                link2 = chat_info.invite_link
                user_id={msg.from_user.id}

            try:
                x = await msg.reply_photo(
                photo=START_IMG,
                caption='»<b>ᴅᴜᴇ ᴛᴏ ʜɪɢʜ ꜱᴇʀᴠᴇʀ ʟᴏᴀᴅ ᴏɴʟʏ ᴍʏ ᴄʜᴀɴɴᴇʟ ᴍᴇᴍʙᴇʀ ᴄᴀɴ ᴜꜱᴇ ᴍᴇ☺️! ᴛʜᴇɴ ᴄʟɪᴄᴋ /start </b>',
                        parse_mode=ParseMode.HTML,
                        reply_markup=InlineKeyboardMarkup(
                            [
                                [
                                    InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ", url=link),
                                    InlineKeyboardButton("ᴄᴏʟʟᴀʙ ᴄʜᴀɴɴᴇʟ ", url=link2)]
                            ]
                        )
                    )
                await msg.stop_propagation()
                
                  
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        pass
        print(f"Promote me as an admin in the UPDATE CHANNEL: {UPDATE_CHNL}!")
        print(f"Promote me as an admin in the SUPPORT_GRP: {SUPPORT_GRP}!")
        
@JN.on_message(filters.regex('〄 ᴍᴀɪɴ ᴍᴇɴᴜ 〄') & filters.private)
async def main_menu_handler(bot, message):
    
    caption = f"Hello {message.from_user.first_name},\n\nɪ'ᴍ ᴘᴏᴡᴇʀꜰᴜʟ ʀᴇꜰᴇʀ ᴀɴᴅ ᴇᴀʀɴ ʙᴏᴛ, ʜᴇʀᴇ ʏᴏᴜ ᴄᴀɴ  ᴇᴀʀɴ ʙʏ ʀᴇꜰᴇʀ ʏᴏᴜʀ ꜰʀɪᴇɴᴅꜱ ᴀɴᴅ ᴀʟꜱᴏ ʏᴏᴜ ᴄᴀɴ ᴇᴀʀɴ ʙʏ ʙᴇᴛꜱ .\n\nMaintained by: <a href='https://t.me/jn_dev/'>JN Dev</a>"
    
    await JN.send_photo(message.chat.id, photo=start_img2, caption=caption, reply_markup=main_button)
    await message.delete()
    
    

