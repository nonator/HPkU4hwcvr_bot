import requests
from bs4 import BeautifulSoup
import telepot
import time
import re


token = '204922160:AAFZhl9leT5cMovHqalSbCvpAuD-uyuHtpw'
chat_id = 322086570
bot = telepot.Bot(token)
url = 'http://gateway.engel/traffic.php'
regex = '[0-9]{1,5}'


def traffic():
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    tt = soup.find_all('tt')[0].text
    numbers = re.findall(pattern=regex, string=tt)
    bleiben_noch = int(numbers[5])
    summary = '%i MB' % (bleiben_noch)
    print(summary)
    return summary


def warning():
    return


class stopwatch():
    def __init__(self, day, hour, minute):
        self.day = day
        self.hour = hour
        self.minute = minute

    def start(self):
        return 'Starte Intervall.'

    def stop(self):
        day = time.localtime()[2]
        hour = time.localtime()[3]
        minute = time.localtime()[4]
        return 'Das muss noch implementiert werden.'

    def exists():
        return True


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if msg['text'] == '/traffic':
        bot.sendMessage(chat_id=chat_id, text=traffic())
    elif msg['text'] == '/start':
        watch = stopwatch(time.localtime()[2], time.localtime()[3], time.localtime()[4])
        bot.sendMessage(chat_id=chat_id, text=watch.start())
    elif msg['text'] == '/stop':
        try:
            bot.sendMessage(chat_id=chat_id, text=watch.stop())
        except:
            bot.sendMessage(chat_id=chat_id, text='Zuerst das Intervall mit /start starten.')


# Keep the bot listening and running
print('Started')
bot.message_loop(handle)
while True:
    time.sleep(10)
