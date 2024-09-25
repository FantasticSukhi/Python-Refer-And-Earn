from .. import JN
import math, time
from datetime import datetime
from pytz import timezone
from config import *
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def progress_for_pyrogram(current, total, ud_type, message, start):
    now = time.time()
    diff = now - start
    if round(diff % 5.00) == 0 or current == total:        
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion

        elapsed_time = TimeFormatter(milliseconds=elapsed_time)
        estimated_total_time = TimeFormatter(milliseconds=estimated_total_time)

        progress = "{0}{1}".format(
            ''.join(["⬢" for i in range(math.floor(percentage / 5))]),
            ''.join(["⬡" for i in range(20 - math.floor(percentage / 5))])
        )            
        tmp = progress + Txt.PROGRESS_BAR.format( 
            round(percentage, 2),
            humanbytes(current),
            humanbytes(total),
            humanbytes(speed),            
            estimated_total_time if estimated_total_time != '' else "0 s"
        )
        try:
            await message.edit(
                text=f"{ud_type}\n\n{tmp}",               
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("✖️ 𝙲𝙰𝙽𝙲𝙴𝙻 ✖️", callback_data="close")]])                                               
            )
        except:
            pass

def humanbytes(size):    
    if not size:
        return ""
    power = 2**10
    n = 0
    Dic_powerN = {0: ' ', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + " " + Dic_powerN[n] + 'ʙ'


def TimeFormatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + "ᴅ, ") if days else "") + \
        ((str(hours) + "ʜ, ") if hours else "") + \
        ((str(minutes) + "ᴍ, ") if minutes else "") + \
        ((str(seconds) + "ꜱ, ") if seconds else "") + \
        ((str(milliseconds) + "ᴍꜱ, ") if milliseconds else "")
    return tmp[:-2] 

def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60      
    return "%d:%02d:%02d" % (hour, minutes, seconds)

async def send_log(b, u):
    if log_channel is not None:
        curr = datetime.now(timezone("Asia/Kolkata"))
        date = curr.strftime('%d %B, %Y')
        time = curr.strftime('%I:%M:%S %p')
        await b.send_message(
            log_channel,
            f"**--Nᴇᴡ Uꜱᴇʀ Sᴛᴀʀᴛᴇᴅ Tʜᴇ Bᴏᴛ--**\n\nUꜱᴇʀ: {u.mention}\nIᴅ: `{u.id}`\nUɴ: @{u.username}\n\nDᴀᴛᴇ: {date}\nTɪᴍᴇ: {time}\n\nBy: {b.mention}"
        )
        



from pyrogram import Client, filters
from pyrogram.enums import MessageMediaType
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply

from hachoir.metadata import extractMetadata
from hachoir.parser import createParser

from asyncio import sleep
from PIL import Image
import os, time
from datetime import datetime
from pytz import timezone


@JN.on_message(filters.private & (filters.document | filters.audio | filters.video))
async def rename_start(JN, message):
    file = getattr(message, message.media.value)
    filename = file.file_name
    if file.file_size > 2000 * 1024 * 1024:
        return await message.reply_text("Sorry, this bot doesn't support files larger than 2GB.")

    # Ask for new filename
    try:
        await message.reply_text(
            text=f"Please enter the new filename.\nOld Filename: `{filename}`",
            reply_to_message_id=message.id,
            reply_markup=ForceReply(True)
        )
        await sleep(30)
    except FloodWait as e:
        await sleep(e.value)
    except:
        pass


@JN.on_message(filters.private & filters.reply)
async def refunc(client, message):
    reply_message = message.reply_to_message
    if reply_message.reply_markup and isinstance(reply_message.reply_markup, ForceReply):
        new_name = message.text
        await message.delete()  # Delete the name message to keep the chat clean
        msg = await client.get_messages(message.chat.id, reply_message.id)
        file = msg.reply_to_message
        media = getattr(file, file.media.value)

        await reply_message.delete()

        # Ask for thumbnail
        await message.reply_text(
            "Please upload the thumbnail or send 'skip' to proceed without a thumbnail.",
            reply_to_message_id=file.id,
            reply_markup=ForceReply(True)
        )


@JN.on_message(filters.private & filters.reply)
async def handle_thumbnail(client, message):
    reply_message = message.reply_to_message
    if reply_message.reply_markup and isinstance(reply_message.reply_markup, ForceReply):
        # Check if the user wants to skip sending the thumbnail
        if message.text and message.text.lower() == 'skip':
            thumbnail = None
        else :
            thumbnail = await client.download_media(message)


        # Retrieve previous messages for filename and media
        msg = await client.get_messages(message.chat.id, reply_message.id)
        file = msg.reply_to_message
        media = getattr(file, file.media.value)
        new_name = reply_message.text  # Use the provided filename

        # Download the file and prepare for upload
        file_path = f"downloads/{new_name}"
        ms = await message.reply("Downloading the file...")

        try:
            path = await client.download_media(file, file_name=file_path)
        except Exception as e:
            return await ms.edit(f"Download error: {e}")

        await ms.edit("Uploading the file as a document...")

        # Upload as a document
        try:
            await client.send_document(
                message.chat.id,
                document=file_path,
                thumb=thumbnail,
                caption=new_name
            )
        except Exception as e:
            await ms.edit(f"Upload error: {e}")
        finally:
            # Clean up the downloaded files
            os.remove(file_path)
            if thumbnail:
                os.remove(thumbnail)

        await ms.delete()