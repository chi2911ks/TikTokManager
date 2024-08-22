import time
from requests import Session
import json
from bs4 import BeautifulSoup
from threading import Semaphore, Thread
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
def checkLive(data):
    id = data.split("|")[0]
    with sema:
        s = Session()
        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-language": "en-US,en;q=0.9",
            "cache-control": "no-cache",
            "pragma": "no-cache",
            "sec-ch-ua": "\"Chromium\";v=\"118\", \"Google Chrome\";v=\"118\", \"Not=A?Brand\";v=\"99\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1"
        }
        s.headers.update(headers)
        try:
            response = s.get("https://www.tiktok.com/@"+id)
        except: 
            time.sleep(5)
            return checkLive(data)
        if response is None:
            time.sleep(5)
            return checkLive(data)
        response = response.text
        soup = BeautifulSoup(response, 'html.parser')
        sigi_state_element = soup.find(id="__UNIVERSAL_DATA_FOR_REHYDRATION__")
        if sigi_state_element is None:
            time.sleep(5)
            return checkLive(data)
        d = json.loads(sigi_state_element.text)
        # file = open("cc.json", "w", encoding="utf-8")
        # json.dump(data, file)
        # print(data)
        if "userInfo" in d["__DEFAULT_SCOPE__"]["webapp.user-detail"]:
            print(bcolors.OKGREEN+id, "live!")
            with open("accLive.txt", "a+", encoding="utf-8") as file:
                file.write(data+"\n")
        else:
            print(bcolors.FAIL+id, "die!")
            with open("accDie.txt", "a+", encoding="utf-8") as file:
                file.write(data+"\n")
fileCheck = input("Nhập file cần check live: ")
threadCount = int(input("Luồng: "))
sema = Semaphore(threadCount)
file = open(fileCheck).read().splitlines()
for data in file:
    # check = checkLive(data)
    Thread(target=checkLive, args=(data, )).start()
# print(checkLive("user385840775580"))"C:\Users\Chido\Documents\Zalo Received Files\acctest.txt"