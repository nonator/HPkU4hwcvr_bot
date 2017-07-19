import telepot
# from pprint import pprint
import time
import re

bot = telepot.Bot('342565093:AAEd2KenIzjmzxZxmSek3fxq-eQRrAWIp5Q')
rex = '[0-9]*'


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    bot.sendMessage(
        chat_id,
        'Hello. I will repeat only numbers at the beginning of your message'
        )

    if content_type == 'text':
        result = re.match(rex, str(msg['text']))
        if result[0]:
            bot.sendMessage(chat_id, result[0])
        else:
            bot.sendMessage(chat_id, 'sorry not working...')


bot.message_loop(handle)
print('Listening...')

while 1:
    time.sleep(10)
