from telepot import Bot
TOKEN = '342565093:AAEd2KenIzjmzxZxmSek3fxq-eQRrAWIp5Q'
CHAT_ID = 322086570
BOT = Bot(TOKEN)

with open('/home/pi/bot.log', 'r') as f:
    BOT.sendMessage(
            chat_id=CHAT_ID,
            document='`bot.log`\n`-------`\n{}'.format(f.read()),
            caption='bot.log'
            )
