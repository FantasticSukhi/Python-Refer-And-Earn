from pyrogram import filters, Client
import asyncio
from .. import JN
from pyrogram.enums import ParseMode
from pyrogram.errors import UserNotParticipant, ChatWriteForbidden, ChatAdminRequired
from config import *
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from ..database import collection, add_refer_balance, add_default_balance, is_new_user


from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# The link variable should contain all the channel URLs in a list format
links = ["https://t.me/jn_bots", "https://t.me/jn_family", "https://t.me/channel3", "https://t.me/channel4"]


buttons = []
joined_button = InlineKeyboardButton("Joined", callback_data=f"joined_{user_id}_{referred_by}")
for i in range(0, len(links), 2):
    row = []
    for j in range(2):
        if i + j < len(links):
            row.append(InlineKeyboardButton(f"Channel {i+j+1}", url=links[i + j]))
    buttons.append(row)

if len(links) == 2:
    
    buttons.append([joined_button])  
elif len(links) == 4:
    if len(buttons[-1]) == 1:
        buttons[-1].append(joined_button)  
        
    else:
        buttons.append([joined_button])  
        
reply_markup1 = InlineKeyboardMarkup(buttons)



@JN.on_message(filters.regex("❤️‍🔥 ʀᴇꜰᴇʀ ᴀɴᴅ ᴇᴀʀɴ") |filters.command("refer"))
async def get_referral_link(client, message):
    document = collection.find_one({"user_id": message.from_user.id})
    user_id = message.from_user.id
    total=document.get("total_refer")
    referral_link = f"ɴᴀᴍᴇ : {message.from_user.mention}\ntotal refer : {total}\n\nʏᴏᴜʀ ʀᴇꜰᴇʀ ʟɪɴᴋ: https://t.me/{JN.username}?start={user_id}"
    referral_link2 = f"https://telegram.me/share/url?url=t.me/{JN.username}?start={user_id}"
    await message.reply(f"{referral_link}",reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton("share url ",url=referral_link2)] 
        ]),disable_web_page_preview=True)

# Force join handler
@JN.on_message(filters.regex(r"/start \d+"))
async def must_join_channel(bot: Client, msg):
    # if not UPDATE_CHNL and not SUPPORT_GRP:
    #     return
    referred_by = int(msg.text.split()[1])
    user_id = msg.from_user.id
    print(referred_by)
    joined_button = InlineKeyboardButton("Joined", callback_data=f"joined_{user_id}_{referred_by}")
    try:
        try:
            await bot.get_chat_member(UPDATE_CHNL, msg.from_user.id)
            await bot.get_chat_member(SUPPORT_GRP, msg.from_user.id)
            
            caption2 = f"Hello {msg.from_user.first_name}, \nI'm {JN.mention}\n\nI'm a powerful SMM bot. You can buy any type of SMM service here.\n\nMaintained by: <a href='https://t.me/jn_dev/'>JN Dev</a>"
            referred_by = int(msg.text.split()[1])
            user_id = msg.from_user.id
            
            document = collection.find_one({"user_id": user_id})

            if is_new_user(msg.from_user.id):
                j = await msg.reply_sticker("CAACAgUAAxkDAAIIImYMPfDBC9C0hwEdm34oVxFYbAYLAAJrDgACIHkgVAjUFXHyK3urHgQ")
                await asyncio.sleep(1)
                await j.delete()
                await JN.send_photo(msg.chat.id, photo=START_IMG, caption=caption2, reply_markup=main_button)

                await JN.send_message(msg.chat.id, text=f"Hey you just got {NEW_USER_BONUS}₹ in your account as new user bonus")
                
                await add_refer_balance(user_id=referred_by, refer_in=REFER_BONUS)
                add_default_balance(user_id=user_id)
                await bot.send_message(referred_by, f"ᴄᴏɴɢʀᴀᴛᴜʟᴀᴛɪᴏɴꜱ 🎉!, ʏᴏᴜ ɢᴏᴛ {REFER_BONUS}₹ ɴᴇᴡ ʀᴇꜰᴇʀ")
                await JN.send_message(log_channel, text=f"🦋 #newuser 🦋,\n\n**ID** : `{msg.from_user.id}`\n**Name**: {msg.from_user.first_name}\n **refer by:**{referred_by}")
            else:
                await msg.reply(f"Hey {msg.from_user.first_name}, are you trying to cheat on me? 😏")
                await bot.send_message(referred_by, "ʏᴏᴜʀ ꜰʀɪᴇɴᴅ ɪꜱ ᴀʟʀᴇᴀᴅʏ ᴀ ᴜꜱᴇʀ ᴏꜰ ᴛʜᴇ ʙᴏᴛ.")
        
        except UserNotParticipant:
            link = "https://t.me/" + UPDATE_CHNL
            link2 = "https://t.me/" + SUPPORT_GRP
            user_id={msg.from_user.id}

            try:
                if is_new_user(msg.from_user.id):
                    m = await msg.reply_sticker("CAACAgUAAxkBAAECPelmA_Oz--iyEJBowQeRCLvWNDVAVAAC1g0AAr0KIVR-vFw5cxMauR4E")
                    await asyncio.sleep(1)
                    await m.delete()
                    x = await msg.reply_photo(
                        photo=START_IMG,
                        caption='»<b>ᴅᴜᴇ ᴛᴏ ʜɪɢʜ ꜱᴇʀᴠᴇʀ ʟᴏᴀᴅ ᴏɴʟʏ ᴍʏ ᴄʜᴀɴɴᴇʟ ᴍᴇᴍʙᴇʀ ᴄᴀɴ ᴜꜱᴇ ᴍᴇ☺️!</b>',
                        parse_mode=ParseMode.HTML,
                        reply_markup=reply_markup1
                    )
                    
                    await JN.send_message(referred_by, f"ʜᴇʏ ʏᴏᴜʀ ꜰʀɪᴇɴᴅ ɪꜱ ꜱᴛᴀʀᴛᴇᴅ ʙᴏᴛ ᴡʜᴇɴ ʜᴇ ᴡɪʟʟ ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ ʏᴏᴜ ᴡɪʟʟ ɢᴇᴛ ʏᴏᴜʀ ʙᴏɴᴜꜱ.")
                    await msg.stop_propagation()
                else:
                    await msg.reply(f"Hey {msg.from_user.first_name}, are you trying to cheat on me? 😏")
                    await bot.send_message(referred_by, "ʏᴏᴜʀ ꜰʀɪᴇɴᴅ ɪꜱ ᴀʟʀᴇᴀᴅʏ ᴀ ᴜꜱᴇʀ ᴏꜰ ᴛʜᴇ ʙᴏᴛ.")
            except ChatWriteForbidden:
                pass
    except ChatWriteForbidden:
        # print(e)
        print(f"Promote me as an admin in the UPDATE CHANNEL: {UPDATE_CHNL}!")
        print(f"Promote me as an admin in the SUPPORT_GRP: {SUPPORT_GRP}!")
        pass
