import os

api_id = 27665762
api_hash = os.environ.get("API_HASH", "b2b6f18e1280f194b8f7349db4737eb9")
bot_token = os.environ.get("BOT_TOKEN")
auth_users = os.environ.get("AUTH_USERS", "7152249320")
sudo_users = [int(num) for num in auth_users.split(",")]
osowner_users = os.environ.get("OWNER_USERS", "7152249320")
owner_users = [int(num) for num in osowner_users.split(",")]
