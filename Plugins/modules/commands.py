from .. import JN
from pyrogram import filters
from pyrogram.types import Message
from ..database import collection
from config import OWNER_ID

# Define a function to handle the /broadcast command
@JN.on_message(filters.private & filters.user(OWNER_ID) & filters.command(["broadcast"]))
async def broadcast_command_handler(b, m: Message):
    # Check if the user is authorized to use the /broadcast command
    if m.reply_to_message:
        ms = await m.reply("Getting All ids from database...\nPlease wait")
        
        # Retrieve all user IDs from the database
        user_ids = [doc['user_id'] for doc in collection.find({}, {'_id': 0, 'user_id': 1})]
        tot = len(user_ids)
        success = 0
        failed = 0
        successid=["userid:"]
        await ms.edit(f"Starting Broadcast...\nSending Message To {tot} Users")
        
        # Send the broadcast message to all users
        for user_id in user_ids:
            try:
                if(int(user_id)==OWNER_ID):
                    continue
                await m.reply_to_message.copy(chat_id=int(user_id))
                
                success += 1
            except Exception as e:
                failed += 1
                # Handle specific exceptions if needed
                
            
                await ms.edit(f"Message sent to {success} chat(s). {failed} chat(s) failed on receiving message.\nTotal - {tot} ")
            
        
        
    else:
        await m.reply("please reply any message to broadcast")
        
        
        
@JN.on_message(filters.private & filters.user(OWNER_ID) & filters.command(["forward"]))
async def broadcast_command_handler(b, m: Message):
    # Check if the user is authorized to use the /broadcast command
    if m.reply_to_message:
        ms = await m.reply("Getting All ids from database...\nPlease wait")
        
        # Retrieve all user IDs from the database
        user_ids = [doc['user_id'] for doc in collection.find({}, {'_id': 0, 'user_id': 1})]
        tot = len(user_ids)
        success = 0
        failed = 0
        successid=["userid:"]
        await ms.edit(f"Starting Broadcast...\nSending Message To {tot} Users")
        
        # Send the broadcast message to all users
        for user_id in user_ids:
            try:
                if(int(user_id)==OWNER_ID):
                    continue
                await b.forward_messages(chat_id=int(user_id), from_chat_id=m.chat.id, message_ids=m.reply_to_message.message_id)
                #await m.reply_to_message.copy(chat_id=int(user_id))
                
                success += 1
            except Exception as e:
                failed += 1
                # Handle specific exceptions if needed
                
            
                await ms.edit(f"Message sent to {success} chat(s). {failed} chat(s) failed on receiving message.\nTotal - {tot} ")
            
        
        
    else:
        await m.reply("please reply any message to broadcast")
        

@JN.on_message(filters.private & filters.command(["stats"]))
async def broadcast_command_handler(b, m: Message):
    # Check if the user is authorized to use the /broadcast command
    if m.from_user.id == int(OWNER_ID):
        ms = await m.reply("Getting All details from database...\nPlease wait")
        
        # Retrieve all user IDs from the database
        user_ids = [doc['user_id'] for doc in collection.find({}, {'_id': 0, 'user_id': 1})]
        tot = len(user_ids)
      
        
        
        
        # Return a confirmation message
        await ms.edit(f"Total users- {tot}\n\nUser ids:- {user_ids}")
    else:
        await m.reply("You are not authorized to use this command.")


from .. import JN
from pyrogram import filters
from ..database import collection

# Define a function to handle the /delete command
@JN.on_message(filters.command("delete") & filters.private)
async def delete_command_handler(bot, message):   
    if message.from_user.id == OWNER_ID:
        if len(message.command) == 2:
            user_id_to_delete = int(message.command[1])
            # Check if the user exists in the database
            if collection.find_one({'user_id': user_id_to_delete}):
                # Delete the user from the database
                collection.delete_one({'user_id': user_id_to_delete})
                await message.reply(f"User with ID {user_id_to_delete} has been deleted from the database.")
            else:
                await message.reply("User not found in the database.")
        else:
            await message.reply("Please provide the user ID to delete.")
    else:
        await message.reply("You are not authorized to use this command.")


@JN.on_message(filters.command("stickerid") & filters.reply)
async def get_sticker_id_command_handler(b, m):
    # Check if the replied message is a sticker
    if m.reply_to_message.sticker:
        # Get the sticker ID
        sticker_id = m.reply_to_message.sticker.file_id
        await m.reply(f"The sticker ID is: `{sticker_id}`")
    else:
        await m.reply("Please reply to a sticker to get its ID.")