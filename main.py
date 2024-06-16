import requests
from bs4 import BeautifulSoup as bs

import settings as config

with open(config.Scrapper.validated_proxies_file, "r") as validFp:
    all_proxies = validFp.readlines()

sites_to_scrape = ["https://www.walmart.com/"]

counter = 0

for site in sites_to_scrape:
    try:
        proxies = {
            "http": all_proxies[counter].strip(),
            "https:": all_proxies[counter].strip(),
        }
        print(f"Trying proxy : {all_proxies[counter]}")
        res = requests.get(site.strip(), proxies=proxies)

    except Exception as error:
        print(f"proxy {all_proxies[counter].strip()}, failed with \n{error}")
    finally:
        counter +=1

    soup = bs(res.text, "html.parser")
    print(soup.div)