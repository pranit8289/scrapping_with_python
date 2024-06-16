import threading
import queue
import requests

import settings as config

q = queue.Queue()

valid_proxies = []

with open(config.Scrapper.all_proxies_file, "r") as proxyFp:
    all_proxies = proxyFp.readlines()
    for p in all_proxies:
        q.put(p)


def check_proxy():
    global q
    with open(config.Scrapper.validated_proxies_file, "w") as validateFp:
        while not q.empty():
            proxy = q.get()
            url = "http://ipinfo.io/json"
            try:
                response = requests.get(
                    url=url,
                    proxies={
                        "http": proxy,
                        "https": proxy
                })
            except Exception as error:
                continue
            if response.status_code == 200:
                # validateFp.write(f"{proxy}\n")
                print(f"{proxy}")

for _ in range(15):
    threading.Thread(target=check_proxy).start()
