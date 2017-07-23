'''This script is called by crontab once a day
to send me a message if my raspberry pi is still up.'''
from telepot import Bot
TOKEN = '342565093:AAEd2KenIzjmzxZxmSek3fxq-eQRrAWIp5Q'
CHAT_ID = 322086570
BOT = Bot(TOKEN)

BOT.sendMessage(chat_id=CHAT_ID,
        parse_mode='Markdown',
        disable_notification=True,
        text='`I am still alive.\nAnd this is a second Test.`')
