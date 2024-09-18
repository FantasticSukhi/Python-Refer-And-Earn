import os
from pyrogram.types import KeyboardButton, InlineKeyboardMarkup,InlineKeyboardButton,WebAppInfo,ReplyKeyboardMarkup

#get from https://my.telegram.org/auth
API_ID:int =(os.environ.get("API_ID",21714376))
API_HASH:str = os.environ.get("API_HASH", "700092e37d7da9a7b781994b7503a4")
BOT_TOKEN:str = os.environ.get("BOT_TOKEN", "")


REFER_BONUS=int(1)
NEW_USER_BONUS=int(1)
#minimum withdrawal amount
WITHDRAWAL=int(2) 


#username without @
UPDATE_CHNL:str = os.environ.get("UPDATE_CHNL", "jn_bots")
SUPPORT_GRP:str = os.environ.get("SUPPORT_GRP", "-1002195994803")

#get it from @username_to_id_bot this bot 

log_channel = int(os.environ.get("LOG_CHANNEL", "-1001918482012"))
OWNER_ID=5597521952


# search on youtube "how to create mongodburl""

MONGO_DB_URI:str = os.environ.get(
    "MONGO_DB_URI",
    "")
	

# The link variable should contain all the channel URLs in a list format
links = ["https://t.me/jn_bots", "https://t.me/jn_family", "https://t.me/channel3"]

# Create a list to hold all the buttons
buttons = []


for i in range(0, len(links), 2):
    row = []
    for j in range(2):
        if i + j < len(links):
            row.append(InlineKeyboardButton(f"Channel {i+j+1}", url=links[i + j]))
    buttons.append(row)










INR_IMG="https://graph.org/file/591e034f3ebaca25e0692.jpg"
START_IMG= "https://graph.org/file/877838e68ea8e3099f343.jpg"
start_img2="https://graph.org/file/e1f08dea685a9051b264c.jpg"
photo="https://graph.org/file/8e2df166f47509590c88e.jpg"
deposit_IMG="https://graph.org/file/d46f6efe8fe5c991491ed.jpg"



                


main_button = ReplyKeyboardMarkup(
        [
            [KeyboardButton("🪪 ᴍʏ ᴘʀᴏꜰɪʟᴇ"), KeyboardButton("🤑 ꜰʀᴇᴇ ᴍᴏɴᴇʏ 🤑")],
            [KeyboardButton("⚡️ ᴡɪᴛʜᴅʀᴀᴡᴀʟ ⚡️")], 
            [KeyboardButton("ᴄʀᴇᴀᴛᴏʀ 😉", web_app=WebAppInfo(url="https://jnbots.netlify.app"))]
        ],
        resize_keyboard=True
    )

all_platform = ReplyKeyboardMarkup(
        [
        [KeyboardButton("⚽️ ꜰᴏᴏᴛʙᴀʟʟ "), KeyboardButton("ᴅɪᴄᴇ ɢᴀᴍᴇ 🥳")],
            [KeyboardButton("❤️‍🔥 ʀᴇꜰᴇʀ ᴀɴᴅ ᴇᴀʀɴ")],
            [ KeyboardButton("〄 ᴍᴀɪɴ ᴍᴇɴᴜ 〄")]
        ],
        resize_keyboard=True
    )
    
    
    
    

