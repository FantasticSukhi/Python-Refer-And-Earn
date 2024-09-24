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

async def must_join_channel(bot: JN, msg):
    
    SUPPORT_GRP2=int(-1002007552392)
    user_id=msg.from_user.id
    
    try:
        await bot.get_chat_member(SUPPORT_GRP, msg.from_user.id)
        print("hello")
    except UserNotParticipant:
        print("hii")
    
                
                
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
            link = "https://t.me/" + UPDATE_CHNL
            link2 = "https://t.me/" + SUPPORT_GRP
            
                

            try:
                x = await msg.reply_photo(
                photo=START_IMG,
                caption='»<b>ᴅᴜᴇ ᴛᴏ ʜɪɢʜ ꜱᴇʀᴠᴇʀ ʟᴏᴀᴅ ᴏɴʟʏ ᴍʏ ᴄʜᴀɴɴᴇʟ ᴍᴇᴍʙᴇʀ ᴄᴀɴ ᴜꜱᴇ ᴍᴇ☺️! ᴛʜᴇɴ ᴄʟɪᴄᴋ /start </b>',
                        parse_mode=ParseMode.HTML)
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
    
    
    
from pyrogram import Client, filters
from pyrogram.enums import MessageMediaType
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply

from hachoir.metadata import extractMetadata
from hachoir.parser import createParser

from helper.utils import progress_for_pyrogram, convert, humanbytes
from helper.database import db

from asyncio import sleep
from PIL import Image
import os, time


@JN.on_message(filters.private & (filters.document | filters.audio | filters.video))
async def rename_start(JN, message):
    file = getattr(message, message.media.value)
    filename = file.file_name  
    if file.file_size > 2000 * 1024 * 1024:
         return await message.reply_text("Sᴏʀʀy Bʀᴏ Tʜɪꜱ Bᴏᴛ Iꜱ Dᴏᴇꜱɴ'ᴛ Sᴜᴩᴩᴏʀᴛ Uᴩʟᴏᴀᴅɪɴɢ Fɪʟᴇꜱ Bɪɢɢᴇʀ Tʜᴀɴ 2Gʙ. ᴄᴏɴᴛᴀᴄᴛ ʙᴏᴛ <a href=https://t.me/Narayan_k_purohit>NARAYAN</a> 💞")

    try:
        await message.reply_text(
            text=f"**__Pʟᴇᴀꜱᴇ Eɴᴛᴇʀ Nᴇᴡ Fɪʟᴇɴᴀᴍᴇ...__**\n\n**Oʟᴅ Fɪʟᴇ Nᴀᴍᴇ** :- `{filename}`",
	    reply_to_message_id=message.id,  
	    reply_markup=ForceReply(True)
        )       
        await sleep(30)
    except FloodWait as e:
        await sleep(e.value)
        await message.reply_text(
            text=f"**__Pʟᴇᴀꜱᴇ Eɴᴛᴇʀ Nᴇᴡ Fɪʟᴇɴᴀᴍᴇ...__**\n\n**Oʟᴅ Fɪʟᴇ Nᴀᴍᴇ** :- `{filename}`",
	    reply_to_message_id=message.id,  
	    reply_markup=ForceReply(True)
        )
    except:
        pass



@JN.on_message(filters.private & filters.reply)
async def refunc(JN, message):
    reply_message = message.reply_to_message
    if (reply_message.reply_markup) and isinstance(reply_message.reply_markup, ForceReply):
        new_name = message.text 
        await message.delete() 
        msg = await JN.get_messages(message.chat.id, reply_message.id)
        file = msg.reply_to_message
        media = getattr(file, file.media.value)
        if not "." in new_name:
            if "." in media.file_name:
                extn = media.file_name.rsplit('.', 1)[-1]
            else:
                extn = "mkv"
            new_name = new_name + "." + extn
        await reply_message.delete()

        button = [[InlineKeyboardButton("📁 Dᴏᴄᴜᴍᴇɴᴛ",callback_data = "upload_document")]]
        if file.media in [MessageMediaType.VIDEO, MessageMediaType.DOCUMENT]:
            button.append([InlineKeyboardButton("🎥 Vɪᴅᴇᴏ", callback_data = "upload_video")])
        elif file.media == MessageMediaType.AUDIO:
            button.append([InlineKeyboardButton("🎵 Aᴜᴅɪᴏ", callback_data = "upload_audio")])
        await message.reply(
            text=f"**Sᴇʟᴇᴄᴛ Tʜᴇ Oᴜᴛᴩᴜᴛ Fɪʟᴇ Tyᴩᴇ**\n**• Fɪʟᴇ Nᴀᴍᴇ :-**`{new_name}`",
            reply_to_message_id=file.id,
            reply_markup=InlineKeyboardMarkup(button)
        )



