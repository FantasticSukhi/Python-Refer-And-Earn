from config import MONGO_DB_URI,NEW_USER_BONUS,REFER_BONUS

from pymongo import MongoClient
client = MongoClient(MONGO_DB_URI)
db = client(f"@{JN.username})
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
