import os
from pyrogram.types import KeyboardButton, InlineKeyboardMarkup,InlineKeyboardButton,WebAppInfo,ReplyKeyboardMarkup

#get from https://my.telegram.org/auth
API_ID:int =(os.environ.get("API_ID",20353207))
API_HASH:str = os.environ.get("API_HASH", "e5b2ac2f9c37bda345fa9fb5ade66961")
BOT_TOKEN:str = os.environ.get("BOT_TOKEN", "7634909458:AAE1uIsxWXxoB88zrC9kYrR5zWtIN-0w1A4")


REFER_BONUS=int(1)
NEW_USER_BONUS=int(1)
#minimum withdrawal amount
WITHDRAWAL=int(2) 


#username without @
UPDATE_CHNL:str = os.environ.get("UPDATE_CHNL", "OFFICIAL_MAMBA_NETWORK")
SUPPORT_GRP:str = os.environ.get("SUPPORT_GRP", "-1002138809373")

#get it from @username_to_id_bot this bot 

log_channel = int(os.environ.get("LOG_CHANNEL", "-1002156100590"))
OWNER_ID=6713994904


# search on youtube "how to create mongodburl""

MONGO_DB_URI:str = os.environ.get(
    "MONGO_DB_URI",
    "mongodb+srv://danishzain1637:papaspartan@cluster0.xdje3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
	

# all channels list you can add more 
links = ["https://t.me/MBV_NETWORK", "https://t.me/OFFICIAL_MAMBA_NETWORK", "https://t.me/OFFICIAL_MAMBA_SUPPORT"]













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
    
    
    
    

