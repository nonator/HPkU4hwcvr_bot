import telepot
from time import sleep, localtime
from datetime import datetime
TOKEN = '342565093:AAEd2KenIzjmzxZxmSek3fxq-eQRrAWIp5Q'
CHAT_ID = 322086570
BOT = telepot.Bot(TOKEN)

def alive():
    BOT.sendMessage(chat_id=CHAT_ID,
        parse_mode='Markdown',
        disable_notification=True,
        text='`I am still alive.`')


def handle(msg):
    ctype, _, cid = telepot.glance(msg)
    if cid == CHAT_ID:
        admin = True
    if msg['text'] == 'hallo':
        alive()
    return
alive()
