import re, os, time
id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyro client config
    # API_ID    = os.environ.get("API_ID", "27996421")
    # API_HASH  = os.environ.get("API_HASH", "5f5cb6a13ecff3d90e1ec73dc366e26d")
    # BOT_TOKEN = os.environ.get("BOT_TOKEN", "7304804258:AAGYCi_E2CpXdp3-fv951KFsTX2kyqptT6Y")
    API_ID    = os.environ.get("API_ID", "26184984")
    API_HASH  = os.environ.get("API_HASH", "d89d7c5ac61ea8f467a6a75aa54a51ca")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6087816605:AAFsPV-uIOs8OhTSF9PN2lOE2GbdAzMTep8")


    # database config
    DB_NAME = os.environ.get("DB_NAME","rename")     
    # DB_URL  = os.environ.get("DB_URL","mongodb+srv://codiyoc903:R8JnDcnrsRh6wy3D@cluster0.z1avpag.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://dapita1597:0irZBo8nAyTn9pdu@cluster0.zurtp5f.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://telegra.ph/file/0737a4e61db2065771a35.jpg")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5050376364 6887525311 6506664860').split()]
    FORCE_SUB   = os.environ.get("FORCE_SUB", "cine_huntsupdates") 
    # LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002123581785"))
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002146552264"))
    
    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", "True"))


class Txt(object):
    # part of text configuration
        
    START_TXT = """Hello {} 
    
➻ This Is An Advanced And Yet Powerful Rename Bot.
    
➻ Using This Bot You Can Auto Rename Of Your Files.
    
➻ This Bot Also Supports Custom Thumbnail And Custom Caption.
    
➻ Use /tutorial Command To Know How To Use Me.

<b>Bot Is Made By @rohankaranjep</b>
"""
    
    FILE_NAME_TXT = """<b><u>SETUP AUTO RENAME FORMAT</u></b>

Use These Keywords To Setup Custom File Name

✓ episode :- To Replace Episode Number
✓ quality :- To Replace Video Resolution

<b>➻ Example :</b> <code> /autorename Naruto Shippuden S02 - EPepisode - quality  [Dual Audio] - @PandaWep </code>

<b>➻ Your Current Auto Rename Format :</b> <code>{format_template}</code> """
    
    ABOUT_TXT = f"""<b>🤖 My Name :</b>
<b>📝 Language :</b> <a href='https://python.org'>Python 3</a>
<b>📚 Library :</b> <a href='https://pyrogram.org'>Pyrogram 2.0</a>
<b>🚀 Server :</b> <a href='https://heroku.com'>Heroku</a>
<b>📢 Channel :</b> <a href=''>Cinehunts</a>
<b>🧑‍💻 Developer :</b> <a href='https://t.me/rohankaranje'>rohankaranje</a>
    
<b>♻️ Bot Made By :</b> @PandaWep"""

    
    THUMBNAIL_TXT = """<b><u>🖼️  HOW TO SET THUMBNAIL</u></b>
    
⦿ You Can Add Custom Thumbnail Simply By Sending A Photo To Me....
    
⦿ /viewthumb - Use This Command To See Your Thumbnail
⦿ /delthumb - Use This Command To Delete Your Thumbnail"""

    CAPTION_TXT = """<b><u>📝  HOW TO SET CAPTION</u></b>
    
⦿ /set_caption - Use This Command To Set Your Caption
⦿ /see_caption - Use This Command To See Your Caption
⦿ /del_caption - Use This Command To Delete Your Caption"""

    PROGRESS_BAR = """<b>\n
╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱━➣
┣⪼ 🗃️ Sɪᴢᴇ: {1} | {2}
┣⪼ ⏳️ Dᴏɴᴇ : {0}%
┣⪼ 🚀 Sᴩᴇᴇᴅ: {3}/s
┣⪼ ⏰️ Eᴛᴀ: {4}
┣⪼ 🥺 joine Plz: @rohankaranje
╰━━━━━━━━━━━━━━━➣ </b>"""
    
    
    DONATE_TXT = """<b>🥲 Thanks For Showing Interest In Donation! ❤️</b>
    
If You Like My Bots & Projects, You Can 🎁 Donate Me Any Amount From 10 Rs Upto Your Choice.
    
<b>My UPI - </b> """
    
    HELP_TXT = """<b>Hey</b> {}
    
Joine To Help """





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @PandaWep
# Developer @AshutoshGoswami24

