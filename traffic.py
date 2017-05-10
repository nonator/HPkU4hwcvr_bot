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
    # readable = soup.prettify()
    # print(readable)
    tt = soup.find_all('tt')[0].text
    # print(tt)
    numbers = re.findall(pattern=regex, string=tt)
    # gesendet = int(numbers[0])
    # empfangen = int(numbers[1])
    # summe = int(numbers[2])
    # limit = int(numbers[3])
    bleiben_noch = int(numbers[5])
    # summary = 'Traffic:\ngesendet:          %i MB\nempfangen:  %i MB\nsumme:             %i MB\n------------------------\nbleiben noch:   %i MB' % (gesendet, empfangen, summe, bleiben_noch)
    summary = '%i MB' % (bleiben_noch)
    # print(summary)
    return summary


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    # print(msg['text'])
    if msg['text'] == '/traffic':
        bot.sendMessage(chat_id=chat_id, text=traffic())


bot.message_loop(handle)
# print('listening...')


while True:
    time.sleep(10)
