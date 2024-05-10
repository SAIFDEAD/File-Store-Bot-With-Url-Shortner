import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", ""))
  API_HASH = os.environ.get("API_HASH", "")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", ""))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "MoneyKamalo.com")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "9972ace070bae89fbb76f073d56e41e5c458c302")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", ""))
  DATABASE_URL = os.environ.get("DATABASE_URL", "")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
This Is A Permanent FileStore Bot. 
Send Me Any Media Or File. I Can Work In Channel Too. Add Me To Channel With Edit Permission, I Will Add Save Uploaded File In Channel And Share A Shareable Link. 

★ 𝗔𝗯𝗼𝘂𝘁 𝗜𝗻𝗳𝗶𝗻𝗶𝘁𝘆 𝗙𝗶𝗹𝗲 𝗦𝗮𝘃𝗲𝗿 
🔸 My Name ☞ [Infinity File Saver](https://t.me/{BOT_USERNAME})
🔸 Language ☞ [Python 3](https://www.python.org)
🔹 Library ☞ [Pyrogram](https://docs.pyrogram.org)

𒊹 𝗝𝗼𝗶𝗻 ☞ @Infinity_Backup
𒊹 𝗕𝗼𝘁 𝗕𝘆 ☞ @DRDIC

"""
  ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [DEAD](https://telegram.me/DRDIC)
 
[Want To Talk With Me !](https://t.me/DRDIC)
"""
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis Is A Permanent **FileStore Bot**.

How to Use Bot & It's Benefits??

📢 Send Me Any File & It Will Be Uploaded In My Database & You Will Get The File Link.

⚠️ Benefits: If You Have A TeleGram Movie Channel Or Any Copyright Channel, Then Its Useful For Daily Usage, You Can Send Me Your File & I Will Send Permanent Link To You & Channel Will Be Safe From **CopyRight Infringement** Issue. I Support Channel Also You Can Check **About Bot**.
"""
