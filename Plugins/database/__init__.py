from config import MONGO_DB_URI,NEW_USER_BONUS,REFER_BONUS
from Plugins import JN
from pymongo import MongoClient
client = MongoClient(MONGO_DB_URI)
db = client['user_balances']
collection = db['balances']
files_collection = db["files"]
# Function to update balance for a user

async def update_balance(user_id, amount):
    query = {'user_id': user_id}
    existing_balance = collection.find_one(query)

    if existing_balance:
        new_balance = existing_balance.get('balance', 0) + amount
        collection.update_one(query, {'$set': {'balance': new_balance}})
    else:
        balance_doc = {'user_id': user_id, 'balance': 1,
            'total_refer': 0,
            'total_deposits': 0,"total_orders":0}
        collection.insert_one(balance_doc)
#add refer



async def add_refer_balance(user_id, refer_in):
    query = {'user_id': user_id}
    existing_user = collection.find_one(query)

    if existing_user:
        new_balance = existing_user.get('balance', 0) + REFER_BONUS
        refer_increase=existing_user.get('total_refer', 0) + 1
        collection.update_one(query, {'$set': {'balance': new_balance}})
        collection.update_one(query,{"$set": {"total_refer": refer_increase}})
    else:
        balance_doc = {'user_id': user_id, "total_refer":0,'balance': 1,"total_orders":0,
            'total_deposits': 0}
        collection.insert_one(balance_doc)

# Add default balance for a user when they start the bot

def add_default_balance(user_id):
    query = {'user_id': user_id}
    existing_balance = collection.find_one(query)
    

    if not existing_balance:
        balance_doc = {
            'user_id': user_id,
            'balance': NEW_USER_BONUS,
            'total_refer': 0,
            'total_deposits': 0,
            'total_orders': 0,
            'check1': 0
        }
        #initial balance to 2 for new users
        collection.insert_one(balance_doc)

def is_new_user(user_id):
    user_data = collection.find_one({'user_id': user_id})
    return user_data is None


#get user ids
def getid():
    user_ids = []
    for doc in collection.find({}, {'_id': 0, 'user_id': 1}):
        user_ids.append(doc['user_id'])
    return user_ids

# Function to delete a user from the database
def delete(user_id):
    try:
        filter_query = {'user_id': user_id}
        collection.delete_one(filter_query)
        print("User deleted successfully.")
    except Exception as e:
        print(f"Error deleting user: {e}")



# Run deposit functionality
async def deposits(user_id, amount):
    add_default_balance(user_id)
    await update_balance(user_id, amount)
    return f"ʜᴇʏ ʏᴏᴜ ɢᴏᴛ {amount} ɪɴʀ ɪɴ ʏᴏᴜʀ ᴀᴄᴄᴏᴜɴᴛ! 🚀"




import math, time
from datetime import datetime
from pytz import timezone
from config import Config, Txt 
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
    if Config.log_channel is not None:
        curr = datetime.now(timezone("Asia/Kolkata"))
        date = curr.strftime('%d %B, %Y')
        time = curr.strftime('%I:%M:%S %p')
        await b.send_message(
            Config.log_channel,
            f"**--Nᴇᴡ Uꜱᴇʀ Sᴛᴀʀᴛᴇᴅ Tʜᴇ Bᴏᴛ--**\n\nUꜱᴇʀ: {u.mention}\nIᴅ: `{u.id}`\nUɴ: @{u.username}\n\nDᴀᴛᴇ: {date}\nTɪᴍᴇ: {time}\n\nBy: {b.mention}"
        )
        

