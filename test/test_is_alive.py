from telepot import Bot
from os import getpid

TOKEN = '342565093:AAEd2KenIzjmzxZxmSek3fxq-eQRrAWIp5Q'
CHAT_ID = 322086570
BOT = Bot(TOKEN)

BOT.sendMessage(chat_id=CHAT_ID,
        parse_mode='Markdown',
        disable_notification=True,
        text='`I am still alive.`')

with open('process_ids.txt', 'a') as f:
    f.write(str(getpid())+'\n')
