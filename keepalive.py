import telepot
token = '342565093:AAEd2KenIzjmzxZxmSek3fxq-eQRrAWIp5Q'
chat_id = 322086570
bot = telepot.Bot(token)

bot.sendMessage(chat_id=chat_id, text='Raspberry Pi is still alive.')