@JN.on_callback_query(filters.regex("upload"))
async def doc(bot, update):    
    new_name = update.message.text
    new_filename = new_name.split(":-")[1]
    file_path = f"downloads/{new_filename}"
    file = update.message.reply_to_message

    ms = await update.message.edit("➣ Tʀyɪɴɢ Tᴏ Dᴏᴡɴʟᴏᴀᴅɪɴɢ....")    
    try:
     	path = await bot.download_media(message=file, file_name=file_path, progress=progress_for_pyrogram,progress_args=("➣ Dᴏᴡɴʟᴏᴀᴅ Sᴛᴀʀᴛᴇᴅ....", ms, time.time()))                    
    except Exception as e:
     	return await ms.edit(e)
     	     
    duration = 0
    try:
        metadata = extractMetadata(createParser(file_path))
        if metadata.has("duration"):
           duration = metadata.get('duration').seconds
    except:
        pass
    ph_path = None
    user_id = int(update.message.chat.id) 
    media = getattr(file, file.media.value)
    c_caption = await db.get_caption(update.message.chat.id)
    c_thumb = await db.get_thumbnail(update.message.chat.id)

    if c_caption:
         try:
             caption = c_caption.format(filename=new_filename, filesize=humanbytes(media.file_size), duration=convert(duration))
         except Exception as e:
             return await ms.edit(text=f"Yᴏᴜʀ Cᴀᴩᴛɪᴏɴ Eʀʀᴏʀ Exᴄᴇᴩᴛ Kᴇyᴡᴏʀᴅ Aʀɢᴜᴍᴇɴᴛ ●> ({e})")             
    else:
         caption = f"**{new_filename}**"
 
    if (media.thumbs or c_thumb):
         if c_thumb:
             ph_path = await bot.download_media(c_thumb) 
         else:
             ph_path = await bot.download_media(media.thumbs[0].file_id)
         Image.open(ph_path).convert("RGB").save(ph_path)
         img = Image.open(ph_path)
         img.resize((320, 320))
         img.save(ph_path, "JPEG")

    await ms.edit("➣ Tʀyɪɴɢ Tᴏ Uᴩʟᴏᴀᴅɪɴɢ....")
    type = update.data.split("_")[1]
    try:
        if type == "document":
            await bot.send_document(
                update.message.chat.id,
                document=file_path,
                thumb=ph_path, 
                caption=caption, 
                progress=progress_for_pyrogram,
                progress_args=("Uᴩʟᴏᴅ Sᴛᴀʀᴛᴇᴅ....", ms, time.time()))
        elif type == "video": 
            await bot.send_video(
		update.message.chat.id,
	        video=file_path,
	        caption=caption,
		thumb=ph_path,
		duration=duration,
	        progress=progress_for_pyrogram,
		progress_args=("Uᴩʟᴏᴅ Sᴛᴀʀᴛᴇᴅ....", ms, time.time()))
        elif type == "audio": 
            await bot.send_audio(
		update.message.chat.id,
		audio=file_path,
		caption=caption,
		thumb=ph_path,
		duration=duration,
	        progress=progress_for_pyrogram,
	        progress_args=("Uᴩʟᴏᴅ Sᴛᴀʀᴛᴇᴅ....", ms, time.time()))
    except Exception as e:          
        os.remove(file_path)
        if ph_path:
            os.remove(ph_path)
        return await ms.edit(f" Eʀʀᴏʀ {e}")
 
    await ms.delete() 
    os.remove(file_path) 
    if ph_path: os.remove(ph_path) 







