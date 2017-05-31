import requests
import re
import telepot
import time
from bs4 import BeautifulSoup


URL = "http://change.pennergame.de/change_please/2795171/"
REGEX = r"€[0-9]{0,1}\.{0,1}[0-9]{3}\,[0-9]{2}"
TOKEN = "348591361:AAHYiQAzLPvgZvsxx9ZqhP8bwfNlleGg5cs"
CHAT_ID = 322086570
BOT = telepot.Bot(TOKEN)


def spende():
    r = requests.get(URL)
    soup = BeautifulSoup(r.text, "html.parser")
    pretty = soup.prettify()
    # Finde die Spende
    money = re.findall(REGEX, pretty)
    # print(money)
    if len(money):
        # Formatiere so, dass ein Python Integer daraus wird
        number = money[0].replace("€", "").replace(".", "").replace(",", ".")
        # print(float(number))
        # BOT.sendMessage(chat_id=CHAT_ID, text='Ihnen wurde %.2f Euro gespendet.' %(float(number)))
        return float(number)
    else:
        # print('Next try...')
        # BOT.sendMessage(chat_id=CHAT_ID, text='Ihnen wurde nicht gespendet.')
        time.sleep(60)
        return spende()


def spenden():
    spenden = []
    for i in range(10):
        spenden.append(spende())
        if i < 9:
            time.sleep(1 + 60 * 60 * 1)  # 1 Stunde
    return sum(spenden)


def message():
    while True:
        TEXT = "Sie haben heute %.2f € Spenden erhalten" % (spenden())
        BOT.sendMessage(chat_id=CHAT_ID, text=TEXT)
        # time.sleep(60 * 60 * 14)  # 14 Stunden
        # spende = spenden()
        checktime()


def checktime():
    hours = time.localtime()[3] + 2
    minutes = time.localtime()[4]
    seconds = time.localtime()[5]
    timeInSeconds = hours * 60 * 60 + minutes * 60 + seconds
    sleeptime = 1 + 10 * 60 + 24 * 60 * 60 - timeInSeconds
    TEXT = "Ich warte jetzt %i:%i h." % (sleeptime//3600, (sleeptime % 3600)//60)
    print(TEXT)
    # BOT.sendMessage(chat_id=CHAT_ID, text=TEXT)
    time.sleep(sleeptime)


def main():
    checktime()  # Warte bis 0:00 Uhr am nächsten Tag
    message()  # Schreibe um ca. 9:00 Uhr die Nachricht mit der Spendensumme


main()
