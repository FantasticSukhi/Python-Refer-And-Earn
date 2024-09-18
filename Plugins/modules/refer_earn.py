from pyrogram import filters, Client
import asyncio
from .. import JN
from pyrogram.enums import ParseMode
from pyrogram.errors import UserNotParticipant, ChatWriteForbidden, ChatAdminRequired
from config import *
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from ..database import collection, add_refer_balance, add_default_balance, is_new_user

# Define the links for the channels



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
        
        


@JN.on_message(filters.regex(r"/start \d+"))
async def must_join_channel(bot: Client, msg):
    referred_by = int(msg.text.split()[1])
    user_id = msg.from_user.id

    # Create a list to hold all the buttons
    buttons = []

    # Loop through the links two at a time and create a new row for each pair
    for i in range(0, len(links), 2):
        row = []
        for j in range(2):
            if i + j < len(links):
                row.append(InlineKeyboardButton(f"Channel {i+j+1}", url=links[i + j]))
        buttons.append(row)

    # Create the joined button with the correct callback data
    joined_button = InlineKeyboardButton("Joined", callback_data=f"joined_{user_id}_{referred_by}")

    # Always add the joined button as a new row, irrespective of channel count
    buttons.append([joined_button])

    # Create the final reply markup with all the buttons
    reply_markup1 = InlineKeyboardMarkup(buttons)

    # Continue with your existing logic (e.g., handling new or existing users)
    try:
        try:
            # Check if the user is part of the channels (example for UPDATE_CHNL and SUPPORT_GRP)
            await bot.get_chat_member(UPDATE_CHNL, msg.from_user.id)
            await bot.get_chat_member(SUPPORT_GRP, msg.from_user.id)

            # Send welcome message with the generated buttons
            caption2 = f"Hello {msg.from_user.first_name}, \nI'm {JN.mention}\n\nI'm a powerful SMM bot. You can buy any type of SMM service here.\n\nMaintained by: <a href='https://t.me/jn_dev/'>JN Dev</a>"

            # Check if the user is new
            if is_new_user(msg.from_user.id):
                await JN.send_photo(msg.chat.id, photo=START_IMG, caption=caption2, reply_markup=reply_markup1)

                # Give bonuses and notify the referrer
                await JN.send_message(msg.chat.id, text=f"Hey you just got {NEW_USER_BONUS}₹ in your account as a new user bonus")
                await add_refer_balance(user_id=referred_by, refer_in=REFER_BONUS)
                add_default_balance(user_id=user_id)
                await bot.send_message(referred_by, f"Congratulations! You got {REFER_BONUS}₹ from a new referral.")
                await JN.send_message(log_channel, text=f"🦋 #newuser 🦋,\n\n**ID** : `{msg.from_user.id}`\n**Name**: {msg.from_user.first_name}\n **refer by:** {referred_by}")

            else:
                await msg.reply(f"Hey {msg.from_user.first_name}, you're already a user!")
                await bot.send_message(referred_by, "Your friend is already a user of the bot.")
        
        except UserNotParticipant:
            # Force the user to join the required channels
            link = "https://t.me/" + UPDATE_CHNL
            link2 = "https://t.me/" + SUPPORT_GRP

            if is_new_user(msg.from_user.id):
                await msg.reply_photo(
                    photo=START_IMG,
                    caption='»<b>You need to join the required channels to use this bot!</b>',
                    parse_mode=ParseMode.HTML,
                    reply_markup=reply_markup1
                )
                await JN.send_message(referred_by, f"Hey, your friend has started the bot! Once they join the channel, you'll get your bonus.")
            else:
                await msg.reply(f"Hey {msg.from_user.first_name}, you're already a user!")

    except ChatWriteForbidden:
        print(f"Promote me as an admin in the channel!")
        pass