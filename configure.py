from tkinter.simpledialog import askstring
import os 

if os.stat('config.py').st_size !=0:
    pass
else:
    TOKEN=askstring("Token", "Enter your token that you get from @BotFather \n Don't close this window before you enter your token") 
    CHAT_ID=askstring("Chat ID", "Enter your chat ID that you get from @My_id_bot \n Don't close this window before you enter your chat ID")
    with open('config.py', 'w') as f:
        f.write("TOKEN = '"+TOKEN+"'\nCHAT_ID = '"+CHAT_ID+"'")
        f.close()

